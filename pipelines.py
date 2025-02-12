# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from time import sleep
from itemadapter import ItemAdapter
import re
from datetime import datetime
from .db_connection import db_helper, Anime

class AnimePipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name == "name":
                sleep(1)
                adapter[field_name] = re.sub(r" \[\d.*", "", adapter[field_name])
        adapter['date_of_production'] = re.sub(r"^c\s*", "", adapter['date_of_production']) 
        adapter['date_of_production'] = datetime.strptime(adapter["date_of_production"], "%d.%m.%Y").date()  
        adapter["age_rating"] =  re.search(r"\((.*?)\)", adapter['age_rating']).group(1)
        return item
    
class DatabaseAdapter:
    def process_item(self, item, spider):
        # Insert item into the database    
        with db_helper.session() as session:  # Using a context manager to ensure the session is closed automatically
            anime = Anime(**item)
            session.add(anime)
            session.commit()
        return item
