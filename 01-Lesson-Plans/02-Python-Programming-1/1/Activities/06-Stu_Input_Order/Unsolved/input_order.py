# Take input of an item the user wants to purchase

item = input("what is the item you want to purchase? ")
# Ask how much the item costs and cast it as a number.
item_cost = float(input("how much does the " + item + "cost? "))

# What type of number should it be cast as?

item_quantity = int(

input("what quantity of " + item + "would you like to" + "purchase? " ))
# Ask what quantity of the item should be purchased and cast it as a number.
# What type of number should it be cast as?


# Print the item cost along with its data type
print("the data type of " + str(item_cost) + "is " + str(type(item_cost)))

# Print the item quantity along with its data type
print("the data type of " + str(item_quantity) + "is " + str(type(item_quantity)))

# Print results
print(

"you want to buy "
+ str(item_quantity)
+ " "
+ item
+ "s for "
+str(item_cost)
+ " each. "
)