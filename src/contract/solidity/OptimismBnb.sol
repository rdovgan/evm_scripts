// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

/**
 * @title Optimism BNB
 * @dev Set & change owner
 */
contract GoldScroll {

    address private owner;

    uint256 optimism;

    event OwnerSet(address indexed oldOwner, address indexed newOwner);

    modifier isOwner() {
        require(msg.sender == owner, "Caller is not owner");
        _;
    }

    constructor() {
        owner = msg.sender;
        emit OwnerSet(address(0), owner);
    }

    function makeOwner(address newOwner) public isOwner {
        emit OwnerSet(owner, newOwner);
        owner = newOwner;
    }

    function makeOptimism() public {
        optimism = optimism + 1;
    }

    function getOptimism() public view returns (uint256) {
        return optimism;
    }

    function getOwner() external view returns (address) {
        return owner;
    }

    function admitOwner() external view returns (address) {
        return owner;
    }
}