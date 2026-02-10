
#establishes all the attributes of a computer
class Computer:
    description: str=""
    processor_type: str="" 
    hard_drive_capacity: int=0.0
    memory: int=0.0
    operating_system: str=""
    year_made: int= 0.0
    price: float=0.0

    #constructor requireing all the specs of a computer, equaling it to the self
    def __init__(self, description: str, processor_type: str, 
                 hard_drive_capacity: int, memory: int, operating_system: str, year_made:int, price: float):
        self.description=description
        self.processor_type=processor_type
        self.hard_drive_capacity= hard_drive_capacity
        self.memory= memory
        self.operating_system= operating_system
        self.year_made= year_made
        self.price= price

    # Made an update method just to test out
    def update(self, description: str, processor_type: str, 
                 hard_drive_capacity: int, memory: int, operating_system: str, year_made:int, price: int):
        self.description=description
        self.processor_type=processor_type
        self.hard_drive_capacity= hard_drive_capacity
        self.memory= memory
        self.operating_system= operating_system
        self.year_made= year_made
        self.price= price

        return "The updated description is", description,processor_type, hard_drive_capacity, memory,operating_system,year_made,price
    
    
    


    
#testing out
def main():
    computerOne:Computer=Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500.99)
    computerTwo:Computer=Computer("Mac (Late 2015)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 2000.99)
    print(computerOne.update("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 128,
        "macOS Big Sur", 2013, 1500.99))
    print(computerTwo.update("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 128,
        "macOS Big Sur", 2013, 2000.99))
    
if __name__ == "__main__":
    main()
    
