// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Voting {
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        bool executed;
        mapping(address => bool) voters;
    }

    address public owner;
    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;
    mapping(address => bool) public members;
    uint256 public memberCount;

    event ProposalCreated(uint256 id, string description);
    event VoteCast(uint256 proposalId, address indexed voter);
    event ProposalExecuted(uint256 proposalId);

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
    }

    function removeMember(address _member) public onlyOwner {
        require(members[_member], "Address is not a member");
        members[_member] = false;
        memberCount--;
    }

    function createProposal(string memory _description) public onlyMember {
        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = _description;
        newProposal.voteCount = 0;
        newProposal.executed = false;
        emit ProposalCreated(proposalCount, _description);
    }

    function vote(uint256 _proposalId) public onlyMember {
        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.executed, "Proposal already executed");
        require(!proposal.voters[msg.sender], "Already voted");

        proposal.voteCount++;
        proposal.voters[msg.sender] = true;
        emit VoteCast(_proposalId, msg.sender);
    }

    function getProposal(uint256 _proposalId) public view returns (string memory, uint256, bool) {
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.description, proposal.voteCount, proposal.executed);
    }

    function executeProposal(uint256 _proposalId) public onlyOwner {
        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.executed, "Proposal already executed");
        require(proposal.voteCount > (memberCount / 2), "Not enough votes");

        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
        // Logic to execute the proposal can be added here
    }
}
