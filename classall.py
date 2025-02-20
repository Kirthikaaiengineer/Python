class multiplefunctions():
    def OddEven():
        num=int(input(" Enter a number:"))
        if (num%2==0):
            print(num,"is Even Number")
        else:
            print(num,"is Odd Number")
    def Elegible():
        a=input(" Your Gender: ") 
        b=int(input("Your Age:")) 
        if(a=="Male") and (b>21):
            print(" ELIGIBLE") 
        elif(a=="Female") and (b>18):
            print("ElIGIBLE") 
        else: 
            print("NOT ELIGIBLE")
    def percentage():
        S1=int(input("Subject1="))
        S2=int(input("Subject2="))
        S3=int(input("Subject3="))
        S4=int(input("Subject4="))
        S5=int(input("Subject5="))
        total = S1 + S2 + S3 + S4 + S5
        print("Total:", total )
        Percentage =(total/500)*100
        print("Percentage:", Percentage )
    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        Areaformula= (Height*Breadth)/2
        print("Area of triangle:",Areaformula )
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        Perimeterformula=Height1+Height2+Breadth
        print("Perimeter of Triangle::",Perimeterformula)
    

    
