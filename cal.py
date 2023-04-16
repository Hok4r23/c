import os
def add(x, y):
   """This function adds two numbers"""

   return x + y

def subtract(x, y):
   """This function subtracts two numbers"""

   return x - y

def multiply(x, y):
   """This function multiplies two numbers"""

   return x * y

def divide(x, y):
   """This function divides two numbers"""

   return x / y

os.system("clear")

print("\u001b[31;1m" + """▄  █ ████▄ █  █▀ ██   █▄▄▄▄ 
█   █ █   █ █▄█   █ █  █  ▄▀ 
██▀▀█ █   █ █▀▄   █▄▄█ █▀▀▌  
█   █ ▀████ █  █  █  █ █  █  
   █          █      █   █   
  ▀          ▀      █   ▀    
                   ▀          """)

print("")


print("\u001b[32;1m" + "1.kokrdnawa")
print("\u001b[35;1m" + "2.kamkrdn")
print("\u001b[34;1m" + "3.karat")
print("\u001b[36;1m" + "4.dabash ")

choice = input("\u001b[37;1m" + "zhmarek halbzhera :")

num1 = int(input("\u001b[32;1m" + "zhmaray yakam: "))
num2 = int(input("\u001b[32;1m" +"zhmaray dwam: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("\u001b[31;1m" + "Invalid input")