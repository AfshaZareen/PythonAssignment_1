'''Write a program that asks the user for their birth year and calculates their age.'''


from datetime import datetime
birth_year = int(input("Enter your Birth Year: "))
#current_year = 2024
current_year = datetime.now().year
print("Your Age is: ", current_year - birth_year)