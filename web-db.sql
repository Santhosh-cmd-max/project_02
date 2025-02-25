CREATE DATABASE imdb_movies;

USE imdb_movies;

CREATE TABLE movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    release_year VARCHAR(10),
    duration VARCHAR(50),
    rating VARCHAR(50),
    imdb_score FLOAT,
    number_of_votes VARCHAR(50)
);

select * from movies;

SELECT COUNT(*) FROM movies;

select Title, imdb_score
from movies
order by imdb_score desc
limit 5;

select Count(release_year), release_year from movies
group by release_year;

select title, release_year from movies
where release_year = 1994;

SELECT title, number_of_votes 
FROM movies 
ORDER BY number_of_votes DESC 
LIMIT 5;




