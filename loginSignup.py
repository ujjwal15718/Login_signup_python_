
import json, os
 
def register():
   if os.path.exists("database.json"):
       with open("database.json", "r") as f:
           allDetails = json.load(f)
   else:
       allDetails = []
 
   userData = {
           "name":input("Enter your name: "),
           "email":input("Enter email: "),
           "password":input("Enter your password: ")
       }
      
  
   allDetails.append(userData)
   with open("database.json", 'w') as f:
    
       json.dump(allDetails, f, indent=4)
     
   print("successfully register\nThankyou!!!!!!!!!!!!!!!!")
 
def login(inputEmail, inputPassword):
   with open("database.json", "r") as f:
       allDetails = json.load(f)
 
   for detail in allDetails:
       if detail['email'] == inputEmail and detail['password'] == inputPassword:
           return f"welcome {detail['name']}"
   return "invalid input"
 
 
choose = int(input("press - 1 for register : - \npresss - 2 for login : - "))
if choose == 1:
   register()
else:
   print(login(input("email"), input("password")))