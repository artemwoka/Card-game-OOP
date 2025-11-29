from card import Card
from hand import Hand
from positionableCard import PositionableCard
from unprintableCard import UnprintableCard
from deck import Deck

my_hand = Hand()
opponent_hand = Hand()
deck = Deck()
deck.populate()
deck.shuffle()

game_rounds = input("Скільки раундів ви хочете зіграти? Введіть число: ")
try:
    rounds = int(game_rounds)
except ValueError:
    print("Будь ласка, введіть дійсне число.")
    rounds = 1
my_points = 0
opponent_points = 0
for _ in range(rounds):
    deck.deal([my_hand, opponent_hand], per_hand=1)
    print("Моя карта", my_hand)
    print("Твоя карта", opponent_hand)

    my_card = my_hand.cards[0]
    opponent_card = opponent_hand.cards[0]

    if my_card.rank > opponent_card.rank:
        print("Я виграв!\n")
        my_points += 1

    elif my_card.rank < opponent_card.rank:
        print("Ти виграв!\n")
        opponent_points += 1

    else:
        print("Нічия!\n")
        print("Додаткові карти для порівняння:")
        deck.deal([my_hand, opponent_hand], per_hand=1)
        print("Моя карта", my_hand)
        print("Твоя карта", opponent_hand)
        my_card = my_hand.cards[1]
        opponent_card = opponent_hand.cards[1]
        if my_card.rank > opponent_card.rank:
            print("Я виграв цей раунд!\n")
            my_points += 1
        elif my_card.rank < opponent_card.rank:
            print("Ти виграв цей раунд!\n")
            opponent_points += 1
        else:
            print("Знову нічия!\n")
    my_hand.clear()
    opponent_hand.clear()



print("Підсумки гри:")
print("Мої очки:", my_points)
print("Твої очки:", opponent_points)
if my_points > opponent_points:
    print("Я виграв гру!")
elif my_points < opponent_points:
    print("Ти виграв гру!")
else:
    print("Гра закінчилася нічиєю!")




    












