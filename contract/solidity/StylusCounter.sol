// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract StylusCounter {

    uint256 goldCount;

    function makeGold() public {
        goldCount = goldCount + 1;
    }

    function getGold() public view returns (uint256) {
        return goldCount;
    }

}