from configuration_entry import ConfigurationEntry
from action import Action


class Bucket(Action):

    def __init__(self, name: str, description: dict):
        ConfigurationEntry.__init__(self, name, description)
        Action.__init__(self, name, description)
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
