import instance_globals


class ConfigurationEntry:

    def __init__(self, name: str, description: dict):
        self.name = name
        self.description = description
        self.parameters = description['parameters']
        self.weight_formula = description['weight_formula']
        self.weight_value = None
        instance_globals.parameters[name] = self.weight_value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> dict:
        return self.__description

    @description.setter
    def description(self, description: dict):
        self.__description = description

    @property
    def weight_formula(self) -> str:
        return self.__weight_formula

    @weight_formula.setter
    def weight_formula(self, weight_formula: str):
        self.__weight_formula = weight_formula

    @property
    def parameters(self) -> list:
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters):
        self.__parameters = parameters

    @property
    def weight_value(self) -> float:
        return self.__weight_value

    @weight_value.setter
    def weight_value(self, weight_value):
        if not weight_value:
            for parameter in self.__parameters:
                locals()[parameter] = instance_globals.parameters[parameter]
            self.__weight_value = eval(self.__weight_formula)
        else:
            self.__weight_value = weight_value
