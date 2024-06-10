// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./Voting.sol";

contract InvestmentExecution is Voting {
    struct Investment {
        uint256 id;
        string name;
        uint256 amount;
        address payable recipient;
        bool funded;
    }

    uint256 public investmentCount;
    mapping(uint256 => Investment) public investments;

    event InvestmentCreated(uint256 id, string name, uint256 amount, address recipient);
    event InvestmentFunded(uint256 id, string name, uint256 amount, address recipient);

    function createInvestment(string memory _name, uint256 _amount, address payable _recipient) public onlyMember {
        investmentCount++;
        investments[investmentCount] = Investment(investmentCount, _name, _amount, _recipient, false);
        emit InvestmentCreated(investmentCount, _name, _amount, _recipient);
    }

    function executeInvestment(uint256 _proposalId, uint256 _investmentId) public onlyOwner {
        Proposal storage proposal = proposals[_proposalId];
        Investment storage investment = investments[_investmentId];
        require(proposal.executed, "Proposal not executed");
        require(!investment.funded, "Investment already funded");
        require(address(this).balance >= investment.amount, "Insufficient funds");

        investment.recipient.transfer(investment.amount);
        investment.funded = true;
        emit InvestmentFunded(investment.id, investment.name, investment.amount, investment.recipient);
    }

    // Function to receive ETH
    receive() external payable {}
}
