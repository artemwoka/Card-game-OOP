from card import Card
class PositionableCard(Card):
    """Гральна карта, яку можна розмістити обличчям вгору або вниз"""

    def __init__(self, rank, suit, face_up=True):
        super().__init__(rank, suit)
        self.is_face_up = face_up
    
    def flip(self):
        """Перевернути карту"""
        self.is_face_up = not self.is_face_up
    
    def __str__(self):
        if self.is_face_up:
            rep = super().__str__()
        else:
            rep = "XX"
        return rep 