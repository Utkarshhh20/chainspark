// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./DataOwnership.sol";
import "./PaymentToken.sol";

contract DataMarketplace is DataOwnership {
    event DataListed(uint256 indexed dataId, address indexed owner, uint256 price, bool qualityChecked);
    event DataPurchased(uint256 indexed dataId, address indexed buyer, uint256 price);
    event CompensationPaid(address indexed uploader, uint256 amount);

    struct DataItem {
        uint256 id;
        address owner;
        uint256 price;
        bool qualityChecked;
        address originalUploader;
        bool initialSale;
    }

    uint256 public dataCounter;
    mapping(uint256 => DataItem> public dataItems;

    PaymentToken public paymentToken;

    uint256 public initialCompensationRate = 10; // Example: 10 tokens per quality score point
    uint256 public resaleCompensationRate = 5; // Example: 5% of each sale

    constructor(address _paymentTokenAddress) {
        paymentToken = PaymentToken(_paymentTokenAddress);
    }

    function listData(uint256 price, bool qualityChecked, uint256 qualityScore) public {
        dataCounter++;
        uint256 initialCompensation = qualityScore * initialCompensationRate;

        // Mint and send initial compensation to the uploader
        paymentToken.mint(msg.sender, initialCompensation);
        emit CompensationPaid(msg.sender, initialCompensation);

        dataItems[dataCounter] = DataItem(dataCounter, msg.sender, price, qualityChecked, msg.sender, true);
        emit DataListed(dataCounter, msg.sender, price, qualityChecked);
    }

    function buyData(uint256 dataId) public payable {
        DataItem storage item = dataItems[dataId];
        require(item.price == msg.value, "Incorrect price");
        require(item.qualityChecked, "Data not quality checked");

        if (item.initialSale) {
            // Calculate and transfer resale compensation to the original uploader
            uint256 resaleCompensation = (msg.value * resaleCompensationRate) / 100;
            payable(item.originalUploader).transfer(resaleCompensation);
            emit CompensationPaid(item.originalUploader, resaleCompensation);

            // Transfer the remaining amount to the current owner
            uint256 amountToOwner = msg.value - resaleCompensation;
            payable(item.owner).transfer(amountToOwner);

            // Keep the data up for sale and restrict resale by buyers
            emit DataPurchased(dataId, msg.sender, item.price);
        } else {
            revert("Resale not allowed");
        }
    }
}
