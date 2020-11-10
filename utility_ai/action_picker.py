import random
from .models.configuration_entry import ConfigurationEntry
from .traits.utility_score_trait import UtilityScoreTrait


class ActionPicker:
    def __init__(self, items: list[UtilityScoreTrait, ConfigurationEntry]):
        self.items = items

    def pick_weighted_random(self):
        weight_sum = 0

        for item in self.__items:
            weight_sum += item.utility_score_int

        random_number = random.randrange(0, weight_sum)
        for item in self.__items:
            if random_number < item.utility_score_int:
                return item
            else:
                random_number -= item.utility_score_int

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, items: list[UtilityScoreTrait, ConfigurationEntry]):
        self.__items = items
