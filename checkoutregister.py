# importing the product class by implementing the inheritence
import product


# class checkoutregister
class checkoutregister():

    # default constructor
    def __init__(self):

        self.storing_products = product.product.list_products
        # price of the products initialisation which is the total amount
        self.price_of_products = 0.0
        # variable storing the amount of the product which is paid by the customer to this program
        self.paying_cost_price = 0.0

        # bucket is the list in customer carry their products
        self.bucket = []

    def get_float(prompt):

        # initialising the float variable called value
        value = float(0.0)

        # run the while loop until the program satisfy the condition
        while True:
            try:
                # get the entered value and cast it into the float value
                value = float(input(prompt))

                # if the entered values is smaller than zero then print the error message and continue to get the
                # real money
                if value < 0.0:
                    print("We don't accept negative money!")
                    continue
                # break the condition
                break

            # if any exception occured like value error then it will print the exception message
            except ValueError:
                print('Please enter a valid floating point value.')

        # value returns which is entered by the user
        return value

    # this is the function of bag products
    def bag_products(product_list):
        # list of bagged items and non bagged items and maximum bag weight
        bag_list = []
        non_bagged_items = []
        MAX_BAG_WEIGHT = 5.0

        # run the for loop to get all the items from the product list
        for product in product_list:

            # product's weight is greater than weight of the products
            # then remove the item from the bag and append it into the non bagged items
            if product.weight > MAX_BAG_WEIGHT:
                product_list.remove(product)
                non_bagged_items.append(product)

        #
        current_bag_contents = []
        current_bag_weight = 0.0

        while len(product_list) > 0:

            # then store the product list's item whichb is at position zero into the product list
            temp_product = product_list[0]
            product_list.remove(temp_product)

            # if current bag weight and temp_product is smaller than the maximum weight of the bag
            if current_bag_weight + temp_product.weight <= MAX_BAG_WEIGHT:

                # append that item into the bag and increment the bag weight
                current_bag_contents.append(temp_product)
                current_bag_weight += temp_product.weight



            # if the weight is greater than the weight of bag
            else:
                bag_list.append(current_bag_contents)
                # append that item into the list of the products
                current_bag_contents = [temp_product]
                current_bag_weight = temp_product.weight
            # run if and  only if product list equals to 0
            if (len(product_list) == 0):
                bag_list.append(current_bag_contents)


        # increase the index and bag items by 1
        for index, bag in enumerate(bag_list):
            output = 'Bag ' + str(index + 1) + ' contains: '

            # display the items which are in the bag
            for product in bag:
                output += product.name + '\t'
            print(output, '\n')

        # if the length of the nonbagged items is greater than zero then output will be given below
        if (len(non_bagged_items) > 0):
            output = 'Non-bagged items: '

            # display items which are not in the bag
            for item in non_bagged_items:
                output += item.name + '\t'
            print(output, '\n')

    # function to get the positive money from the user
    def accept_payment(self, some_amount):
        # casting the money into float
        some_amount = float(some_amount)
        # total amount
        self.paying_cost_price = self.paying_cost_price + some_amount
        # rest due payment
        self.price_of_products = self.price_of_products - some_amount
        return self.price_of_products

    # scanned items function
    def scan_items(self, some_product):
        temp = int(0)
        for pro_data in range(len(self.storing_products)):
            if self.storing_products[pro_data][0].__contains__(some_product):
                # store the items into the product list
                data_in_list = product.product(self.storing_products[pro_data][0],
                                               self.storing_products[pro_data][1],
                                               self.storing_products[pro_data][2],
                                               self.storing_products[pro_data][3])
                self.bucket.append(data_in_list)
                self.price_of_products += float(self.storing_products[pro_data][3])
                temp = 1
                print(self.storing_products[pro_data][1] + ", " + self.storing_products[pro_data][2] + " - $" +
                      self.storing_products[pro_data][3])
                break
        self.temp_pro_amount = self.price_of_products

        if temp == 0:
            print("This product does not exists in our inventory.")

    # printing the receipt
    def print_receipt(self):
        print("\n---- Final Receipt ----\n")
        for i in range(len(self.bucket)):
            print(self.bucket[i].name + ", " + self.bucket[i].p_weight + "\t\t$" + self.bucket[i].p_amount)

        # total amount due message
        print("\n Total amount due: \t$" + str(self.temp_pro_amount) + "\n Amount received:\t$" + str(
            round((self.paying_cost_price), 2)) + "\n Change given:\t\t$" + str(
            abs(round((self.paying_cost_price - self.temp_pro_amount), 2))))
        print()
