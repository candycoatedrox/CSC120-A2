from computer import Computer

class ResaleShop:

    def __init__(self):
        self.inventory : list = []

    def __getitem__(self, i: int):
        return self.inventory[i]

    """
    Takes in all the information about a computer,
    adds it to the inventory, returns its index in the inventory
    """
    def buy(self, c: Computer):
        self.inventory.append(c)
        return len(self.inventory) - 1
    
    """
    Takes in an item index, removes the associated computer if it is the inventory, 
    prints error message otherwise
    """
    def sell(self, id: int):
        if self[id] is not None:
            c = self.inventory.pop(id)
            print(f'Item {id} ({c.desc}) sold!')
        else:
            print(f'Item {id} not found. Please select another item to sell.')
    
    """
    Prints all the items in the inventory (if it isn't empty), prints error otherwise
    """
    def printInventory(self):
        if self.inventory:
            for id in range(len(self.inventory)):
                print(f'({id + 1}.) {self[id]}')
        else:
            print("No inventory to display.")

def main():
    comp = Computer(
        "2019 MacBook Pro",
        "Intel",
        256, 16,
        "High Sierra", 2019, 1000)
    comp2 = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    shop = ResaleShop()

    shop.buy(comp)
    shop.printInventory()
    shop.buy(comp2)
    shop.printInventory()

    shop.sell(0)
    shop.printInventory()

    shop[0].refurbish()
    shop.printInventory()

main()