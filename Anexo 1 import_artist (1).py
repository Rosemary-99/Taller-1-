import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, Text
import psycopg2


# establish connections
conn_string = 'postgresql://postgres:12345@127.0.0.1/Spotify'
  
engine = create_engine(conn_string)
conn = engine.connect()
conn1 = psycopg2.connect(
    database="Spotify",
  user='postgres', 
  password='12345', 
  host='127.0.0.1', 
  port= '5432'
)
  

data = pd.read_csv('C:\\Users\\Rosemary\\segundoRosemary\\normal_artist.csv')
data = data.drop("Unnamed: 0", axis=1)
# create a metadata object
metadata = MetaData(bind=engine)

# define your table structure
table_name = Table('artists', metadata,
    Column('id', Text, primary_key=True),
    Column('followers', Float),
    Column('genres', String),
    Column('name', String),               
    Column('popularity', String),
)

# create the table
metadata.create_all()

# insert data into the table
data.to_sql('artists', conn, if_exists='replace', index=False)