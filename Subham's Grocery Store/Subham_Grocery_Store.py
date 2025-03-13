#OBJ: TO MAKE A GROCERY STORE PROGRAM
print("Welcome to Subham's Fresh Store ")
print('We offer Vegetables, Meat, Eggs , Fishes and Packed Items')
getInToken = int(input('Enter 1 to Proceed shopping else to exit : '))
#declaring quantity variables for each item to start from 0
cart_total = 0
#veggies quantity variables
potato_quantity = 0
onion_quantity = 0
cucumbur_quantity = 0
 #snacks quantity variables
#function to add item to cart
#now main shop starts
while getInToken == 1:
    print(' Here is the guidance menu, please follow accordingly !')
    print(" 1: Veggies \n 2: Snacks \n 3: Meats & Fishes \n 4: Proceed to Checkout! ")
    CusChMain = int(input('Your Choice is:'))
    match CusChMain:
      case 1:
         print('Welcome to Veggies Section!!')
         CusChVeg = 1
         while CusChVeg==1:
            print("SN : Veggies \t Price per KG in Rupees:\n")
            print(' 1: Potatoes \t 80\n 2: Cucumbers \t 130 \n 3: Onions \t 160 \n')
            VeggCh = int(input('Your Choice:'))
            match VeggCh:
                  case 1:
                    print('You selected Potatoes')
                    potato_quantity = int(input(print("Your desired quantity is: ")))
                    print('This purchase costs: Rs', potato_quantity*80)
                    cart_total += potato_quantity*80
                  case 2:
                     print('You selected Cucumbers')
                     cucumber_quantity = int(input(print("Your desired quantity is: ")))
                     print('This purchase costs: Rs', cucumber_quantity*130)
                     cart_total += cucumber_quantity*130
                  case 3:
                     print('You selected Onions')
                     onion_quantity = int(input(print("Your desired quantity is: ")))
                     print('This purchase costs: Rs', onion_quantity*160)
                     cart_total += onion_quantity*160
                  case _:
                     print('You have chosen to go back to Veggies menu\n')
            CusChVeg = int(input('Do you want to add more veggies to your cart? (1 for yes, 0 for no)\n'))
      case 2:
         print('Welcome to Snacks Section!!')
         CusChSnack = 1
         while CusChSnack==1:
            print("SN : Snacks \t Price per KG in Rupees:\n")
            print(' 1: Bread \t 20\n 2: Milk \t 50 \n 3: Chocolate \t 100 \n')
            SnackCh = int(input('Your Choice is:'))
            match SnackCh:
                  case 1:
                     print('You selected Bread')
                     bread_quantity = int(input(print("Your desired quantity is: ")))
                     print('This purchase costs: Rs', bread_quantity*20)
                     cart_total += bread_quantity*20
                  case 2:
                     print('You selected Milk')
                     milk_quantity = int(input(print("Your desired quantity is: ")))
                     print('This purchase costs: Rs', milk_quantity*50)
                     cart_total += milk_quantity*50
                  case 3:
                     print('You selected Chocolate')
                     chocolate_quantity = int(input(print("Your desired quantity is: ")))
                     print('This purchase costs: Rs', chocolate_quantity*100)
                     cart_total += chocolate_quantity*100
                  case _:
                     print('You have chosen to go back to Snacks menu\n')
            CusChSnack = int(input('Do you want to add more snacks to your cart? (1 for yes, 0 for no)\n'))
      case 3:
         print('Welcome to Meats & Fishes Section!!')
         CusChMeat = 1
         while CusChMeat==1:
            print("SN : Meats & Fishes \t Price per KG in Rupees:\n")
            print(' 1: Chicken \t 150\n 2: Beef \t 250 \n 3: Fish \t 300 \n')
            MeatCh = int(input('Your Choice:'))
            match MeatCh:
                  case 1:
                     print('You selected Chicken')
                     chicken_quantity = int(input(print("Your desired quantity is: ")))
                     print('This purchase costs: Rs', chicken_quantity*150)
                     cart_total += chicken_quantity*150
                  case 2:
                     print('You selected Beef')
                     beef_quantity = int(input(print("Your desired quantity is: ")))
                     print('This purchase costs: Rs', beef_quantity*250)
                     cart_total += beef_quantity*250
                  case 3:
                     print('You selected Fish')
                     fish_quantity = int(input(print("Your desired quantity is: ")))
                     print('This purchase costs: Rs', fish_quantity*300)
                     cart_total += fish_quantity*300
                  case _:
                     print('You have chosen to go back to Meats & Fishes menu\n')
            CusChMeat = int(input('Do you want to add more meats to your cart? (1 for yes, 0 for no)\n'))
      case 4:
         print('Thank you for shopping with us. Your total bill is:', cart_total)
         getInToken = int(input('Do you want to make another purchase? (1 for yes, 0 for no)'))
         if getInToken == 0:
            print('Thank you for shopping in Subham\'s Fresh Store. Have a nice day!!!')
            break
         else:
            cart_total = 0
            print('Your cart have been refreshed, kindly shop again!.')
            continue
      case _:
         print('Invalid choice, please try again!')
         continue
print('Program ended. Thank you for shopping with us. Have a nice day!!!')