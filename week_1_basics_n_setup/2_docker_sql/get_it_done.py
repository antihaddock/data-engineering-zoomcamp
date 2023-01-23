import pandas as pd
from sqlalchemy import create_engine


engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
engine.connect()

df = pd.read_parquet('/home/antihaddock/Repos/data-engineering-zoomcamp/data/yellow_tripdata_2019-01.parquet')

df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

df.to_sql(name='yellow_tripdata_trip', con=engine, index=False)