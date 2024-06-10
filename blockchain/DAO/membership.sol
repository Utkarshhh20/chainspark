// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DAOMembership {
    address public owner;
    mapping(address => bool) public members;
    uint256 public memberCount;

    event MemberAdded(address indexed member);
    event MemberRemoved(address indexed member);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier onlyMember() {
        require(members[msg.sender], "Only members can call this function");
        _;
    }

    function addMember(address _member) public onlyOwner {
        require(!members[_member], "Address is already a member");
        members[_member] = true;
        memberCount++;
        emit MemberAdded(_member);
    }

    function removeMember(address _member) public onlyOwner {
        require(members[_member], "Address is not a member");
        members[_member] = false;
        memberCount--;
        emit MemberRemoved(_member);
    }

    function isMember(address _member) public view returns (bool) {
        return members[_member];
    }
}
