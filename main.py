class EventTicket:
    def __init__(self, name, price, discount=0):
        self.name = name
        self.price = price
        self.discount = discount

    def get_price(self):
        return self.price - (self.price * self.discount / 100)

class EventTicketComparator:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def compare_tickets(self):
        self.tickets.sort(key=lambda x: x.get_price())
        return self.tickets

# Misol uchun ma'lumotlarni kiritish
comparator = EventTicketComparator()

ticket1 = EventTicket("Ticket 1", 100, 10)
ticket2 = EventTicket("Ticket 2", 80, 5)
ticket3 = EventTicket("Ticket 3", 120, 15)

comparator.add_ticket(ticket1)
comparator.add_ticket(ticket2)
comparator.add_ticket(ticket3)

sorted_tickets = comparator.compare_tickets()

for i, ticket in enumerate(sorted_tickets):
    print(f"{i+1}. {ticket.name}: {ticket.get_price()} so'm")
```

Kodda EventTicket klassi eventning nomi, narxi va faqatgina narxning foiz bo'yicha kamayishi kabi xususiyatlarni saqlaydi. EventTicketComparator klassi eventlar ro'yxatini saqlaydi va ularni narx bo'yicha tartibga soladi. Misol uchun ma'lumotlarni kiritish uchun EventTicketComparator klassi yaratiladi, keyin eventlar qo'shilib, ularni narx bo'yicha tartibga solish uchun compare_tickets metodidan foydalaniladi.
