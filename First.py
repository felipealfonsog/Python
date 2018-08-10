# printf("Hello World")

class MITxStaff(object):
    firstname = ""
    lastname = ""


    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

# there's an issue here
class TA(MITxStaff):
       awesomeLevel = 0

       def __init__(self, firstname, lastname, awesomeLevel):
           self.awesomeLevel = awesomeLevel
           MITxStaff.__init__(self, firstname, lastname)


       def toString(self):
           return "{} {} has an awesome level of {}".format(self.firstname, self.lastname, self.awesomeLevel)





Nitish = TA("Nitish", "Mital", 100)
Jing = TA("Jing", "Ma", 9001)

print(Nitish.toString())
print(Jing.toString())