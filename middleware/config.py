# Stdlib imports
import os

DEBUG = bool(os.getenv('NEWSAI_KNOWLEDGE_DEBUG', False))
ALCHEMY_API = os.getenv('NEWSAI_ALCHEMY_API', '')
GOOGLE_KNOWLEDGE_API = os.getenv('NEWSAI_GOOGLE_KNOWLEDGE_API', '')
NYTIMES_SEMANTIC_API = os.getenv('NEWSAI_NYTIMES_SEMANTIC_API', '')
CONTEXT_API_USERNAME = os.environ.get('NEWSAI_CONTEXT_API_USERNAME', '')
CONTEXT_API_PASSWORD = os.environ.get('NEWSAI_CONTEXT_API_PASSWORD', '')

BASE_URL = 'https://context.newsai.org/api'
