class Hotstar:

    def __init__(self,name):
        self.name=name
        print(f"Hello {self.name}, Welcome to Hotstar---------")

    
    def login(self):
        print("You can login")
    def search(self):
        print("You can search")
    def categories(self):
        print("You can see the divisions")
    def playcontrollers(self):
        print("You can pause,resume and play")
    def livesports(self):
        print("You can watch sports on live")


    def ads(self):
        print("Ads will run")
    def movies(self):
        print("Limited Movies")
    def download(self):
        print("cannot download")
    def quality(self):
        print("quality is low")

class Hotstarpremium(Hotstar):

    def __init__(self,name):
        self.name=name
        print(f"Hello {self.name}, Welcome to Hotstar Premium---------")

    def ads(self):
        print("Ads will not run")
    def movies(self):
        print("Unlimited Movies")
    def download(self):
        print("can download")
    def quality(self):
        print("quality is high")


pavi=Hotstar("pavi")
pavi.login()
pavi.search()
pavi.categories()
pavi.playcontrollers()
pavi.livesports()
pavi.ads()
pavi.movies()
pavi.download()
pavi.quality()


pooji=Hotstarpremium("pooji")
pooji.login()
pooji.search()
pooji.categories()
pooji.playcontrollers()
pooji.livesports()
pooji.ads()
pooji.movies()
pooji.download()
pooji.quality()







    

    
    
    
        
