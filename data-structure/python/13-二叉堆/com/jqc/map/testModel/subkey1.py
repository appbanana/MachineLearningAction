from .key import Key


class SubKey1(Key):
    def __eq__(self, other):
        if self is other:
            return True
        if other is None or not isinstance(other, Key):
            return False
        return self.value == other.value
    
    def __hash__(self):
        return super().__hash__()
