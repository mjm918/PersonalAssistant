import sqlite3


class Data:
    connection = None

    def __init__(self):
        self.connection = sqlite3.connect('localdata.db')

    def __enter__(self):
        return self

    def select(self, query):
        return self.connection.execute(query)

    def insert(self, query):
        try:
            self.connection.execute(query)
            self.connection.commit()
            return 1
        except sqlite3.OperationalError:
            return -1

    def update_or_delete(self, query):
        try:
            self.connection.execute(query)
            self.connection.commit()
            return self.connection.total_changes
        except sqlite3.OperationalError:
            return -1

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


