from enum import Enum

class IdGenerator(Enum):
    def _generate_next_value_(name, _start, _count, _last_values):
        return name