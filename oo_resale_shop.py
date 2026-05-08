#import to be able to use computer class and constructor
from computer import *

print("---------------Welcome to the Resale Shop!---------------\n")
class resale_shop:
    inventory: list=[]
    #define resale shop constructor with the inventory (I am failing to see what other attributes I have to add besides inventory)
    def __init__(self, inventory=[]):
        self.inventory= inventory

      
    #buy method taking in all the specific computer specs to buy, specs are the same as the computer constructor because I will be inputting it into the constructor
    def buy(self, computer):
        #append into empty inventory list
        self.inventory.append(computer)
        #text for readibility
        print(f"Yay you bought a new computer! Check the inventory!\n")
    
    #printing inventory function, no real attribute as it prints everything
    def print_inventory(self):
        #check if inventory is empty or not
        if self.inventory:
             print("Your inventory is:")
             #to make other methods easier, numbered the inventory list, making it start at 1 for readbility
             for i, computer in enumerate(self.inventory, start=1):
                #just readbility stuff
                print(f"------------------------------------------------------\n" 
                      f"{i}: {computer.description}\n" 
                      f"Processor Type: {computer.processor_type}\n"
                      f"Hard Drive Capacity: {computer.hard_drive_capacity}\n" 
                      f"Memory: {computer.memory}\n" 
                      f"Operating System: {computer.operating_system}\n"
                      f"Year: {computer.year_made}\n" 
                      f"Price: {computer.price}\n"
                      f"------------------------------------------------------\n")
        #error
        else: 
            print("There is nothing in the inventory.\n")

    #sell method
    def sell(self, computer):
        #check if list empty or not for error message
        if len(self.inventory)>0:
         #removes from the list the specific number computer in the inventory list, minus zero to make up for the start = 1 I did earlier
         self.inventory.remove(computer)
         print(f"You sold computer number {computer.description} in the inventory. Check the inventory to see what's left!\n")
        else:
           #error
           print("There is nothing in your inventory!\n")

    #updating price method
    def update_price(self, computer, amt=float):  
        #checks if list is empty or not
        if len(self.inventory)>0:
            #using similar way to find the numbered computer, this one specifically singles out the price and makes it equal to the new amount entered
            computer.price=amt
        else:
            #error
            print("Computer not found. Cannot update price.")

    #refurbish method
    def refurbish(self, computer):
         #checking if list empty
         if len(self.inventory)>0:
                #calls the specific number in list and singles out the year made and the price to make updates according to the manufacturing date
                if computer.year_made < 2000:
                    computer.price = 0 
                elif computer.year_made < 2012:
                    computer.price = 250 
                elif computer.year_made < 2018:
                    computer.price = 550
                else:
                    computer.price = 1000 
         else:
            #error
            print("Computer not found. Please select another item to refurbish.")

    #update OS method
    def update_OS(self, computer, newOS= str):
        #checks if inputted OS is equal to the current OS by calling the specific OS of computer.
        if computer.operating_system == newOS:
            print("The computer's operating system is up to date!")
        #easily updates OS to the new version (probably unlike reality)
        else:
           print("The computer's operating system is not up to date, updating in proccess...\n") 
           computer.operating_system = newOS

          




def main():
    #establishing shop and then testing out all the methods
    shop=resale_shop([])
    first_computer= Computer(description="Mac Pro (Late 2013)",
        processor_type="3.5 GHc 6-Core Intel Xeon E5",
        hard_drive_capacity=1024, 
        memory=64,
        operating_system= "macOS Big Sur", 
        year_made=2013, 
        price=1500.99)
    second_computer= Computer(
        description="Mac Pro (Late 2020)",
        processor_type="3.5 GHc 6-Core Intel Xeon E5",
        hard_drive_capacity=1024, 
        memory=128,
        operating_system= "macOS Big Sur", 
        year_made=2020, 
        price=2000.99)
    shop.buy(first_computer)
    shop.buy(second_computer)
    shop.print_inventory()
    shop.sell(second_computer)
    shop.update_price(second_computer, 3000.99)
    shop.print_inventory()
    shop.refurbish(first_computer)
    shop.update_OS(first_computer, "macOS Tahoe")
    shop.print_inventory()
    shop.sell(first_computer)
    shop.print_inventory()

if __name__ == "__main__":
    main()
