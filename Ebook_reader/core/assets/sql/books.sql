-- name: update_book_progress
-- update book progress in the database
update books set (chapter_index, chapter_progress, total_book_progress) 
= (:chapter_index, :chapter_progress, :total_book_progress)
where hashed_book = :hashed_book

-- name: book_exist
-- check if book exist in the database
select hashed_book from books where hashed_book = :hashed_book