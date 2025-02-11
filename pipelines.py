# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from time import sleep
from itemadapter import ItemAdapter
import re
from .db_connection.db_helper import db_helper
from .db_connection.models import BASE

class AnimePipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name == "name":
                sleep(1)
                adapter[field_name] = re.sub(r" \[\d.*", "", adapter[field_name])
        return item
    
class DatabaseAdapter:
    
    def process_item(self, item, spider):
        # Insert item into the database
        BASE.metadata.create_all(db_helper.engine)
    
        with db_helper.session() as session:
            session.add(item)
            session.commit()
