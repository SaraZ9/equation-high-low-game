# Equation Hi-Lo Game

**Equation Hi-Lo** is a unique fusion of mathematics and card games that maximizes player strategy and selection. Inspired by *The Devil's Plan* on Netflix, the game combines elements from three fundamental games: **Poker**, **Hi-Lo**, and the **24 game**. By emphasizing strategy over luck, Equation Hi-Lo reduces randomness, turning each round into a mathematical puzzle that requires critical thinking and careful decision-making.

## Game Rules

1. **Cards**:
   - There are 44 numeric cards numbered from 0 to 10, each with one of four types: **gold**, **silver**, **bronze**, and **dirt** (4 of each number-type combination).
   - Special cards: 4 square root (`√`) cards and 4 multiplication (`*`) cards.

2. **Setup**:
   - The dealer asks how many players will join the game, and each player starts with 1 coin for betting.
   - Each player is dealt a **hidden card** (must be a numeric card, not `*` or `√`). This hidden card is visible only to the player.
   - Each player is given three basic operation cards: `+`, `-`, and `/`.

3. **Gameplay**:
   - **Rounds of Dealing**:
     - In each round, the dealer gives each player one card from the deck.
     - If a player receives a `*` card, they must drop one of their `+`, `-`, or `/` operation cards in exchange. The dealer continues dealing until a numeric card is received.
     - If a player receives a `√` card, they keep it, and the dealer continues dealing until they receive a numeric card.
   - **First Bet Phase** (after two open cards):
     - Players can either match the previous player’s bet, raise, or fold.
     - The first player may pass, as can the second, but once any player bets, passing is no longer allowed for others.
     - The maximum bet a player can place is limited by the least number of coins held among all players.
   - **Final Card Deal**:
     - Each player receives a third open card.
   - **Equation Formulation Phase**:
     - Players have 5 minutes to create an equation using their hidden card, open cards, and available operations.
     - The square root (`√`) operation can only be applied to a single number in the equation.
   - **Final Bet Phase**:
     - Another betting round occurs, following the same rules as the first bet phase.

4. **Choosing High, Low, or Swing Bets**:
   - Each player chooses to bet either **High** (close to 20), **Low** (close to 1), or a **Swing Bet**.
   - Swing Bet: Players must create two equations, one targeting High and one targeting Low. To win, they must succeed in both bets.

5. **Determining the Winner**:
   - After all players reveal their equations, those who bet High compete to be closest to 20, and those who bet Low aim to be closest to 1.
   - If there is a tie:
     - For High bets, the player with the highest numeric card type wins (gold > silver > bronze > dirt).
     - For Low bets, the player with the lowest numeric card type wins (dirt > bronze > silver > gold).
   - Swing Bet players must win both High and Low targets to be considered victorious.
   - The winners of High and Low each receive half of the total pot. If there is an odd coin, it is discarded.

## How to Play

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/equation-high-low-game.git
   cd equation-high-low-game

2. Run the game
```python main_game.py```

3. Select Players and Start Game:
You can follow the instruction on the terminal to add human players, bots, or a combination of both.

## Adding Custom Bots

Would you like to add your own custom bot to Equation Hi-Lo? It’s easy to create a bot that can automatically make decisions and compete with other players.

### Use the Template:
Start by copying `template_bot.py`, which provides the basic structure for creating a bot. Save your new bot file in the `/bots` folder.

### Implement Core Functions
Each bot requires three core functions:

- **`welcome_msg()`**: Returns a brief message introducing your bot’s strategy to players.

- **`decision_for_drop(bot_data)`**: Defines which operation to drop if the bot receives a `*` card. The `bot_data` dictionary provides the bot's current state, including available operations.

- **`make_a_bet_and_equation(bot_data)`**: The main function where your bot will:
  - Choose a bet (`high` or `low`).
  - Form an equation using all number and operation cards exactly once.


## Future Improvement

This section provides an overview of active development efforts and future improvements planned for the Equation Hi-Lo Game.

1. **Betting Coins Functionality**:
   - Add betting mechanics with coins, enforce betting rules, and handle coin distribution based on the final results.
---

