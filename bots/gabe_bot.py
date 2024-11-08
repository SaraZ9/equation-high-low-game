# bots/template_bot.py
import math
import random
def welcome_msg():
    """Displays a welcome message describing the bot's strategy.
    
    Requirements:
    - This function does not take any parameters.
    - It should return a string message that introduces the bot's strategy.
    - The message should be short and convey the bot's general approach to the game.
    
    Returns:
    str: The bot's welcome message.
    """
    return "Hello! I'm Gabe. I do not know math!"

def decision_for_drop(bot_data):
    """Chooses an operator to drop when receiving a '*' card.
    
    Requirements:
    - This function must receive the bot's data as a parameter, specifically `bot_data`.
    - The `bot_data` dictionary should contain:
        - 'operation_cards' (list): The list of operation cards available to the bot, including '*'.
    - If the bot has a '*', it should drop a specific operator to maintain a balanced set of operations.
    - Preference for dropping '-' if it exists, otherwise drop any other available operator.
    
    Parameters:
    bot_data (dict): The bot's data, containing at least the key 'operation_cards'.
    
    Returns:
    str: The operator chosen to be dropped.
    """
    operation_cards = bot_data['operation_cards']
    valid_operations = [op for op in operation_cards if op in ['+', '-', '*']]
    hidden_card = bot_data['hidden_card']
    open_cards = bot_data['open_cards']
    numbers = [hidden_card[0]] + [card[0] for card in open_cards]
    
    #  always drop + if all numbers are below 5
    if all([num < 5 for num in numbers]):
        if '+' in valid_operations:
            operator = '+'
        else :
            operator = '*'
            
    elif all([num > 5 for num in numbers]):
    # if all numbers are above 5, drop -
        if '-' in valid_operations:
            operator = '-'
        else:
            operator = '*'            
    else:
        operator = '*'
    return operator

def make_a_bet_and_equation(bot_data, strictness=None, depth=0, max_depth=100):
    """Constructs a bet ('high' or 'low') and an equation using all cards and operators exactly once.
    
    Requirements:
    - This function receives `bot_data` as input and constructs a betting decision and a valid equation.
    - The `bot_data` dictionary should contain:
        - 'hidden_card' (tuple): A tuple representing the hidden card (value, type).
        - 'open_cards' (list of tuples): A list of tuples for open cards, each (value, type).
        - 'operation_cards' (list): The list of operations available for the bot (e.g., ['+', '-', '*', '√']).
    - The function must use all numbers and operators exactly once in the equation.
    - The equation must be formatted with spaces between numbers and operators.
    - If the operation card list includes '√', use 'v' before a number to represent it.
    
    Parameters:
    bot_data (dict): The bot's data, containing 'hidden_card', 'open_cards', and 'operation_cards'.
    
    Returns:
    tuple: A tuple with the bet ('high' or 'low') and the constructed equation (str).
    """
    import random
    strictness = random.randint(1, 10)
    print(f"Gabe is calculating with a strictness of ", strictness)
    if depth >= max_depth:
        print("Gabe is exhausted!")
        bet = ''
        equation = ''
        return bet=='low', equation=='None'
    else:
    
        hidden_card = bot_data['hidden_card']
        open_cards = bot_data['open_cards']
        operation_cards = bot_data['operation_cards']
        copy_operation_cards = operation_cards.copy()
        
        target_values = (20, 1)    
        numbers = [hidden_card[0]] + [card[0] for card in open_cards]
        
        if 10 in numbers:
            bet = 'high'
        elif 0 in numbers:
            bet = 'low'
        else:
            # if the average of the numbers is greater than 5, bet high
            if sum(numbers) / len(numbers) > 5:
                bet = 'high'
            else:
                bet = 'low'
        if bet == 'high':
            # if the bet is high and there is a multiplication, multiply the two largest values
            if '*' in operation_cards:
                numbers.sort()
                equation = f"{numbers[-1]} * {numbers[-2]}"
                # remove the two numbers that were multiplied from the list
                numbers.pop()
                numbers.pop() 
                
                # remove the multiplication operator from the list
                copy_operation_cards.remove('*')
                

            else:
                # if there is no multiplication, the two largest values are added
                equation = f"{numbers[-1]} + {numbers[-2]}"
                numbers.pop()
                numbers.pop()
                # remove the addition operator from the list
                copy_operation_cards.remove('+')

        elif bet == 'low':
            # if the bet is low and there is a subtraction, subtract the two smallest values
            if '-' in operation_cards:
                numbers.sort()
                equation = f"{numbers[0]} - {numbers[1]}"
                numbers.pop(1)
                numbers.pop(0)
                # remove the subtraction operator from the list
                copy_operation_cards.remove('-')            
            else:
                # if there is no subtraction, the two smallest values are added
                if '+' in operation_cards:
                    equation = f"{numbers[0]} + {numbers[1]}"
                    numbers.pop(1)
                    numbers.pop(0)
                # remove the addition operator from the list
                    copy_operation_cards.remove('+')

        #for the rest of the numbers, randomly include them in the equation
        sqrt_added = False
        sqrt_needed = False
        if copy_operation_cards.count('√') > 0:
            copy_operation_cards.remove('√')
            sqrt_needed = True
        for i in range(len(copy_operation_cards)):        
            equation += f" {copy_operation_cards[i]} {numbers[i]}"
            
        import random
        
        if sqrt_needed:
            # if the square root is needed, add it in front of any random number in the equation
            equation_parts = equation.split()
            number_indices = [i for i, part in enumerate(equation_parts) if part.isdigit()]
            if number_indices:
                random_index = random.choice(number_indices)
                equation_parts[random_index] = 'v ' + equation_parts[random_index]
            equation = ' '.join(equation_parts)
        #    print(f"Equation:", equation)

        # Evaluate the equation
        result = evaluate_equation(equation)
        
        if result is None:
            #print("Failed to evaluate the equation.")
            return bet, equation

        #print(f"Equation: {equation}")
        #print(f"Result: {result}")

        distance_from_1 = abs(1 - result)
        distance_from_20 = abs(20 - result)
        # Test how far the equation is from the target value
        if bet == 'high':
            
            #print(f"Distance from 20: {distance_from_20}")
            if distance_from_20 > 10:
                bet = 'low'
                #print("Changing bet to 'low'")
                # show the distance to the new target value
                distance_from_1 = abs(1 - result)
                #print(f"New distance from 1: {distance_from_1}")
        else:
            
            #print(f"Distance from 1: {distance_from_1}")
            if distance_from_1 > 10:
                bet = 'high'
                #print("Changing bet to 'high'")
                # show the distance to the new target value
                distance_from_20 = abs(20 - result)
                #print(f"New distance from 20: {distance_from_20}")


        # If the result the value is too far from the target, recalculate the equation
        if (bet == 'high' and distance_from_20 > strictness) or (bet == 'low' and distance_from_1 > strictness):
            print("Recalculating equation...")
            if not sqrt_needed:
                # equation won't have square root, so nothing will change if we run the function again
                print("Oops, without square root I can't do much.")
                return bet, equation
            else:    
                return make_a_bet_and_equation(bot_data, strictness, depth + 1, max_depth)

    return bet, equation

def evaluate_equation(equation):
    """Evaluates the generated equation and returns the result."""
    # Replace 'v' with 'math.sqrt(' and ensure it is properly closed with ')'
    formatted_equation = equation.replace('v ', 'math.sqrt(')
    # Find all instances of 'math.sqrt(' and ensure they are properly closed
    parts = formatted_equation.split()
    for i, part in enumerate(parts):
        if part.startswith('math.sqrt('):
            parts[i] = part + ')'
    formatted_equation = ' '.join(parts)
    
    try:
        result = eval(formatted_equation, {"math": math})
        #print(f"Evaluated equation: {formatted_equation} = {result}")  # Debug print
    except (SyntaxError, ZeroDivisionError, ValueError, NameError) as e:
        print(f"Failed to evaluate equation: {formatted_equation}. Error: {e}")  # Debug print
        return None
    return result


# example of bot_data:{
#     'hidden_card': (4, 'silver'),
#     'open_cards': [(3, 'silver'), (1, 'dirt'), (2, 'bronze')],
#     'operation_cards': ['+', '-', '/', '√'],
#     'high_low_bet': None,
#     'equation': None,
#     'bot_type': 'template_bot'
# }


# Test the bot -- uncomment the following lines to test the bot
# assign random 1 to 10 values for each card
#card_1 = (random.randint(1, 10), 'silver')
#card_2 = (random.randint(1, 10), 'dirt')
#card_3 = (random.randint(1, 10), 'bronze')
#card_4 = (random.randint(1, 10), 'silver')

#bot_data = {
#     'hidden_card': card_1,
#     'open_cards': [card_2, card_3, card_4],
#     'operation_cards': ['+', '-', '/', '√'],
#     'high_low_bet': None,
#     'equation': None,
#     'bot_type': 'template_bot'
#}

#print cards
#print("Hidden Card:", card_1)
#print("Open Cards:", [card_2, card_3, card_4])
# this bot will randomly decide how strict it will be with the target value

#strictness = random.randint(1, 10)

#print(f"Strictness: {strictness}")
#print(make_a_bet_and_equation(bot_data))

