
water_feature = input("Enter the water feature: ")
pH = float(input("Enter the  pH: "))
free_chlorine = float(input("Enter FC: "))
total_chlorine = float(input("Enter TC: "))
stabilizer = float(input("Enter stabilizer: "))

if water_feature == "creek side" or water_feature == "creekside" or water_feature == "CreekSide" or water_feature == "Creek Side" or water_feature == "Creekside":
    if 7.2 <= pH <= 7.8:
        print(f"No muriatic acid is needed.")
    elif pH < 7.1:
        print(f"Add 2 gallons of muriatic acid.")
    else:
        print(f"pH is way too high. No chemical needed.")

    if free_chlorine <= 0.9:
        print(f"Add 120-130 Chlorine tabs and a case of liquid chlorine.")
    elif 1 <= free_chlorine <= 5:
        print(f"Free Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
    else:
        print(f"Free Chlorine is way too high. No chemical needed.")

    if total_chlorine <= 0.9:
        print(f"Add 120-130 Chlorine tabs and a case of liquid chlorine.")
    elif 1 <= total_chlorine <= 5:
        print(f"Total Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
    else:
        print(f"Total Chlorine is way too high. No chemical needed.")

    if stabilizer <= 29:
        print(f"Add 5 pounds of Stabilizer.")
    elif 30 <= stabilizer <= 50 or 30 <= stabilizer <= 100:
        print(f"Stabilizer is ideal. Stabilizer is NOT needed in this water feature.")
    elif stabilizer > 101:
        print(f"Stabilizer is HIGH. Stabilizer is NOT needed in this water feature.")
    else:
        print(f"Stabilizer is HIGH.")

if water_feature == "riverview" or water_feature == "River View" or water_feature == "river view" or water_feature == "RiverView":
    if 7.2 <= pH <= 7.8:
        print(f"No muriatic acid is needed.")
    elif pH < 7.1:
        print(f"Add 1 gallon of muriatic acid.")
    else:
        print(f"pH is way too high. No chemical needed.")

    if free_chlorine <= 0.9:
        print(f"Add 8 Chlorine tabs.")
    elif 1 <= free_chlorine <= 5:
        print(f"Free Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
    else:
        print(f"Free Chlorine is way too high. No chemical needed.")

    if total_chlorine <= 0.9:
        print(f"Add 8 Chlorine tabs.")
    elif 1 <= total_chlorine <= 5:
        print(f"Total Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
    else:
        print(f"Total Chlorine is way too high. No chemical needed.")

    if stabilizer <= 29:
        print(f"Add 1 pound of Stabilizer.")
    elif 30 <= stabilizer <= 50 or 30 <= stabilizer <= 100:
        print(f"Stabilizer is ideal. Stabilizer is NOT needed in this water feature.")
    elif stabilizer > 101:
        print(f"Stabilizer is HIGH. Stabilizer is NOT needed in this water feature.")
    else:
        print(f"Stabilizer is HIGH.")

if water_feature == "steel creek" or water_feature == "Steel Creek" or water_feature == "steelcreek" or water_feature == "SteelCreek":
    if 7.2 <= pH <= 7.8:
        print(f"No muriatic acid is needed.")
    elif pH < 7.1:
        print(f"Add 2 gallons of muriatic acid.")
    else:
        print(f"pH is way too high. No chemical needed.")

    if free_chlorine <= 0.9:
        print(f"Add a whole case (32 pints) of liquid chlorine.")
    elif 1 <= free_chlorine <= 5:
        print(f"Free Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
    else:
        print(f"Free Chlorine is way too high. No chemical needed.")

    if total_chlorine <= 0.9:
        print(f"Add a whole case (32 pints) of liquid chlorine.")
    elif 1 <= total_chlorine <= 5:
        print(f"Total Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
    else:
        print(f"Total Chlorine is way too high. No chemical needed.")

    if stabilizer <= 29:
        print(f"Add 5 pounds of Stabilizer.")
    elif 30 <= stabilizer <= 50 or 30 <= stabilizer <= 100:
        print(f"Stabilizer is ideal. Stabilizer is NOT needed in this water feature.")
    elif stabilizer > 101:
        print(f"Stabilizer is HIGH. Stabilizer is NOT needed in this water feature.")
    else:
        print(f"Stabilizer is HIGH.")

if water_feature == "eilan (big basin)" or water_feature == "Eilan (big basin)":
    if 7.2 <= pH <= 7.8:
        print(f"No muriatic acid is needed.")
    elif pH < 7.1:
        print(f"Add 1 gallon of muriatic acid.")
    else:
        print(f"pH is too high. No chemical needed.")

    if free_chlorine <= 0.9:
        print(f"Add 10 tabs of chlorine.")
    elif 1 <= free_chlorine <= 5:
        print(f"Free Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
    else:
        print(f"Free Chlorine is way too high. No chemical needed.")

    if total_chlorine <= 0.9:
        print(f"Add 10 tabs of chlorine.")
    elif 1 <= total_chlorine <= 5:
        print(f"Total Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
    else:
        print(f"Total Chlorine is way too high. No chemical needed.")

    if stabilizer <= 29:
        print(f"Add 2 pounds of Stabilizer.")
    elif 30 <= stabilizer <= 50 or 30 <= stabilizer <= 100:
        print(f"Stabilizer is ideal. Stabilizer is NOT needed in this water feature.")
    elif stabilizer > 101:
        print(f"Stabilizer is HIGH. Stabilizer is NOT needed in this water feature.")
    else:
        print(f"Stabilizer is HIGH.")

if water_feature == "eilan (small basin)" or water_feature == "Eilan (small basin)":
    if 7.2 <= pH <= 7.8:
        print(f"No muriatic acid is needed.")
    elif pH < 7.1:
        print(f"Add 1 gallon of muriatic acid.")
    else:
        print(f"pH is too high. No chemical needed.")

    if free_chlorine <= 0.9:
        print(f"Add 10 tabs of chlorine.")
    elif 1 <= free_chlorine <= 5:
        print(f"Free Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
    else:
        print(f"Free Chlorine is way too high. No chemical needed.")

    if total_chlorine <= 0.9:
        print(f"Add 10 tabs of chlorine.")
    elif 1 <= total_chlorine <= 5:
        print(f"Total Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
    else:
        print(f"Total Chlorine is way too high. No chemical needed.")

    if stabilizer <= 29:
        print(f"Add 1 pound of Stabilizer.")
    elif 30 <= stabilizer <= 50 or 30 <= stabilizer <= 100:
        print(f"Stabilizer is ideal. Stabilizer is NOT needed in this water feature.")
    elif stabilizer > 101:
        print(f"Stabilizer is HIGH. Stabilizer is NOT needed in this water feature.")
    else:
        print(f"Stabilizer is HIGH.")

if water_feature == "redbird" or water_feature == "Redbird" or water_feature == "red bird" or water_feature == "Red Bird" or water_feature == "Red Bird":
    if 7.2 <= pH <= 7.8:
        print(f"No muriatic acid is needed.")
    elif pH < 7.1:
        print(f"Add 1 gallon of muriatic acid.")
    else:
        print(f"pH is too high. No chemical needed.")

    if free_chlorine <= 0.9:
        print(f"Add 10 tabs of chlorine.")
    elif 1 <= free_chlorine <= 5:
        print(f"Free Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
    else:
        print(f"Free Chlorine is way too high. No chemical needed.")

    if total_chlorine <= 0.9:
        print(f"Add 10 tabs of chlorine.")
    elif 1 <= total_chlorine <= 5:
        print(f"Total Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
    else:
        print(f"Total Chlorine is way too high. No chemical needed.")

    if stabilizer <= 29:
        print(f"Add 3 pounds of Stabilizer.")
    elif 30 <= stabilizer <= 50 or 30 <= stabilizer <= 100:
        print(f"Stabilizer is ideal. Stabilizer is NOT needed in this water feature.")
    elif stabilizer > 101:
        print(f"Stabilizer is HIGH. Stabilizer is NOT needed in this water feature.")
    else:
        print(f"Stabilizer is HIGH.")

if water_feature == "alamo ranch" or water_feature == "Alamo Ranch" or water_feature == "AlamoRanch" or water_feature == "alamoranch":
    if 7.2 <= pH <= 7.8:
        print(f"No muriatic acid is needed.")
    elif pH < 7.1:
        print(f"Add 1 gallon of muriatic acid.")
    else:
        print(f"pH is too high. No chemical needed.")

    if free_chlorine <= 0.9:
        print(f"Add 16 pints of liquid chlorine.")
    elif 1 <= free_chlorine <= 5:
        print(f"Free Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
    else:
        print(f"Free Chlorine is way too high. No chemical needed.")

    if total_chlorine <= 0.9:
        print(f"Add 16 pints of liquid chlorine.")
    elif 1 <= total_chlorine <= 5:
        print(f"Total Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
    else:
        print(f"Total Chlorine is way too high. No chemical needed.")

    if stabilizer <= 29:
        print(f"Add 3 pounds of Stabilizer.")
    elif 30 <= stabilizer <= 50 or 30 <= stabilizer <= 100:
        print(f"Stabilizer is ideal. Stabilizer is NOT needed in this water feature.")
    elif stabilizer > 101:
        print(f"Stabilizer is HIGH. Stabilizer is NOT needed in this water feature.")
    else:
        print(f"Stabilizer is HIGH.")

