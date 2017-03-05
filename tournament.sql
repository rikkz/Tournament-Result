-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
Drop database if exists tournament;

Drop table if exists player CASCADE;

Drop table if exists match CASCADE;

CREATE DATABASE tournament;

\c tournament;

CREATE TABLE player( id serial PRIMARY KEY , name text );

CREATE TABLE match( match_id serial PRIMARY KEY ,
                    winner INTEGER,
                    loser INTEGER,
                    FOREIGN KEY( winner) REFERENCES player( id ),
                    FOREIGN KEY( loser ) REFERENCES player( id ));

CREATE VIEW final_result as select player.id , player.name,
    COALESCE((SELECT COUNT(winner) FROM MATCH WHERE player.id = match.winner),0) AS wins,
    COALESCE((SELECT COUNT(*) FROM MATCH WHERE player.id = match.winner or player.id = match.loser),0) AS matches
    FROM player LEFT JOIN match on player.id = match.winner GROUP BY player.id ORDER BY wins DESC;


