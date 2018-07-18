-- Query all of the entries in the Genre table
SELECT *
FROM Genre

-- Using the INSERT statement, add one of your favorite artists to the Artist table.

INSERT INTO Artist(ArtistName, YearEstablished)
VALUES ("Superchick", 1999)

-- Using the INSERT statement, add one, or more, albums by your artist to the Album table.

-- Do it explicitly
INSERT INTO Album(Title, ReleaseDate, AlbumLength, Label, ArtistId, GenreId)
VALUES ("Rock What You Got", "06/24/2008", 4568, "Inpop", 28, 2)

-- Do it with a sub-select

INSERT INTO Album
SELECT null, "Beauty from Pain", "03/29/2005", 2968, "Inpop", Artist.ArtistId,  Genre.GenreId
FROM Artist, Genre
WHERE Artist.ArtistName = "Superchick"
AND Genre.Label = "Punk" 

-- Using the INSERT statement, add some songs that are on that album to the Song table.
-- Do it explicitly

INSERT INTO Song(Title, SongLength, ReleaseDate, GenreId, ArtistId, AlbumId)
VALUES ("Alive", 166, "06/24/2008", 2, 28,  24)

-- Do it with a sub-select

INSERT INTO Song
SELECT null, "Stand in the Rain", 548, "03/29/2005", Genre.GenreId, Artist.ArtistId,  Album.AlbumId
FROM Artist, Genre, Album
WHERE Artist.ArtistName = "Superchick"
AND Genre.Label = "Punk"
AND Album.Title = "Beauty from Pain"


-- Write a SELECT query that provides the song titles, album title, and artist name for all of the data you just entered in. Use the LEFT JOIN keyword sequence to connect the tables, and the WHERE keyword to filter the results to the album and artist you added.

SELECT Song.Title, Artist.ArtistName, Album.Title
FROM Song
LEFT JOIN Artist
ON Artist.ArtistId = Song.ArtistId
LEFT JOIN Album
ON Album.AlbumId = Song.AlbumId
WHERE Artist.ArtistName = "Superchick"

-- Write a SELECT statement to display how many songs exist for each album. You'll need to use the COUNT() function and the GROUP BY keyword sequence.

SELECT COUNT() AS "Number of Songs" , Album.Title AS "Album Title"
FROM Album
JOIN Song ON Song.AlbumId = Album.AlbumId
GROUP BY Album.Title

-- Write a SELECT statement to display how many songs exist for each artist. You'll need to use the COUNT() function and the GROUP BY keyword sequence.

SELECT COUNT() AS "Songs each Artist Has", Artist.ArtistName AS "Artist"
FROM Artist
JOIN Song ON Song.ArtistId = Artist.ArtistId
GROUP BY Artist.ArtistName

-- Write a SELECT statement to display how many songs exist for each genre. You'll need to use the COUNT() function and the GROUP BY keyword sequence.

SELECT COUNT() AS "Number of Songs in Genre", Genre.Label AS "Genre"
FROM Genre
JOIN Song ON Song.GenreId = Genre.GenreId
GROUP BY Genre.Label

-- Using MAX() function, write a select statement to find the album with the longest duration. The result should display the album title and the duration.

SELECT MAX(Album.AlbumLength) AS "Album Duration", Album.Title
FROM Album

-- Using MAX() function, write a select statement to find the song with the longest duration. The result should display the song title and the duration.

SELECT MAX(song.SongLength) AS "Song Duration", Song.Title
FROM Song

-- Modify the previous query to also display the title of the album.

SELECT MAX(song.SongLength) AS "Song Duration", song.Title AS "Song Title", Album.Title "Title of Album"
FROM Song
JOIN Album ON Album.AlbumId = Song.AlbumId