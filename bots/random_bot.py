# # # # # # # bots/template_bot.py
# # # # # # import random
# # # # # # import math

# # # # # # def welcome_msg():
# # # # # #     """Displays a welcome message describing the bot's strategy."""
# # # # # #     return f"Hello! I'm a random. I trust in luck and I make random choice!"

# # # # # # def decision_for_drop(bot_data):
# # # # # #     """Returns an operator to drop when receiving a '*' card."""
# # # # # #     operation_cards = bot_data['operation_cards']

# # # # # #     # Filter operation_cards to include only +, -, or * if they are present
# # # # # #     valid_operations = [op for op in operation_cards if op in ['+', '-', '*']]
    
# # # # # #     # Randomly choose one from the valid operations, if available
# # # # # #     if valid_operations:
# # # # # #         drop = random.choice(valid_operations)
# # # # # #         return drop


# # # # # # def make_a_bet_and_equation(bot_data):
# # # # # #     """Returns the bot's bet and equation based on its cards."""
# # # # # #     hidden_card = bot_data['hidden_card']
# # # # # #     open_cards = bot_data['open_cards']
# # # # # #     operation_cards = bot_data['operation_cards']
    
# # # # # #     bet = random.choice(["high", "low"])

# # # # # #     """Allow bot to create an equation using their cards."""

# # # # # #     # Extract the numbers from the hidden card and open cards
# # # # # #     numbers = [hidden_card[0]] + [card[0] for card in open_cards]

# # # # # #     # Choose a random number of operations (1 or 2 operations for simplicity)
# # # # # #     num_operations = random.randint(1, min(len(numbers) - 1, len(operation_cards)))
    
# # # # # #     # Select operations randomly from operation_cards
# # # # # #     selected_operations = random.sample(operation_cards, num_operations)
    
# # # # # #     # Randomly shuffle the numbers to create different equation structures
# # # # # #     random.shuffle(numbers)
    
# # # # # #     # Construct the equation string
# # # # # #     equation = str(numbers[0])
# # # # # #     for i in range(num_operations):
# # # # # #         equation += f" {selected_operations[i]} {numbers[i + 1]}"
    
# # # # # #     # Handle square root if selected and applicable
# # # # # #     if '√' in operation_cards:
# # # # # #         if random.choice([True, False]):  # Randomly decide to apply square root
# # # # # #             equation = f"math.sqrt({equation})"
# # # # # #     # result = bot_evaluate_equation(equation)
# # # # # #     return bet, equation
# # # # # # # Example usage:

# # # # # # print(make_a_bet_and_equation({
# # # # # #     'hidden_card': (4, 'silver'),
# # # # # #     'open_cards': [(3, 'silver'), (1, 'dirt'), (2, 'bronze')],
# # # # # #     'operation_cards': ['+', '-', '/', '√'],
# # # # # #     'high_low_bet': None,
# # # # # #     'equation': None,
# # # # # #     'bot_type': 'random_bot'
# # # # # # }))

# # # # # # bots/template_bot.py
# # # # # import random
# # # # # import math

# # # # # def welcome_msg():
# # # # #     """Displays a welcome message describing the bot's strategy."""
# # # # #     return f"Hello! I'm a random. I trust in luck and I make random choice!"

# # # # # def decision_for_drop(bot_data):
# # # # #     """Returns an operator to drop when receiving a '*' card."""
# # # # #     operation_cards = bot_data['operation_cards']

# # # # #     # Filter operation_cards to include only +, -, or * if they are present
# # # # #     valid_operations = [op for op in operation_cards if op in ['+', '-', '*']]
    
# # # # #     # Randomly choose one from the valid operations, if available
# # # # #     if valid_operations:
# # # # #         drop = random.choice(valid_operations)
# # # # #         return drop


# # # # # def make_a_bet_and_equation(bot_data):
# # # # #     """Returns the bot's bet and equation based on its cards."""
# # # # #     hidden_card = bot_data['hidden_card']
# # # # #     open_cards = bot_data['open_cards']
# # # # #     operation_cards = bot_data['operation_cards']
    
# # # # #     bet = random.choice(["high", "low"])

# # # # #     """Allow bot to create an equation using their cards."""

# # # # #     # Extract the numbers from the hidden card and open cards
# # # # #     numbers = [hidden_card[0]] + [card[0] for card in open_cards]

# # # # #     # Choose a random number of operations (1 or 2 operations for simplicity)
# # # # #     num_operations = random.randint(1, min(len(numbers) - 1, len(operation_cards)))
    
# # # # #     # Select operations randomly from operation_cards
# # # # #     selected_operations = random.sample(operation_cards, num_operations)
    
# # # # #     # Randomly shuffle the numbers to create different equation structures
# # # # #     random.shuffle(numbers)
    
# # # # #     # Construct the equation string
# # # # #     equation = str(numbers[0])
# # # # #     for i in range(num_operations):
# # # # #         equation += f" {selected_operations[i]} {numbers[i + 1]}"
    
# # # # #     # Handle square root if selected and applicable
# # # # #     if '√' in operation_cards:
# # # # #         if random.choice([True, False]):  # Randomly decide to apply square root
# # # # #             equation = f"math.sqrt({equation})"
# # # # #     # result = bot_evaluate_equation(equation)
# # # # #     return bet, equation
# # # # # # Example usage:

# # # # # print(make_a_bet_and_equation({
# # # # #     'hidden_card': (4, 'silver'),
# # # # #     'open_cards': [(3, 'silver'), (1, 'dirt'), (2, 'bronze')],
# # # # #     'operation_cards': ['+', '-', '/', '√'],
# # # # #     'high_low_bet': None,
# # # # #     'equation': None,
# # # # #     'bot_type': 'random_bot'
# # # # # }))

# # # # import random
# # # # import math

# # # # def welcome_msg():
# # # #     """Displays a welcome message describing the bot's strategy."""
# # # #     return "Hello! I'm a Random Bot. I trust in luck and make random choices with every card!"

# # # # def decision_for_drop(bot_data):
# # # #     """Returns an operator to drop when receiving a '*' card."""
# # # #     operation_cards = bot_data['operation_cards']

# # # #     # Filter operation_cards to include only +, -, or * if they are present
# # # #     valid_operations = [op for op in operation_cards if op in ['+', '-', '*']]
    
# # # #     # Randomly choose one from the valid operations, if available
# # # #     if valid_operations:
# # # #         return random.choice(valid_operations)

# # # # def make_a_bet_and_equation(bot_data):
# # # #     """Returns the bot's random bet and an equation using all its cards."""
# # # #     hidden_card = bot_data['hidden_card']
# # # #     open_cards = bot_data['open_cards']
# # # #     operation_cards = bot_data['operation_cards']
    
# # # #     # Randomly choose "high" or "low" bet
# # # #     bet = random.choice(["high", "low"])

# # # #     # Gather all numbers from hidden and open cards
# # # #     numbers = [hidden_card[0]] + [card[0] for card in open_cards]
    
# # # #     # Shuffle numbers and operations to ensure randomness in the equation structure
# # # #     random.shuffle(numbers)
# # # #     random.shuffle(operation_cards)

# # # #     # Construct the equation with all numbers and operations exactly once
# # # #     equation_parts = []
# # # #     equation_parts.append(str(numbers[0]))

# # # #     # Build the equation by iterating through all numbers and operations
# # # #     for op, num in zip(operation_cards, numbers[1:]):
# # # #         if op == "√":
# # # #             # If the operation is square root, apply it to the next number directly and use 'v' for display
# # # #             equation_parts.append(f"v {num}")
# # # #         else:
# # # #             # Otherwise, add standard operations between numbers
# # # #             equation_parts.append(op)
# # # #             equation_parts.append(str(num))

# # # #     # Join all parts into a single equation string
# # # #     equation_str = " ".join(equation_parts)
# # # #     return bet, equation_str

# # # # def evaluate_equation(equation):
# # # #     """Evaluates the generated equation and returns the result."""
# # # #     # Replace 'v ' with 'math.sqrt(' and add closing parentheses correctly for square roots
# # # #     formatted_equation = equation.replace('v ', 'math.sqrt(').replace(' ', ') ', 1)
# # # #     try:
# # # #         result = eval(formatted_equation, {"math": math})
# # # #         print(f"Evaluated equation: {formatted_equation} = {result}")  # Debug print
# # # #     except (SyntaxError, ZeroDivisionError, ValueError, NameError) as e:
# # # #         print(f"Failed to evaluate equation: {formatted_equation}. Error: {e}")  # Debug print
# # # #         return None
# # # #     return result

# # # # # Example usage
# # # # print(make_a_bet_and_equation({
# # # #     'hidden_card': (4, 'silver'),
# # # #     'open_cards': [(3, 'silver'), (1, 'dirt'), (2, 'bronze')],
# # # #     'operation_cards': ['+', '-', '/', '√'],
# # # #     'high_low_bet': None,
# # # #     'equation': None,
# # # #     'bot_type': 'random_bot'
# # # # }))

# # # import random
# # # import math

# # # def welcome_msg():
# # #     """Displays a welcome message describing the bot's strategy."""
# # #     return "Hello! I'm a Random Bot. I trust in luck and make random choices with every card!"

# # # def decision_for_drop(bot_data):
# # #     """Returns an operator to drop when receiving a '*' card."""
# # #     operation_cards = bot_data['operation_cards']

# # #     # Filter operation_cards to include only +, -, or * if they are present
# # #     valid_operations = [op for op in operation_cards if op in ['+', '-', '*']]
    
# # #     # Randomly choose one from the valid operations, if available
# # #     if valid_operations:
# # #         return random.choice(valid_operations)

# # # def make_a_bet_and_equation(bot_data):
# # #     """Returns the bot's random bet and an equation using all its cards exactly once."""
# # #     hidden_card = bot_data['hidden_card']
# # #     open_cards = bot_data['open_cards']
# # #     operation_cards = bot_data['operation_cards']
    
# # #     # Randomly choose "high" or "low" bet
# # #     bet = random.choice(["high", "low"])

# # #     # Gather all numbers from hidden and open cards
# # #     numbers = [hidden_card[0]] + [card[0] for card in open_cards]
    
# # #     # Shuffle numbers and operations to ensure randomness in the equation structure
# # #     random.shuffle(numbers)
# # #     random.shuffle(operation_cards)

# # #     # Construct the equation using all numbers and operations exactly once
# # #     equation_parts = []
# # #     equation_parts.append(str(numbers[0]))

    
# # #     # Build the equation by iterating through all numbers and operations
# # #     for op, num in zip(operation_cards, numbers[1:]):
# # #         if op != "√":
# # #             equation_parts.append(op)
# # #             equation_parts.append(str(num))
        
# # #     if "√" in op:
# # #         # randomly put v in front of a number

# # #     # Join all parts into a single equation string
# # #     equation_str = " ".join(equation_parts)
# # #     return bet, equation_str

# # # def evaluate_equation(equation):
# # #     """Evaluates the generated equation and returns the result."""
# # #     # Replace 'v' with 'math.sqrt' for evaluation
# # #     formatted_equation = equation.replace('v ', 'math.sqrt(').replace(' ', ') ', 1)
# # #     try:
# # #         result = eval(formatted_equation, {"math": math})
# # #         print(f"Evaluated equation: {formatted_equation} = {result}")  # Debug print
# # #     except (SyntaxError, ZeroDivisionError, ValueError, NameError) as e:
# # #         print(f"Failed to evaluate equation: {formatted_equation}. Error: {e}")  # Debug print
# # #         return None
# # #     return result

# # # # Example usage
# # # print(make_a_bet_and_equation({
# # #     'hidden_card': (4, 'silver'),
# # #     'open_cards': [(3, 'silver'), (1, 'dirt'), (2, 'bronze')],
# # #     'operation_cards': ['+', '-', '/', '√'],
# # #     'high_low_bet': None,
# # #     'equation': None,
# # #     'bot_type': 'random_bot'
# # # }))

# # import random
# # import math

# # def welcome_msg():
# #     """Displays a welcome message describing the bot's strategy."""
# #     return "Hello! I'm a Random Bot. I trust in luck and make random choices with every card!"

# # def decision_for_drop(bot_data):
# #     """Returns an operator to drop when receiving a '*' card."""
# #     operation_cards = bot_data['operation_cards']

# #     # Filter operation_cards to include only +, -, or * if they are present
# #     valid_operations = [op for op in operation_cards if op in ['+', '-', '*']]
    
# #     # Randomly choose one from the valid operations, if available
# #     if valid_operations:
# #         return random.choice(valid_operations)

# # def make_a_bet_and_equation(bot_data):
# #     """Returns the bot's random bet and an equation using all its cards exactly once."""
# #     hidden_card = bot_data['hidden_card']
# #     open_cards = bot_data['open_cards']
# #     operation_cards = bot_data['operation_cards']
    
# #     # Randomly choose "high" or "low" bet
# #     bet = random.choice(["high", "low"])

# #     # Gather all numbers from hidden and open cards
# #     numbers = [hidden_card[0]] + [card[0] for card in open_cards]
    
# #     # Shuffle numbers and operations to ensure randomness in the equation structure
# #     random.shuffle(numbers)
# #     random.shuffle(operation_cards)

# #     # Construct the equation using all numbers and operations exactly once
# #     equation_parts = [str(numbers[0])]

# #     # Apply each operation to remaining numbers, ensuring all are used exactly once
# #     for op, num in zip(operation_cards, numbers[1:]):
# #         if op == "√":
# #             # Apply 'v' for square root in front of the selected number
# #             equation_parts.append(f"v {num}")
# #         else:
# #             # Add standard operations between numbers
# #             equation_parts.append(op)
# #             equation_parts.append(str(num))

# #     # Join all parts into a single equation string
# #     equation_str = " ".join(equation_parts)
# #     return bet, equation_str

# # def evaluate_equation(equation):
# #     """Evaluates the generated equation and returns the result."""
# #     # Replace 'v' with 'math.sqrt' for evaluation
# #     formatted_equation = equation.replace('v ', 'math.sqrt(').replace(' ', ') ', 1)
# #     try:
# #         result = eval(formatted_equation, {"math": math})
# #         print(f"Evaluated equation: {formatted_equation} = {result}")  # Debug print
# #     except (SyntaxError, ZeroDivisionError, ValueError, NameError) as e:
# #         print(f"Failed to evaluate equation: {formatted_equation}. Error: {e}")  # Debug print
# #         return None
# #     return result

# # # Example usage
# # print(make_a_bet_and_equation({
# #     'hidden_card': (4, 'silver'),
# #     'open_cards': [(3, 'silver'), (1, 'dirt'), (2, 'bronze')],
# #     'operation_cards': ['+', '-', '/', '√'],
# #     'high_low_bet': None,
# #     'equation': None,
# #     'bot_type': 'random_bot'
# # }))


# import random
# import math

# def welcome_msg():
#     """Displays a welcome message describing the bot's strategy."""
#     return "Hello! I'm a Random Bot. I trust in luck and make random choices with every card!"

# def decision_for_drop(bot_data):
#     """Returns an operator to drop when receiving a '*' card."""
#     operation_cards = bot_data['operation_cards']

#     # Filter operation_cards to include only +, -, or * if they are present
#     valid_operations = [op for op in operation_cards if op in ['+', '-', '*']]
    
#     # Randomly choose one from the valid operations, if available
#     if valid_operations:
#         return random.choice(valid_operations)

# def make_a_bet_and_equation(bot_data):
#     """Returns the bot's random bet and an equation using all its cards exactly once."""
#     hidden_card = bot_data['hidden_card']
#     open_cards = bot_data['open_cards']
#     operation_cards = bot_data['operation_cards']
    
#     # Randomly choose "high" or "low" bet
#     bet = random.choice(["high", "low"])

#     # Gather all numbers from hidden and open cards
#     numbers = [hidden_card[0]] + [card[0] for card in open_cards]
    
#     # Shuffle numbers and operations to ensure randomness in the equation structure
#     random.shuffle(numbers)
#     random.shuffle(operation_cards)

#     # If square root is present, apply it to a random number first
#     equation_parts = []
#     sqrt_applied = False

#     for op in operation_cards:
#         if op == "√" and not sqrt_applied:
#             # Choose a random number to apply 'v' to
#             index = random.randint(0, len(numbers) - 1)
#             equation_parts.append(f"v {numbers[index]}")
#             numbers.pop(index)  # Remove this number as it's used
#             sqrt_applied = True
#         else:
#             # Add other operators to the remaining numbers
#             equation_parts.append(op)
#             equation_parts.append(str(numbers.pop(0)))

#     # Join all parts into a single equation string
#     equation_str = " ".join(equation_parts)
#     return bet, equation_str

# def evaluate_equation(equation):
#     """Evaluates the generated equation and returns the result."""
#     # Replace 'v' with 'math.sqrt' for evaluation
#     formatted_equation = equation.replace('v ', 'math.sqrt(').replace(' ', ') ', 1)
#     try:
#         result = eval(formatted_equation, {"math": math})
#         print(f"Evaluated equation: {formatted_equation} = {result}")  # Debug print
#     except (SyntaxError, ZeroDivisionError, ValueError, NameError) as e:
#         print(f"Failed to evaluate equation: {formatted_equation}. Error: {e}")  # Debug print
#         return None
#     return result

# # Example usage
# print(make_a_bet_and_equation({
#     'hidden_card': (4, 'silver'),
#     'open_cards': [(3, 'silver'), (1, 'dirt'), (2, 'bronze')],
#     'operation_cards': ['+', '-', '/', '√'],
#     'high_low_bet': None,
#     'equation': None,
#     'bot_type': 'random_bot'
# }))
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

# Example usage
# print(make_a_bet_and_equation({
#     'hidden_card': (4, 'silver'),
#     'open_cards': [(3, 'silver'), (1, 'dirt'), (2, 'bronze')],
#     'operation_cards': ['+', '-', '/', '√'],
#     'high_low_bet': None,
#     'equation': None,
#     'bot_type': 'random_bot'
# }))
