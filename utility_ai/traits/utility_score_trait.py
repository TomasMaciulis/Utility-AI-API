from numbers import Number


class UtilityScoreTrait:
    def __init__(self, utility_score_formula: str, weight_value: Number):
        self.utility_score_formula = utility_score_formula
        self.weight_value = weight_value
        self.utility_score = None

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
        else:
            self.__utility_score = utility_score

        self.utility_score_int = int(self.__utility_score * 10000)
