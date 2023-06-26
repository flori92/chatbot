from llama_index import download_loader

DatabaseReader = download_loader('DatabaseReader')
#please give your own dbs informations here
reader = DatabaseReader(
    scheme = "postgresql", # Database Scheme
    host = "localhost", # Database Host
    port = "5432", # Database Port
    user = "postgres", # Database User
    password = "FakeExamplePassword", # Database Password
    dbname = "postgres", # Database Name
)

query = f"""This your querysect to interrrogate your dbs
"""

documents = reader.load_data(query=query)
