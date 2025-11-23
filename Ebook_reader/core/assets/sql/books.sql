-- name: update_book_progress
-- update book progress in the database
update books set (chapter_index, chapter_progress, total_book_progress, last_read) 
= (:chapter_index, :chapter_progress, :total_book_progress,:last_read)
where hashed_book = :hashed_book

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