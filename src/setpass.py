import getpass
import os

openai_pass = getpass.getpass("openai api pass:")
os.environ["OPENAI_API_KEY"] = openai_pass

