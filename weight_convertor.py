weight = int(input("Enter your weight : "))
ask = input("In kg or pound : ")
kg_to_pound = weight * 2.20462
pound_to_kg = weight * 0.453592
if ask == "kg" :
    print(f"You are {kg_to_pound} pound")
    # print("You weigh " + kg_to_pound + " pound")
elif ask == "pound" :
    print("You weigh " + str(pound_to_kg) + " kg")
