import random
import math
import time

# Define deck with cards (numeric cards with types and operation cards)
numeric_cards = [(n, t) for n in range(11) for t in ["gold", "silver", "bronze", "dirt"]]  # Cards 0-10 with types
operation_cards = ['+', '-', '/', '*', '√'] * 4  # 4 of each operation card

# Shuffle the deck
deck = numeric_cards + operation_cards
random.shuffle(deck)

def deal_hidden_card():
    """Deal a hidden numeric card, ensuring it's not an operation card."""
    while True:
        card = deck.pop()
        if isinstance(card, tuple):  # It's a numeric card
            return card

def deal_card():
    """Deal a visible numeric card or additional operation cards as needed."""
    while True:
        card = deck.pop()
        if isinstance(card, tuple) or card == "√" or card == "*":
            return card

def initial_setup():
    """Set up the game: define players and assign each a hidden card."""
    while True:
        try:
            player_count = int(input("Enter the number of players: "))
            if player_count < 2:
                print("There must be at least 2 players.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    players = {f"Player {i+1}": {'hidden_card': None, 'open_cards': [], 'operation_cards': ['+', '-', '/']} for i in range(player_count)}
    
    # Deal hidden cards to each player with instructions for viewing them individually
    for player in players:
        input(f"{player}, please ensure only you are looking at the screen. Press Enter when ready to see your hidden card.")
        players[player]['hidden_card'] = deal_hidden_card()
        print(f"{player}, your hidden card is: {players[player]['hidden_card']}")
        input("Memorize your hidden card. Press Enter when ready to clear the screen for the next player.")
        print("\033[H\033[J")  # Clear screen (works in most terminals)
    
    return players

def deal_round_card_with_rules(player, player_data):
    """Deal a round card following the rules for * and √ cards."""
    while True:
        card = deal_card()
        if card == "*":
            print(f"{player} received '*'. They must drop one of '+', '-', or '/'.")
            while True:
                drop = input(f"{player}, which operation would you like to drop (+, -, /)? ").strip()
                if drop in player_data['operation_cards']:
                    player_data['operation_cards'].remove(drop)
                    player_data['operation_cards'].append('*')
                    break
                else:
                    print("Invalid choice. You can only drop '+', '-', or '/'.")
        elif card == "√":
            print(f"{player} received '√'.")
            player_data['operation_cards'].append("√")
        else:
            print(f"{player} received {card}.")
            player_data['open_cards'].append(card)
            break

def create_equation(hidden_card, open_cards, operation_cards):
    """Allow players to create an equation using their cards."""
    print("\nYour turn to create an equation!")
    print(f"Hidden card: {hidden_card}")
    print(f"Open cards: {open_cards}")
    print(f"Operation cards: {operation_cards}")
    print("Instructions:")
    print(" - Create an equation using the provided cards. Use spaces between numbers and operations.")
    print(" - Example format: '3 + 5 * 2' (you may use '√' for square root, which applies to the next number).")
    
    while True:
        equation = input("Enter your equation: ")
        result = evaluate_equation(equation)
        if result is not None:
            return equation, result
        print("Invalid equation format. Please try again.")

def evaluate_equation(equation):
    """Evaluates the player's equation and returns the result."""
    equation = equation.replace("√", "math.sqrt")
    try:
        result = eval(equation)
    except (SyntaxError, ZeroDivisionError, NameError) as e:
        return None
    return result

# def evaluate_equation(equation):
#     """Evaluates the player's equation and returns the result."""
#     # Replace the square root symbol with the correct math.sqrt function
#     equation = equation.replace("√", "math.sqrt")
    
#     try:
#         # Pass math in globals to allow use of math functions in eval
#         result = eval(equation, {"math": math})
#     except (SyntaxError, ZeroDivisionError, NameError) as e:
#         return None
#     return result


def determine_winners(players, high_low):
    """Determine the winning players for high or low bets based on equation results."""
    high_bets = {}
    low_bets = {}

    for player in players:
        equation, result = create_equation(players[player]['hidden_card'], players[player]['open_cards'], players[player]['operation_cards'])
        if high_low[player] == "high":
            high_bets[player] = result
            print(f"{player}'s result is {result}")
        elif high_low[player] == "low":
            low_bets[player] = result
            print(f"{player}'s result is {result}")

    high_winner, low_winner = None, None
    
    # Determine high winner if there are players who bet high
    if high_bets:
        high_winner = min(high_bets, key=lambda x: abs(20 - high_bets[x]))
    else:
        print("No players bet on high, so no high winner this round.")

    # Determine low winner if there are players who bet low
    if low_bets:
        low_winner = min(low_bets, key=lambda x: abs(1 - low_bets[x]))
    else:
        print("No players bet on low, so no low winner this round.")

    return high_winner, low_winner


def work_on_equations():
    """Provide a 5-minute timer with an option to end early."""
    print("\nYou have 5 minutes to work on your equations! If you're ready sooner, type 'ready' to proceed.")
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= 300:
            print("Time's up!")
            break
        if input("Type 'ready' if you want to end early: ").strip().lower() == "ready":
            break
        print(f"{int(300 - elapsed_time)} seconds remaining...")

def play_game():
    """Main function to start and control the game flow."""
    players = initial_setup()
    
    # Deal two open cards to each player
    print("======== Dealing Round 1 ========")
    for player in players:
        deal_round_card_with_rules(player, players[player])  # First open card
    input("Press Enter to proceed to the next round.")

    
    print("======== Dealing Round 2 ========")
    for player in players:
        deal_round_card_with_rules(player, players[player])  # Second open card
    input("Please place your bet.")
    input("Press Enter to proceed to the next round.")
    
    print("======== Dealing Round 3 ========")
    for player in players:
        deal_round_card_with_rules(player, players[player])
    input("Press Enter to proceed to the next round.")
    # Work on equations phase with option to end early
    work_on_equations()
    
    # Determine high/low bets
    high_low = {}
    for player in players:
        while True:
            bet = input(f"{player}, are you betting 'high' or 'low'?: ").lower()
            if bet in ["high", "low"]:
                high_low[player] = bet
                break
            print("Invalid choice. Please enter 'high' or 'low'.")

    # Determine winners
    high_winner, low_winner = determine_winners(players, high_low)
    
    if high_winner is not None:
        print(f"{high_winner} wins the high bet closest to 20.")
    else:
        print("No high bet winner.")

    if low_winner is not None:
        print(f"{low_winner} wins the low bet closest to 1.")
    else:
        print("No low bet winner.")

# Start the game
if __name__ == "__main__":
    print("Welcome to Equation Hi-Lo!")
    play_game()
