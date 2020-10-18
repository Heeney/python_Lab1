#SU Shop 


class Shop:
    cap_price = 5
    shirt_price = 10
    hoodies_price = 20
    
    def __init__(self, caps_number, hoodies_number, shirts_number):
            self.caps_no = caps_number
            self.hoodies_no = hoodies_number
            self.shirts_no = shirts_number
            
    def calculate_total_cost(self):
        self.cost = self.shirts_no * Shop.shirt_price + self.caps_no * Shop.cap_price + self.hoodies_no * Shop.hoodies_price
        return self.cost
        
        
print ('Welcome to the student Union Shop \n How many caps would you like to buy ?')
caps = int(input())

print ('How many shirts would you like to buy?')
shirts = int(input())

print ('How many hoodies would you like to buy')
hoodies = int(input())

s = Shop(caps, shirts, hoodies)
cost = s.calculate_total_cost()
print('total cost is:', cost)