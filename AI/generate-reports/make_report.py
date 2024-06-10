from openai import OpenAI
from llama_index.packs.finchat import FinanceChatPack
from llama_index.core import Document

import sqlite3

# Create a SQLite database file
db_file = 'finance_chat_pack.db'
'''conn = sqlite3.connect(db_file)
conn.close()'''

OPENAI_API_KEY = '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'
POLYGON_API_KEY = 'cnr9sWyeiOqw4_acFRo06QzXiZeW_Nms'
ALPHA_VANTAGE_API_KEY = 'YVCY5T9RD3U9A6QC'
FINNHUB_API_KEY = 'cp4nu7hr01qnnlpbp5f0cp4nu7hr01qnnlpbp5fg'
NEWSAPI_API_KEY =  'f92e03e9f1b5497b96117c9ed2bad6b7'
sqlite_db_uri = f'sqlite:///{db_file}'

finance_chat_pack = FinanceChatPack(
    POLYGON_API_KEY,
    FINNHUB_API_KEY,
    ALPHA_VANTAGE_API_KEY,
    NEWSAPI_API_KEY,
    OPENAI_API_KEY,
    sqlite_db_uri
)

# Sample documents for indexing
documents = [
    Document(text = "Financial data for Tesla's Q1 2023 shows a significant increase in revenue by 20%."),
    Document(text = "The stock price of Company Tesla has risen by 10% in the last week."),
]

# Query the index
#query = "What is the revenue increase in Q1 2023 for Tesla?"
query = "Give me a complete financial analysis and report for the Tesla stock"
response = finance_chat_pack.run(query)

print("FinanceChatPack Response:", response)

'''client = OpenAI(OPENAI_API_KEY)

query = 'Can you please compare amazon aws vs google cloud platform. Please provide data'

extracted_content = ""

completion = client.chat.completions.create(
  model="text-davinci-002",
  messages=[
    {"role": "system", "content": "You are a financial analyst and investment advisor, skilled in analyzing industry and company data, formulating predicitions and providing investment advice."},
    {"role": "user", "content": query},
    {"role": "user", "content": extracted_content}
  ],
  max_tokens=1000, # Adjust based on how long you expect the answer to be
  temperature=0, # A higher temperature encourages creativity. Adjust based on your needs
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None # You can specify a stop sequence if there's a clear endpoint. Otherwise, leave it as None
)

print(completion.choices[0])



'''