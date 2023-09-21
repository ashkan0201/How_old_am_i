# <<< Dedicated to the most important person in my life (: >>>

# Required libraries
from datetime import datetime
from tabulate import tabulate

today = datetime.today()

# Create a table
table = [[today.strftime(" Dedicated to the most important person in my life (: \nFor example =>>> %Y/%m/%d  \nUse the 'Ctrl + c' or write: 'exit' to finish\n")]]
print(tabulate(table, tablefmt="grid"))