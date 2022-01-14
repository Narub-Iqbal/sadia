import pandas as pd
print("WELCOME to SADIAS's RESTURANT!")
client_name=input("May I know Your Good name please?\n")
client_response=input("How are you doing today "+ client_name+"?\n")
if client_response== "fine" and "good" and "i am good" and "i am fine":
    print(client_name, "I am glad to know that you are", client_response,"\n")
else:
    print(client_name, "I am really sorry to know that you are ",client_response)
    client_ill=input(client_name+" Are you ill today?")
    if client_ill== "yes":
        print(client_name,"\n I'am really sorry that according to Covid-19 SOP's we can't offer you any service.\n You should visit a doctor soon for a proper checkup and care.\nhope to see you again!\nBye")
    else :
        print(client_name," Sorry I cannot understand you!\nI think you should visit a phycologist soon for you mental treatment.\nbye")

client_work=input(client_name+" Would you like to check our menu?\n")
if client_work== "yes" and "true" and "yup" and "obviously" and "indeed":
    print('''Today we are serving the following items:
    1- BURGER
    2- PIZZA\n''')
    client_option=input(client_name+" What would you like us to serve you?\n")
    no_items= 0
    if client_option== "1" and "BURGER" and "Burger" and "burger" :
        print(client_name,''' We are offering you following burgers:
        1- Patty burger
        2- zinger burger
        3-double patty burger
        Price of each Burger is Rs.250\n''')
        client_burger=input(client_name+" Which burger would you like us to serve you?\n")
        if client_burger== "1" or "2" or "3" :
            print(client_name+ "you really have a great choice! ",client_burger," is our best serving!\n")
            no_items=int(input("how many burgers do you want?\n" ))
            bill=no_items*250
            print("Your bill is :", bill)
            payment=input("would you like to pay online here? or cash on delivery?\n")
            if payment== "here" and "online":
                print(client_name,'''here are some accounts
                EasyPaisa: 03123456789
                JazzCash:  03012345678
                HBL:       11223344556677889''')
            elif payment=="cash on delivery":
                name=input("Enter your Name: ")
                address=input("Enter your address: ")
                sec_code=input("Enter your security code: ")
                df=pd.DataFrame({'Names':[name],'Address':[address],'Scurity Code':[sec_code],'Order for':[client_option],'Total Bill':[bill]})
                print(df)
                df.to_csv("delivery.csv",index=False)
    elif client_option=="2" and "PIZZA" and "Pizza" and "pizza":
        print(client_name,''' We are offering you following Pizzas:
        1- Chicken Tikka
        2- Chicken BBQ
        3- Smoked Chicken with egg
        Price of each Pizza is Rs.1500\n''')
        client_pizza=input(client_name+" Which Pizza would you like us to serve you?\n")
        if client_pizza== "1" or "2" or "3":
            print(client_name+ " you really have a great choice! ",client_pizza," is our best serving!\n")
            no_items=int(input("how many Pizzas do you want?\n" ))
            bill=no_items*1500
            print("Your bill is :", bill)
            payment1=input("would you like to pay online here? or cash on delivery?\n")
            if payment1== "here" and "online":
                print(client_name,'''here are some accounts
                EasyPaisa: 03123456789
                JazzCash:  03012345678
                HBL:       11223344556677889''')
            elif payment1=="cash on delivery":
                name=input("Enter Your Name: ")
                address=input("Enter Your Address: ")
                sec_code=input("Enter Your Security code: ")
                df=pd.DataFrame({'Names':[name],'Address':[address],'Scurity Code':[sec_code],'Order for':[client_option],'Total Bill':[bill]})
                print(df)
                df.to_csv("delivery.csv",index=False)

            else:
                print("Sorry ",client_name+" Your payment is not equal to your bill. So, we can't provide you your order. Bye Bye")
    else :
        print("Sorry ", client_name, "your input in invalid... make sure that your input is in accordance with numbers given in menu.")
else :
    print("ok then bye bye")
print("Thank You for Visiting us")