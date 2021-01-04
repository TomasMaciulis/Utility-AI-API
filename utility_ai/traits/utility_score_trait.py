from numbers import Number
from utility_ai import instance_globals

class UtilityScoreTrait:
    def __init__(
            self,
            utility_score_formula: str,
            weight_value: Number,
            name
    ):
        self.utility_score_formula = utility_score_formula
        self.weight_value = weight_value
        self.utility_score = None
        self.name = name

    @property
    def utility_score_formula(self) -> str:
        return self.__utility_score_formula

    @utility_score_formula.setter
    def utility_score_formula(self, utility_score_formula: str):
        self.__utility_score_formula = utility_score_formula

    @property
    def utility_score(self) -> float:
        return self.__utility_score

    @utility_score.setter
    def utility_score(self, utility_score: float):
        if not utility_score:
            x = self.weight_value
            self.__utility_score = eval(self.__utility_score_formula)
            if (
                    self.name == instance_globals.parameters['currentAction']
                    or
                    self.name == instance_globals.parameters['currentBucket']
            ):
                self.__utility_score = self.__utility_score + self.__utility_score / 100 * 80
        else:
            self.__utility_score = utility_score

        self.utility_score_int = int(self.__utility_score * 10000)
