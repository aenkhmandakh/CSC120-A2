class Computer:
    description: str=""
    processor_type: str="" 
    hard_drive_capacity: int=0.0
    memory: int=0.0
    operating_system: str=""
    year_made: int= 0.0
    price: int=""

    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str, processor_type: str, 
                 hard_drive_capacity: int, memory: int, operating_system: str, year_made:int, price: int):
        self.description=description
        self.processor_type=processor_type
        self.hard_drive_capacity= hard_drive_capacity
        self.memory= memory
        self.operating_system= operating_system
        self.year_made= year_made
        self.price= price

        pass # You'll remove this when you fill out your constructor

    # What methods will you need?
    def store(self, description: str, processor_type: str, 
                 hard_drive_capacity: int, memory: int, operating_system: str, year_made:int, price: int):
        self.description=description
        self.processor_type=processor_type
        self.hard_drive_capacity= hard_drive_capacity
        self.memory= memory
        self.operating_system= operating_system
        self.year_made= year_made
        self.price= price

        return "The updated description is", description,processor_type, hard_drive_capacity, memory,operating_system,year_made,price

def main():
    computerOne:Computer=Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
    print(computerOne.store("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 128,
        "macOS Big Sur", 2013, 1500))
    
if __name__ == "__main__":
    main()
    
