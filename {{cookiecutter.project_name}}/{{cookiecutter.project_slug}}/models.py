import typing
{% if cookiecutter.sql_database == 'y' -%}
import orm
from orm import Base

class SampleModel(Base):
    pass 

    class Config:
        table_name = "sample_model"
        table_config = {
            "id": {"primary_key": True, "index": True, "unique": True},
        }

def init_tables(database, replica_database=None):
    metadata = orm.utils.init_tables(Base, database, replica_database=replica_database)
    return metadata
{% endif %}



