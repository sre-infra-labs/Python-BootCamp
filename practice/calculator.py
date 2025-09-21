print("Welcome to Simple Interest Calculator: ")
principle = input("Enter the principle amount: ")
rate_of_interest = input("Enter the rate of interest: ")
time = input("Enter the time in months: ")
interest = int(principle) * int(rate_of_interest) * int(time) / 100
print("Interest Amount: Rs. " + str(interest))

if(int(principle) < 0):
    print ('invalid amount')
    print ('enter again')