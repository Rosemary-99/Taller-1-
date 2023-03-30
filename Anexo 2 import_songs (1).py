import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, Text, ARRAY
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
  
#conn1.autocommit = True

#cursor = conn1.cursor()

data = pd.read_csv('C:\\Users\\Rosemary\\segundoRosemary\\normal_track3.csv')
data = data.drop("Unnamed: 0", axis=1)

# create a metadata object
metadata = MetaData(bind=engine)

# define your table structure
table_name = Table('songs', metadata,
    Column('id', Text, primary_key=True),
    Column('name', Text),
    Column('popularity', Integer),
    Column('duration_ms', Integer),
    Column('explicit', Integer),
    Column('artists', ARRAY(Text)),
    Column('id_artists', ARRAY(Text)),
    Column('release_date', Text),
    Column('danceability', Float),
    Column('energy', Float),
    Column('key', Float),
    Column('loudness', Float),
    Column('mode', Float),
    Column('speechiness', Float),
    Column('acousticness', Text),
    Column('instrumentalness', Text),
    Column('liveness', Text),
    Column('valence', Text),
    Column('tempo', Text),
    Column('time_signature', Text)
)

# create the table
metadata.create_all()

# insert data into the table
data.to_sql('songs', conn, if_exists='replace', index=False)