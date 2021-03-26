# 1.10.3
class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def clients_base(self):
        return f'Клиент: {self.name}; Баланс = {self.balance} рублёфф'


new_client = Client("Вася Пупкин", 50)
print(new_client.clients_base())


# 1.10.4
class Guest(Client):
    def __init__(self, name, balance, city, status):
        super().__init__(name, balance)
        self.city = city
        self.status = status

    def get_status(self):
        return self.status

    def get_city(self):
        return self.city

    def get_balance(self):
        return self.balance


clients = [
    {'name': 'Ивашка Дятлов', 'balance': 100, 'city': 'Москва', 'status': 'Учитель'},
    {'name': 'Роберт Дауни', 'balance': 2750, 'city': 'Сталинград', 'status': 'Артист'},
    {'name': 'Виктор Кимималов', 'balance': 150, 'city': 'Воронеж', 'status': 'Велосипедист профессиональный'},
    {'name': 'Хамали Наваилов', 'balance': 10, 'city': 'Омск', 'status': 'Певец'}
           ]
party_guests = [Guest(p['name'], p['balance'], p['city'], p['status']) for p in clients]
for guest in party_guests:
    print(f'"{guest.get_name()}", г.{guest.get_city()}, статус "{guest.get_status()}"')
