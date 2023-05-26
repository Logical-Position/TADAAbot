import sqlite3

class SqliteManager:
    def __init__(self, name, schema):
        self.name = name
        self.schema = schema

        self.table = 'audits'
        self.cols = [
            'client',
            'domain',
            'data'
        ]

    def connect(self):
        return sqlite3.connect(self.name)

    def initialize_database(self):
        db = self.connect()
        cur = db.cursor()

        # Check if the table exists
        # Create it if it doesn't
        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.table}'")
        if (cur.rowcount == 0):
            cur.execute(f"CREATE TABLE {self.table}({self.cols[0]}, {self.cols[1]}, {self.cols[2]})")
            db.commit() 
        
        db.commit()

        cur.close()
        db.close()





    # Starter CRUD Functions
    # -- Deprecated --

    def create(self):
        db = self.connect()
        cur = db.cursor()

        # Check if the table exists
        # Create it if it doesn't
        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.table}'")
        if (cur.rowcount == 0):
            cur.execute(f"CREATE TABLE {self.table}({self.cols[0]}, {self.cols[1]}, {self.cols[2]})")
            db.commit()

        # Dummy data for now
        data = [
            ('AM Star Construction Inc.', 'https://metalbuildingsales.com/', 'this-should-point-to-another-table'),
            ('Elegance Lamps', 'https://www.elegancelamps.com/', 'this-should-point-to-another-table')
        ]

        # There shoudn't be a loop once real data is used
        # Only one datum should be pass to the function
        for item in data:
            name = item[0]
            cur.execute(f"INSERT INTO audits VALUES ('{item[0]}', '{item[1]}', '{item[2]}')")
        
        db.commit()

        cur.close()
        db.close()
        return {"create_result": True}

    def read(self):
        db = self.connect()
        cur = db.cursor()
        res = cur.execute(f"SELECT * FROM {self.table}")
        data = res.fetchall()
        cur.close()
        db.close()
        return {"read_result": data}

    def update(self):
        return {"update_result": False}

    def delete(self):
        db = self.connect()
        cur = db.cursor()
        res = cur.execute(f"DELETE FROM {self.table}")
        db.commit()
        cur.close()
        db.close()
        return {"delete_result": True}
