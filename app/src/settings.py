import os

DATABASE_URL = os.getenv('DATABASE_URL', 'mysql+pymysql://user:password@db:3306/text_classification')
