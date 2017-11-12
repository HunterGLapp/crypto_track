my_file = open("crypto", "r")
full_text = my_file.read()
sections = full_text.split(";")
[btc, eth, ltc] = sections[:-1]
print(btc)

class Transaction:
    """Represents one currency transaction"""
    def __init__(self, a, w, d):
        self.amount = a
        self.worth = w
        self.date = d
        

def split_section(my_str):
    lines = my_str.splitlines[1:]
    for line in lines:
        for 
        
