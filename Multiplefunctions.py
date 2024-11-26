class multiplefunctionstest():
    def __init__(self):
        self.lists=("Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "NaturalLanguageProcessing")
    def display_AISubfields(self):
        print("Sub-fields in AI are: ")
        for item in self.lists:
            print(item)    
    
    def OddEven():    
        number=int(input("Enter the Number: "))
        if number%2==0:
            print("The given number is even")
            message=("This number is even")
        else:
            print("The given number is odd")
            message=("This number is odd")
        return message
    
    def eligibilityformarriage():  
        age=int(input("Enter your age"))
        if age==20:
            print("Not Eligible for Marriage")
            eligibilitycat=("you are not eligible")
        elif age>>20:
            print("Eligible")
            eligibilitycat=("you are eligible")
        else:
            print("Not Eligible")
            eligibilitycat=("you are not eligible")
            return eligibilitycat
    
    def findpercentage():
        subject1= 98
        subject2= 87
        subject3= 95
        subject4= 95
        subject5= 93  
        maximummarks=500 
        totalmarks=subject1 + subject2 + subject3 + subject4 + subject5
        percentage = (totalmarks / maximummarks) * 100  
        print("Percentage:", percentage)  
    
    
        