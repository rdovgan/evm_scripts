// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.8.2 <0.9.0;

contract LineaTest {

    uint256 c;

    function store(uint256 a) public {
        c = a;
    }

    function retrieve() public view returns (uint256){
        return c;
    }
}