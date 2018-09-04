# using inheritance importing product
import product
# and checkoutregister classes
import checkoutregister

# adding some products into the supermarket
product.product("123", "Milk", "2 Litres", "2.0")
product.product("789", "Fruits", "2 kgs", "4.0")
product.product("456", "Bread", "", "3.5")

# greeting message generated for the user
print("-----Welcome to FedUni checkout! -----")

while True:
    # using the checkoutregister class from checkoutregister file
    check_pro_list_items = checkoutregister.checkoutregister()

    # while condition is true run the code
    while True:
        main_class_list = product.product.list_products
        print()

        # prompt to get the entry of the product from the user
        product_code_data = input("Please enter the barcode of your item: ")
        # add the entered data and scan the product if it is available or not
        check_pro_list_items.scan_items(product_code_data)

        print()

        # prompt to get the entry from the user to continue or not
        user_loop = input("Would you like to scan another product? (Y/N) ").upper()

        # if user enter 'N' and then break the loop
        if user_loop == 'N':
            break

    print()
    while True:

        # show the payment to be paid/payment due to the user
        print("Payment due: $" + str(round((check_pro_list_items.price_of_products), 2)))
        # get the payment from the user
        paying_amount = checkoutregister.checkoutregister.get_float("Please enter an amount to pay: ")
        # check if the payment is done or not if yes then break the program
        if float(check_pro_list_items.accept_payment(paying_amount)) <= 0:
            break

    check_pro_list_items.print_receipt()
    # give the bag to the items which have low weight then bag
    checkoutregister.checkoutregister.bag_products(check_pro_list_items.bucket)

    # printing the thankou message to the user
    print("Thank you for shopping at FedUni!\n")

    # show user to continue to enter the product details of the next customer or he/she wants to quit
    enter_new = input("(N)ext customer, or (Q)uit?")

    # if user enter 'Q' then exits from the program
    if enter_new.upper() == 'Q':
        break
