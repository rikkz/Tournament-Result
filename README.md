# Tournament-Result

<h2> Introduction </h2>
<p> This is a python module that uses the PostgreSQL database to keep track of players and matches in a game tournament using swiss system
</p>

<h2> Code Templates </h2>
<ul type="disc">
  <li>tournament.py - This file provides access to database via a library of functions required for tournament game.</li>
  <li>tournament_test.py - This is a client program for testing implementaion of code which uses functions written in the tournament.py module.</li>
  <li>tournament.sql - This file describes the database schema.</li>
</ul> 

<h2> Functions in tournament.py </h2>
<ul type = "disc">
  <li><b> registerPlayer(name) </b></li>
  <p> Adds a player to the tournament by putting an entry in the database. The database assigns a unique ID number to the player. </p>
  <li><b> countPlayers() </b></li>
  <p> Returns the number of currently registered players. </p>
  <li><b> deletePlayers() </b></li>
  <p> Clear out all the player records from the database. </p>
  <li><b> reportMatch(winner, loser) </b></li>
  <p> Stores the outcome of a single match between two players in the database. </p>
  <li><b> deleteMatches() </b></li>
  <p> Clear out all the match records from the database. </p>
  <li><b> playerStandings() </b></li>
  <p> Returns a list of (id, name, wins, matches) for each player, sorted by the number of wins each player has. </p>
  <li><b> swissPairings() </b></li>
  <p> This function generates and returns a list of pairings according to the Swiss system. This function use playerStandings() to find the ranking of players. </p>
</ul>

<h2> Instructions </h2>
<ul type = "disc">
  <li><b> Set Up Databse </b>
    <p> Set up database using following command: </p>
    <pre> $ psql -f tournament.sql</pre>
  </li>
  <li><b> Run Module </b>
    <pre>$ python tournament_test.py </pre>
  </li>
</ul>
