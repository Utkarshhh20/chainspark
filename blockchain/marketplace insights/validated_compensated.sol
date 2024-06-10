// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "./data-ownership.sol";

contract PaymentToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("PaymentToken", "PTK") {
        _mint(msg.sender, initialSupply);
    }
}

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
    }

    uint256 public dataCounter;
    mapping(uint256 => DataItem) public dataItems;

    // Payment token contract instance
    PaymentToken public paymentToken;

    // Compensation rates
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

        dataItems[dataCounter] = DataItem(dataCounter, msg.sender, price, qualityChecked, msg.sender);
        emit DataListed(dataCounter, msg.sender, price, qualityChecked);
    }

    function buyData(uint256 dataId) public payable {
        DataItem memory item = dataItems[dataId];
        require(item.price == msg.value, "Incorrect price");
        require(item.qualityChecked, "Data not quality checked");

        // Calculate and transfer resale compensation to the original uploader
        uint256 resaleCompensation = (msg.value * resaleCompensationRate) / 100;
        payable(item.originalUploader).transfer(resaleCompensation);
        emit CompensationPaid(item.originalUploader, resaleCompensation);

        // Transfer the remaining amount to the current owner
        uint256 amountToOwner = msg.value - resaleCompensation;
        payable(item.owner).transfer(amountToOwner);

        // Transfer ownership of the data
        _transferOwnership(item.owner, msg.sender, dataId);
        dataItems[dataId].owner = msg.sender;

        emit DataPurchased(dataId, msg.sender, item.price);
    }
}
