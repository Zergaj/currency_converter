class Email(object):

    def __init__(self, email="", subject="", body=""):
        self.email = email
        self.subject = subject
        self.body = body

    @classmethod
    def test_email(cls):
        return cls(
            email="zergaj@mail.ru",
            subject="test_email",
            body="adsf asdf asdf asdf asdf"
        )