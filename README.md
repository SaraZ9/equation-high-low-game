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
---

