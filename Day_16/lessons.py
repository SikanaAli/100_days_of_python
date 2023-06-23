# from turtle import Turtle, Screen
#
# pawpaw = Turtle()
#
# pawpaw.shape("turtle")
# pawpaw.color("coral")
# pawpaw.forward(100)
#
# my_screen = Screen()
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()


p_names = ["Pikachu","Charmander","Squirtle"]
p_type = ["lightning", "fire", "water"]

table.add_column("Pokemon Name", p_names)
table.add_column("Type", p_type)

table.align = "l"

print(table)

# lesson was looking at importing classes and using objects