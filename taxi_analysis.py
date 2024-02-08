import pandas as pd 
from sqlalchemy import  create_engine , text

engine = create_engine('postgresql://postgres:Salam123@localhost:5432/postgres')
engine.connect()

try:
    # Connect to the database
    with engine.connect() as connection:
        # Execute a test query
        result = connection.execute(text("SELECT 1"))
        # Fetch the result of the test query
        print(result.fetchone())
        print("Connection successful.")
except Exception as e:
    print("An error occurred:", e)

df = pd.read_parquet('yellow_tripdata_2023-01.parquet')

# print(pd.io.sql.get_schema(df , name='yellow_taxi_data' , con=engine))

df.head(n=0).to_sql(name='postgres' , con = engine)