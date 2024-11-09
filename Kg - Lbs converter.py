weight = float(input("weight: "))
unit = input("(K)g or (L)bs: ")


if unit == str("k"):
    calculation = weight * 2.2
    print("the weight in Lbs is: " , calculation) 


elif unit == str("l"):
    calculation = weight * 0.45
    print("the weight in Kg is: " , calculation )

input("press ENTER to exit: ")

