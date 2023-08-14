# Lottery Smart Contract README.md

## Description

This repository contains a decentralized lottery system built on the Ethereum blockchain. Players can enter the lottery by paying a dynamic entrance fee in Ether, which is based on the current Ether to USD conversion rate. Once the lottery ends, a winner is randomly selected using Chainlink's VRF (Verifiable Random Function) for true randomness. The entire Ether balance of the contract is then transferred to the winner.

## Smart Contract Features

- Uses Chainlink VRF for provable randomness.
- Utilizes OpenZeppelin's Ownable pattern, ensuring that only the contract owner can start or end the lottery.
- Dynamic entrance fee based on the current Ether to USD price, retrieved from a Chainlink Price Feed.
- Easily start or end the lottery through exposed functions.
- A decentralized and trustless mechanism for a fair lottery system.

## Contracts

- `Lottery.sol`: The main contract which contains the logic for the lottery system.
- Dependencies:
  - Chainlink's `AggregatorV3Interface` for fetching the latest Ether to USD price.
  - Chainlink's `VRFConsumerBase` for randomness.
  - OpenZeppelin's `Ownable` for ownership management.

## Scripts

- `deploy_lottery.py`: Deployment script to deploy the `Lottery` contract onto the Ethereum blockchain using Brownie.

## Prerequisites

1. [Brownie](https://eth-brownie.readthedocs.io/en/stable/)
2. [Chainlink contracts](https://github.com/smartcontractkit/chainlink)
3. [OpenZeppelin contracts](https://github.com/OpenZeppelin/openzeppelin-contracts)

## Setup

1. Clone the repository.
2. Install the necessary node packages.
   ```
   npm install
   ```
3. Compile the contracts using Brownie.
   ```
   brownie compile
   ```

## Deployment

To deploy the `Lottery` contract:

```bash
brownie run deploy_lottery.py
```

## Interacting with the Contract

- To enter the lottery:
  ```solidity
  function enter() public payable
  ```

- To get the current entrance fee in Ether:
  ```solidity
  function getEntranceFee() public view returns (uint256)
  ```

- To start the lottery (only owner):
  ```solidity
  function startLottery() public onlyOwner
  ```

- To end the lottery and select a winner (only owner):
  ```solidity
  function endLottery() public onlyOwner
  ```

## Note

Remember to fund the deployed contract with LINK tokens, as Chainlink VRF requires them to generate randomness.

## License

MIT
