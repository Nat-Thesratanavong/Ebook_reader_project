import sqlite3
from datetime import datetime
import aiosql
import os

class library_database:
    def __init__(self, db_path = 'library.db'):
        self.db_path = db_path
        self._create_table()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)
    
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
                print(f"An error has occured: {e}")
            finally:
                conn.close()

    def update_progress(self, book_hash, chapter_index, chapter_progress, total_book_progress ):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        sql_path = os.path.join(base_dir, '..', 'assets', 'sql', 'books.sql')
        queries = aiosql.from_path(sql_path,"sqlite3")

        with self._get_connection() as conn:
            conn.row_factory =sqlite3.Row
            try:
                queries.update_book_progress(conn, book_hash, chapter_index, chapter_progress, total_book_progress)
                conn.commit()
            except Exception as e:
                print(f"An error has occured while update book: {e}")
            finally:
                conn.close()
            
            

