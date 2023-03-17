import os
import psycopg2
from psycopg2.extras import DictCursor


class DBConnection:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def get_connection(self, cf=None):
        conn_params = {
            "user": self.user,
            "password": self.password,
            "host": self.host,
            "port": self.port,
            "database": self.database
        }
        conn = psycopg2.connect(**conn_params)
        cursor_factory = DictCursor if cf == "dict_cursor" else None
        cursor = conn.cursor(cursor_factory=cursor_factory)
        return conn, cursor
