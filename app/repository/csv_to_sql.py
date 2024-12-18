import pandas as pd
from app.db.database import  engine


def fill_the_database(file_path):
    df = pd.read_csv(file_path, encoding='iso-8859-1')
    df.to_sql('terror', engine, if_exists='append', index=False)

