from .configuration_entry import ConfigurationEntry
from utility_ai.traits.utility_score_trait import UtilityScoreTrait


class Action(ConfigurationEntry, UtilityScoreTrait):

    def __init__(self, name: str, description: dict):
        ConfigurationEntry.__init__(self, name, description)
        UtilityScoreTrait.__init__(
            self,
            description['utility_score_formula'],
            super().weight_value,
            name
        )
