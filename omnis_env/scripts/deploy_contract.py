# omnis/scripts/deploy_contract.py

from brownie import OmnisStrategy, accounts, network

def deploy_contract():
    dev_account = accounts.load('dev_account')  # Load your account
    uniswap_router_address = "0x..."  # Uniswap Router Address
    contract = OmnisStrategy.deploy(uniswap_router_address, {'from': dev_account})
    print(f"Contract deployed at {contract.address}")

if __name__ == "__main__":
    network.connect('development')
    deploy_contract()
