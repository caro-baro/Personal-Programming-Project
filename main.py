## Personal Programming Project - Carolina 
import random

fund = 1000
deck = ['🂡', '🂱', '🃁', '🃑',
        '🂢', '🂲', '🃂', '🃒',
        '🂣', '🂳', '🃃', '🃓',
        '🂤', '🂴', '🃄', '🃔',
        '🂥', '🂵', '🃅', '🃕',
        '🂦', '🂶', '🃆', '🃖', 
        '🂧', '🂷', '🃇', '🃗', 
        '🂨', '🂸', '🃈', '🃘',
        '🂩', '🂹', '🃉', '🃙',
        '🂪', '🂺', '🃊', '🃚',
        '🂫', '🂻', '🃋', '🃛',
        '🂬', '🂼', '🃌', '🃜',
        '🂭', '🂽', '🃍', '🃝',
        '🂮', '🂾', '🃎', '🃞']

values = [11, 11, 11, 11,
        2, 2, 2, 2,
        3, 3, 3, 3,
        4, 4, 4, 4,
        5, 5, 5, 5,
        6, 6, 6, 6, 
        7, 7, 7, 7, 
        8, 8, 8, 8,
        9, 9, 9, 9,
        10, 10, 10, 10,
        10, 10, 10, 10,
        10, 10, 10, 10,
        10, 10, 10, 10,
        10, 10, 10, 10]

dict: {'🂡':11, '🂱':11, '🃁':11, '🃑':11,
        '🂢':2, '🂲':2, '🃂':2, '🃒':2,
        '🂣':3, '🂳':3, '🃃':3, '🃓':3,
        '🂤':4, '🂴':4, '🃄':4, '🃔':4,
        '🂥':5, '🂵':5, '🃅':5, '🃕':5,
        '🂦':6, '🂶':6, '🃆':6, '🃖':6, 
        '🂧':7, '🂷':7, '🃇':7, '🃗':7, 
        '🂨':8, '🂸':8, '🃈':8, '🃘':8,
        '🂩':9, '🂹':9, '🃉':9, '🃙':9,
        '🂪':10, '🂺':10, '🃊':10, '🃚':10,
        '🂫':10, '🂻':10, '🃋':10, '🃛':10,
        '🂬':10, '🂼':10, '🃌':10, '🃜':10,
        '🂭':10, '🂽':10, '🃍':10, '🃝':10,
        '🂮':10, '🂾':10, '🃎':10, '🃞':10}

deck_and_values = zip(deck,values)

        
user_hand = []
dealer_hand = []
ucard1 = deck[0]
ucard2 = deck[1]
dcard1= deck[2]
newcard = deck
game_over = False

user_hand.append(ucard1)
user_hand.append(ucard2)
dealer_hand.append(dcard1)
def ask_choice():
    choice = choice.lower()
    return choice

def user_new_card(user_hand):
    user_hand.append(newcard)
    return user_hand


def dealer_new_card(dealer_hand):
    dealer_hand.append(newcard) 
    return dealer_hand



def gen_new_card(choice):
    if choice == "hit":
      user_new_card(user_hand,dealer_hand)
      user_new_card(user_hand)
      return user_hand
    elif choice == "stand":
      dealer_new_card(user_hand,dealer_hand)
      dealer_new_card(dealer_hand)
      return dealer_hand

def check_if_over_21(utotal,dtotal):
    if utotal > 21:
        print("dealer wins.")
        game_over = True
    elif dtotal > 21:
        print("user wins.")
        game_over = True
    else:
        game_over = False
    
    return game_over, utotal, dtotal


def check_if_closer_21(utotal, dtotal):
    u = 21- utotal
    d = 21 - dtotal
    if u < d:
        user_wins = True
    elif u > d:
        user_wins = False
    return user_wins


if __name__ == "__main__":
    hello_to_user()
    place_bets(fund)
    show_cards(user_hand,dealer_hand)
    choice = ask_choice()
    if choice == "hit":
      user_hand = user_new_card(user_hand,dealer_hand)
    elif choice == "stand":
      dealer_hand = dealer_new_card(user_hand,dealer_hand)
    sgow
        
    while game_over == False:
        show_cards(user_hand,dealer_hand)
        choice = ask_choice()
        gen_new_card(choice)
        show_cards(user_hand,dealer_hand)
        utotal = sum(user_hand)
        dtotal = sum(dealer_hand)
        check_if_over_21(utotal,dtotal)
      #  check_if_closer_21(utotal,dtotal)
