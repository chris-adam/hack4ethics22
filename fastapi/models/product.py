import datetime

class Product():

    def __init__(self, product_name: str, decision: datetime.date, expiration_date: datetime.date):
        self._product_name = product_name
        self._decision = decision
        self._expiration_date = expiration_date

    @property
    def product_name(self):
        return self._product_name

    @property
    def decision(self):
        return self._decision

    @property
    def expiration_date(self):
        return self._expiration_date
