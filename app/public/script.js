// Initialize Web3
let web3;

// Check if MetaMask is installed
if (typeof window.ethereum !== 'undefined') {
    web3 = new Web3(window.ethereum);
} else {
    console.log("MetaMask not found. Please install MetaMask and try again.");
}

// Contract ABI and Address
const contractABI = [{"inputs":[],"name":"retrieve","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"num","type":"uint256"}],"name":"store","outputs":[],"stateMutability":"nonpayable","type":"function"}];
const contractAddress = '0xcf2f92D6F5bF398B10E49D789e6cC8C3Ca509fd5';

// Create a contract instance
const contract = new web3.eth.Contract(contractABI, contractAddress);

// Function to call a contract method
async function callContractMethod() {
    try {
        const inputValue = document.getElementById('inputValue').value;
        console.log('Calling store() with value:', inputValue);

        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Got accounts:', accounts);
        const account = accounts[0];
        console.log('Using account:', account);

        const result = await contract.methods.store(inputValue).call({ from: account });
        console.log('Method Result:', result);
    } catch (error) {
        console.error('Error:', error);
    }
}

// Attach the function to the button click event
const callMethodButton = document.getElementById('callMethodButton');
callMethodButton.addEventListener('click', callContractMethod);
