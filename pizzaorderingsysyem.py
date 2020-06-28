# -*- coding: utf-8 -*-
"""
Created on Sun Dec 09 19:18:17 2018

@author: manalijain
"""

import re
import matplotlib.pyplot as plt
import pandas as pd
global orderno
orderno=0 #ORDERNO for customers
df=pd.read_csv("C:/Users/manalijain/Documents/project(py).csv")
num=int(input("ENTER THE MOBILE NUMBER:"))
print(df[df.PhoneNumber==num])
pickupCost = 0
deliveryCost = 5
running = True #Loop
global pizzaMenu
global pizzaPrice
#LISTS
h=[]
pizzaMenu = [ "Pepperoni", "Hawaiian", "Cheese", "Italian", "Margherita", "Apricot Chicken", "BBQ Meatlovers", "Chicken and Cranberry" ]
pizzaPrice = [ 99, 299, 79, 299, 499, 153, 233, 453 ]
cost = []
customerOrder = []

def pick_or_deli():#Want to pickup or delivery of pizza
  global delivery
  delivery = raw_input("P - pick up / D - delivery:")
  delivery = delivery.upper()
  if delivery == "D":
    while running == True:
      global customer_name #customer name
      customer_name = raw_input("Name:")
      h.append(raw_input)
      print(h)
      if not re.match("^[a-zA-Z ]*$", customer_name): 
        print("Please use letters only!!")
      elif len(customer_name) == 0: 
        print("Please enter a valid input!!")
      else:
        customer_name = customer_name.title()
        break 
    
    while running == True:
      global customer_telephone #phone no
      customer_telephone = raw_input("Telephone:")
      h.append(raw_input)
      if not re.match("^[0-9 ]*$", customer_telephone): 
        print("Please use numbers only!!")
      elif len(customer_telephone) == 0:  
        print("Please enter a valid input!!")
      else:
        break 
    
    
    while running == True:
      global house_no
      house_no = raw_input("House number:")#house number
      if not re.match("^[0-9 /]*$", house_no): 
        print("Please use numbers only!!")
      elif len(house_no) == 0: 
        print("Please enter a valid input!!")
      else:
        break 
    
    
    while running == True:
      global street_name #street name
      street_name = raw_input("Street name:")
      if not re.match("^[a-zA-Z ]*$", street_name): 
        print("Please use letters only")
      elif len(street_name) == 0: 
        print("Please enter a valid input!!")
      else:
        street_name = street_name.title()
        break 
    
    
    
    
    
  elif delivery == "P":
    while running == True: #customer details
      global customer_name #customer name
      customer_name = raw_input("Name:")
      if not re.match("^[a-zA-Z ]*$", customer_name): 
        print("Please use letters only")
      elif len(customer_name) == 0: 
        print("Please enter a valid input!!")
      else:
        customer_name = customer_name.title()
        break 
    
    while running == True:
      global customer_telephone #telephone
      customer_telephone = raw_input("Telephone:")
      if not re.match("^[0-9 ]*$", customer_telephone):
        print("Please use numbers only")
      elif len(customer_telephone) == 0:  
        print("Please enter a valid input!!")
      else:
        break 
    
  else:
    print("Please enter P or D.")
    
pick_or_deli()
print("Please use numbers only!!")

def print_menu():
  print ("""
  -----------------------------------------------
  |                 PIZZA MENU                  |
  |                                             |                       
  |              $9 classic pizzas              |
  |             -------------------             |
  |                1. Pepperoni                 |
  |                2. Hawaiian                  |
  |                3. Cheese                    |
  |                4. Italian                   |
  |                5. Margherita                |
  |                                             |
  |              $13 premium pizzas             |
  |             -------------------             |
  |              6. Apricot Chicken             |
  |              7. BBQ Meatlovers              |    
  |              8. Chicken & Cranberry         |
  |                                             |
  -----------------------------------------------
  """)
print_menu()

def order():
  global pizza_no
  while True:
    try: #Validating inputs
      pizza_no = int(raw_input("No. of pizzas (min 1 - max 5):"))
      if pizza_no < 1:
        print("Please order between 1 - 5 pizzas") 
        continue
      if pizza_no > 5:
        print("Please order between 1 - 5 pizzas")
        continue
      else:
        break 
    except ValueError: 
      print("Please use numbers only")
      continue
order()
  

def Choice_of_pizza(): 
    global pizza_no #total number of pizzas and what is the customer choice
    for i in range(1,pizza_no+1): 
      while True:
        try: 
          pizza_kind = int(raw_input("Choice of pizza(s):"))
          if pizza_kind < 1: #check condition for wrong input
            print("Refer to PIZZA MENU for pizza number")
            continue
          if pizza_kind > 8: #check condition for wrong input
            print("Refer to PIZZA MENU for pizza number")
            continue
          else:
            pizza = pizza_kind - 1 
            cost.append(pizzaPrice[pizza])
            customerOrder.append(pizzaMenu[pizza])
            global total_cost
            total_cost = sum(cost) 
            global grandTotal #to find grandtotal by taking total cost to make pizzas and delivery cost
            if delivery == "D":
              grandTotal = total_cost + deliveryCost
            else:  
              grandTotal = total_cost
            break
        except ValueError: 
          print("Please use numbers only!!")
          continue
Choice_of_pizza()


def customerDetails(): 
  if delivery == "D":
    print ("")
    print ("CUSTOMER AND ORDER DETAILS")
    print ("")
    print ("NAME:"), customer_name
    print ("TELEPHONE:"), customer_telephone
    print ("ADDRESS:"), house_no, street_name
    
    print ("ORDER:", customerOrder)
    print ("TOTAL: $", total_cost)
    print ("TOTAL + DELIVERY: $", grandTotal)
  else:
    print ("")
    print ("CUSTOMER AND ORDER DETAILS")
    print ("")
    print ("NAME:"), customer_name
    print ("TELEPHONE:"), customer_telephone
    print ("ORDER:"), customerOrder
    print ("TOTAL: $"), total_cost
customerDetails()
print ("")


def confirm(orderno): #To confirm the order
  confirmation = raw_input("Y - CONFIRM order / N - CANCEL order:")
  confirmation = confirmation.upper()  
  
  if confirmation == "Y":
      
      print("DETAILS CONFIRMED")
      bt=[]
      print("Enter the order number: ")
      n=int(input())
      print("Enter the cooking time of the processes: \n")
      bt=list(map(int, raw_input().split()))
      wt=[]
      avgwt=0
      tat=[]
      avgtat=0
      wt.insert(0,0)
      tat.insert(0,bt[0])
      for i in range(1,len(bt)):
         wt.insert(i,wt[i-1]+bt[i-1])
         tat.insert(i,wt[i]+bt[i])
         avgwt+=wt[i]
         avgtat+=tat[i]
      avgwt=float(avgwt)/n
      avgtat=float(avgtat)/n
      print("\n")
      print("order number\t  cooking Time\t  Waiting Time\t  ")
      for i in range(0,n):
         print(str(i)+"\t\t\t"+str(bt[i])+"\t\t"+str(wt[i]))
         print("\n")
      print("Average Waiting time is: "+str(avgwt))
      print("Average Turn Arount Time is: "+str(avgtat))
      
      
      
confirm(orderno)
print("")  

def order_some_more(): 
  order_more = raw_input("Z - order more / X - exit program:")
  order_more = order_more.upper() 
  '''cost[:] = []'''
  if order_more == "Z":
    print_menu() 
    order()
    Choice_of_pizza()
    customerDetails()
    confirm(orderno)
    print ("")
    print ("THANK YOU FOR YOUR ORDER")
    if delivery == "D":
      print ("Your order will be delivered in 25mins")  
    elif delivery == "P":
      print ("Your order will be ready to pick up in 5mins") 
  elif order_more == "X":
    print ("")
    print ("THANK YOU FOR YOUR ORDER")
    if delivery == "D":
      print ("Your order will be delivered in 25mins") 
    elif delivery == "P":
      print ("Your order will be ready to pick up in 20mins")  
  else:
    print ("Please enter X or Z") 
    
order_some_more()            
              
                  


print("\nTHE FREQUENCIES OF PEOPLE VISITED\n")

df=pd.read_csv("C:/Users/manalijain/Documents/project(py).csv")
k=df['visited']
fc=0
mfc=0
lfc=0
l1=[]
l=[]
for i in k:
    l1.append(i)
print(l1)
for i in l1:
    if i=='freq':
        fc=fc+1

    elif i=='more freq':
        mfc=mfc+1
    elif i=='less freq':
        lfc=lfc+1
    else:
        break
print(fc)
print(mfc)
print(lfc)
l.append(fc)
l.append(mfc)
l.append(lfc)
print(l)
used=['frequently used','more frequently used','less frequently used']
plt.pie(l,labels=used,startangle=0,explode=(0,0,0),shadow=True,autopct='%.1f')

plt.title('frequencies of customers in shop')
plt.legend()
plt.show()    