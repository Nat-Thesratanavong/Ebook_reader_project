import sqlite3
from datetime import datetime
import aiosql
import os
import logging

logging.basicConfig(
    level=logging.INFO,         
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

logger = logging.getLogger(__name__)

class LibraryDatabase:
    def __init__(self, db_path = 'library.db'):
        self.db_path = db_path
        self._load_queries()
        self._create_table()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)
    
    def _load_queries(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        sql_path = os.path.join(base_dir, '..', 'assets', 'sql', 'books.sql')
        self.queries = aiosql.from_path(sql_path, "sqlite3")

    def _create_table(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        sql_path = os.path.join(base_dir, '..', 'assets', 'sql', 'schema.sql')
        with open(sql_path, 'r') as f:
            sql_script = f.read()
            try:
                with self._get_connection() as conn:
                    cursor = conn.cursor()
                    cursor.executescript(sql_script)
                    conn.commit()
            except Exception as e:
                logger.exception(f"An error has occcured while creating table.")
                raise
            

    def update_progress(self, book_hash, chapter_index, chapter_progress, total_book_progress ):
        
        with self._get_connection() as conn:
            conn.row_factory = sqlite3.Row
            try:
                self.queries.update_book_progress(conn, book_hash, chapter_index, chapter_progress, total_book_progress)
                conn.commit()
            except Exception as e:
                logger.exception(f"An error has occured while update book.")
                raise
            

    def book_exist(self, book_hash):

        with self._get_connection() as conn:
            conn.row_factory = sqlite3.Row
            try:
                exist = self.queries.book_exist(conn, book_hash)
                return exist
            except Exception as e:
                logger.exception(f"An error occured during checking book.")
                raise 
            
    # def add_book(self, book_hash):
        

