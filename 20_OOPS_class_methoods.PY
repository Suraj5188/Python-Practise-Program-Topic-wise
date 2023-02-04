#Class Methoods 


class Product:

    no_of_product=100
    
    def product_details(self):
        return f"{self.name}\t{self.no_of_product}"

    @classmethod
    def change_product(cls ,new_product):
        cls.new_Product=new_product
       

    
product1=Product()
product2=Product()

product1.name="Computer"
product1.quality="Good"

product1.change_product(12)
    
product2.name="Smart Phone"
product2.quality="Good"

print(product1.no_of_product)