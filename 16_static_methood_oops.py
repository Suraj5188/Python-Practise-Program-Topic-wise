#Static methood in oops 

import this


class Company:
    company_name="Google"

    def simple_methood(self, name):
        print(f"GoOd EveN!nG {name}")


    #We Can make number of static methood in program

    #Static methood-1
    @staticmethod
    def getname():
        print(f"Name of company is {suraj.company_name} & locaton in {suraj.company_location}")

    #static methood-2
    @staticmethod
    def static_methood_2():
        print("Hello") 

suraj=Company()

suraj.company_location="USA"

suraj.getname()
suraj.static_methood_2()

suraj.simple_methood("suraj")