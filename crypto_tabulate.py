from locale import *
setlocale(LC_NUMERIC, '')

my_file = open("crypto", "r")
full_text = my_file.read()
sections = full_text.split(";")
[btc, eth, ltc] = sections[:-1]

class Transaction:
    """Represents one currency transaction"""
    def __init__(self, a, w, d):
        self.amount = atof(a)
        self.worth = atof(w)
        self.date = d
        self.fee = 1.5
        
    def cost(self):
        return (self.amount * self.worth)
        

def split_section(my_str):
    stripped = my_str.strip()
    transaction_list = list()
    lines = stripped.splitlines()[1:]
    for line in lines:
        words = line.split(" ")
        curr_transaction = Transaction(words[0], words[1], words[2])
        transaction_list.append(curr_transaction)
    return transaction_list
        
btc_transactions = split_section(btc)
eth_transactions = split_section(eth)
ltc_transactions = split_section(ltc)

def total_cost(transaction_list):
    cost = 0
    for transaction in transaction_list:
        cost += transaction.cost()
    return cost

def total_worth(transaction_list, curr_price):
    amt = 0
    for transaction in transaction_list:
        amt += transaction.amount
    return amt * curr_price

def profit(transactions, price):
    return total_worth(transactions, price) - total_cost(transactions)

def readout(t_l, c_p, currency):
    print("-------------------------")
    print(currency)
    print("-------------------------\n")
    print("Spent:")
    print("        " + str(total_cost(t_l)))
    print("Worth:")
    print("        " + str(total_worth(t_l, c_p)))
    print("Profit:")
    print("        " + str(profit(t_l, c_p)))
    print("\n")

readout(btc_transactions, 6050.25, "BTC")
