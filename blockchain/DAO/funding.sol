// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./DAOVoting.sol";

contract DAOFunding is DAOVoting {
    mapping(uint256 => uint256) public proposalFunds;

    event FundsAllocated(uint256 proposalId, uint256 amount);

    function allocateFunds(uint256 _proposalId, uint256 _amount) public onlyOwner {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.executed, "Proposal not executed");

        proposalFunds[_proposalId] += _amount;
        emit FundsAllocated(_proposalId, _amount);
    }

    function withdrawFunds(uint256 _proposalId) public onlyMember {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.executed, "Proposal not executed");
        require(proposalFunds[_proposalId] > 0, "No funds allocated");

        uint256 amount = proposalFunds[_proposalId];
        proposalFunds[_proposalId] = 0;

        payable(msg.sender).transfer(amount);
    }

    // Function to receive ETH
    receive() external payable {}
}
