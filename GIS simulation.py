# GIS Simulation

forest = [ # forest is a variable that stores the entire forest
    [10, 12, 15], # brackets -> create list; list is like a container for items
    [8, 9, 11], # inner brackets [..] -> represents row of forest patches
    [13, 9, 11] # #'s like 10 or 12 represent how many trees are in that patch
] # this is a 3x3 grid -> 3 rows, 3 columns

def forest_growth (forest, years): # def is function definition.
    for year in range( 1, years + 1): # numbers from 1 to years (inclusive)
        for i in range (len(forest)): #len(forest) -> counts how many items in the list forest.
            for j in range (len(forest[i])):
                trees = forest[i][j] # pick the cell at row i, column j
                if ( i + j + year) % 2 == 0:
                    trees += 3
                else:
                    trees -= 2
                forest[i][j] = trees
    return forest

new_forest = forest_growth(forest, 3)

for row in new_forest:
    print(row)






































































