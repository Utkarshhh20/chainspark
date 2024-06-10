// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./DAOMembership.sol";

contract DAOVoting is DAOMembership {
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        bool executed;
        mapping(address => bool) voted;
    }

    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;

    event ProposalCreated(uint256 id, string description);
    event VoteCast(uint256 proposalId, address indexed voter);

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
        require(!proposal.voted[msg.sender], "Already voted");

        proposal.voteCount++;
        proposal.voted[msg.sender] = true;
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
        // Logic to execute the proposal can be added here
    }
}
