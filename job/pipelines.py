# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from .dbtools import DatabaseAgent
from .models.python import Python


class JobPipeline(object):
    def __init__(self):
        self.db_agent = DatabaseAgent()

    def process_item(self, item, spider):
        self.db_agent.add(
            kwargs=dict(item),
            orm_model=Python
        )
        return item
