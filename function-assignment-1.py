class SubfieldsInAI:
    def Subfields(self):
        for name in list1:
            print(name)

list1=["Machine Learning", "Neural Networks","Vision", "Robotics", "Speech Processing","Natural Language Processing"]
ai = SubfieldsInAI()
ai.Subfields()

class OddEven:
    def oddEven(self,num):
       # num= int(input("Enter a number: "))
        if(num%2 == 0):
            print("Even")
        else:
            print("Odd")
#num=5
oe = OddEven()
oe.oddEven(5)

class ElegiblityForMarriage:
    def Elegible(self, gender, age):
        print(f"gender: {gender}")
        print(f"age: {age}")
        if(gender.lower() =="male"):
            if(age >= 21):
                print("Eligible")
            else:
                print("Not Eligible")
        elif gender.lower() == "female":
            if age >= 18:
                print("Eligible")
            else:
                print("Not Eligible")
        else:
            print("Invalid gender input")

person = ElegiblityForMarriage()
person.Elegible("male", 18)

class FindPercent:
    def percentage(self, s1, s2, s3, s4, s5):
        total = s1 + s2 + s3 + s4 + s5
        percent = (total / 500) * 100  # Assuming each subject is out of 100
        print(f"Subject1= {s1}")
        print(f"Subject2= {s2}")
        print(f"Subject3= {s3}")
        print(f"Subject4= {s4}")
        print(f"Subject5= {s5}")
        print(f"Total : {total}")
        print(f"Percentage : {percent}")

# Example usage:
marks = FindPercent()
marks.percentage(98, 87, 95, 95, 93)


class Triangle:
    def triangle(self):
        # Area calculation
        height = 32
        breadth = 34
        area = (height * breadth) / 2
        print(f"Height:{height}")
        print(f"Breadth:{breadth}")
        print("Area formula: (Height*Breadth)/2")
        print(f"Area of Triangle: {area}")

        # Perimeter calculation
        height1 = 2
        height2 = 4
        breadth_perimeter = 4
        perimeter = height1 + height2 + breadth_perimeter
        print(f"Height1:{height1}")
        print(f"Height2:{height2}")
        print(f"Breadth:{breadth_perimeter}")
        print("Perimeter formula: Height1+Height2+Breadth")
        print(f"Perimeter of Triangle: {perimeter}")

# Example usage:
triangle = Triangle()
triangle.triangle()


