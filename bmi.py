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
    elif 18.5 <= bmi <= 25.0:
        print("Weight Classification: Normal Weight")
    else:
        print("Weight Classification: Over Weight")

calculate_bmi(weight=57, height=1.73)