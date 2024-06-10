from web3 import Web3

# Initialize Web3 connection
web3 = Web3(Web3.HTTPProvider('https://rinkeby.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# Contract ABI and address
contract_abi = [...]  # Contract ABI
contract_address = 'YOUR_CONTRACT_ADDRESS'
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Validation function
def validate_and_list_data(data, data_type, text=None):
    is_valid = validate_data(data, data_type, text)
    if is_valid:
        tx_hash = contract.functions.listData(data['price'], True).transact({'from': web3.eth.accounts[0]})
        web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Data listed with transaction hash: {tx_hash.hex()}")
    else:
        print("Data validation failed")