# Rock Paper Scissors

ho3-battleship is a Python terminal game, which runs in the mock terminal on Heroku

Users can try to beat the computer by finding all of the computer's battleships before the computer finds theirs. Each battleship occupies one cell or more on board respecting to the user grid selection at the start of the game.

![Responsive Mockup](./assets/screenshots/mockup.png)

## How to play

ho3-battleship is based on classic pen-and-paper game. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)).

In this version, the player can choose between three size of the grid.

After choosing the grid size you should setup your ship's positions. And also computer generating random position for it's ships that you can't see them on it's board.

Now the game has begun and you should guess the positions of the computer's ships each turn. Of course computer will try to guess your ship's positioning and you should find the before the computer.

When you or computer sink all of their opponent's ships the winner will be announced.

## Features

- __Instruction of the game__

    - There is an instruction for the game that user understand the rule of the game. User also should chosse the size of the grid.

![Instruction](./assets/screenshots/instruction.png)

- __Ship Location__

    - After choosing the size user should start positioning his/her ships on the board. After choosing a position you can see the ship emoji on your board.

![Ship Location](./assets/screenshots/ship-location.png)

- __Shooting each other__

    - Now the fun has begun. User should try to guess the position of the computer's ships if the user hit you can see a flame emoji on the board, if the user miss there will be a cross emoji on the board.

![Matching View](./assets/screenshots/matching-view.png)

- __Winner or Loser__

    - When any opponent manage to sink all of the opponent's ships the winner will be announced and ask the user that if he wants to play the game again or quit.

![Winner or Loser](./assets/screenshots/winner-looser.png)

## Bugs

  - There was a bug while announcing the winner twice, fixed it with changing the while loop with if. 

## Testing

  - The project is responsive in all devices


### Validator testing

- PEP8

  - No errors were returned from PEP8online.com

### Remaining Bugs

- No bugs remaining

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

- Steps for deployment:

  - Fork or clone this repository

  - Create a new Heroku app

  - Set the buildpacks to Python and NodeJS in that order

  - Link the Heroku app to the repository

  - Click on Deploy

## Credits

- Code Institute for the deployment terminal

- Wikipedia for the details of the Battleship game

- Clear screen function from [Fabio Musanni - Programming Channel](https://www.youtube.com/watch?v=Kmu6rmPQt4c&ab_channel=FabioMusanni-ProgrammingChannel)  youtube channel.