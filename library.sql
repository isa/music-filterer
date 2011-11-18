CREATE TABLE artist (
   id INTEGER NOT NULL PRIMARY KEY,
   name VARCHAR(255) NOT NULL
);

CREATE TABLE song (
   id INTEGER NOT NULL PRIMARY KEY,
   album VARCHAR(255),
   title VARCHAR(255) NOT NULL,
   time_signature NUMERIC NOT NULL,
   minor_major NUMERIC NOT NULL,
   key NUMERIC NOT NULL,
   energy REAL NOT NULL,
   tempo REAL NOT NULL,
   danceability REAL NOT NULL,
   loudness REAL NOT NULL,
   duration REAL NOT NULL,
   artist_id INTEGER NOT NULL REFERENCES artist(id) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE term (
   id INTEGER NOT NULL PRIMARY KEY,
   value VARCHAR(255) NOT NULL,
   artist_id INTEGER NOT NULL REFERENCES artist(id) DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE mood (
   id INTEGER NOT NULL PRIMARY KEY,
   value VARCHAR(255) NOT NULL,
   artist_id INTEGER NOT NULL REFERENCES artist(id) DEFERRABLE INITIALLY DEFERRED
);

CREATE INDEX song_artist_idx on song(artist_id);
CREATE INDEX term_artist_idx on term(artist_id);
CREATE INDEX mood_artist_idx on mood(artist_id);


