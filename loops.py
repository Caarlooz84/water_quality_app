#loops

#total = 0 -> keeps track of the total amount as the loop runs
#for i in range (start, stop) -> Begin loop: i is a "counter" that goes through each step (like each day, sample, or year). The RANGE decides how many times the loop runs.

#if...: -> Conditional step. It only runs if the condition is true. (Like "if it's day 10, add 8 back".)
#    total+= ->

#if...: -> Another condition. You use a second if when both rules might apply in the same cycle.
#    total+= ->

#total += -> Always a do step. Something that happens every single loop cycle, no matter what.
# print(total): -> Result

total = 0
for i in range(1, 21):
    if i % 7 == 0:
        total += 4
    if i % 5 == 0:
        total -= 3
    total += 2
print(total)





























