import typing
import orm
from orm import Base



def init_tables(database, replica_database=None):
    metadata = orm.utils.init_tables(Base, database, replica_database=replica_database)
    return metadata
