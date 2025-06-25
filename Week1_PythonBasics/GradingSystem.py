#Accept avg score from student and display result. Let the input be int.
''' 0 to 69 Fail
70 to 84 Second class
85 to 95 First class
96 to 100 Excellent'''
score = int(input("Enter avg score: "))
if score>=0 and score<=100:
    if score >= 96:
        print("Excellent") 
    elif score >= 85:
        print("First class")
    elif score >=70:
        print("Second class")
    else:
        print("FAIL")
else:
    print("Invalid")