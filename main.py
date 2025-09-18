# Import the Computer class and its methods from computer.py
from computer import Computer

# Import the ResaleShop class and its methods from oo_resale_shop.py
from oo_resale_shop import ResaleShop

def main():

    # First, let's create a resale shop and a computer
    shop = ResaleShop()
    comp = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    comp2 = Computer(
        "2019 MacBook Pro",
        "Intel",
        256, 16,
        "High Sierra", 2019, 1000
    )

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add the first computer to the resale store's inventory
    print("Buying", comp.desc)
    print("Adding to inventory...")
    id = shop.buy(comp)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.printInventory()
    print("Done.\n")

    # Now, let's refurbish it
    newOS = "MacOS Monterey"
    print("Refurbishing Item ID:", id, ", updating OS to", newOS)
    print("Updating inventory...")
    shop[id].refurbish(newOS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.printInventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", id)
    shop.sell(id)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.printInventory()
    print("Done.\n")

# Calls the main() function when this file is run
if __name__ == "__main__": main()
