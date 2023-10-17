import sqlite3
from flask import g, jsonify


class SqliteManager:
    def __init__(self, name, schema):
        self.name = name
        self.schema = schema

        self.initialize_database()

    def connect(self):
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(self.name)
        db.row_factory = sqlite3.Row
        return db

    def disconnect(self):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

    def initialize_database(self):
        db = self.connect()

        


        # db = self.connect()
        # cur = db.cursor()        

        # # Check if the table(s) exists. If not, create them.
        # # Note: this does not verify the columns match the schema.
        # for table in self.schema:       
        #     table_name = table['table']
        #     query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"
        #     cur.execute(query)
        #     print(cur.rowcount)
        #     if (cur.rowcount == 0):
        #         is_initial = True
        #         query = f"CREATE TABLE {table_name}("
        #         for col in table['columns']:
        #             if (is_initial):
        #                 query += f"{col}"
        #                 is_initial = False
        #             else:
        #                 query += f", {col}"
                
        #         query += ")"
        #         print(query)
        #         #cur.execute(query)
                
        #         db.commit()


        
        # db.commit()

        # cur.close()
        # db.close()

    def create_audit(self):
        pass

    def read_all_clients(self):
        pass

    # This is connect()
    # def get_db():
    #     db = getattr(g, '_database', None)
    #     if db is None:
    #         db = g._database = sqlite3.connect(DB_NAME)
    #     return db

    # Got this helper function from the docs, along with
    #   a lot of the general patterns used here.
    # https://flask.palletsprojects.com/en/2.3.x/patterns/sqlite3/
    def query(self, query, args=(), one=False):
        cur = self.connect().execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv 
















    def create_audit(self):
        return {"create_result": True}


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
