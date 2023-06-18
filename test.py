class Test:
    def __init__(self, **kwargs) -> None:
        self.name = kwargs.get("name")
        self.tester = kwargs["tester"]


test = Test(name="Test 1", tester="A")
