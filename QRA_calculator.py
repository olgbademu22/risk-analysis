# This function calculates the Single loss expectancy
def SLE(Asset_Value, Exposure_Factor):
    return Asset_Value * Exposure_Factor

# This function calculates the Annual loss expectancy
def ALE(Single_Loss_Expectancy, Annualized_Rate_of_Occurrence):
    return Single_Loss_Expectancy * Annualized_Rate_of_Occurrence


print("Select operation.")
print("1.Single Loss Expectancy")
print("2.Annual Loss Expectancy") 


while True:
    # take input from the user
    choice = input("Enter choice(1/2): ")

    # check if choice is one of the four options
    if choice in ('1', '2'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print("Single Loss Expectancy = Asset Value * Exposure factor:")
            print(num1, "*", num2, "=", SLE(num1, num2))

        elif choice == '2':
            print("Annualized Loss Expectancy = Single Loss Expectancy * Annualized Rate of Occurrence:")
            print(num1, "*", num2, "=", ALE(num1, num2))

        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Do you want to calculate again? (yes/no): ")
        if next_calculation == "no":
          print('See you later.')
          break
    else:
        print("Invalid Input")