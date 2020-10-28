from configuration_entry import ConfigurationEntry


class Action(ConfigurationEntry):

    def __init__(self, name: str, description: dict):
        super().__init__(name, description)

        self.utility_score_formula = description['utility_score_formula']
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
            x = super().weight_value
            self.__utility_score = eval(self.__utility_score_formula)
        else:
            self.__utility_score = utility_score
