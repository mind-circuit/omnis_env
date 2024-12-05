# omnis/config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database configuration
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

# Web3 configuration
WEB3_PROVIDER_URI = os.getenv('WEB3_PROVIDER_URI')

# Private keys
PRIVATE_KEY = os.getenv('PRIVATE_KEY')

# RabbitMQ configuration
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
RABBITMQ_PORT = os.getenv('RABBITMQ_PORT')

# DeFi protocol addresses
UNISWAP_ROUTER_ADDRESS = os.getenv('UNISWAP_ROUTER_ADDRESS')
