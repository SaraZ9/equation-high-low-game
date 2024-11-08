import random
import math
import time
import threading
import sys
import itertools
import importlib
import os
import re

# Define deck with cards (numeric cards with types and operation cards)
numeric_cards = [(n, t) for n in range(11) for t in ["gold", "silver", "bronze", "dirt"]]  # Cards 0-10 with types
operation_cards = ['*', '√'] * 4  # 4 of each operation card

# Shuffle the deck
deck = numeric_cards + operation_cards
random.shuffle(deck)
print("Deck initialized with", len(deck), "cards")  # Debug message

# bots and players set up
bots = {}
players = {}

def load_bots():
    """Dynamically load all bot modules from the bots/ directory."""
    # bots = {}
    game_msg("LOADING BOTS")
    bots_dir = "bots"
    for filename in os.listdir(bots_dir):
        if filename.endswith(".py") and filename != "template_bot.py":  # Exclude template_bot:
            module_name = filename[:-3]
            module_path = f"bots.{module_name}"
            bot_module = importlib.import_module(module_path)
            
            # Check if the bot module has all required functions
            if all(hasattr(bot_module, func) for func in ['welcome_msg', 'decision_for_drop', 'make_a_bet_and_equation']):
                bots[module_name] = bot_module
                print(f"Loaded bot: {module_name}")
            else:
                print(f"Bot {module_name} is missing required functions and was not loaded.")
    return bots


def deal_number_card():
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

def game_msg(msg):
    print("\n" + "=" * 30)
    print(msg)
    print("=" * 30)
     
def initial_setup():
    global players, bots 
    """Set up the game: define players and assign each a hidden card."""
    game_msg("WELCOME TO EQUATION HI-LO SETUP")
    
    # Get number of human players
    while True:
        try:
            player_count = int(input("Enter the number of human players: "))
            # if player_count < 1:
            #     print("There must be at least 1 human player.")
            #     continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Initialize human players
    players = {f"Player {i+1}": {'hidden_card': None, 'open_cards': [], 'operation_cards': ['+', '-', '/'], 'high_low_bet' : None, "equation": None} for i in range(player_count)}
    
    # Load available bots from the bots directory
    bots = load_bots()
    
    print("Available bot types:")

    # Display available bots
    # for i, bot_name in enumerate(bots.keys(), 1):
    #     print(f"{i}. {bot_name}")
    #     print(f"{bot_name}: {bot_module.welcome_msg()}")

    for i, (bot_name, bot_module) in enumerate(bots.items(), 1):
        welcome_message = bot_module.welcome_msg()  # Call the welcome_msg function
        print(f"{i}. {bot_name} - {welcome_message}")

    game_msg("BOT SELECTION")
    # Prompt for bot quantities
    bot_counts = {}
    for bot_name in bots.keys():
        while True:
            try:
                count = int(input(f"How many {bot_name} bots would you like to add? (Enter 0 for none): "))
                if count < 0:
                    print("Please enter a positive number.")
                else:
                    bot_counts[bot_name] = count
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Add the chosen bots to the players dictionary
    for bot_name, count in bot_counts.items():
        for i in range(count):
            bot_instance_name = f"{bot_name}_{i+1}"
            players[bot_instance_name] = {
                'hidden_card': None,
                'open_cards': [],
                'operation_cards': ['+', '-', '/'],
                'high_low_bet' : None,
                "equation": None,
                'bot_type': bot_name
            }

def deal_hidden_card():
    # Deal hidden cards to each player
    game_msg("DEALING HIDDEN CARDS")
    
    for player in players:
        if 'bot_type' in players[player]:
            players[player]['hidden_card'] = deal_number_card()
            print(f"{player}'s hidden card is: HIDDEN")
        else:
            input(f"{player}, please ensure only you are looking at the screen. Press Enter when ready to see your hidden card.")
            players[player]['hidden_card'] = deal_number_card()
            print(f"{player}, your hidden card is: {players[player]['hidden_card']}")
            input("Memorize your hidden card. Press Enter when ready to clear the screen for the next player.")
            print("\033[H\033[J")  # Clear screen (works in most terminals)





def deal_round_card_with_rules(player, player_data):
    """Deal a round card following the rules for * and √ cards."""
    while True:
        card = deal_card()
        if card == "*":
            player_data['operation_cards'].append('*')
            print(f"{player} received '*'.")

            if 'bot_type' in player_data:
                    # drop = player.decision_for_drop(player_data)
                    bot_type = players[player]['bot_type']
                    bot_module = bots.get(bot_type)
                    drop = bot_module.decision_for_drop(player_data)
                    if drop in player_data['operation_cards'] and drop in ['+', '-', '*']:
                        player_data['operation_cards'].remove(drop)
                        print(f"{player} dropeed {drop}")
                    else:
                        print("Invalid choice. The system will drop for bot randomly.")
                        valid_operations = [op for op in player_data["operation_cards"] if op in ['+', '-', '*']]
                        # Randomly choose one from the valid operations, if available
                        if valid_operations:
                            drop = random.choice(valid_operations)
            else:
                while True:
                    drop = input(f"{player}, which operation would you like to drop? Your current operation cards are {player_data['operation_cards']}, and you can not drop '/' or '√'.").strip()
                    if drop in player_data['operation_cards'] and drop in ['+', '-', '*']:
                        player_data['operation_cards'].remove(drop)
                        break
                    else:
                        print("Invalid choice.")
            

        elif card == "√":
            print(f"{player} received '√'.")
            player_data['operation_cards'].append("√")
        else:
            print(f"{player} received {card}.")
            player_data['open_cards'].append(card)
            break

# input equation is in valid format (use v to indicate the sqrt)
def evaluate_equation(equation):
    """Evaluates the generated equation and returns the result."""
    formatted_equation = re.sub(r'v (\d+)', r'math.sqrt(\1)', equation)

    try:
        result = eval(formatted_equation, {"math": math})
    except (SyntaxError, ZeroDivisionError, ValueError, NameError):
        return None  # In case of invalid equations or math errors
    return result

def check_bot_valid_equation(bot_data):
    hidden_card = bot_data['hidden_card']
    open_cards = bot_data["open_cards"]
    operation_cards = bot_data["operation_cards"]
    equation = bot_data["equation"]

    # Prepare expected components
    all_numbers = [str(hidden_card[0])] + [str(card[0]) for card in open_cards]
    all_operations = operation_cards.copy()

    # Check if all numbers are used exactly once
    numbers_used = [num for num in all_numbers if f' {num} ' in f' {equation} ']
    if len(numbers_used) != len(all_numbers):
        print("Invalid equation: You must use all numbers exactly once.")
        return False
        
    # Check if each operation is used exactly once
    # Special handling for 'v' (square root)
    operations_used = []
    for op in all_operations:
        if op == '√' or op == 'v':
            if 'v' in equation:
                operations_used.append('v')
        elif f' {op} ' in f' {equation} ':
            operations_used.append(op)
    
    if len(operations_used) != len(all_operations):
        print("Invalid equation: You must use all operations exactly once.")
        return False
    return True

def player_create_equation(player):
    """Allow players to create an equation using all their cards exactly once."""
    hidden_card = players[player]["hidden_card"]
    open_cards = players[player]["open_cards"]
    operation_cards= players[player]["operation_cards"]
    
    print(f"\n{player}'s turn to create an equation!")
    print(f"Hidden card: {players[player]["hidden_card"]}")
    print(f"Open cards: {players[player]["open_cards"]}")
    print(f"Operation cards: {players[player]["operation_cards"]}")
    print(f"Bet: {players[player]["high_low_bet"]}")
    
    # Prepare expected components
    all_numbers = [str(hidden_card[0])] + [str(card[0]) for card in open_cards]
    all_operations = operation_cards.copy()

    while True:
        equation = input("Enter your equation: ")
        players[player]["equation"] = equation

        # Check if all numbers are used exactly once
        numbers_used = [num for num in all_numbers if f' {num} ' in f' {equation} ']
        if len(numbers_used) != len(all_numbers):
            print("Invalid equation: You must use all numbers exactly once.")
            continue
        
        # Check if each operation is used exactly once
        # Special handling for 'v' (square root)
        operations_used = []
        for op in all_operations:
            if op == '√' or op == 'v':
                if 'v' in equation:
                    operations_used.append('v')
            elif f' {op} ' in f' {equation} ':
                operations_used.append(op)
        
        if len(operations_used) != len(all_operations):
            print("Invalid equation: You must use all operations exactly once.")
            continue

        # Attempt to evaluate the equation
        result = evaluate_equation(equation)
        if result is not None:
            return equation, result
        
        print("Invalid equation format. Please try again.")


def determine_winners():
    """Determine the winning players for high or low bets based on equation results."""
    high_bets = {}
    low_bets = {}

    # Go through each player and evaluate their equation based on their bet (high or low)

    print("Instructions:")
    print(" - Create an equation using each card exactly once. Use spaces between numbers and operations.")
    print(" - Use 'v' for square root, applied to the next number (e.g., 'v 9' for √9).")

    for player in players:
        if 'bot_type' in players[player]:
            print(f"\n{player}'s turn to create an equation!")
            print(f"Hidden card: {players[player]["hidden_card"]}")
            print(f"Open cards: {players[player]["open_cards"]}")
            print(f"Operation cards: {players[player]["operation_cards"]}")
            print(f"Bet: {players[player]["high_low_bet"]}")

            if check_bot_valid_equation(players[player]):
                result = evaluate_equation(players[player]["equation"])
                print(f"{player}'s equation: {players[player]["equation"]}, result: {result}")
            else:
                print(f"{player}'s equation: {players[player]["equation"]}")
                result = None
                players[player]["high_low_bet"] = None
                print(f"{player}'s equation is not valid. This bot is eliminated.")
                print("Congrats, everyone else! One less competitor.")
        else:
            equation, result = player_create_equation(player)
            # equation, result = player_create_equation(players[player]['hidden_card'], players[player]['open_cards'], players[player]['operation_cards'])
            print(f"{player}'s equation: {equation}, result: {result}")

        # Sort players into high or low bets based on their choice
        if players[player]["high_low_bet"]== "high":
            high_bets[player] = result
        elif players[player]["high_low_bet"] == "low":
            low_bets[player] = result

    # Determine the winners for high and low bets
    high_winner, low_winner = None, None
    # High bet winner: closest to 20
    if high_bets:
        # Filter out any invalid entries (None or inf values)
        valid_high_bets = {player: result for player, result in high_bets.items() if result is not None and result != float('inf')}

        if valid_high_bets:
            high_winner = min(valid_high_bets, key=lambda x: abs(20 - valid_high_bets[x]))
        else:
            print("No valid high bets, so no high winner this round.")
    else:
        print("No players bet on high, so no high winner this round.")


    if low_bets:
        # Filter out any invalid entries (None or inf values)
        valid_low_bets = {player: result for player, result in low_bets.items() if result is not None and result != float('inf')}

        if valid_low_bets:
            low_winner = min(valid_low_bets, key=lambda x: abs(20 - valid_low_bets[x]))
        else:
            print("No valid low bets, so no low winner this round.")
    else:
        print("No players bet on low, so no low winner this round.")
    
    return high_winner, low_winner

def player_betting_round():
    """Let each player place high or low bets."""
    game_msg("BETTING ROUND")
    input("\nPlease place your bet coins on the table now. Press Enter when all players finish.")


    for player in players:
        if 'bot_type' not in players[player]:
            while True:
                bet = input(f"{player}, are you betting 'high' or 'low'?: ").lower()
                if bet in ["high", "low"]:
                    players[player]["high_low_bet"] = bet
                    break
                print("Invalid choice. Please enter 'high' or 'low'.")
        else:
            print(f"{player} bet on {players[player]["high_low_bet"]}.")

def deal_round(players, round_number):
    """Deal cards to each player for a specific round."""
    print(f"\n======== Dealing Round {round_number} ========")
    
    for player in players:
        deal_round_card_with_rules(player, players[player])
    if round_number == 2:
        input("\nPlease place your bet coins on the table now.")
    input("\nPress Enter to proceed to the next round.")

def bots_work_on_equations_and_bet():
    for player in players:
        if 'bot_type' in players[player]:
            bot_type = players[player]['bot_type']
            bot_module = bots.get(bot_type)
            bet, equation = bot_module.make_a_bet_and_equation(players[player])
            # high_low[player] = bet
            # equations[player] = equation
            players[player]["high_low_bet"] = bet
            players[player]["equation"] = equation
        
def player_work_on_equations():
    """Allow players to work on equations with a timer."""
    game_msg("WORKING ON EQUATIONS")

    print("\nYou have 5 minutes to work on your equations! If you're ready sooner, type 'ready' to proceed.")
    print("Type 'ready' and press Enter when done.")
    
    # Function to listen for 'ready' input
    def check_input():
        while True:
            user_input = input()
            if user_input.lower() == 'ready':
                print("\nProceeding early as requested.")
                break
    
    input_thread = threading.Thread(target=check_input)
    input_thread.start()
    
    # Start timer loop
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        remaining_time = 300 - elapsed_time
        minutes, seconds = divmod(remaining_time, 60)
        time_format = f"{int(minutes):02}:{int(seconds):02}"
        
        # Display the countdown on a single line
        sys.stdout.write(f"\rTime remaining: {time_format}   ")  # Extra spaces to clear remnants
        sys.stdout.flush()
        time.sleep(1)
        
        # Break on timeout or early input
        if elapsed_time >= 300:
            print("\nTime's up!")
            break
        if not input_thread.is_alive():
            break
    
    input_thread.join()
    # Clear the timer line
    sys.stdout.write("\r" + " " * 30 + "\r")  # Overwrite with spaces and reset the cursor
    sys.stdout.flush()


def determine_and_announce_winners():
    """Determine and announce winners for high and low bets."""
    game_msg("DETERMINING WINNERS")

    high_winner, low_winner = determine_winners()
    
    game_msg("ANNOUNCE WINNERS")
    if high_winner:
        print(f"{high_winner} wins the high bet closest to 20.")
    else:
        print("No high bet winner.")

    if low_winner:
        print(f"{low_winner} wins the low bet closest to 1.")
    else:
        print("No low bet winner.")


# Main function to control the game flow
def play_game():
    """Main function to control the game flow."""
    initial_setup()
    # print("Players set up:", players)

    game_msg("GAME START. Please try your best and have fun!")

    deal_hidden_card()
    
    # Dealing rounds
    deal_round(players, round_number=1)
    deal_round(players, round_number=2)
    deal_round(players, round_number=3)

    # Players work on equations
    player_work_on_equations()

    # Bots work on equations 
    # Record their bets and equations
    bots_work_on_equations_and_bet()

    # Betting round
    # Record players bets
    player_betting_round()

    # record players equations and 
    # Determine winners
    determine_and_announce_winners()
    
    game_msg("GAME OVER. Thank you for playing Equation Hi-Lo!")

if __name__ == "__main__":
    print("Welcome to Equation Hi-Lo!")
    play_game()
