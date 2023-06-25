import os
from dotenv import load_dotenv
from llama_index import GPTSimpleVectorIndex, QuestionAnswerPrompt, download_loader

load_dotenv()
openai_api_key = os.environ.get('OPENAI_API_KEY')

DatabaseReader = download_loader('DatabaseReader')

reader = DatabaseReader(
    scheme="postgresql",  # Database Scheme
    host="localhost",  # Database Host
    port="5432",  # Database Port
    user="postgres",  # Database User
    password="FakeExamplePassword",  # Database Password
    dbname="postgres",  # Database Name
)

# Assuming `query` is defined somewhere

query = f"""
SELECT
    CONCAT(name, ' is ', age, ' years old.') AS text
FROM public.users"""

documents = reader.load_data(query=query)

index = GPTSimpleVectorIndex(documents)

index.save_to_disk('')
