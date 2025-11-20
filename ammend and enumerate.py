#enumerate and append

#fruits = ["apple", "banana", "orange"]

#for index, fruit in enumerate(fruits, start=1):
    #print(f"{index}. {fruit}")

#--------------------------------------------------------------------------------

#tree_count = []

#trees = int(input("Enter the number of trees: "))

#for year in range(1,13):
#    trees += 5
#   if year % 4 ==0:
#        trees -= 12
#    tree_count.append(trees)

#for index, trees in enumerate(tree_count, start =1):
#    print(f"Tree {index}: {trees} trees")

#---------------------------------------------------------------------------------

#plants = 8

#plants_count = []

#for week in range(1,11):
 #   plants += 2
 #   if week % 3 == 0:
#        plants -= 5
 #   plants_count.append(plants)

#for index, plants in enumerate(plants_count, start=1):
 #   print(f"Week {index}: {plants}")

#------------------------------------------------------------------------------------

#pollution_units= 100

#pollution_level = []

#for weeks in range(1,16):
 #   pollution_units -= 4
 #  if weeks % 5 == 0:
  #      pollution_units += 12
#   pollution_level.append(pollution_units)

#for weeks, pollution_level in enumerate(pollution_level, start = 1):
#    print(f"Week {weeks}: Level {pollution_level}")

#---------------------------------------------------------------------------------------

#plants = 20

#plant_population = []

#for week in range(1,13):
 #   plants += 7
  #  if week % 5 ==0:
   #     plants -= 15
 #   plant_population.append(plants)

#for week, plant_population in enumerate(plant_population, start = 1):
 #   print(f"Week {week}: Plant Population {plants}")

#--------------------------------------------------------------------------------------

fish = 50

population = []

for week in range (1,13):
    fish += 6
    if week % 4 == 0:
        fish -= 10
    population.append(fish)

for week, population in enumerate(population, start=1):
    print(f"Week {week}: fish population {population}")


















