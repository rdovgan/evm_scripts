// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

/**
 * @title Owner
 * @dev Set & change owner Guava
 */
contract Owner {

    address private owner;

    uint256 goldCount;

    event OwnerSet(address indexed oldOwner, address indexed newOwner);

    modifier isOwner() {
        require(msg.sender == owner, "Caller is not owner");
        _;
    }

    constructor() {
        owner = msg.sender;
        emit OwnerSet(address(0), owner);
    }

    function makeGuava(address newOwner) public isOwner {
        emit OwnerSet(owner, newOwner);
        owner = newOwner;
    }

    function makeGold() public {
        goldCount = goldCount + 1;
    }

    function getGold() public view returns (uint256) {
        return goldCount;
    }

    function getOwner() external view returns (address) {
        return owner;
    }

    function admitOwner(address newOwner) external view returns (address) {
        return owner;
    }
}