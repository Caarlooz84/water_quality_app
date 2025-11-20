import streamlit as st


pH = st.number_input("Enter the  pH: ")
free_chlorine = st.number_input("Enter FC: ")
total_chlorine = st.number_input("Enter TC: ")
stabilizer = st.number_input("Enter stabilizer: ")

if 7.2 <= pH <= 7.8:
    st.write(f"No muriatic acid is needed.")
elif pH < 7.1:
    st.write(f"Muriatic acid is needed.")
else:
    st.write(f"pH is way too high. No chemical needed.")

if free_chlorine <= 0.9:
    st.write(f"Free Chlorine is low. Chlorine tabs or liquid chlorine is needed.")
elif 1 <= free_chlorine <= 5:
    st.write(f"Free Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
else:
    st.write(f"Free Chlorine is way too high. No chemical needed.")

if total_chlorine <= 0.9:
    st.write(f"Total Chlorine is low. Chlorine tabs or liquid chlorine is needed.")
elif 1 <= total_chlorine <= 5:
    st.write(f"Total Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
else:
    st.write(f"Total Chlorine is way too high. No chemical needed.")

if stabilizer <= 29:
    st.write(f"Stabilizer is low. Stabilizer is needed in this water feature.")
elif 30 <= stabilizer <= 50 or 30 <= stabilizer <= 100:
    st.write(f"Stabilizer is ideal. Stabilizer is NOT needed in this water feature.")
elif stabilizer > 101:
    st.write(f"Stabilizer is HIGH. Stabilizer is NOT needed in this water feature.")
else:
    st.write(f"Stabilizer is HIGH.")