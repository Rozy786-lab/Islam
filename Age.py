from datetime import datetime
#Get user input
birth_year  = int(input("Enter Birth Year: "))
birth_month = int(input("Enter Month(1-12): "))
birth_date  = int(input("Enter Date(1-31): "))
#Create current Date
today = datetime.now()
#Get Current Age
age = today.year - birth_year
#Conditioning if the birthday hasn't occured adjust age
if(today.month, today.day) < (birth_month, birth_date):
    age -=1
#Print current Age
print(f"Current Age is: {age}") 
#Get Upcoming Birthday
current_year = today.year
#Conditioning if the birthday has already passed
if(today.month,today.day) >= (birth_month, birth_date):
    current_year +=1

next_birthday = datetime(current_year,birth_month,birth_date)    
#Calculate remaining days for your birthday
remaining_days = (next_birthday - today).days
#Printing the statement
print(f"Upcomming Birthday: {next_birthday.strftime('%Y-%m-%d')}")
print(f"Remaning Days:{remaining_days}")
   
   