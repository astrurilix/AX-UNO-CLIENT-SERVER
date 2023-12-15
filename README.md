# AX-UNO-CLIENT-SERVER-COMPUTING

Multiplayer UNO using Python (V1.0)

Created By

`21.K1.0017  KENLY KRISAGUINO SANTOSO`

`21.K1.0012  SOEN ANITA SANJAYA`

###### HOW TO START:

1. Setup your Server IP ADDRESS in `server_connection.txt` (Replace existing configuration, NO SPACE ALLOWED)
2. Setup `self.server` in `network.py` value to be the server's IP (Configured in `server_connection.txt`)
3. Start ``server.py``
4. Start ``client.py`` (Need 2 client to start the game)
5. You can play the game now

###### **GAMEPLAY RULE:**

1. Each player start with 7 cards each
2. Player can only play if the card on the deck has the same value or has the same color as the card shown on the center of the screen
3. There are special cards and wild cards. It has it's own ability.
   1. **Special Cards**
      1. Plus 2 (d2) : Add 2 cards to the enemy player
      2. Reverse (rev) : Skip the enemy player's turn
      3. Skip (skip) : Skip the enemy player's turn
   2. **Wild Cards**
      1. Change Color (cc) : Change current color to the available color.
      2. Plus 4 (p4) : Add 4 cards to the enemy player and change the current color to the available color.
4. Wild card can be played if it is the player's turn and with any color in the center of the screen
5. If the player has less than 2 cards, a UNO button will show up
6. If player has only 1 card, they MUST press the UNO button in the range of 5 second
7. If the player failed to press the UNO button between the range of 5 second, they will get 2 additional cards as punishment
8. If the player succeeded, they won't get punished
9. If a player emptied their deck of cards, they win the game
