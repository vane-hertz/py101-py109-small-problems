from datetime import datetime

age = input("What is your age? ")
age_retire = input("At what age would you like to retire? ")
current_year = datetime.now().year
years_to_go = int(age_retire) - int(age)

print(f"It's {current_year}. You will retire in {current_year + years_to_go}.\nYou have only {years_to_go} years of work to go!")