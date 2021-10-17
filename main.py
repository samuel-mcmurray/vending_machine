# main

from classes.vending_machine.c_vending_machine import vending_machine

vm1 = vending_machine("Test Dummy 2")
vm1.printWelcomeMessage()
vm1.printStockOptions()

user_input = input("\nYour selection: ")

print("\nThankyou for selecting:", user_input)
