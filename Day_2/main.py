#  PROGRAM START
#######################################

print("#############################################")
print("#\t\t\t\tTIP CALCULATOR\t\t\t\t#")
print("#############################################\n\n")

print("Welcome to the tip calculator")

total_bill = input("What was the total bill? $")
tip_percentage = input("WHat tip percentage would you like to give? 10, 12, 15? ")
total_people = input("How many people to split the bill? ")

# convert input to float/int
total_bill_f = float(total_bill)
tip_percentage_i = int(tip_percentage)
total_people_f = int(total_people)

tip_from_bill = total_bill_f * (tip_percentage_i/100)  # calculate tip
final_bill = total_bill_f + tip_from_bill  # add tip to total bill
bill_per_person = final_bill/total_people_f

bill_per_person_rounded = round(bill_per_person, 2)  # round to the nearest two decimal places

print(f"Each person will pay ${bill_per_person_rounded}")

