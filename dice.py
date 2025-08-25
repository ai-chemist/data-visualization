from random import randint

class Dice:
    """주사위 하나를 나타내는 클래스"""

    def __init__(self, sides=6):
        """sides - 몇 면체 주사위인지"""
        self.sides = sides

    def roll(self):
        """1 to sides 까지의 숫자 중 1개 반환"""
        return randint(1, self.sides)