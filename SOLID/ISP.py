'''Interface Segregation Principle'''

class Printable:
    def print(self):
        pass

class Scannable:
    def scan(self):
        pass

class Printter(Printable):
    def print(self):
        print("Printing...")

class Scanner(Scannable):
    def scan(self):
        print("Scanning...")

'''маленькі інтерфейси,принтер не зобов’язаний сканувати'''