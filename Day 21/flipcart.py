class Flipkart:
    products={'laptop':78543,
              'phone':20500,
              'earphones':854,
              'bags':123}
    @classmethod
    def showproducts(cls):
        print(cls.products)
        
    def register(self,name,phno):
        self.username=name
        self.phonenumber=phno
        print(f"Welcome to FLipkart {self.username},shop now!!!")

    @staticmethod
    def discount():
        print("Hey all, 10% discount is going on,show now!!!!!!!!!!!")

pavitra=Flipkart()
pavitra.register('pavitra','13223444867')
pavitra.discount()
pavitra.showproducts()
    
