from action import Action
from utility import Utility
import json


class Configuration:

    def __init__(self, configuration_json: str):
        self.configuration = json.loads(configuration_json)

        utilities = []
        for name, description in self.__configuration['utilities'].items():
            utilities.append(Utility(name, description))
        self.utilities = utilities

        actions = []
        for name, description in self.__configuration['actions'].items():
            actions.append(Action(name, description))
        self.actions = actions

    @property
    def configuration(self) -> dict:
        return self.__configuration

    @configuration.setter
    def configuration(self, configuration: dict):
        self.__configuration = configuration

    @property
    def utilities(self) -> list[Utility]:
        return self.__utilities

    @utilities.setter
    def utilities(self, utilities: list[Utility]):
        self.__utilities = utilities

    @property
    def actions(self) -> list[Action]:
        return self.__actions

    @actions.setter
    def actions(self, actions: list[Action]):
        self.__actions = actions
