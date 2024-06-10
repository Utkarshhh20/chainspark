// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./IERC20.sol";

contract MarketplacePayments {
    enum PaymentMethod { ETH, Token }

    struct Payment {
        uint256 id;
        address buyer;
        address seller;
        uint256 amount;
        PaymentMethod method;
        bool completed;
    }

    mapping(uint256 => Payment) public payments;
    uint256 public paymentCount;

    event PaymentCreated(uint256 id, address indexed buyer, address indexed seller, uint256 amount, PaymentMethod method);
    event PaymentCompleted(uint256 id, address indexed buyer, address indexed seller, uint256 amount, PaymentMethod method);

    function createPayment(address seller, uint256 amount, PaymentMethod method) public payable returns (uint256) {
        require(method == PaymentMethod.ETH || msg.value == 0, "ETH amount should be zero for token payments");
        if (method == PaymentMethod.ETH) {
            require(msg.value == amount, "Incorrect ETH amount sent");
        }

        paymentCount++;
        payments[paymentCount] = Payment(paymentCount, msg.sender, seller, amount, method, false);

        emit PaymentCreated(paymentCount, msg.sender, seller, amount, method);
        return paymentCount;
    }

    function completePayment(uint256 paymentId, address tokenAddress) public {
        Payment storage payment = payments[paymentId];
        require(payment.id == paymentId, "Invalid payment ID");
        require(payment.completed == false, "Payment already completed");

        if (payment.method == PaymentMethod.ETH) {
            payable(payment.seller).transfer(payment.amount);
        } else {
            IERC20 token = IERC20(tokenAddress);
            require(token.balanceOf(msg.sender) >= payment.amount, "Insufficient token balance");
            require(token.transferFrom(msg.sender, payment.seller, payment.amount), "Token transfer failed");
        }

        payment.completed = true;
        emit PaymentCompleted(paymentId, payment.buyer, payment.seller, payment.amount, payment.method);
    }
}
