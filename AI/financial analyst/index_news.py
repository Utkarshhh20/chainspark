import os

# from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
# new version replaces GPTSimpleVectorIndex with GPTVectorStoreIndex

from llama_index.core import GPTVectorStoreIndex, SimpleDirectoryReader

OPENAI_API_KEY = ""
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

documents = SimpleDirectoryReader('articles').load_data()

index = GPTVectorStoreIndex.from_documents(documents)

# llama index 0.6 replaces index.save_to_disk() with index.storage_context.persist()
# json files will be stored in a storage/ directory instead of index_new.json
# index.save_to_disk('index_news.json')

index.storage_context.persist()