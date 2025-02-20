lists=["Machine Learning" , "Neural Networks", "Vision" , "Robotics" , "Speech Processing" , "Natural Language Processing"]
class SubfieldsInAI:
    def Subfields():
        print("Sub-fields in AI are:", end='\n')
        for AI in lists:
            print(AI)
    def OddEven():
        num=int(input(" Enter a number:"))
        if (num%2==0):
            print(num,"is Even Number")
        else:
            print(num,"is Odd Number")
    def Elegible():
        a=input(" Your Gender: ") 
        b=int(input("Your Age:")) 
        if(a=="Male") and (b>25):
            print(" ELIGIBLE") 
        elif(a=="Female") and (b>18):
            print("ElIGIBLE") 
        else:
            print("NOT ELIGIBLE")