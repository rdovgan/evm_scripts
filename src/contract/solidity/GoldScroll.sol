// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

/**
 * @title Scroll Alpha
 * @dev Set & change owner
 */
contract GoldScroll {

    address private owner;

    uint256 scroll;

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

    function makeGold() public {
        scroll = scroll + 1;
    }

    function getScroll() public view returns (uint256) {
        return scroll;
    }

    function getOwner() external view returns (address) {
        return owner;
    }

    function admitOwner() external view returns (address) {
        return owner;
    }
}