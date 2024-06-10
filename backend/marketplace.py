from web3 import Web3
import openai
import ipfshttpclient
import requests

# Initialize Web3 connection
INFURA_PROJECT_ID = '1600384e063046608881158958bcb6c8'
web3 = Web3(Web3.HTTPProvider('https://rinkeby.infura.io/v3/{}'.format(INFURA_PROJECT_ID)))

# Contract ABI and address
contract_abi = [
    
]  # Contract ABI
payment_token_abi = [
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "initialSupply",
				"type": "uint256"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "spender",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "allowance",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "needed",
				"type": "uint256"
			}
		],
		"name": "ERC20InsufficientAllowance",
		"type": "error"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "sender",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "balance",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "needed",
				"type": "uint256"
			}
		],
		"name": "ERC20InsufficientBalance",
		"type": "error"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "approver",
				"type": "address"
			}
		],
		"name": "ERC20InvalidApprover",
		"type": "error"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "receiver",
				"type": "address"
			}
		],
		"name": "ERC20InvalidReceiver",
		"type": "error"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "sender",
				"type": "address"
			}
		],
		"name": "ERC20InvalidSender",
		"type": "error"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "spender",
				"type": "address"
			}
		],
		"name": "ERC20InvalidSpender",
		"type": "error"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "spender",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "Approval",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "Transfer",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "spender",
				"type": "address"
			}
		],
		"name": "allowance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "spender",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "approve",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "account",
				"type": "address"
			}
		],
		"name": "balanceOf",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "decimals",
		"outputs": [
			{
				"internalType": "uint8",
				"name": "",
				"type": "uint8"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "mint",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "name",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "symbol",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "totalSupply",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "transfer",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "transferFrom",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]  # Use the ABI you provided for PaymentToken
payment_token_address = '0xf8e81D47203A594245E36C48e151709F0C19fBe8'

marketplace_abi = [
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "dataId",
				"type": "uint256"
			}
		],
		"name": "buyData",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_paymentTokenAddress",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "uploader",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "CompensationPaid",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "uint256",
				"name": "dataId",
				"type": "uint256"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "price",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "bool",
				"name": "qualityChecked",
				"type": "bool"
			}
		],
		"name": "DataListed",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "uint256",
				"name": "dataId",
				"type": "uint256"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "buyer",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "price",
				"type": "uint256"
			}
		],
		"name": "DataPurchased",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "price",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "qualityChecked",
				"type": "bool"
			},
			{
				"internalType": "uint256",
				"name": "qualityScore",
				"type": "uint256"
			}
		],
		"name": "listData",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "previousOwner",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "uint256",
				"name": "dataId",
				"type": "uint256"
			}
		],
		"name": "OwnershipTransferred",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "dataCounter",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "dataItems",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "price",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "qualityChecked",
				"type": "bool"
			},
			{
				"internalType": "address",
				"name": "originalUploader",
				"type": "address"
			},
			{
				"internalType": "bool",
				"name": "initialSale",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "initialCompensationRate",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "dataId",
				"type": "uint256"
			}
		],
		"name": "ownerOf",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "paymentToken",
		"outputs": [
			{
				"internalType": "contract PaymentToken",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "resaleCompensationRate",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]  # Use the ABI you provided for DataMarketplace
marketplace_address = '0xD7ACd2a9FD159E69Bb102A1ca21C9a3e3A5F771B'

# Initialize contracts
payment_token_contract = web3.eth.contract(address=payment_token_address, abi=payment_token_abi)
marketplace_contract = web3.eth.contract(address=marketplace_address, abi=marketplace_abi)

# OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

def query_chatgpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def validate_data(data, data_type, text=None):
    factors = {
        "completeness": "Check if all required fields are filled and optional fields are appropriately filled.",
        "accuracy": "Compare data against known benchmarks or historical data for error rates.",
        "consistency": "Ensure data follows expected formats and check for duplications.",
        "relevance": "Assess if the data is pertinent to market insights and is up-to-date.",
        "validity": "Verify data conforms to industry standards and maintains logical integrity.",
        "coherence": "Evaluate the coherence of textual data and logical consistency.",
        "richness": "Determine the level of detail and comprehensive coverage.",
        "usability": "Assess ease of interpretation and presence of documentation.",
        "authenticity": "Validate the source and ensure data genuineness.",
        "innovation": "Evaluate novelty and predictive value of the data.",
        "security": "Check compliance with privacy regulations and data encryption.",
        "user_feedback": "Collect ratings and reviews, and check community endorsements."
    }

    scores = {}
    for factor, prompt in factors.items():
        query = f"Evaluate the following data for {factor}: {data}\n{prompt}"
        score = query_chatgpt(query)
        scores[factor] = float(score) if score.replace('.', '', 1).isdigit() else 0

    weights = {
        "completeness": 0.1,
        "accuracy": 0.1,
        "consistency": 0.1,
        "relevance": 0.1,
        "validity": 0.1,
        "coherence": 0.1,
        "richness": 0.05,
        "usability": 0.05,
        "authenticity": 0.1,
        "innovation": 0.05,
        "security": 0.1,
        "user_feedback": 0.05
    }

    total_score = sum(scores[factor] * weights[factor] for factor in scores)
    return total_score >= 0.7, total_score  # Example threshold for acceptance

def store_report_on_ipfs(report):
    url = 'https://ipfs.infura.io:5001/api/v0/add'
    files = {'file': ('report.txt', report)}
    response = requests.post(url, files=files)
    ipfs_hash = response.json()['Hash']
    return f"https://ipfs.infura.io/ipfs/{ipfs_hash}"

# Retrieve report from IPFS
def retrieve_report_from_ipfs(ipfs_hash):
    client = ipfshttpclient.connect('/dns/ipfs.infura.io/tcp/5001/https')
    data = client.cat(ipfs_hash)
    return data.decode('utf-8')

# Example function to list data on the blockchain
def list_data_on_blockchain(data, price, owner_address):
    is_valid, quality_score = validate_data(data, "text", data)
    if is_valid:
        report_url = store_report_on_ipfs(data)
        tx_hash = marketplace_contract.functions.listData(price, True, quality_score*100).transact({'from': owner_address})
        web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Data listed with transaction hash: {tx_hash.hex()} and IPFS URL: {report_url}")

def list_ai_report_on_blockchain(report, price, owner_address):
    is_valid, quality_score = validate_data(report, "text", report)
    if is_valid:
        report_url = store_report_on_ipfs(report)
        tx_hash = marketplace_contract.functions.listData(price, True, quality_score).transact({'from': owner_address})
        web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"AI report listed with transaction hash: {tx_hash.hex()} and IPFS URL: {report_url}")
    else:
        print("AI report validation failed")

# Retrieve report from IPFS
def retrieve_report_from_ipfs(ipfs_hash):
    client = ipfshttpclient.connect('/dns/ipfs.infura.io/tcp/5001/https')
    data = client.cat(ipfs_hash)
    return data.decode('utf-8')
    
# Example function to buy data
def buy_data_on_blockchain(data_id, buyer_address, price):
    tx_hash = marketplace_contract.functions.buyData(data_id).transact({'from': buyer_address, 'value': price})
    web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Data bought with transaction hash: {tx_hash.hex()}")

# Example usage
data = {
    'price': [100, 200, 150],
    'market': ['stock', 'crypto', 'stock'],
    'analysis': 'This is a detailed market analysis...',
    'source': 'Reputable Source'
}

owner_address = '0xYourWalletAddress'  # Replace with your wallet address
list_data_on_blockchain(data, 1000, owner_address)  # Replace with your wallet address

buyer_address = '0xAnotherWalletAddress'  # Replace with another wallet address
buy_data_on_blockchain(1, buyer_address, 1000)  # Replace with data ID and price

# SWITCH FROM REMIX VM TO INJECTED AND USE RINKEBY/MAINNET (MAINLY RINKEBY) TO DEPLOY FOR EXTERNAL USE

'''
NOTE:
SWITCH FROM REMIX VM TO INJECTED AND USE RINKEBY/MAINNET (MAINLY RINKEBY) TO DEPLOY FOR EXTERNAL USE

Remix VM (Cancun) is local to your browser and not accessible externally. For actual deployment and integration, you need to use a testnet (like Rinkeby) or the mainnet.
MetaMask or another Web3 provider can be used to connect to a testnet or mainnet for actual deployment.
If you plan to deploy the contracts on a testnet like Rinkeby or the mainnet, follow the same deployment steps you used with Remix VM but switch to the "Injected Web3" environment in Remix and use MetaMask connected to the desired network.


ALSO MIGHT HAVE TO CHANGE WHERE DOC/REPORT STORED. RN ON IPFS INFURA, SHIFT TO STANDARD DB
'''