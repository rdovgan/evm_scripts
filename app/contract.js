const Web3 = require('web3');

const web3 = new Web3('https://base-goerli.public.blastapi.io');

const contractAbi = ['']; // Replace with your contract's ABI
const contractAddress = '0x...'; // Replace with your contract's address

const contract = new web3.eth.Contract(contractAbi, contractAddress);