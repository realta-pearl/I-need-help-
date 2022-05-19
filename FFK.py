#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 11:22:22 2022

@author: fayanafate
"""
# this is a code to self-order at a fast food kiosk
# note that bg stands for burger beef_bg_quantity = 0
import os
import configparser

config = configparser.ConfigParser()
# config.read('insert file name')
config.read("config.txt")
# prices of each food item
beef_bg_cost = float(config["ITEM_COST"]["beef_burger_cost"])
fish_bg_cost = float(config["ITEM_COST"]["fish_burger_cost"])
french_fries_cost = float(config["ITEM_COST"]["french_fries_cost"])
cold_drinks_cost = float(config["ITEM_COST"]["cold_drinks_cost"])


# price list/menu, to be printeed when ordering
def price_list_and_food_ordered(
    beef_bg_quantity,
    fish_bg_quantity,
    french_fries_quantity,
    cold_drinks_quantity,
):
    os.system("clear")
    print("********** Welcome to Fuzz Food Self-Ordering Kiosk! *********")
    print("\n")
    print("*********************** Price List ************************")
    print("\n")
    print("*          1. Beef Burger: $", beef_bg_cost, "            *")
    print("*          2. Fish Burger: $", fish_bg_cost, "            *")
    print("*          3. French Fries: $", french_fries_cost, "           *")
    print("*          4. Cold Drinks: $", cold_drinks_cost, "            *")
    print("\n")
    print("***********************************************************")
    print("\n")

    print("Food Ordered: ")
    print(
        "1. Beef Burgers ordered = ",
        beef_bg_quantity,
        "x",
        "{:.2f}".format(beef_bg_cost),
        "=",
        "{:.2f}".format(beef_bg_quantity * beef_bg_cost),
    )
    print(
        "2. Fish Burgers ordered = ",
        fish_bg_quantity,
        "x",
        "{:.2f}".format(fish_bg_cost),
        "=",
        "{:.2f}".format(fish_bg_quantity * fish_bg_cost),
    )
    print(
        "3. French Fries ordered = ",
        french_fries_quantity,
        "x",
        "{:.2f}".format(french_fries_cost),
        "=",
        "{:.2f}".format(french_fries_quantity * french_fries_cost),
    )
    print(
        "4. Cold Drinks ordered  = ",
        cold_drinks_quantity,
        "x",
        "{:.2f}".format(cold_drinks_cost),
        "=",
        "{:.2f}".format(cold_drinks_quantity * cold_drinks_cost),
    )
    print("\n")

    subtotal = (
        (beef_bg_quantity * beef_bg_cost)
        + (fish_bg_quantity * fish_bg_cost)
        + (french_fries_quantity * french_fries_cost)
        + (cold_drinks_quantity * cold_drinks_cost)
    )

    print("Total (exclusive of GST)=", "{:.2f}".format(subtotal))


def receipt(
    beef_bg_quantity,
    fish_bg_quantity,
    french_fries_quantity,
    cold_drinks_quantity,
):
    os.system("clear")
    print("************************ Checkout ************************")
    if beef_bg_quantity >= 1:
        print(
            "Beef Burgers = ",
            beef_bg_quantity,
            "x",
            "{:.2f}".format(beef_bg_cost),
            "=",
            "{:.2f}".format(beef_bg_quantity * beef_bg_cost),
        )

    if fish_bg_quantity >= 1:
        print(
            "Fish Burgers = ",
            fish_bg_quantity,
            "x",
            "{:.2f}".format(fish_bg_cost),
            "=",
            "{:.2f}".format(fish_bg_quantity * fish_bg_cost),
        )

    if french_fries_quantity >= 1:
        print(
            "French Fries = ",
            french_fries_quantity,
            "x",
            "{:.2f}".format(french_fries_cost),
            "=",
            "{:.2f}".format(french_fries_quantity * french_fries_cost),
        )

    if cold_drinks_quantity >= 1:
        print(
            "Cold Drinks = ",
            cold_drinks_quantity,
            "x",
            "{:.2f}".format(cold_drinks_cost),
            "=",
            "{:.2f}".format(cold_drinks_quantity * cold_drinks_cost),
        )

    subtotal = (
        (beef_bg_quantity * beef_bg_cost)
        + (fish_bg_quantity * fish_bg_cost)
        + (french_fries_quantity * french_fries_cost)
        + (cold_drinks_quantity * cold_drinks_cost)
    )
    GST = 7 / 100 * subtotal
    Total = subtotal + GST
    print("\n")
    print("Subtotal = %.2f" % subtotal)
    print("GST = %.2f" % GST)
    print("Total = %.2f" % Total)


def ask_food(food_item):
    quantity = int(input(config["QUESTION"][str(food_item)] + " "))
    return quantity


def main():
    # define queue number to be used during while loop
    # food item quantity
    beef_bg_quantity = 0
    fish_bg_quantity = 0
    french_fries_quantity = 0
    cold_drinks_quantity = 0
    queue_no = 0

    # choosing of food items
    while True:
        price_list_and_food_ordered(
            beef_bg_quantity,
            fish_bg_quantity,
            french_fries_quantity,
            cold_drinks_quantity,
        )
        try:
            food_item = int(
                input("Enter Food ID (1 to 4) to edit cart (0 to checkout): ")
            )
            # if customer checks out, screen should be cleared and receipt printed
            if food_item == 0:
                receipt(
                    beef_bg_quantity,
                    fish_bg_quantity,
                    french_fries_quantity,
                    cold_drinks_quantity,
                )
                queue_no = queue_no + 1
                print("The queue number is: ", queue_no)
                input("Press any key to continue... ")

                # reset quantities and price for the next customer
                beef_bg_quantity = 0
                fish_bg_quantity = 0
                french_fries_quantity = 0
                cold_drinks_quantity = 0
            elif food_item > 0 and food_item < 5:
                quantity = ask_food(food_item)
                if food_item == 1:
                    beef_bg_quantity = quantity
                elif food_item == 2:
                    fish_bg_quantity = quantity
                elif food_item == 3:
                    french_fries_quantity = quantity
                elif food_item == 4:
                    cold_drinks_quantity = quantity

                price_list_and_food_ordered(
                    beef_bg_quantity,
                    fish_bg_quantity,
                    french_fries_quantity,
                    cold_drinks_quantity,
                )
        except:
            print("Invalid character entered. Please input only 0 to 4. ")

    else:
        os.system("clear")
        price_list_and_food_ordered()
        print("Please input only 0 to 4. ")


if __name__ == "__main__":
    main()
