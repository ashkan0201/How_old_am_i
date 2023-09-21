# <<< Dedicated to the most important person in my life (: >>>

# Required libraries
from datetime import datetime
from tabulate import tabulate

today = datetime.today()

# Create a table
table = [[today.strftime(" Dedicated to the most important person in my life (: \nFor example =>>> %Y/%m/%d  \nUse the 'Ctrl + c' or write: 'exit' to finish\n")]]
print(tabulate(table, tablefmt="grid"))

"""The main code and conditions section are checked and displayed in the output."""
while True:
    user_date_of_bron = input(" Please write your date of birth =>>> ")
    spliter = user_date_of_bron.split("/")
    
    if user_date_of_bron == "exit":
        break 

    if len(spliter) == 3 and len(spliter[0]) == 4 and len(spliter[2]) in [1,2] and int(spliter[0]) in list(range(1000, today.year+1)) and int(spliter[1]) in list(range(1,13)) and int(spliter[2]) in list(range(1,32)):
    
        if today.month == int(spliter[1]) and today.day == int(spliter[2]):
            print(f"\n ===> Age: You are {today.year - int(spliter[0])} years, {0} months and {0} days old")
#
        elif today.month > int(spliter[1]) and today.day > int(spliter[2]):
            print(f"\n ===> Age: You are {today.year - int(spliter[0])} years, {today.month - int(spliter[1])} months and {today.day - int(spliter[2])} days old")
#
        elif today.month < int(spliter[1]) and today.day < int(spliter[2]) and today.month in [5,7,10]:
            print(f"\n ===> Age: You are {today.year - int(spliter[0])-1} years, {abs(today.month - int(spliter[1])+11)} months and {today.day - int(spliter[2])+30} days old")

        elif today.month < int(spliter[1]) and today.day < int(spliter[2]) and today.month in [1,2,4,6,8,9,11,12]:
            print(f"\n ===> Age: You are {today.year - int(spliter[0])-1} years, {abs(today.month - int(spliter[1])+11)} months and {today.day - int(spliter[2])+31} days old")

        elif today.month < int(spliter[1]) and today.day < int(spliter[2]) and today.month == 3:
            print(f"\n ===> Age: You are {today.year - int(spliter[0])-1} years, {abs(today.month - int(spliter[1])+11)} months and {today.day - int(spliter[2])+28} days old")
#
        elif today.month > int(spliter[1]) and today.day < int(spliter[2]) and today.month in [1,2,4,6,8,9,11]:
            print(f"\n ===> Age: You are {today.year - int(spliter[0])} years, {today.month - int(spliter[1])-1} months and {today.day - int(spliter[2])+31} days old")

        elif today.month > int(spliter[1]) and today.day < int(spliter[2]) and today.month in [5,7,10,12]:
            print(f"\n ===> Age: You are {today.year - int(spliter[0])} years, {today.month - int(spliter[1])-1} months and {today.day - int(spliter[2])+30} days old")

        elif today.month > int(spliter[1]) and today.day < int(spliter[2]) and today.month == 3:
            print(f"\n ===> Age: You are {today.year - int(spliter[0])} years, {today.month - int(spliter[1])-1} months and {today.day - int(spliter[2])+28} days old")
#
        elif today.month < int(spliter[1]) and today.day > int(spliter[2]):
            print(f"\n ===> Age: You are {today.year - int(spliter[0])-1} years, {abs(today.month - int(spliter[1])+12)} months and {today.day - int(spliter[2])} days old")
#
        elif today.month == int(spliter[1]) and today.day < int(spliter[2]) and int(spliter[1]) in [1,2,4,6,8,9,11]:
            print(f"\n ===> Age: You are {today.year - int(spliter[0])-1} years, {abs(today.month - int(spliter[1])+11)} months and {today.day - int(spliter[2])+31} days old")
    
        elif today.month == int(spliter[1]) and today.day < int(spliter[2]) and int(spliter[1]) in [5,7,10,12]:
            print(f"\n ===> Age: You are {today.year - int(spliter[0])-1} years, {abs(today.month - int(spliter[1])+11)} months and {today.day - int(spliter[2])+30} days old")
    
        elif today.month == int(spliter[1]) and today.day < int(spliter[2]) and int(spliter[1]) in [3]:
            print(f"\n ===> Age: You are {today.year - int(spliter[0])-1} years, {abs(today.month - int(spliter[1])+11)} months and {today.day - int(spliter[2])+28} days old")
#
        elif today.month == int(spliter[1]) and today.day > int(spliter[2]):
            print(f"\n ===> Age: You are {today.year - int(spliter[0])} years, {0} months and {today.day - int(spliter[2])} days old")
#
        elif today.month > int(spliter[1]) and today.day == int(spliter[2]):
            print(f"\n ===> Age: You are {today.year - int(spliter[0])} years, {today.month - int(spliter[1])} months and {0} days old")
#
        elif today.month < int(spliter[1]) and today.day == int(spliter[2]):
            print(f"\n ===> Age: You are {today.year - int(spliter[0])-1} years, {abs(today.month - int(spliter[1])+12)} months and {0} days old")
            
        birthday = today.replace(year = int(spliter[0]), month = int(spliter[1]), day = int(spliter[2]))
        deltatime = today - birthday
        result = deltatime.days
        print(" ===> Days:", result, "\n")
#
    else:
        print("\n----PLEASE TRY AGAIN !!!----\n")