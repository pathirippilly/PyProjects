from typing import Dict


class InvalidInputArgumentType(Exception):
    def __init__(self, input_args_types: Dict):
        self.input_args_types = input_args_types
        self.message = "One or more arguments has invalid type. Please refer below required types for all arguments: " \
                       f"{[k + ' is of type ' + self.input_args_types[k] for k in input_args_types]}"
        super().__init__(self.message)