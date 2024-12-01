def place_order(menu):
    """
    Displays a restaurant menu, asks customers for their order, then returns
    their receipt and total price.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their 
                       prices, using the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                  and quantity ordered.
    order_total (float): The total price of the order.
    """
    # Set up order list. Order list will store a list of dictionaries for
    # menu item name, item price, and quantity ordered
    order = []

    # Get the menu items mapped to the menu numbers
    menu_items = get_menu_items_dict(menu)

    # Launch the store and present a greeting to the customer
    print("Welcome to the Generic Take Out Restaurant.")

    # TODO: Create a continuous while loop so customers can order multiple items
def get_order_details():
    item_name = input("Please enter the name of the item: ")
    quantity = int(input(f"Please enter the quantity of {item_name}: "))
    price = float(input(f"Please enter the price of {item_name}: "))
    return item_name, quantity, price

def main():
    orders = []
    keep_ordering = True
    
    while keep_ordering:
        item_name, quantity, price = get_order_details()
        orders.append({"item_name": item_name, "quantity": quantity, "price": price})
        
        another_order = input("Do you want to order another item? (yes/no): ").strip().lower()
        if another_order != 'yes':
            keep_ordering = False
    
    # Display the orders
    for order in orders:
        print(f"Item: {order['item_name']}, Quantity: {order['quantity']}, Price: ${order['price']:.2f}")

if __name__ == "__main__":
    main()

        # TODO: Ask the customer what they want to order
def ask_customer_order():
    order = input("What would you like to order? ")
    return order

# Example usage
order = ask_customer_order()
print(f"You want to order: {order}")


        # Create a variable for the menu item number
        i = 1

        # Print the menu header
        print_menu_heading()

        # TODO: Loop through the menu dictionary
 #       menu = {
#    "Appetizers": {
#        "Fries": 2.99,
#        "Onion Rings": 3.49
#    },
#    "Main Courses": {
#        "Burger": 8.99,
#        "Chicken Sandwich": 7.99,
#        "Salad": 5.99
#    },
#    "Drinks": {
#        "Soda": 1.49,
#        "Coffee": 1.99,
#        "Tea": 1.49
#    }
#}

# Loop through the menu dictionary
for category, items in menu.items():
    print(f"\nCategory: {category}")
    for item, price in items.items():
        print(f"  {item}: ${price:.2f}")



        # TODO: Extract the food category and the options for each category

for category, items in menu.items(): print(f"\nCategory: {category}") 
for item, price in items.items(): print(f" {item}: ${price:.2f}")
            # TODO: Loop through the options for each food category

for category, items in menu.items(): print(f"\nCategory: {category}") 
for item, price in items.items(): print(f" {item}: ${price:.2f}")

            # TODO: Extract the meal and the price for each option
                # Print the menu item number, food category, meal, and price

for category, items in menu.items(): for item, price in items.items(): print(f"{item_number}. 
             Category: {category}, Meal: {item}, Price: ${price:.2f}") item_number += 1
                # TODO: Only if you used different variable names
                
                # TODO: Update the variable names in the following function
print_menu_line(i, food_category, meal, price)

                # Update the menu selection number
                i += 1

        # TODO: Ask customer to input menu item number


        # TODO: Update the order list using the update_order function
        # TODO: Send the order list, menu selection, and menu items as arguments


        # TODO: Ask the customer if they would like to order anything else
        # TODO: Let the customer know if they should type 'n' or 'N' to quit


        # TODO: Write a conditional statement that checks the user's input
        # TODO: The conditional statement should check for 'n' or 'N'

            # TODO: Write a print statement that thanks the customer for their order


            # TODO: Use list comprehension to create a list called prices_list,
            # TODO: which contains the total prices for each item in the order list:
            # TODO: The total price for each item should multiply the price by quantity


            # TODO: Create an order_total from the prices list using sum()
            # TODO: Round the prices to 2 decimal places.


            # TODO: Exit the ordering loop
            # TODO: Either use a break statement or set the condition to False


    # TODO: Return the order list and the order total


def update_order(order, menu_selection, menu_items):
    """
    Checks if the customer menu selection is valid, then updates the order.

    Parameters:
    order (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    menu_selection (str): The customer's menu selection.
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered (updated as needed).
    """
    # TODO: Check if the customer typed a number

        # TODO: Convert the menu selection to an integer


        # TODO: Check if the menu selection is in the menu items keys

            # TODO: Store the item name as a variable


            # TODO: Ask the customer for the quantity of the menu item
            # TODO: Use the item name variable in the question


            # TODO: Check if the quantity is a number, default to 1 if not


            # TODO: Add a dictionary to the order list 
            # TODO: The dictionary should include the item name, price, and quantity
            # TODO: Use the following names for the dictionary keys:
            # TODO: "Item name", "Price", "Quantity"

        # TODO: When the user's input isn't valid, 
        # TODO: tell the customer that their input isn't valid

    # TODO: When the menu selection wasn't valid:
    # TODO: Print the menu selection and 
    # TODO: Tell the customer they didn't select a menu option


    # TODO: Return the updated order


def print_itemized_receipt(receipt):
    """
    Prints an itemized receipt for the customer.

    Parameters:
    receipt (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    """
    # Uncomment the following line if you need to check the structure of the receipt
    #print(receipt)

    # TODO: Loop through the items in the customer's receipt

        # TODO Store the dictionary items as variables


        # TODO: Print the receipt line using the print_receipt_line function
        # TODO: Send the item name, price, and quantity as separate arguments


##################################################
#  STARTER CODE
#  Do not modify any of the code below this line:
##################################################

def print_receipt_line(item_name, price, quantity):
    """
    Prints a line of the receipt.

    Parameters:
    item_name (str): The name of the meal item.
    price (float): The price of the meal item.
    quantity (int): The quantity of the meal item.
    """
    # Calculate the number of spaces for formatted printing
    num_item_spaces = 32 - len(item_name)
    num_price_spaces = 6 - len(str(price))

    # Create space strings
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces

    # Print the item name, price, and quantity
    print(f"{item_name}{item_spaces}| ${price}{price_spaces}| {quantity}")

def print_receipt_heading():
    """
    Prints the receipt heading.
    """
    print("----------------------------------------------------")
    print("Item name                       | Price  | Quantity")
    print("--------------------------------|--------|----------")

def print_receipt_footer(total_price):
    """
    Prints the receipt footer with the total price of the order.

    Parameters:
    total_price (float): The total price of the order.
    """
    print("----------------------------------------------------")
    print(f"Total price: ${total_price:.2f}")
    print("----------------------------------------------------")

def print_menu_heading():
    """
    Prints the menu heading.
    """
    print("--------------------------------------------------")
    print("Item # | Item name                        | Price")
    print("-------|----------------------------------|-------")

def print_menu_line(index, food_category, meal, price):
    """
    Prints a line of the menu.

    Parameters:
    index (int): The menu item number.
    food_category (str): The category of the food item.
    meal (str): The name of the meal item.
    price (float): The price of the meal item.
    """
    # Print the menu item number, food category, meal, and price
    num_item_spaces = 32 - len(food_category + meal) - 3
    item_spaces = " " * num_item_spaces
    if index < 10:
        i_spaces = " " * 6
    else:
        i_spaces = " " * 5
    print(f"{index}{i_spaces}| {food_category} - {meal}{item_spaces} | ${price}")

def get_menu_items_dict(menu):
    """
    Creates a dictionary of menu items and their prices mapped to their menu 
    number.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their
                        prices.

    Returns:
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.
    """
    # Create an empty dictionary to store the menu items
    menu_items = {}

    # Create a variable for the menu item number
    i = 1

    # Loop through the menu dictionary
    for food_category, options in menu.items():
        # Loop through the options for each food category
        for meal, price in options.items():
            # Store the menu item number, item name and price in the menu_items
            menu_items[i] = {
                "Item name": food_category + " - " + meal,
                "Price": price
            }
            i += 1

    return menu_items

def get_menu_dictionary():
    """
    Returns a dictionary of menu items and their prices.

    Returns:
    meals (dictionary): A nested dictionary containing the menu items and their
                        prices in the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }
    """
    # Create a meal menu dictionary
    #"""
    meals = {
        "Burrito": {
            "Chicken": 4.49,
            "Beef": 5.49,
            "Vegetarian": 3.99
        },
        "Rice Bowl": {
            "Teriyaki Chicken": 9.99,
            "Sweet and Sour Pork": 8.99
        },
        "Sushi": {
            "California Roll": 7.49,
            "Spicy Tuna Roll": 8.49
        },
        "Noodles": {
            "Pad Thai": 6.99,
            "Lo Mein": 7.99,
            "Mee Goreng": 8.99
        },
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    }
    """
    # This menu is just for testing purposes
    meals = {
        "Cake": {
            "Kuih Lapis": 3.49,
            "Strawberry Cheesecake": 6.49,
            "Chocolate Crepe Cake": 6.99
        },
        "Pie": {
            "Apple": 4.99,
            "Lemon Meringue": 5.49
        },
        "Ice-cream": {
            "2-Scoop Vanilla Cone": 3.49,
            "Banana Split": 8.49,
            "Chocolate Sundae": 6.99
        }
    }
    """
    return meals

# Run the program
if __name__ == "__main__":
    # Get the menu dictionary
    meals = get_menu_dictionary()

    receipt, total_price = place_order(meals)

    # Print out the customer's order
    print("This is what we are preparing for you.\n")

    # Print the receipt heading
    print_receipt_heading()

    # Print the customer's itemized receipt
    print_itemized_receipt(receipt)

    # Print the receipt footer with the total price
    print_receipt_footer(total_price)
