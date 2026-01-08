'''Open/Closed Principle'''

class OrderProc:
    def process_order(self, order):
        pass

class VIP_order(OrderProc):
    def process_order(self, order):
        pass

class Custom_order(OrderProc):
    def process_order(self, order):
        pass

'''Відкритий для розширення, закритий для змін'''