# Equation Hi-Lo Game

**Equation Hi-Lo** is a strategic math-based game inspired by *The Devil's Plan* on Netflix. In this game, players are given a set of numeric and operation cards and must form equations to reach specific target values. The game combines elements of mathematics and psychology, challenging players to create equations that are either close to 1 ("Low") or 20 ("High") while making strategic decisions with limited operation cards.

## Game Rules

1. **Objective**: Players aim to create equations that are as close as possible to the target values of 1 (Low) or 20 (High).
2. **Cards**: Each player is dealt:
   - One hidden numeric card (not visible to other players).
   - Three visible numeric cards over three rounds.
3. **Operations**:
   - Players receive a set of basic operations: `+`, `-`, `/`, and `*`.
   - During the game, players may receive special cards: `√` (square root) or an additional `*`. When a `*` card is drawn, players must drop one of their other operations (`+`, `-`, or `/`).
4. **Creating Equations**:
   - Players must use their hidden and open cards along with their available operations to create an equation.
   - The goal is to either bet on **High** (closest to 20) or **Low** (closest to 1).
5. **Determining the Winner**:
   - After all players create their equations, the player with the result closest to 20 (for High bets) and the player closest to 1 (for Low bets) are declared the winners for the round.

## How to Play

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/equation-high-low-game.git
   cd equation-high-low-game
