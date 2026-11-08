// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract Voting {
    uint[2] public votes;
    mapping(address => bool) public hasVoted;

    function vote(uint candidate) public {
        require(!hasVoted[msg.sender], "You already voted");
        require(candidate < 2, "Invalid candidate");
        hasVoted[msg.sender] = true;
        votes[candidate]++;
    }
}
