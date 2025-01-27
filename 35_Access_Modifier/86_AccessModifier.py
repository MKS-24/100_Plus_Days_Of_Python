# Public kahi se bhi Access kersakhte hai
# Private Bahir se access nh kiye jasakhte
# Protected only classes me access kiye ja sakhte hai
# python me acces modifiers nh hote ye user as a convention use kerte hai
class Employee:
    def __init__(self):
        self.__name = "Hey"  #  double underscore se variable private hojata hai
    def _subject(self):  # _ se protected kiya jata hai
        print("Maths")
# class student(Employee):
#     pass


a = Employee()
# print(a.__name)
# ager private ko access kerna hai tu kuch aesa karo
# print(a._Employee__name)
# print(a.__dir__())
a._subject()
