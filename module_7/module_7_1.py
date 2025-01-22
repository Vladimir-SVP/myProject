class Product():
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'    
class Shop():
    __file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r')
        content = file.read()
        file.close
        return content
    def add(self, *products):
        file = open(self.__file_name, 'r+')
        content = self.get_products()
        for i in range(len(products)):
            if f'{products[i]}' in content:
                print(f'Продукт {products[i].name} уже есть в магазине')
            else:                
                file.write(f'{products[i]}\n')
        file.close()
print('=========================')              
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())