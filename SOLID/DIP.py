'''Dependency Inversion Principle'''

class DeliveryService:
    def deliver(self, order):
        pass

class InPost(DeliveryService):
    def deliver(self, order):
        print("Delivered by InPost")

class DPD(DeliveryService):
    def deliver(self, order):
        print("Delivered by DPD")

class OrderProcess:
    def __init__(self, delivery_service):
        self.delivery_service = delivery_service

    def process_order(self, order):
        self.delivery_service.deliver(order)

'''залежимо від абстракцій,можемо легко змінювати конкретний сервіс доставки'''