#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    conn = connect()
    curr = conn.cursor()
    curr.execute("TRUNCATE TABLE match CASCADE")
    conn.commit()
    conn.close()

def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    curr = conn.cursor()
    curr.execute("TRUNCATE TABLE player CASCADE")
    conn.commit()
    conn.close()

def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    curr = conn.cursor()
    curr.execute("SELECT COUNT(*) FROM player")
    count = curr.fetchone()[0]
    conn.close()
    return count

def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    curr = conn.cursor()
    curr.execute("INSERT INTO player(name) VALUES(%s)",(name,))
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    curr = conn.cursor()
    curr.execute("SELECT * FROM final_result")
    answer = curr.fetchall()
    conn.close()
    return answer



def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    curr = conn.cursor()
    curr.execute("INSERT INTO match(winner,loser) VALUES(%s,%s)",(winner,loser,))
    conn.commit()
    conn.close()



def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    list = []
    player_standing = playerStandings()
    arr_len = len( player_standing )
    for i in range( 0 , arr_len - 1 , 2 ):
        pair = (player_standing[i][0] ,player_standing[i][1],player_standing[i+1][0],player_standing[i+1][1])
        list.append(pair)
    return list


