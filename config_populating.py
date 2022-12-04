#!/usr/bin/python3

import random

class Table:
    name = "table_name"
    attributes = {'firstAttribute': 1, 
                'secondAttribute' : "name" }

    def __init__(self, name : str, attributes : dict):
        self.name = name
        self.attributes = attributes
    
    def add(self, conn : Connection, values : set(tuple, ..., tuple)):
        sql = f"INSERT INTO {self.name} VALUES "
        for value in values:
            sql += sql + str(value) + ','
        sql = sql[:-1]
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        return cur.lastrowid

    def generateValues(names : list) -> set:
        values = set()
        for i in range(len(names)):
            # you can set only the NOT NULL attributes in your table
            value = (i, names[i], "null")
            values.add(value)
        return values

    
    def generateValues(max=30, differents=False) -> set:
        values = set()
        for i in range(1, max):
            value = (random.randint(1, max), random.randint(1,max))
        if not (value[0] == value[1] and differents):
            values.add(value)
        return values

    def populate(self, values : set):
        self.add(conn, values)
if "__main__" == __name__:
    
    pass