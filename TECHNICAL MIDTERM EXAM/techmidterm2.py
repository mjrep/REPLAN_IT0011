import datetime  

date_input = input("Enter the date (mm/dd/yyyy): ")  
date_obj = datetime.datetime.strptime(date_input, "%m/%d/%Y")  
print("Date Output:", date_obj.strftime("%B %d, %Y"))  
