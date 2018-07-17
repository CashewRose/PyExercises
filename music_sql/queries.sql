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
SELECT null, "Beauty from Pain", "03/29/2005", 2968, "Inpop", artist.Artistid,  Genre.genreid
FROM ARTIST, GENRE
WHERE Artist.Artistname = "Superchick"
AND Genre.label = "Punk" 

-- Using the INSERT statement, add some songs that are on that album to the Song table.

-- Do it explicitly

INSERT INTO Song(Title, SongLength, ReleaseDate, GenreId, ArtistId, AlbumId)
VALUES ("Alive", 166, "06/24/2008", 2, 28,  24)

-- Do it with a sub-select

INSERT INTO Song
SELECT null, "Stand in the Rain", 548, "03/29/2005", Genre.genreid, artist.Artistid,  Album.AlbumId
FROM ARTIST, GENRE, Album
WHERE Artist.Artistname = "Superchick"
AND Genre.label = "Punk"
AND Album.Title = "Beauty from Pain"


-- Write a SELECT query that provides the song titles, album title, and artist name for all of the data you just entered in. Use the LEFT JOIN keyword sequence to connect the tables, and the WHERE keyword to filter the results to the album and artist you added.

SELECT Song.Title, Artist.ArtistName, Album.Title
FROM Song
LEFT JOIN Artist
ON Artist.ArtistId = song.ArtistId
LEFT JOIN Album
ON Album.AlbumId = Song.AlbumId
WHERE Artist.Artistname = "Superchick"

-- Write a SELECT statement to display how many songs exist for each album. You'll need to use the COUNT() function and the GROUP BY keyword sequence.

SELECT count() AS "Number of Songs" , Album.Title AS "Album Title"
FROM Album
JOIN Song ON song.AlbumId = Album.AlbumId
GROUP BY Album.Title