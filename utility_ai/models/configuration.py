from .bucket import Bucket
from .utility import Utility
import json


class Configuration:

    def __init__(self, configuration_json: str):
        self.configuration = json.loads(configuration_json)

        utilities = []
        for name, description in self.__configuration['utilities'].items():
            utilities.append(Utility(name, description))
        self.utilities = utilities

        buckets = []
        for name, description in self.__configuration['buckets'].items():
            buckets.append(Bucket(name, description))
        self.buckets = buckets

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
    def buckets(self) -> list[Bucket]:
        return self.__buckets

    @buckets.setter
    def buckets(self, buckets: list[Bucket]):
        self.__buckets = buckets
