import getpass
import os

openai = getpass.getpass("openai api pass:")
pc = getpass.getpass("pinecone api pass:")

os.environ["OPENAI_API_KEY"] = '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'
os.environ['PINECONE_API_KEY'] = '582a0d83-c1c8-4b92-94b9-675284ad59c8'
os.environ['PINECONE_INDEX_NAME'] = 'starter-index'