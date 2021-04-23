class User:
    first_name: str
    last_name: str
    __phone: str


class Seller(User):
    phone: str


class Product:
    price: float
    picture: ...
    definition: str
    age: float  # karkard


class Types(Product):
    ...


class Product_Basket:
    ...
