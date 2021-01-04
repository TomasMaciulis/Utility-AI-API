from .configuration_entry import ConfigurationEntry
from .action import Action
from utility_ai.traits.utility_score_trait import UtilityScoreTrait


class Bucket(ConfigurationEntry, UtilityScoreTrait):

    def __init__(self, name: str, description: dict):
        ConfigurationEntry.__init__(self, name, description)
        UtilityScoreTrait.__init__(
            self,
            description['utility_score_formula'],
            super().weight_value,
            name
        )
        self.actions = description['actions']

    @property
    def actions(self):
        return self.__actions

    @actions.setter
    def actions(self, actions: dict):
        act = []
        for action, value in actions.items():
            act.append(Action(action, value))
        self.__actions = act
