-- name: update_book_progress
-- update book progress in the database
update books set (chapter_index, chapter_progress, total_book_progress) 
= (:chapter_index, :chapter_progress, :total_book_progress)
where hashed_book = :hashed_book