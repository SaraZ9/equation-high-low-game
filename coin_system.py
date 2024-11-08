# coin_system.py
# from tabulate import tabulate

def enable_coin_system(players):
    """Enable the coin system."""
    players_coins = {}
    coin_each_play = 20
    for player in players:
        # no need to distinguish a human player or a bot player
        # otherwise, add 'bot_type'
        players_coins[player] = {
            'coins': coin_each_play
        }
        
    print(f"Coin system enabled with {coin_each_play} coins for each player.")
    
    return players_coins

def opening_round(players, players_coins):
    for player in players_coins:
        players_coins[player]['coins'] -= 1
    coin_msg("Opening Round: everyone place the initial mandatory bet 1 coin")
    # print_coins(players_coins) 
    return players_coins


def coin_msg(msg):
    print("\n" + "$" * 30)
    print(msg)
    print("$" * 30)


# should not change anything in players
def calculate_possible_choices(player, bet_placed, current_bet,players_coins):
    """Calculate possible choices based on player's coins and current bet state."""
    unique_bets = set()  # Use a set to ensure no repeated choices
    # player can always fold
    
    choices = ["fold"]
    player_coins = players_coins[player]
    min_coins = min(players_coins.values())

    if not bet_placed:
        choices.append("pass")
        # Allow the player to bet any amount from 1 up to the lower of their coins or the minimum coin count
        limit = min(player_coins, min_coins)
        for i in range(1, limit + 1):
            unique_bets.add(i)
    else:
        # If a bet has been placed, allow the player to match or raise from current_bet to the limit
        limit = min(player_coins, min_coins)
        for i in range(current_bet, limit + 1):
            unique_bets.add(i)
    
    # Combine the string options with the unique integer bets
    choices.extend(sorted(unique_bets, reverse=True))  # Add sorted integers in descending order

    return choices

# def handle_bet(player, amount):
#     """Deduct coins from player for a bet or raise."""
#     if player['coins'] >= amount:
#         player['coins'] -= amount
#         return True
#     return False

# def reset_player_bet(player):
#     """Reset any bet a player has made, if needed."""
#     player['bet'] = 0




def print_coins(players_coins):
    print("Calling print_coins...")
    
    # Print each player and their coins in a formatted way
    for player, info in players_coins.items():
        coins = info['coins']  # Access coins directly since it's an integer
        print(f"{player:<15} {coins:<5}")
