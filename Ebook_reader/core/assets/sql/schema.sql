
CREATE TABLE IF NOT EXISTS books (
hashed_book TEXT PRIMARY KEY,
file_path TEXT,
cover_path TEXT,    
title TEXT,
author TEXT,
current_chapter INTEGER DEFAULT 0,
chapter_progress REAL DEFAULT 0.0,
total_book_progress REAL DEFAULT 0.0,
last_read TIMESTAMP
);

CREATE INDEX IF NOT EXISTS hashed_book_idx ON books (hashed_book);
            