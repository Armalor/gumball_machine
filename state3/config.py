class Config:

    __instance = None

    def __new__(cls, *args, **kwargs):

        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.debug = False


c1 = Config()
c2 = Config()

c1.debug = True

print(c1, c2, c1 is c2)
