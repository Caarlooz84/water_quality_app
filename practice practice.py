pH = float(input("Enter the  pH: "))
free_chlorine = float(input("Enter FC: "))
total_chlorine = float(input("Enter TC: "))
stabilizer = float(input("Enter stabilizer: "))

if 7.2 <= pH <= 7.8:
    print(f"No muriatic acid is needed.")
elif pH < 7.1:
    print(f"Muriatic acid is needed.")
else:
    print(f"pH is way too high. No chemical needed.")

if free_chlorine <= 0.9:
    print(f"Free Chlorine is low. Chlorine tabs or liquid chlorine is needed.")
elif 1 <= free_chlorine <= 5:
    print(f"Free Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
else:
    print(f"Free Chlorine is way too high. No chemical needed.")

if total_chlorine <= 0.9:
    print(f"Total Chlorine is low. Chlorine tabs or liquid chlorine is needed.")
elif 1 <= total_chlorine <= 5:
    print(f"Total Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
else:
    print(f"Total Chlorine is way too high. No chemical needed.")

if stabilizer <= 29:
    print(f"Stabilizer is low. Stabilizer is needed in this water feature.")
elif 30 <= stabilizer <= 50 or 30 <= stabilizer <= 100:
    print(f"Stabilizer is ideal. Stabilizer is NOT needed in this water feature.")
elif stabilizer > 101:
    print(f"Stabilizer is HIGH. Stabilizer is NOT needed in this water feature.")
else:
    print(f"Stabilizer is HIGH.")











