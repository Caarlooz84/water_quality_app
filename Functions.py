# functions

#def my_function(parameter1, parameter2):
 #   variable1 = parameter1
  #  variable2 = []
   # for i in range(1, parameter2 + 1):
    #    pass
   #return variable2

#---------------------------------------------------------------------------------------

# Define the function
#-def fish_population(start_fish, growth, removal, weeks):
 #-   total_fish = start_fish         # starting number of fish
  #-  history = []                    # “empty notebook” to record population each week

   #- for week in range(1, weeks + 1):
    #-    total_fish += growth         # add new fish each week
     #-   if week % 4 == 0:            # remove fish every 4th week
      #  -    total_fish -= removal
    #-    history.append(total_fish)   # record population for this week

  # - return history                    # send the results back

# Call the function with specific values
#-result = fish_population(50, 6, 10, 12)

# Print population week by week
#-for week, population in enumerate(result, start=1):
 #-   print(f"Week {week}: Fish Population {population}")

#---------------------------------------------------------------------------------


#def grow_plants(5,4,2):
#    plants += 5
 #   history = []
  #  for week in range (1, week + 1):

#------------------------------------------------------------------------------------

#def grow_flowers (start_flowers, weeks, new_each_week):
#    flowers = start_flowers
 #   history = []
 #   for week in range (1, weeks + 1):
  #      flowers += new_each_week
   #     history.append(flowers)
   # return history
#result = grow_flowers(5,4,2)
#for week_num, flower_count in enumerate(result, start = 1):
 #   print(f"Week {week_num}: {flower_count} flowers")

 #------------------------------------------------------------------------------------

#def start_trees_limited (start_trees, weeks, new_each_week):
 #    trees = start_trees
  #   history = []
   #  for week in range(1, weeks + 1):
    #     if trees >= 20:
     #        break
      #   trees += new_each_week
       #  history.append(trees)
   #  return history

# result = start_trees_limited(5,6,3)
# for week_num, tree_count in enumerate (result, start =1):
 #   print(f" Week {week_num}: {tree_count} trees")

#--------------------------------------------------------------------------------------------

#def start_trees_limited (start_trees, weeks, new_each_week):
 #   trees = start_trees
  #  history = []
 #   for week in range(1, weeks + 1):
  #      if week <= 3:
   #         trees += new_each_week
    #    elif week >= 4:
     #       trees += new_each_week * 2
      #  else:
     #       break
    #    history.append (trees)
  #  return history

#result = start_trees_limited (5,6,3)
#for week_num, tree_count in enumerate(result, start = 1):
 #   print(f"Week {week_num}: {tree_count} Trees")

#--------------------------------------------------------------------------------------------

#def grow_fish (start_fish, weeks, new_each_week):
 #   fish = start_fish
  #  history = []
   # for week in range(1, weeks + 1):
    #    if week % 2 == 1:
     #       fish += 2
      #  elif week % 2 == 0:
       #     fish -= 1
      #  history.append (fish)
   # return history

#result = grow_fish (5,6,2)
#for week_num, fish_count in enumerate(result, start = 1):
 #   print(f"Week {week_num}: {fish_count} fish")

#--------------------------------------------------------------------------------------------

#def fish_growing (start_fish, weeks):
 #   fish = start_fish
  #  history = []
   # for week in range (1, weeks + 1):
    #    if week % 2 == 1:
     #       fish = fish * 2
      #  elif week % 2 == 0:
       #     fish -= 3
        #if fish >= 50:
         #   break
       # history.append(fish)
   # return history

#result = fish_growing(4,6)

#for week_num, fish_count in enumerate(result, start =1):
 #   print(f"Week {week_num}: {fish_count} fish")

#--------------------------------------------------------------------------------------------

def pond_growth(start_fish, weeks):
    fish = start_fish
    history = []
    for week in range (1, weeks + 1):
        if week % 2 == 1:
            fish = fish * 2
        elif week % 2 == 0:
            fish = fish - 4
        history.append(fish)
        if fish >= 100:
            break
    return history

result = pond_growth (20, 9)

for week_num, fish_count in enumerate (result, start =1):
    print(f"Week {week_num}: {fish_count} fish")















































