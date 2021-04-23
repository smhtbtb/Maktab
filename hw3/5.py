class asar:

    def __init__(self, onvan, saahebha=None):
        self.onvan = onvan
        self.saahebha = saahebha


class maqaale(asar):

    def __init__(self, onvan, saahebha=None, naame_majalle=None, saale_enteshaar=None):
        self.naame_majalle = naame_majalle
        self.saale_enteshaar = saale_enteshaar
        super().__init__(onvan, saahebha)


class sher(asar):

    def __init__(self, onvan, saahebha=None, qaalebe_adabi=None):
        self.qaalebe_adabi = qaalebe_adabi
        super().__init__(onvan, saahebha)


class ketab(asar):

    def __init__(self, ISBN, onvan, saahebha=None):
        self.ISBN = ISBN
        super().__init__(onvan, saahebha)


class user:

    def __init__(self, name, email=None, jensiat=None):
        self.name = name
        self.email = email
        self.jensiat = jensiat


class pazhooheshgar(user):

    def __init__(self, reshte, name, daneshgah=None, email=None, jensiat=None):
        super().__init__(name, email, jensiat)
        self.reshte = reshte
        self.daneshgah = daneshgah


class shaer(user):

    def __init__(self, name, sabk=None, email=None, jensiat=None):
        super().__init__(name, email, jensiat)
        self.sabk = sabk


class nevisande(user):

    def __init__(self, code_nevisandegi, name, genre=None, email=None, jensiat=None):
        super().__init__(name, email, jensiat)
        self.code_nevisandegi = code_nevisandegi
        self.genre = genre


