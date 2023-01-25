# WUNO (Like Uno with Words)
A game by Ben Snyder, Daniel Cruz, Theo McGlashan, and Susanne Goldstein

## Controls
- Mouse: select and confirm cards, interact with buttons
- Space/Return: end turn

## Description and Rules
An Uno-like word game using letters instead of numbers, also taking inspiration from the word game Ghost. Four players take turns placing letter cards in the center, building a word by adding letters onto the end. Players begin with five cards, and a player wins when they have no cards remaining.
- A player may draw a card from the deck at any point, giving them more options to continue the current word.
- When a player places a card they believe completes the word, they may state it is complete. If they are correct, the word is reset; if not, addition to the word continues and the player draws two cards from the deck. The word must be three letters or more in order to claim complete.
- If a player believes the card placed by the previous player completes the word, they may state it is complete before placing a card. If they are correct, the word is reset and the previous player draws two cards; if not, addition to the word continues and the current player draws two cards.
- If a player believes the current word cannot be added to to form a valid word, they may raise a challenge before placing a card. If they are correct, the previous player draws all cards from the center; if not, the current player draws all cards from the center.
- The distribution of cards in the deck is exactly the same as that of Scrabble tiles.

## Notes
- This package's code contains remnants of attempts to allow for local multiplayer using socket and json. We got to the point where game data was successfully being transmitted between devices, but due to time constraints we weren't able to figure out how to use this data to sync game states.
- The game is also currently only functional for four players; however, with some minor changes it could be played with two or three.