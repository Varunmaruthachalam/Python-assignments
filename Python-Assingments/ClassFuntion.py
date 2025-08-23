class Classfunction():
    def Subfields():
        subfields = ["MachineLearning",
           "NeuralNetworks",
           "Vision",
           "Robotics",
           "SpeechProcessing",
           "Natural Language Processing"]
        print("Sub-fields in AI are:")
        for temp in subfields:
            print(temp)
    
    def OddEven():
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print(f"{num} is Even number")
        else:
            print(f"{num} is Odd number")
            
    def Eligible():
        gender = input("Your Gender:")
        age = int(input("Your Age:"))

        if (gender=="male" and age>=21)or(gender=="female" and age>=18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
            
    def findpercent():
        s1 = int(input("Subject1= "))
        s2 = int(input("Subject2= "))
        s3 = int(input("Subject3= "))
        s4 = int(input("Subject4= "))
        s5 = int(input("Subject5= "))

        total = s1 + s2 + s3 + s4 + s5
        percent = (total / 500) * 100

        print("Total :", total)
        print("Percentage :", percent)
    
    def triangle():
        h = int(input("Height:"))
        b = int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        area = (h * b) / 2
        print("Area of Triangle:", area)
        h1 = int(input("Height1:"))
        h2 = int(input("Height2:"))
        b2 = int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter = h1 + h2 + b2
        print("Perimeter of Triangle:", perimeter)