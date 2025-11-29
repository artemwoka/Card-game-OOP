from card import Card
class UnprintableCard(Card):
    """Гральна карта, яку не можна надрукувати"""

    def __str__(self):
        return "<не можна надрукована >"
