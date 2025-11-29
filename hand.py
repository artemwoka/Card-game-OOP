class Hand:
    """ Рука гравця: набір карт на руках у одного гравця """

    def __init__(self):
        self.cards = []
    
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "<пусто>"
        return rep
    
    def clear(self):
        """Очистити руку від карт"""
        self.cards = []
    
    def add(self, card):
        """Додати карту до руки"""
        self.cards.append(card)
    
    def give(self, card, other_hand):
        """Передати карту іншій руці"""
        self.cards.remove(card)
        other_hand.add(card)