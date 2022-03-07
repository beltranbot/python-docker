class Test:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


test = Test("my name")
print(test.name)
print(test._name)

