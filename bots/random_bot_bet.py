import random
import math

def welcome_msg():
    """Displays a welcome message describing the bot's strategy."""
    return "Hello! I'm a Random Bot. I trust in luck and make random choices with every card!"

def decision_for_drop(bot_data):
    """Returns an operator to drop when receiving a '*' card."""
    operation_cards = bot_data['operation_cards']

    # Filter operation_cards to include only +, -, or * if they are present
    valid_operations = [op for op in operation_cards if op in ['+', '-', '*']]
    
    # Randomly choose one from the valid operations, if available
    if valid_operations:
        return random.choice(valid_operations)

def make_a_bet_and_equation(bot_data):
    """Returns the bot's random bet and an equation using all its cards exactly once."""
    hidden_card = bot_data['hidden_card']
    open_cards = bot_data['open_cards']
    operation_cards = [op for op in bot_data['operation_cards'] if op != '√']
    
    # Randomly choose "high" or "low" bet
    bet = random.choice(["high", "low"])

    # Gather all numbers from hidden and open cards
    numbers = [hidden_card[0]] + [card[0] for card in open_cards]
    
    # Shuffle numbers and operations to ensure randomness in the equation structure
    random.shuffle(numbers)
    random.shuffle(operation_cards)

    # Construct the base equation without the square root
    equation_parts = [str(numbers[0])]
    for op, num in zip(operation_cards, numbers[1:]):
        equation_parts.append(op)
        equation_parts.append(str(num))
    
    # Join parts to form the base equation
    equation_str = " ".join(equation_parts)
    
    # Randomly insert 'v' for square root in front of one number if '√' was in operation cards
    if '√' in bot_data['operation_cards']:
        # Split equation into parts for modification
        equation_elements = equation_str.split(" ")
        
        # Choose a random index corresponding to a number
        num_indices = [i for i, elem in enumerate(equation_elements) if elem.isdigit()]
        if num_indices:
            sqrt_index = random.choice(num_indices)
            equation_elements[sqrt_index] = f"v {equation_elements[sqrt_index]}"
        
        # Rejoin the elements to form the final equation
        equation_str = " ".join(equation_elements)

    return bet, equation_str

def evaluate_equation(equation):
    """Evaluates the generated equation and returns the result."""
    # Replace 'v' with 'math.sqrt' for evaluation
    formatted_equation = equation.replace('v ', 'math.sqrt(').replace(' ', ') ', 1)
    try:
        result = eval(formatted_equation, {"math": math})
        print(f"Evaluated equation: {formatted_equation} = {result}")  # Debug print
    except (SyntaxError, ZeroDivisionError, ValueError, NameError) as e:
        print(f"Failed to evaluate equation: {formatted_equation}. Error: {e}")  # Debug print
        return None
    return result

def first_betting(bot_data, players_coins, possible_choices):
    # bot will know the bot_data, and all players coin status, and what options they have
    # decision can be from the possible_choices:
    # pass, match, raise (will be told how many coind can be), fold
    decision = random.choice(possible_choices)
    return decision

def second_betting(bot_data, players_coins, possible_choices):
    # bot will know the bot_data, and all players coin status, and what options they have
    # decision can be from the possible_choices:
    # pass, match, raise (will be told how many coind can be), fold
    
    decision = random.choice(possible_choices)
    return decision

# Example usage
# print(make_a_bet_and_equation({
#     'hidden_card': (4, 'silver'),
#     'open_cards': [(3, 'silver'), (1, 'dirt'), (2, 'bronze')],
#     'operation_cards': ['+', '-', '/', '√'],
#     'high_low_bet': None,
#     'equation': None,
#     'bot_type': 'random_bot'
# }))
