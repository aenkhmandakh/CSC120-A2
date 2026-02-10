
from computer import *

print("---------------Welcome to the Resale Shop!---------------\n")
class ResaleShop:
    inventory: list=[]

    def __init__(self):
        self.inventory= []

    def buy(self, description,processor_type, hard_drive_capacity, memory,operating_system,year_made,price):
        computer=Computer(description,processor_type, hard_drive_capacity, memory,operating_system,year_made,price)
        self.inventory.append(computer)
        print(f"Yay you bought a new computer! Check the inventory!\n")
    
    def printInventory(self):
        if self.inventory:
             print("Your inventory is:")
             for i, computer in enumerate(self.inventory, start=1):
                print(f"------------------------------------------------------\n" 
                      f"{i}: {computer.description},\n" 
                      f"Processor Type:{computer.processor_type} \n"
                      f"Hard Drive Capacity:{computer.hard_drive_capacity},\n" 
                      f"Memory: {computer.memory},\n" 
                      f"Operating System: {computer.operating_system}\n"
                      f"Year: {computer.year_made},\n" 
                      f"Price: {computer.price}\n"
                      f"------------------------------------------------------\n")
        else: 
            print("There is nothing in the inventory.\n")

    def sell(self, number_in_list):
        if self.inventory:
         self.inventory.remove(self.inventory[number_in_list-1])
         print(f"You sold computer number {number_in_list} in the inventory. Check the inventory to see what's left!\n")
        else:
           print("There is noting in your inventory!\n")




def main():
    shop=ResaleShop()
    shop.buy(
        description="Mac Pro (Late 2013)",
        processor_type="3.5 GHc 6-Core Intel Xeon E5",
        hard_drive_capacity=1024, 
        memory=64,
        operating_system= "macOS Big Sur", 
        year_made=2013, 
        price=1500.99)
    shop.buy(
        description="Mac Pro (Late 2020)",
        processor_type="3.5 GHc 6-Core Intel Xeon E5",
        hard_drive_capacity=1024, 
        memory=128,
        operating_system= "macOS Big Sur", 
        year_made=2020, 
        price=2000.99)
    shop.printInventory()
    shop.sell(1)
    shop.printInventory()

if __name__ == "__main__":
    main()
