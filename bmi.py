def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    #Add code here to calculate BMI
    bmi = weight / (height ** 2)
    #Add code here to display calculate BMI
    print("BMI = {:.2f}".format(bmi))

    # Determine weight classification
    if bmi < 18.5:
        print("Weight Classification: Under Weight")
        return -1
    elif 18.5 <= bmi <= 25.0:
        print("Weight Classification: Normal Weight")
        return 0
    else:
        print("Weight Classification: Over Weight")
        return 1

result = calculate_bmi(weight=57, height=1.73)
print("Return Value:", result)