// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./data-ownership.sol";
import "./payment-token.sol";

contract DataMarketplace is DataOwnership {
    event DataListed(uint256 indexed dataId, address indexed owner, uint256 price, bool qualityChecked);
    event DataPurchased(uint256 indexed dataId, address indexed buyer, uint256 price);

    struct DataItem {
        uint256 id;
        address owner;
        uint256 price;
        bool qualityChecked;
    }

    uint256 public dataCounter;
    mapping(uint256 => DataItem) public dataItems;

    function listData(uint256 price, bool qualityChecked) public {
        dataCounter++;
        dataItems[dataCounter] = DataItem(dataCounter, msg.sender, price, qualityChecked);
        emit DataListed(dataCounter, msg.sender, price, qualityChecked);
    }

    function buyData(uint256 dataId) public payable {
        DataItem memory item = dataItems[dataId];
        require(item.price == msg.value, "Incorrect price");
        require(item.qualityChecked, "Data not quality checked");

        payable(item.owner).transfer(msg.value);
        _transferOwnership(item.owner, msg.sender, dataId);

        dataItems[dataId].owner = msg.sender;
        emit DataPurchased(dataId, msg.sender, item.price);
    }
}
