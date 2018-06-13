class User(object):

    def __init__(self, login="", password=""):
        self.login = login
        self.password = password

    @classmethod
    def test_user(cls):
        return cls(
            login="vidan.ugil",
            password="^Tomato_65^"
        )
