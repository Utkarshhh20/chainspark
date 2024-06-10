// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DataOwnership {
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner, uint256 indexed dataId);

    mapping(uint256 => address) private dataOwners;

    modifier onlyOwner(uint256 dataId) {
        require(dataOwners[dataId] == msg.sender, "Caller is not the owner");
        _;
    }

    function _transferOwnership(address previousOwner, address newOwner, uint256 dataId) internal {
        dataOwners[dataId] = newOwner;
        emit OwnershipTransferred(previousOwner, newOwner, dataId);
    }

    function ownerOf(uint256 dataId) public view returns (address) {
        return dataOwners[dataId];
    }
}
