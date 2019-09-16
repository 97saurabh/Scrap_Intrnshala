# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector

class InternshalaPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        #print("CONNECTION STABLISH")
        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Saurabh@123",
            database="jobs_db"

        )
        self.curr=self.conn.cursor()
    def create_table(self):
        #print("CREATE TABLE")
        self.curr.execute("DROP TABLE IF EXISTS JOBS")
        self.curr.execute("""
                    create table JOBS(
                    title text,
                    company text,
                    location text,
                    start_date text,
                    duration text,
                    link text
                    )""")

    def process_item(self, item, spider):
        #print("STORIN G DATA")
        self.store_data(item)
        return item
    def store_data(self,item):
        self.curr.execute("""
                          insert into JOBS values(%s,%s,%s,%s,%s,%s)""",(item["title"],item["company"],item["location"],item["start_date"],item["duration"],item["link"]))
        self.conn.commit()
