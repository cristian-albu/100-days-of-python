import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
game_still_going = True
the_winner = ''

player_hand = {
    "cards": [],
    "total": 0
}
dealer_hand = {
    "cards": [],
    "total": 0
}

def deal_card(hand):
    hand["cards"].append(random.choice(cards))

def calculate_total(hand):
    total = 0
    ace_count = hand["cards"].count("A")
    
    for card in hand["cards"]:
        if card in ["J", "Q", "K"]:
            total += 10
        elif card != "A":
            total += card
    for _ in range(ace_count):
        if total + 11 > 21:
            total += 1
        else:
            total += 11
    hand["total"] = total

def evaluate_winner():
    calculate_total(player_hand)
    calculate_total(dealer_hand)

    if player_hand["total"] == dealer_hand["total"]:
        return "Draw"
    elif player_hand["total"] > 21:
        return "Dealer"
    elif dealer_hand["total"] > 21:
        return "Player"
    elif player_hand["total"] > dealer_hand["total"]:
        return "Player"
    else:
        return "Dealer"

deal_card(player_hand)
deal_card(dealer_hand)
deal_card(player_hand)
deal_card(dealer_hand)

while game_still_going:
    calculate_total(player_hand)
    calculate_total(dealer_hand)
    print(f"Your hand: {player_hand}")
    print(f"Dealer's hand: {dealer_hand}")

    if dealer_hand["total"] < 15:
        deal_card(dealer_hand)

    choice = input("Want another card? y/n: ")

    if choice == "y":
        deal_card(player_hand)
    else:
        game_still_going = False
        the_winner = evaluate_winner()

print(f"Player's hand: {player_hand}")
print(f"Dealer's hand: {dealer_hand}")
print(f"The winner is: {the_winner}")





