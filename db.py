from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from time import gmtime, strftime
from datetime import datetime

strftime("%Y-%m-%d %H:%M:%S", gmtime())

# ModelBase = declarative_base() 

schema = 'mysql+pymysql://ubq_ems_user@localhost:ubq2018@23.20.246.186:3306/ubq_ems_db'
engine = create_engine(schema, pool_size=10 , max_overflow=-1, pool_recycle=1200)
connection = engine.connect()

# create_table = text('CREATE TABLE IF NOT EXISTS simulation_data_2 (time datetime DEFAULT NULL, customer_id varchar(32) DEFAULT NULL, loc_x int(32) DEFAULT NULL, loc_y int(32) DEFAULT NULL, product_id varchar(32) DEFAULT NULL) ENGINE=InnoDB DEFAULT CHARSET=latin1')
# connection.execute(create_table)

metadata = MetaData()
locations = Table('simulation_data_2', metadata,
    Column('time', DateTime),
    Column('customer_id', String),
    Column('loc_y', String),
    Column('loc_y', String),
    Column('product_id', String),
)


def bulk_insert(simulations):
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    locs = list(map(lambda data : {'time': time, 'customer_id' : data[0], 'loc_x': data[1], 'loc_y' : data[2], 'product_id': 'na'}, simulations))    
    result = connection.execute(locations.insert(), locs)

# data = [
#     ('c60', 1, 2,),
#     ('c60', 1, 3),
#     ('c60', 1, 4),
# ]
# bulk_insert(data)