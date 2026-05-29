class InstagramV1:
    def post(self):
        print("You can upload posts")
    def reel(self):
        print("You can upload reels")

class InstagramV2(InstagramV1):
    def story(self):
        print("You can upload story")
    def live(self):
        print("You can go for the live")

class Whatsapp:
    def wpstatus(self):
        print("You can upload whatsapp status")

class Facebook:
    def fbstory(self):
        print("You can upload facebook story")

class InstagramV3:
    def note(self):
        print("You can update the note")

class InstagramV4:
    def instants(self):
        print("You can update the snap")

class InstagramV5(InstagramV3,InstagramV4,Whatsapp,Facebook):
    def crossPlatforms(self):
        print("you can upload same story on your whatsapp status")
        print("you can upload same story on your Facebook status")
        


pooji=InstagramV1()
print("Pooji-InstagramV1")
pooji.post()
pooji.reel()


chitti=InstagramV2()
print("chitti-InstagramV2")
chitti.post()
chitti.reel()
chitti.story()
chitti.live()


pavitra=InstagramV5()
print("pavitra-InstagramV3")
pavitra.instants()
pavitra.note()
pavitra.wpstatus()
pavitra.fbstory()
pavitra.crossPlatforms()

