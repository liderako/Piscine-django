class Intern:
    
    class Coffee:
        def     __str__(self):
            return ("This is the worst coffee you ever tasted.")

    def     __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.name = name

    def     __str__(self):
        return (self.name)

    def     work(self):
        raise Exception("I’m just an intern, I can’t do that...")
    
    def     make_coffee(self):
        return (self.Coffee())

def testMain():
    oneInternWithoutName = Intern()
    twoInternWithName = Intern("Antonio")
    print ("< One Intern name >", oneInternWithoutName)
    print ("< Two Intern name >", twoInternWithName)
    late = twoInternWithName.make_coffee()
    print ("<", twoInternWithName, "make coffee >", late)
    try:
        oneInternWithoutName.work()
    except Exception:
        print ("I’m just an intern, I can’t do that...")

if __name__ == '__main__':
    testMain()
