import random
import math
import itertools
import re

def welcome_msg():
    """Displays a welcome message describing the bot's strategy."""
    return "Hello! I'm a smart bot. I will use every card strategically to create the best equation!"

def decision_for_drop(bot_data):
    """Returns an operator to drop when receiving a '*' card."""
    operation_cards = bot_data['operation_cards']
    valid_operations = [op for op in operation_cards if op in ['+', '-', '*']]
    if valid_operations:
        return random.choice(valid_operations)

def make_a_bet_and_equation(bot_data):
    """Returns the bot's bet and optimal equation based on its cards."""
    hidden_card = bot_data['hidden_card']
    open_cards = bot_data['open_cards']
    operation_cards = bot_data['operation_cards']
    target_values = (20, 1)
    
    # Extract numbers from cards
    numbers = [hidden_card[0]] + [card[0] for card in open_cards]
    possible_equations = []

    # Generate all possible permutations of numbers and operations
    for number_perm in itertools.permutations(numbers):
        for op_perm in itertools.permutations(operation_cards, len(numbers) - 1):
            # Construct the equation using all numbers and operations
            equation_parts = []
            numbers_used = iter(number_perm)
            operations_used = iter(op_perm)
            
            # Apply square root if "√" is in operation_cards
            if '√' in operation_cards:
                sqrt_number = next(numbers_used)  # Apply sqrt to the first number in permutation
                equation_parts.append(f"math.sqrt({sqrt_number})")
            else:
                equation_parts.append(str(next(numbers_used)))
            
            # Build equation with remaining numbers and operations
            for op in operations_used:
                equation_parts.append(op)
                equation_parts.append(str(next(numbers_used)))
                
            # Join all parts into a single equation string
            equation = " ".join(equation_parts)
            
            # Evaluate the equation
            result = evaluate_equation(equation)
            if result is not None:
                possible_equations.append((equation, result))
    
    # Find the equation closest to the target values
    optimal_equation, optimal_result, min_distance = None, None, float('inf')
    closest_target = None

    for equation, result in possible_equations:
        # Calculate distance to each target
        distances = [(abs(result - target), target) for target in target_values]
        distance, target = min(distances)  # Get closest target and distance
        if distance < min_distance:
            optimal_equation, optimal_result, min_distance = equation, result, distance
            closest_target = target

    # Determine bet based on closest target
    bet = "high" if closest_target == 20 else "low"

    return bet, format_equation_with_sqrt(optimal_equation)

def format_equation_with_sqrt(equation):
    """
    Convert an equation with `math.sqrt` to `v` notation.
    
    Example:
        Input: 'math.sqrt(4) - 3 / 1 + 2'
        Output: 'v 4 - 3 / 1 + 2'
    """
    # Replace instances of `math.sqrt(x)` with `v x`
    formatted_equation = re.sub(r'math\.sqrt\((\d+)\)', r'v \1', equation)
    return formatted_equation


def evaluate_equation(equation):
    """Evaluates the generated equation and returns the result."""
    try:
        result = eval(equation, {"math": math})
    except (SyntaxError, ZeroDivisionError, ValueError, NameError):
        return None  # In case of invalid equations or math errors
    return result

# Example usage:
# print(make_a_bet_and_equation({
#     'hidden_card': (9, 'silver'),
#     'open_cards': [(3, 'silver'), (3, 'dirt'), (10, 'bronze')],
#     'operation_cards': ['+', '*', '/', '√'],
#     'high_low_bet': None,
#     'equation': None,
#     'bot_type': 'smart_bot'
# }))
