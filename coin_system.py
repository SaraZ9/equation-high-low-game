# coin_system.py
# from tabulate import tabulate

def enable_coin_system(players):
    """Enable the coin system."""
    players_coins = {}
    coin_each_player = 20
    for player in players:
        # no need to distinguish a human player or a bot player
        # otherwise, add 'bot_type'
        players_coins[player] = {
            'coins': coin_each_player,
            'active': True
        }
        
    print(f"Coin system enabled with {coin_each_player} coins for each player.")
    
    return players_coins

def prepare_bet_record_before_betting_round(players_coins):
    bet_record = {}
    for player in players_coins:
        if check_active_player(player, players_coins):
            bet_record[player] = {
                    'choice': ""
                }
    return bet_record

def betting_matched(bet_record):
    # Filter out players who have folded
    active_choices = [record['choice'] for record in bet_record.values() if record['choice'] != "fold"]
    print(">>>>>>>>>>>>>DEBUG, active_choices in betting_matched  <<<<<<<<<<<<<<")
    print(active_choices)

    # If there are no active choices, or if all active choices are the same, return True
    if not active_choices:
        return False  # No active bets made, so no match
    
    # Check if all active choices are the same
    return all(choice == active_choices[0] and active_choices[0] != "" for choice in active_choices)


def update_bet_record(player, choice, bet_record):
    old_choice = bet_record[player]['choice']
    
    if choice == "pass" or choice == "fold" or choice =="":
        bet_record[player] = {
                'choice': choice
            }
    else:
        if old_choice == "pass" or old_choice == "fold" or old_choice == "":
            bet_record[player] = {
                'choice': choice
            }
        else:
            bet_record[player] = {
                    'choice': choice + old_choice
                }
    print(">>>>>>>>>>>>>DEBUG, bet_record in update_bet_record  <<<<<<<<<<<<<<")
    print(bet_record)
    return bet_record

# return the highest number in bet_record for this betting round
def get_current_bet(bet_record):
    # Filter out players did not bet coins
    active_choices = [record['choice'] for record in bet_record.values() if record['choice'] != "fold" and record['choice'] != "pass" and record['choice'] != ""]

    # If there are no active choices, return 0
    if not active_choices:
        return 0
    
    # return max
    return max(active_choices)

def inactive_player(player, players_coins, bet_record):
    players_coins[player]['active'] = False
    if player in bet_record:
        del bet_record[player]

    return bet_record, players_coins

def prepare_player_before_game_round(players, players_coins):
    for player in players:
        players_coins[player]['active'] = True 
        if players_coins[player]['coins'] <= 0 :
           players_coins[player]['active'] = False 
    return players_coins

def check_active_player(player, players_coins):
    return players_coins[player]['active']

def opening_round(players, players_coins, dealer_coin):
    for player in players_coins:
        players_coins[player]['coins'] -= 1
        dealer_coin += 1
    coin_msg("Opening Round: everyone place the initial mandatory bet 1 coin")
    # print_coins(players_coins) 
    return players_coins, dealer_coin


def coin_msg(msg):
    print("\n" + "$" * 30)
    print(msg)
    print("$" * 30)


# should not change anything in players
def calculate_possible_choices(player, bet_placed, current_bet,players_coins,bet_record):
    """Calculate possible choices based on player's coins and current bet state."""
    unique_bets = set()  # Use a set to ensure no repeated choices
    # player can always fold
    
    print(players_coins)
    choices = ["fold"]

    # Retrieve the player's coin amount
    player_coins = players_coins[player]['coins']
    
    # Find the minimum coin amount among active players
    min_coins = min(p['coins'] for p in players_coins.values() if p['active'])

    # Find the coin amounts needed for each player to match current bet
    min_coins_needed_to_match_bet = {}
    
    for p in bet_record:
        # when it is a number
        if bet_record[p]['choice']!= "" and bet_record[p]['choice']!= "fold" and bet_record[p]['choice']!= "pass":
            min_coins_needed_to_match_bet[p] = current_bet - bet_record[p]['choice']
        else:
            min_coins_needed_to_match_bet[p] = current_bet
    print("!!!!print min_coins_needed_to_match_bet")
    print(min_coins_needed_to_match_bet)

    # find avalible coin amounts for each player after they match current bet
    aval_coins_after_match = {}
    for p in bet_record:
        aval_coins_after_match[p] = players_coins[p]['coins'] - min_coins_needed_to_match_bet[p]
    print("!!!!print aval_coins_after_match")
    print(aval_coins_after_match)

    # find min
    min_aval_coins_after_match = min(p for p in aval_coins_after_match.values())
    print("!!!!print min_aval_coins_after_match")
    print(min_aval_coins_after_match)


    print("!!!!print bet_placed")
    print(bet_placed)
    # main logic
    if not bet_placed:
        choices.append("pass")
        # Allow the player to bet any amount from 1 up to the lower of their coins or the minimum coin count
        limit = min(player_coins, min_coins)
        for i in range(1, limit + 1):
            unique_bets.add(i)
    else:
        # If a bet has been placed, allow the player to match or raise from current_bet to the limit
        if bet_record[player]['choice'] == "" or bet_record[player]['choice'] == "pass":
            # unique_bets.add(current_bet)
            # limit = min(player_coins, min_coins)
            # for i in range(current_bet, limit+1):
            #     unique_bets.add(i)

            limit = current_bet + min_aval_coins_after_match
            for i in range(current_bet, limit+1):
                unique_bets.add(i)
        else:
            # limit = min(player_coins, min_coins)
            limit = current_bet - bet_record[player]['choice'] + min_aval_coins_after_match
            for i in range(current_bet - bet_record[player]['choice'], limit + 1):
                unique_bets.add(i)
    
    # Combine the string options with the unique integer bets
    choices.extend(sorted(unique_bets, reverse=True))  # Add sorted integers in descending order

    return choices

def handle_bet(player, coin_record, amount, dealer_coin):
    """Deduct coins from player for a bet or raise."""
    # if coin_record[player]['coins'] >= amount:
    coin_record[player]['coins'] -= amount
    dealer_coin += amount
        # return coin_record, dealer_coin
    return coin_record, dealer_coin

# def reset_player_bet(player):
#     """Reset any bet a player has made, if needed."""
#     player['bet'] = 0

def distribute_coin(high_winner, low_winner,dealer_coin, coin_record):
    dealer_coin = int(dealer_coin/2)
    coin_record[high_winner]['coins'] = dealer_coin
    coin_record[low_winner]['coins'] = dealer_coin
    dealer_coin = 0
    return coin_record



def print_coins(players_coins):
    print("Calling print_coins...")
    
    # Print each player and their coins in a formatted way
    for player, info in players_coins.items():
        coins = info['coins']  # Access coins directly since it's an integer
        print(f"{player:<15} {coins:<5}")
