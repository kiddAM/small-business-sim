# Small Business Simulator by Chloé Matthews
# Currently, simulates a single day at a small business
# Performs actions such as: Daily restock, Inventory check,
# Randomized transactions, & End-of-Day Sales Summary

from random import randrange

sales_counter = [0, 0, 0]

item_a = item_b = item_c = 0

def restock():
    global item_a, item_b, item_c

    item_a = item_b = item_c = 50

    print("Supply Room Ronnie: \"All items have been restocked.\"")

def get_inventory():
    inventory_update = """Supply Room Ronnie: \"Check out our inventory:\"
        {0} item_a(s),
        {1} item_b(s),
        {2} item_c(s)
        """
    print(inventory_update.format(item_a, item_b, item_c))

def transact():
    global sales_counter
    global item_a, item_b, item_c

    new_transaction = [randrange(10), randrange(10), randrange(10)]
    customer = """Customer: \"I would like to purchase:
        {0} item_a(s),
        {1} item_b(s),
        {2} item_c(s).\"
        """

    print(customer.format(new_transaction[0], new_transaction[1], new_transaction[2]))

    low_stock_msg_a = "Supply Room Ronnie: \"We have {} item_a(s) left.\"".format(item_a)
    low_stock_msg_b = "Supply Room Ronnie: \"We have {} item_b(s) left.\"".format(item_b)
    low_stock_msg_c = "Supply Room Ronnie: \"We have {} item_c(s) left.\"".format(item_c)

    if new_transaction[0] <= item_a:
        item_a = item_a - new_transaction[0]
        sales_counter[0] += new_transaction[0]
    else:
        print(low_stock_msg_a)

    if new_transaction[1] <= item_b:
        item_b = item_b - new_transaction[1]
        sales_counter[1] += new_transaction[1]
    else:
        print(low_stock_msg_b)

    if new_transaction[2] <= item_c:
        item_c = item_c - new_transaction[2]
        sales_counter[2] += new_transaction[2]
    else:
        print(low_stock_msg_c)

def report_sales():
    total_sales = sales_counter[0] + sales_counter[1] + sales_counter[2]
    sales_report = """Supply Room Ronnie: \"Here's today's sales report:\"
        {} item_a(s) sold,
        {} item_b(s) sold,
        {} item_c(s) sold,

        Total items sold: {}
        """

    print(sales_report.format(sales_counter[0], sales_counter[1],
        sales_counter[2], total_sales))

def simulate_day():
    transactions_til_close = 10

    print("Supply Room Ronnie: \"It's a new day!\"")
    restock()
    get_inventory()

    while transactions_til_close:
        transact()
        get_inventory()
        transactions_til_close -= 1

    print("Supply Room Ronnie: \"Closing time!\"")
    report_sales()

simulate_day()
