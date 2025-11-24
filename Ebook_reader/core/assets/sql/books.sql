-- name: update_book_progress
-- update book progress in the database
update books set (chapter_index, chapter_progress, total_book_progress, last_read) 
= (:chapter_index, :chapter_progress, :total_book_progress,:last_read)
where hashed_book = :hashed_book

-- name: get_reading_progress
-- get reading progress
SELECT current_chapter, chapter_progress, total_book_progress FROM books WHERE hashed_book = :hashed_book

-- name: book_exist
-- check if book exist in the database
select hashed_book from books where hashed_book = :hashed_book


-- name: insert_book
-- insert new book into the database
insert into books (hashed_book, 
file_path, 
cover_path, 
title, 
author, 
current_chapter, 
chapter_progress, 
total_book_progress, 
last_read) values (
:hashed_book, 
:file_path,
:cover_path,
:title,
:author,
coalesce(:current_chapter,0),
coalesce(:chapter_progress,0.0),
coalesce(:total_book_progress,0.0),
:last_read
)

-- name: get_all_books
-- get all books in the library
SELECT hashed_book, file_path, cover_path, title, author, current_chapter, chapter_progress, total_book_progress, last_read 
FROM books 
ORDER BY last_read

-- name: get_book_count
-- get Total number of books
select COUNT(hashed_book) FROM books

-- name: get_author_stats
-- get Total number of each book for Author
select author, COUNT(hashed_book) from books group by author

-- name: get_genres_stats
-- get Total number of books for each genre
select genre, COUNT(hashed_book) from books group by genre

-- name: get_reading_progress
-- get reading progress
SELECT current_chapter, chapter_progress, total_book_progress FROM books WHERE hashed_book = :hashed_book

-- name: get_book
-- get book by hash
SELECT hashed_book, file_path, cover_path, title, author, current_chapter, chapter_progress, total_book_progress, last_read
FROM books
WHERE hashed_book = :hashed_book
