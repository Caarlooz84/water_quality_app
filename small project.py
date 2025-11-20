#small project

total_fish = int(input("Enter starting number of fish: "))
growth = int(input("Enter number of fish born each month: "))
months = int(input("Enter number of months: "))


for months in range(1, months + 1):
    total_fish += 3

    if months % 6 == 0:
        total_fish -= 8


print(f"month {months}: {total_fish} fish")











































