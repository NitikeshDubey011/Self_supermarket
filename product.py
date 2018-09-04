class product():
    # list in which products will be keep
    list_products = []

    # default constructor which have parameters i.e. product code, product name , product weight and product amount
    def __init__(self, pro_code, pro_name, pro_weight, pro_amount):
        # this is the product code which will be scanned by the barcode scanner
        self.prod_code = pro_code
        # this is the name of the product
        self.name = pro_name
        # this is the weight of the product
        self.p_weight = pro_weight

        # if the product is empty or nill then the product's weight is zero
        if pro_weight == '':
            self.weight = 0
        else:
            temp_weight = ",".join((self.p_weight).split())
            self.weight = float(temp_weight[0])

        # this is the amount of the product
        self.p_amount = pro_amount

        # list to get the items at one place
        pro_list = [self.prod_code, self.name, self.p_weight, self.p_amount]
        # and append the data into the default list
        self.list_products.append(pro_list)
