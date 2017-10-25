"""
This program do something

Author: ArCHaven
"""
print('Mad Libs is starting!')
name = input("Enter name: ")
first_adj = input("Enter an adjective: ")
first_verb = input("Enter a verb: ")
first_noun = input("Enter a noun: ")
second_adj = input("Enter a second adjective: ")
second_verb = input("Enter a second verb: ")
second_noun = input("Enter a second noun: ")
third_adj = input("Enter a third adjective: ")
third_verb = input("Enter a third verb: ")
third_noun = input("Enter a third noun: ")
fourth_noun = input("Enter a fourth noun: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")
fruit = input("Enter a fruit: ")
number = input("Enter a number: ")
superhero = input("Enter a superhero: ")
country = input("Enter a country: ")
dessert = input("Enter a dessert: ")
year = input("Enter a year: ")
#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %s protesting to keep %s in stores. The crowd began to %s to the rhythm of the %s, which made all of the %s very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %s ruled the world."
print(STORY % (first_adj, name, first_verb, second_adj, first_noun, second_noun, animal, food, second_verb, third_noun, fruit, third_adj, name, third_verb, number, name, superhero, superhero, name, country, name, dessert, name, year, fourth_noun))
