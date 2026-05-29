from abc import ABC,abstractmethod

class Phonepay:
    def input(self):
        print("You can scan and enter the amount")
    def amount(self):
        print("You have the amount to pay")
    def pin(self):
        print("You can enter the  pin")

    @abstractmethod
    def verification(self):
        pass

    def paymentstatus(self):
        print("Your amount is transferred successfully/failed")

class HDFC(Phonepay):
    def verification(self):
        print("Verification is completed through hdfc")

class SBI(Phonepay):
    def verification(self):
        print("Verification is completed through sbi")

class UNION(Phonepay):
    def verification(self):
        print("Verification is completed through union")

class AXIS(Phonepay):
    def verification(self):
        print("Verification is completed through axis")


vyshu=HDFC()
vyshu.input()
vyshu.amount()
vyshu.pin()
vyshu.verification()
vyshu.paymentstatus()


deepi=SBI()
deepi.input()
deepi.amount()
deepi.pin()
deepi.verification()
deepi.paymentstatus()

sri=UNION()
sri.input()
sri.amount()
sri.pin()
sri.verification()
sri.paymentstatus()

chandana=AXIS()
chandana.input()
chandana.amount()
chandana.pin()
chandana.verification()
chandana.paymentstatus()


        
        
