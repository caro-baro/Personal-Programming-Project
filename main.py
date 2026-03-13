## Personal Programming Project - Carolina 
fund = 1000
deck = ['U+1F0A1']

def hello_to_user():
    print("Hello, we are playing\nBlackjack")
    


def place_bets(bet):
    print(f"You have: ${fund}")
    bet = int(input("Place your bets:\n"))
    return bet



def show_cards():
    print()



def ask_choice():
    choice = input("Hit or Stand?")




if __name__ == "__main__":
    hello_to_user()
    place_bets(fund)

