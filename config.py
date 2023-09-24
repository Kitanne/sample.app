import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://finadv-cosmosdb.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'ka45jSE1cBzLWJxKIr4u2zSmhWc29rHX8qgp7e84FZbbYjGDSFiZhPbmHO6pI0ANqgS3REeBiR5DACDb4JUyUw=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'ToDoList'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Items'),
}