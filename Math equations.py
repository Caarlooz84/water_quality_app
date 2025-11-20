#project 1

#total = 50

#for month in range(1,25):
 #   total += 3
  #  if month % 6 == 0:
 #       total -= 8

#rint (f"Month {month}: {total} fish")


pH = float(input("What is the total pH of the water feature?"))
free_chlorine = float(input("What is the free chlorine?"))
stabilizer = float(input("What is the total stabilizer?"))

if pH < 5:
    print(f"The water feature needs Muriatic Acid.")
elif pH >= 5 and pH <= 10:
    print(f"The water feature does NOT need Muriatic Acid.")
if free_chlorine < 1:
    print(f"The water feature needs chlorine tabs or liquid chlorine.")
elif 1 < free_chlorine < 3:
    print(f"The water feature does NOT need chlorine tabs or liquid chlorine.")
if 6 < stabilizer < 8:
    print(f"The water feature does NOT need stabilizer.")
elif stabilizer < 5:
    print(f"The water feature does need stabilizer.")
























