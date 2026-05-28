#Encapsulation
class instagram:
    def __init__(self,username,password,cf):
        self.username=username
        self.__password=password
        self._cf=cf

    def getpassword(self):
        return self.__password

    def setpassword(self,new_password):
        self.__password=new_password

    @property
    def accesscf(self):
        return self._cf

    @accesscf.setter
    def accesscf(self,new_friend):
        self._cf.append(new_friend)

        
        


pavitra=instagram('pavitra','pavi@2005',['pooji','deepi','mahee','vyshu'])
print("Befor USername:",pavitra.username)
pavitra.username='pooji'
print("After USername:",pavitra.username)

print("Before password:",pavitra.getpassword())
pavitra.setpassword('pooji@20')
print("After password:",pavitra.getpassword())

print("Before closefriends:",pavitra.accesscf)
pavitra.accesscf='chitti'
print("After closefriends:",pavitra.accesscf)

