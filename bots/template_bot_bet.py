# bots/template_bot.py

def welcome_msg():
    """Displays a welcome message describing the bot's strategy.
    
    Requirements:
    - This function does not take any parameters.
    - It should return a string message that introduces the bot's strategy.
    - The message should be short and convey the bot's general approach to the game.
    
    Returns:
    str: The bot's welcome message.
    """
    return "Hello! I'm a template bot. I am waiting for you to implement me!"

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
    operator = ""
    return operator

def make_a_bet_and_equation(bot_data):
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
    bet = ""
    equation = ""
    return bet, equation

def first_betting(bot_data, players_coins, possible_choices):
    # bot will know the bot_data, and all players coin status, and what options they have
    # decision can be from the possible_choices:
    # pass, match, raise (will be told how many coind can be), fold
    
    decision = ""
    return decision
def second_betting(bot_data, players_coins, possible_choices):
    # bot will know the bot_data, and all players coin status, and what options they have
    # decision can be from the possible_choices:
    # pass, match, raise (will be told how many coind can be), fold
    
    decision = ""
    return decision
# example of bot_data:{
#     'hidden_card': (4, 'silver'),
#     'open_cards': [(3, 'silver'), (1, 'dirt'), (2, 'bronze')],
#     'operation_cards': ['+', '-', '/', '√'],
#     'high_low_bet': None,
#     'equation': None,
#     'bot_type': 'template_bot'
# }