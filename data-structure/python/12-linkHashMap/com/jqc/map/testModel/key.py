class Key(object):
    
    def __init__(self, value):
        self.value = value
    
    def __hash__(self):
        return self.value // 10
    
    def __eq__(self, other):
        if self is other:
            return True
        if other is None or self.__class__.__name__ != other.__class__.__name__:
            return False
        return self.value == other.value
    
    def __str__(self):
        return 'Key(' + str(self.value) + ')'
