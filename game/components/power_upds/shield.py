from game.components.power_upds.power_up import PowerUp
from game.utils.constants import SHIELD,SHIELD_TYPE,HEART,HEART_TYPE,DUPLICATE,DUPLICATE_TYPE,COIN,COIN_TYPE

class Shield(PowerUp):
    def __init__(self):
        super().__init__(SHIELD,SHIELD_TYPE)

    
class Heart(PowerUp):
    def __init__(self):
        super().__init__(HEART,HEART_TYPE)

class Duplicate(PowerUp):
    def __init__(self):
        super().__init__(DUPLICATE,DUPLICATE_TYPE)


class Coin(PowerUp):
    def __init__(self):
        super().__init__(COIN,COIN_TYPE)
