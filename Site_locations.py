import streamlit as st
import folium
from streamlit_folium import st_folium

st.image("LMSS.png", width=450)
st.markdown("Lake & AWF Maintenance Dashboard for routine maintenance, treatment identification, and reporting.")

side = st.selectbox("Choose your side:", ["Select", "Lake", "AWF"])
#site = st.text_input("Enter site name")

if side == "AWF":
    site = st.selectbox("Choose water feature", ["Search", "River View", "Winding Creek", "Steele Creek", "Redbird", "Alamo Ranch", "Creekside", "Éilan", "Brookestone"])

    if site == "River View":
        page = st.radio("Select", ["Routine Maintenance", "Water quality levels", "Map", "Report Generator"], horizontal=True)
        if page == "Routine Maintenance":
            st.subheader("River View")
            st.image("river_view.png", caption="River View", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat water feature")
            st.checkbox(" Remove debris from water feature")
            st.checkbox("Clean out pump strainers")
            st.checkbox("Backwash and rinse filter pump")
            st.checkbox("Do any specific task for today")
        elif page == "Map":
            st.write("1205 River Terrace Dr, Georgetown, TX 78628")
            m = folium.Map(location=[30.632489, -97.735146], zoom_start=12)
            folium.Marker(location=[30.632489, -97.735146], popup="River View",icon=folium.Icon(color="blue", icon="tint")).add_to(m)
            st_folium(m)
        elif page == "Water quality levels":
            pH = st.number_input("Enter the  pH: ")
            chlorine = st.number_input("Enter TC and FC: ")
            stabilizer = st.number_input("Enter stabilizer: ")
            if 7.2 <= pH <= 7.8:
                st.write(f"No muriatic acid is needed.")
            elif pH < 7.1:
                st.write(f"No muriatic acid is needed.")
            else:
                st.write(f"pH is high. Add 1 gallon of muriatic acid.")

            if chlorine <= 0.9:
                st.write(f"Add 8 Chlorine tabs.")
            elif 1 <= chlorine <= 5:
                st.write(f"Total and Free Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
            else:
                st.write(f"Total and Free Chlorine is way too high. No chemical needed.")

            if stabilizer <= 29:
                st.write(f"Add 1 pound of Stabilizer.")
            elif 30 <= stabilizer <= 50 or 30 <= stabilizer <= 100:
                st.write(f"Stabilizer is ideal. Stabilizer is NOT needed in this water feature.")
            elif stabilizer > 101:
                st.write(f"Stabilizer is HIGH. Stabilizer is NOT needed in this water feature.")
            else:
                st.write(f"Stabilizer is HIGH.")
        elif page == "Report Generator":
            st.header("Tasks")

            # sump_clean = st.checkbox("Sump Cleaning")
            starter = st.checkbox("Starter")
            Water_test_treatment = st.checkbox("Water test treatment")
            Trash_pump_strainer= st.checkbox("Trash pump strainer")
            Filter_pump= st.checkbox("Filter pump")
            Water_pump_removal = st.checkbox("Water Pump removal")
            Vacuum = st.checkbox("Vacuum")
            Nozzles_Valve_bodies = st.checkbox("Nozzles and Valve bodies")
            Water_filling = st.checkbox("Water filling")
            Damaged_pipe = st.checkbox("Damaged pipe and fixed")
            Sump_clean = st.checkbox("Sump clean")
            Motor_nonOperational = st.checkbox("Motor nonoperational")
            Motor_removal = st.checkbox("Motor removal")
            Motor_Reinstalled = st.checkbox("Motor re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")
            Ending = st.checkbox("Ending")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if starter:
                report.append("Today we perform routine maintenance on this water feature. An inspection was conducted to assess current conditions and maintenance needs. After the inspection,")
            if Water_test_treatment:
                report.append("The water quality was tested and the water feature was treated with chemical accordingly.")
            if Trash_pump_strainer:
                report.append("Trash/debris was removed from the water feature and from the pump strainers.")
            if Filter_pump:
                report.append("All filter pumps were backwashed and rinsed.")
            if Water_pump_removal:
                report.append("The submersible water pump in basin [X] was found to be non-operational and was removed from the water feature for further inspection and service.")
            if Vacuum:
                report.append("The water feature in basin [X] was vacuumed to removed buildup debris on the hardscape.")
            if Nozzles_Valve_bodies:
                report.append("Debris was removed from the main water feature's nozzles and vale bodies to restore proper water flow and improve the water effects.")
            if Water_filling:
                report.append("All basins of the water feature were filled back to their optimal water level.")
            if Damaged_pipe:
                report.append("A damaged section of pipe was removed and replaced to restore proper water flow and prevent leakage.")
            if Sump_clean:
                report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")
            if Motor_nonOperational:
                report.append("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
            if Motor_removal:
                report.append("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if Motor_Reinstalled:
                report.append("The motor was reinstalled, tested, and is fully operational at this time.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Ending:
                report.append("The water feature was left in good conditions at the time of departure.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)


    if site == "Winding Creek":
        page = st.radio("Select", ["Routine Maintenance", "Water quality levels", "Map", "Report Generator"], horizontal=True)
        if page == "Routine Maintenance":
            st.subheader("Winding Creek")
            st.image(f"Winding_Creek.png", caption="Winding Creek", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat water feature")
            st.checkbox("Remove debris from water feature")
            st.checkbox("Clean out both pump strainers")
            st.checkbox("Backwash and rinse both filter pumps")
            st.checkbox("Do any specific task for today")
        elif page == "Map":
            st.write(f"1833-1801 Chianti Pass Canyon Lake, Texas")
            m = folium.Map(location=[29.623099, -98.125060], zoom_start=12)
            folium.Marker(location=[29.623099, -98.125060], popup = "Winding Creek", icon=folium.Icon(color="blue", icon="tint")).add_to(m)
            st_folium(m)
        elif page == "Water quality levels":
            pH = st.number_input("Enter the  pH: ")
            chlorine = st.number_input("Enter TC and FC: ")
            stabilizer = st.number_input("Enter stabilizer: ")
            if 7.2 <= pH <= 7.8:
                st.write(f"No muriatic acid is needed.")
            elif pH < 7.1:
                st.write(f"No muriatic acid is needed.")
            else:
                st.write(f"pH is high. Add 1 gallon of muriatic acid.")

            if chlorine <= 0.9:
                st.write(f"Total and Free Chlorine is too low. No chemical needed.")
            elif 1 <= chlorine <= 5:
                st.write(f"Total and Free Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
            else:
                st.write(f"Add 20 Chlorine tabs.")

            if stabilizer <= 29:
                st.write(f"Add 1 pound of Stabilizer.")
            elif 30 <= stabilizer <= 50 or 30 <= stabilizer <= 100:
                st.write(f"Stabilizer is ideal. Stabilizer is NOT needed in this water feature.")
            elif stabilizer > 101:
                st.write(f"Stabilizer is HIGH. Stabilizer is NOT needed in this water feature.")
            else:
                st.write(f"Stabilizer is HIGH.")
        elif page == "Report Generator":
            st.header("Tasks")

            # sump_clean = st.checkbox("Sump Cleaning")
            starter = st.checkbox("Starter")
            Water_test_treatment = st.checkbox("Water test treatment")
            Trash_pump_strainer= st.checkbox("Trash pump strainer")
            Filter_pump= st.checkbox("Filter pump")
            Water_pump_removal = st.checkbox("Water Pump removal")
            Vacuum = st.checkbox("Vacuum")
            Nozzles_Valve_bodies = st.checkbox("Nozzles and Valve bodies")
            Water_filling = st.checkbox("Water filling")
            Damaged_pipe = st.checkbox("Damaged pipe and fixed")
            Sump_clean = st.checkbox("Sump clean")
            Motor_nonOperational = st.checkbox("Motor nonoperational")
            Motor_removal = st.checkbox("Motor removal")
            Motor_Reinstalled = st.checkbox("Motor re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")
            Ending = st.checkbox("Ending")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if starter:
                report.append("Today we perform routine maintenance on both water features. An inspection was conducted to assess current conditions and maintenance needs. After the inspection,")
            if Water_test_treatment:
                report.append("The water quality was tested and both water features were treated with chemical accordingly.")
            if Trash_pump_strainer:
                report.append("Trash/debris was removed from both water features and from the pump strainers.")
            if Filter_pump:
                report.append("Both filter pumps were backwashed and rinsed.")
            if Water_pump_removal:
                report.append("The submersible water pump in basin [X] was found to be non-operational and was removed from the water feature for further inspection and service.")
            if Vacuum:
                report.append("The water feature in basin [X] was vacuumed to removed buildup debris on the hardscape.")
            if Nozzles_Valve_bodies:
                report.append("Debris was removed from the main water feature's nozzles and vale bodies to restore proper water flow and improve the water effects.")
            if Water_filling:
                report.append("All basins of the water feature were filled back to their optimal water level.")
            if Damaged_pipe:
                report.append("A damaged section of pipe was removed and replaced to restore proper water flow and prevent leakage.")
            if Sump_clean:
                report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")
            if Motor_nonOperational:
                report.append("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
            if Motor_removal:
                report.append("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if Motor_Reinstalled:
                report.append("The motor was reinstalled, tested, and is fully operational at this time.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Ending:
                report.append("The water features were left in good conditions at the time of departure.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)


    if site == "Steele Creek":
        page = st.radio("Select", ["Routine Maintenance", "Water quality levels", "Map", "Report Generator"], horizontal=True)
        if page == "Routine Maintenance":
            st.subheader("Steel Creek")
            st.image(f"Steele_Creek.png", caption="Steele Creek", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat water feature")
            st.checkbox("Remove debris from water feature")
            st.checkbox("Backwash and rinse filter pump")
            st.checkbox("Do any specific task for today")
        elif page == "Map":
            st.write(f"599-501 Steel Rpds, Cibolo, TX")
            m = folium.Map(location=[29.572180, -98.218894], zoom_start=12)
            folium.Marker(location=[29.572180, -98.218894], popup = "Steele Creek", icon=folium.Icon(color="blue", icon="tint")).add_to(m)
            st_folium(m)
        elif page == "Water quality levels":
            pH = st.number_input("Enter the  pH: ")
            chlorine = st.number_input("Enter TC and FC: ")
            stabilizer = st.number_input("Enter stabilizer: ")
            if 7.2 <= pH <= 7.8:
                st.write(f"No muriatic acid is needed.")
            elif pH < 7.1:
                st.write(f"No muriatic acid is needed.")
            else:
                st.write(f"pH is high. Add 1 gallon of muriatic acid.")

            if chlorine <= 0.9:
                st.write(f"Total and Free Chlorine is low. Add a whole case (32 pints) of liquid chlorine.")
            elif 1 <= chlorine <= 5:
                st.write(f"Total and Free Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
            else:
                st.write(f"Total and Free chlorine is high. No chemical needed.")

            if stabilizer <= 29:
                st.write(f"Add 1 pound of Stabilizer.")
            elif 30 <= stabilizer <= 50 or 30 <= stabilizer <= 100:
                st.write(f"Stabilizer is ideal. Stabilizer is NOT needed in this water feature.")
            elif stabilizer > 101:
                st.write(f"Stabilizer is HIGH. Stabilizer is NOT needed in this water feature.")
            else:
                st.write(f"Stabilizer is HIGH.")
        elif page == "Report Generator":
            st.header("Tasks")

            # sump_clean = st.checkbox("Sump Cleaning")
            starter = st.checkbox("Starter")
            Water_test_treatment = st.checkbox("Water test treatment")
            Filter_pump= st.checkbox("Filter pump")
            Water_pump_removal = st.checkbox("Water Pump removal")
            Vacuum = st.checkbox("Vacuum")
            Nozzles_Valve_bodies = st.checkbox("Nozzles and Valve bodies")
            Water_filling = st.checkbox("Water filling")
            Damaged_pipe = st.checkbox("Damaged pipe and fixed")
            Sump_clean = st.checkbox("Sump clean")
            Motor_nonOperational = st.checkbox("Motor nonoperational")
            Motor_removal = st.checkbox("Motor removal")
            Motor_Reinstalled = st.checkbox("Motor re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")
            Ending = st.checkbox("Ending")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if starter:
                report.append("Today we perform routine maintenance on this water feature. An inspection was conducted to assess current conditions and maintenance needs. After the inspection, ")
            if Water_test_treatment:
                report.append("The water quality was tested and the water feature was treated with chemical accordingly.")
            if Filter_pump:
                report.append("The filter pump was backwashed and rinsed.")
            if Water_pump_removal:
                report.append("The submersible water pump in basin [X] was found to be non-operational and was removed from the water feature for further inspection and service.")
            if Vacuum:
                report.append("The water feature in the lower basin was vacuumed to removed buildup debris on the hardscape.")
            if Nozzles_Valve_bodies:
                report.append("Debris was removed from the main water feature's nozzles and vale bodies to restore proper water flow and improve the water effects.")
            if Water_filling:
                report.append("All basins of the water feature were filled back to their optimal water level.")
            if Damaged_pipe:
                report.append("A damaged section of pipe was removed and replaced to restore proper water flow and prevent leakage.")
            if Sump_clean:
                report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")
            if Motor_nonOperational:
                report.append("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
            if Motor_removal:
                report.append("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if Motor_Reinstalled:
                report.append("The motor was reinstalled, tested, and is fully operational at this time.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash/debris was removed from all basins to maintain a neat and accessible environment.")
            if Ending:
                report.append("The water feature was left in good conditions at the time of departure.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)


    if site == "Redbird":
        page = st.radio("Select", ["Routine Maintenance", "Water quality levels", "Map", "Report Generator"], horizontal=True)
        if page == "Routine Maintenance":
            st.subheader("Redbird")
            st.image(f"Redbird.png", caption="Redbird", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat water feature")
            st.checkbox("Remove debris from water feature")
            st.checkbox("Clean out pump strainer")
            st.checkbox("Backwash and rinse both filter pumps")
            st.checkbox("Do any specific task for today")
        elif page == "Map":
            st.write("214-202 Redbird Cir, San Antonio, TX")
            m = folium.Map(location=[29.431115, -98.798014], zoom_start=12)
            folium.Marker(location=[29.431115, -98.798014], popup = "Redbird", icon=folium.Icon(color="blue", icon="tint")).add_to(m)
            st_folium(m)
        elif page == "Water quality levels":
            pH = st.number_input("Enter the  pH: ")
            chlorine = st.number_input("Enter TC and FC: ")
            stabilizer = st.number_input("Enter stabilizer: ")
            if 7.2 <= pH <= 7.8:
                st.write(f"No muriatic acid is needed.")
            elif pH < 7.1:
                st.write(f"pH is low. No chemical needed.")
            else:
                st.write(f"Add 1 gallon of muriatic acid.")

            if chlorine <= 0.9:
                st.write(f"Add 10 tabs of chlorine.")
            elif 1 <= chlorine <= 5:
                st.write(f"Total and Free Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
            else:
                st.write(f"Total and Free Chlorine is way too high. No chemical needed.")

            if stabilizer <= 29:
                st.write(f"Add 3 pounds of Stabilizer.")
            elif 30 <= stabilizer <= 50 or 30 <= stabilizer <= 100:
                st.write(f"Stabilizer is ideal. Stabilizer is NOT needed in this water feature.")
            elif stabilizer > 101:
                st.write(f"Stabilizer is HIGH. Stabilizer is NOT needed in this water feature.")
            else:
                st.write(f"Stabilizer is HIGH.")
        elif page == "Report Generator":
            st.header("Tasks")

            # sump_clean = st.checkbox("Sump Cleaning")
            starter = st.checkbox("Starter")
            Water_test_treatment = st.checkbox("Water test treatment")
            Trash_pump_strainer= st.checkbox("Trash pump strainer")
            Filter_pump= st.checkbox("Filter pump")
            Water_pump_removal = st.checkbox("Water Pump removal")
            Vacuum = st.checkbox("Vacuum")
            Nozzles_Valve_bodies = st.checkbox("Nozzles and Valve bodies")
            Water_filling = st.checkbox("Water filling")
            Damaged_pipe = st.checkbox("Damaged pipe and fixed")
            Sump_clean = st.checkbox("Sump clean")
            Motor_nonOperational = st.checkbox("Motor nonoperational")
            Motor_removal = st.checkbox("Motor removal")
            Motor_Reinstalled = st.checkbox("Motor re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")
            Ending = st.checkbox("Ending")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if starter:
                report.append("Today we perform routine maintenance on this water feature. An inspection was conducted to assess current conditions and maintenance needs. After the inspection,")
            if Water_test_treatment:
                report.append("The water quality was tested and the water feature was treated with chemical accordingly.")
            if Trash_pump_strainer:
                report.append("Trash/debris was removed from the water feature and from the pump strainer.")
            if Filter_pump:
                report.append("The filter pump was backwashed and rinsed.")
            if Water_pump_removal:
                report.append("The submersible water pump in basin [X] was found to be non-operational and was removed from the water feature for further inspection and service.")
            if Vacuum:
                report.append("The water feature was vacuumed to removed buildup debris on the hardscape.")
            if Nozzles_Valve_bodies:
                report.append("Debris was removed from the main water feature's nozzles and vale bodies to restore proper water flow and improve the water effects.")
            if Water_filling:
                report.append("All basins of the water feature were filled back to their optimal water level.")
            if Damaged_pipe:
                report.append("A damaged section of pipe was removed and replaced to restore proper water flow and prevent leakage.")
            if Sump_clean:
                report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")
            if Motor_nonOperational:
                report.append("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
            if Motor_removal:
                report.append("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if Motor_Reinstalled:
                report.append("The motor was reinstalled, tested, and is fully operational at this time.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Ending:
                report.append("The water feature was left in good conditions at the time of departure.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)


    if site == "Alamo Ranch":
        page = st.radio("Select", ["Routine Maintenance", "Water quality levels", "Map", "Report Generator"], horizontal=True)
        if page == "Routine Maintenance":
            st.subheader("Alamo Ranch")
            st.image(f"Alamo_Ranch.png", caption="Alamo Ranch", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat water feature")
            st.checkbox("Remove debris from water feature")
            st.checkbox("Do any specific task for today")
        elif page == "Map":
            st.write ("Alamo Pkwy, San Antonio, TX 78253")
            m = folium.Map(location=[29.4834609, -98.7338868], zoom_start=12)
            folium.Marker(location=[29.4834609, -98.7338868], popup = "Alamo Ranch", icon=folium.Icon(color="blue", icon="tint")).add_to(m)
            st_folium(m)
        elif page == "Water quality levels":
            pH = st.number_input("Enter the  pH: ")
            chlorine = st.number_input("Enter TC and FC: ")
            stabilizer = st.number_input("Enter stabilizer: ")
            if 7.2 <= pH <= 7.8:
                st.write(f"No muriatic acid is needed.")
            elif pH < 7.1:
                st.write(f"No muriatic acid is needed.")
            else:
                st.write(f"pH is high. Add 1 gallon of muriatic acid.")

            if chlorine <= 0.9:
                st.write(f"Add 16 pints of liquid chlorine.")
            elif 1 <= chlorine <= 5:
                st.write(f"Total and Free Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
            else:
                st.write(f"Total and Free Chlorine is way too high. No chemical needed.")

            if stabilizer <= 29:
                st.write(f"Add 3 pounds of Stabilizer.")
            elif 30 <= stabilizer <= 50 or 30 <= stabilizer <= 100:
                st.write(f"Stabilizer is ideal. Stabilizer is NOT needed in this water feature.")
            elif stabilizer > 101:
                st.write(f"Stabilizer is HIGH. Stabilizer is NOT needed in this water feature.")
            else:
                st.write(f"Stabilizer is HIGH.")
        elif page == "Report Generator":
            st.header("Tasks")

            # sump_clean = st.checkbox("Sump Cleaning")
            starter = st.checkbox("Starter")
            Water_test_treatment = st.checkbox("Water test treatment")
            Trash_pump_strainer= st.checkbox("Trash pump strainer")
            Filter_pump= st.checkbox("Filter pump")
            Water_pump_removal = st.checkbox("Water Pump removal")
            Vacuum = st.checkbox("Vacuum")
            Nozzles_Valve_bodies = st.checkbox("Nozzles and Valve bodies")
            Water_filling = st.checkbox("Water filling")
            Damaged_pipe = st.checkbox("Damaged pipe and fixed")
            Sump_clean = st.checkbox("Sump clean")
            Motor_nonOperational = st.checkbox("Motor nonoperational")
            Motor_removal = st.checkbox("Motor removal")
            Motor_Reinstalled = st.checkbox("Motor re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")
            Ending = st.checkbox("Ending")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if starter:
                report.append("Today we perform routine maintenance on all basins of this water feature. An inspection was conducted to assess current conditions and maintenance needs. After the inspection,")
            if Water_test_treatment:
                report.append("The water quality was tested and the water feature was treated with chemical accordingly.")
            if Trash_pump_strainer:
                report.append("Trash/debris was removed from the water feature and from the pump strainers.")
            if Filter_pump:
                report.append("The filter pump was backwashed and rinsed.")
            if Water_pump_removal:
                report.append("The submersible water pump in basin [X] was found to be non-operational and was removed from the water feature for further inspection and service.")
            if Vacuum:
                report.append("The water feature in basin [X] was vacuumed to removed buildup debris on the hardscape.")
            if Nozzles_Valve_bodies:
                report.append("Debris was removed from the main water feature's nozzles and vale bodies to restore proper water flow and improve the water effects.")
            if Water_filling:
                report.append("All basins of the water feature were filled back to their optimal water level.")
            if Damaged_pipe:
                report.append("A damaged section of pipe was removed and replaced to restore proper water flow and prevent leakage.")
            if Sump_clean:
                report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")
            if Motor_nonOperational:
                report.append("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
            if Motor_removal:
                report.append("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if Motor_Reinstalled:
                report.append("The motor was reinstalled, tested, and is fully operational at this time.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash/debris was removed from all basins to maintain a neat and accessible environment.")
            if Ending:
                report.append("The water feature was left in good conditions at the time of departure.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)


    if site == "Creekside":
        page = st.radio("Select", ["Routine Maintenance", "Water quality levels", "Map", "Report Generator"], horizontal=True)
        if page == "Routine Maintenance":
            st.subheader("Creekside")
            st.image(f"Creek_Side.png", caption="Creekside", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat all basins")
            st.checkbox("Remove debris from all basins")
            st.checkbox("Fill up all basins to their optimal water levels")
            st.checkbox("Do any specific task for today")
        elif page == "Map":
            st.write(f"2966 Cold Spring Dr, New Braunfels, TX")
            m = folium.Map(location=[29.7298477, -98.0750534], zoom_start=12)
            folium.Marker(location=[29.7298477, -98.0750534], popup = "Creekside", icon=folium.Icon(color="blue", icon="tint")).add_to(m)
            st_folium(m)
        elif page == "Water quality levels":
            pH = st.number_input("Enter the  pH: ")
            chlorine = st.number_input("Enter TC and FC: ")
            stabilizer = st.number_input("Enter stabilizer: ")
            if 7.2 <= pH <= 7.8:
                st.write(f"No muriatic acid is needed.")
            elif pH < 7.1:
                st.write(f"pH is low. No chemical needed.")
            else:
                st.write(f"Add 2 gallons of muriatic acid.")

            if chlorine <= 0.9:
                st.write(f"Add 120-130 Chlorine tabs and a case of liquid chlorine.")
            elif 1 <= chlorine <= 5:
                st.write(f"Total and Free Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
            else:
                st.write(f"Total and Free Chlorine is way too high. No chemical needed.")

            if stabilizer <= 29:
                st.write(f"Add 5 pounds of Stabilizer.")
            elif 30 <= stabilizer <= 50 or 30 <= stabilizer <= 100:
                st.write(f"Stabilizer is ideal. Stabilizer is NOT needed in this water feature.")
            elif stabilizer > 101:
                st.write(f"Stabilizer is HIGH. Stabilizer is NOT needed in this water feature.")
            else:
                st.write(f"Stabilizer is HIGH.")

        elif page == "Report Generator":
            st.header("Tasks")

            # sump_clean = st.checkbox("Sump Cleaning")
            starter = st.checkbox("Starter")
            Water_test_treatment = st.checkbox("Water test treatment")
            Trash_pump_strainer= st.checkbox("Trash pump strainer")
            Filter_pump= st.checkbox("Filter pump")
            Water_pump_removal = st.checkbox("Water Pump removal")
            Vacuum = st.checkbox("Vacuum")
            Nozzles_Valve_bodies = st.checkbox("Nozzles and Valve bodies")
            Water_filling = st.checkbox("Water filling")
            Damaged_pipe = st.checkbox("Damaged pipe and fixed")
            Sump_clean = st.checkbox("Sump clean")
            Motor_nonOperational = st.checkbox("Motor nonoperational")
            Motor_removal = st.checkbox("Motor removal")
            Motor_Reinstalled = st.checkbox("Motor re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")
            Ending = st.checkbox("Ending")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if starter:
                report.append("Today we perform routine maintenance on all basins of this water feature. An inspection was conducted to assess current conditions and maintenance needs. After the inspection,")
            if Water_test_treatment:
                report.append("The water quality was tested and all basins were treated with chemical accordingly.")
            if Trash_pump_strainer:
                report.append("Trash/debris was removed from the water feature and from the pump strainers.")
            if Filter_pump:
                report.append("The filter pump was backwashed and rinsed.")
            if Water_pump_removal:
                report.append("The submersible water pump in basin [X] was found to be non-operational and was removed from the water feature for further inspection and service.")
            if Vacuum:
                report.append("The water feature in basin [X] was vacuumed to removed buildup debris on the hardscape.")
            if Nozzles_Valve_bodies:
                report.append("Debris was removed from the main water feature's nozzles and vale bodies to restore proper water flow and improve the water effects.")
            if Water_filling:
                report.append("All basins of the water feature were filled back to their optimal water level.")
            if Damaged_pipe:
                report.append("A damaged section of pipe was removed and replaced to restore proper water flow and prevent leakage.")
            if Sump_clean:
                report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")
            if Motor_nonOperational:
                report.append("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
            if Motor_removal:
                report.append("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if Motor_Reinstalled:
                report.append("The motor was reinstalled, tested, and is fully operational at this time.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash/debris was removed from all basins to maintain a neat and accessible environment.")
            if Ending:
                report.append("The water feature was left in good conditions at the time of departure.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Éilan":
        page = st.radio("Select", ["Routine Maintenance", "Water quality levels", "Map", "Report Generator"], horizontal=True)
        if page == "Routine Maintenance":
            st.subheader("Éilan")
            st.image(f"Eilan.png", caption="Éilan", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat all basins (main, middle and bird bath")
            st.checkbox("Remove debris from all basins")
            st.checkbox("Clean out all pump strainers (2)")
            st.checkbox("Backwash and rinse filter pump")
            st.checkbox("Fill up all basins to their optimal water levels")
            st.checkbox("Depending on water effects, clear out nozzles from debris")
            st.checkbox("Do any specific task for today")
        elif page == "Map":
            st.write("17803 La Cantera Terrace #1104, San Antonio, TX 78256")
            m = folium.Map(location=[29.6102167, -98.6057597], zoom_start=12)
            folium.Marker(location=[29.6102167, -98.6057597], popup="Éilan",
            icon=folium.Icon(color="blue", icon="tint")).add_to(m)
            st_folium(m)
        elif page == "Water quality levels":
            pH = st.number_input("Enter the  pH: ")
            chlorine = st.number_input("Enter TC and FC: ")
            stabilizer = st.number_input("Enter stabilizer: ")
            if 7.2 <= pH <= 7.8:
                st.write(f"No muriatic acid is needed.")
            elif pH < 7.1:
                st.write(f"No muriatic acid is needed.")
            else:
                st.write(f"pH is high. Add 1 gallon of muriatic acid.")

            if chlorine <= 0.9:
                st.write(f"Add 10 tabs of chlorine.")
            elif 1 <= chlorine <= 5:
                st.write(f"Total and Free Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
            else:
                st.write(f"Total and Free Chlorine is high. No chemical needed.")

            if stabilizer <= 29:
                st.write(f"Add 2 pounds of Stabilizer.")
            elif 30 <= stabilizer <= 50 or 30 <= stabilizer <= 100:
                st.write(f"Stabilizer is ideal. Stabilizer is NOT needed in this water feature.")
            elif stabilizer > 101:
                st.write(f"Stabilizer is HIGH. Stabilizer is NOT needed in this water feature.")
            else:
                st.write(f"Stabilizer is HIGH.")
        elif page == "Report Generator":
            st.header("Tasks")

            # sump_clean = st.checkbox("Sump Cleaning")
            Starter = st.checkbox("Starter")
            Water_test_treatment = st.checkbox("Water test treatment")
            Water_test_no_treatment = st.checkbox("Water test no treatment")
            Trash_pump_strainer= st.checkbox("Trash pump strainer")
            Filter_pump= st.checkbox("Filter pump")
            Water_pump_removal = st.checkbox("Water Pump removal")
            Vacuum = st.checkbox("Vacuum")
            Nozzles_Valve_bodies = st.checkbox("Nozzles and Valve bodies")
            Water_filling = st.checkbox("Water filling")
            No_water = st.checkbox("No water")
            Damaged_pipe = st.checkbox("Damaged pipe and fixed")
            Sump_clean = st.checkbox("Sump clean")
            Motor_nonOperational = st.checkbox("Motor nonoperational")
            Motor_removal = st.checkbox("Motor removal")
            Motor_Reinstalled = st.checkbox("Motor re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")
            Ending = st.checkbox("Ending")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Starter:
                report.append("Today we perform routine maintenance on all water features. An inspection was conducted to assess current conditions and maintenance needs. After the inspection,")
            if Water_test_treatment:
                report.append("The water quality was tested and the water features were treated with chemical accordingly.")
            if Water_test_no_treatment:
                report.append("The water quality was tested and the water features did not need any treatment at this time.")
            if Trash_pump_strainer:
                report.append("Trash/debris was removed from the water features and from the pump strainers.")
            if Filter_pump:
                report.append("The filter pump was backwashed and rinsed.")
            if Water_pump_removal:
                report.append("The submersible water pump was found to be non-operational and was removed from the water feature for further inspection and service.")
            if Vacuum:
                report.append("The water feature was vacuumed to removed buildup debris on the hardscape of the water feature.")
            if Nozzles_Valve_bodies:
                report.append("Debris was removed from the main water feature's nozzles and vale bodies to restore proper water flow and improve the water effects.")
            if Water_filling:
                report.append("All water features were filled back to their optimal water level.")
            if No_water:
                report.append("The water features were unable to be filled back to their optimal water level due to the irrigation being shut off.")
            if Damaged_pipe:
                report.append("A damaged section of pipe was removed and replaced to restore proper water flow and prevent leakage.")
            if Sump_clean:
                report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")
            if Motor_nonOperational:
                report.append("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
            if Motor_removal:
                report.append("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if Motor_Reinstalled:
                report.append("The motor was reinstalled, tested, and is fully operational at this time.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash/debris was removed from all water features to improve accessibility and site appearance.")
            if Ending:
                report.append("The water feature was left in good conditions at the time of departure.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Brookestone":
        page = st.radio("Select", ["Routine Maintenance", "Water quality levels", "Map", "Report Generator"], horizontal=True)
        if page == "Routine Maintenance":
            st.subheader("Brookestone(Evans)")
            st.image(f"Brookestone_Evans.png", caption="Brookestone(Evans)", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat water feature")
            st.checkbox("Remove debris from water feature")
            st.checkbox("Clean out all pump strainers")
            st.checkbox("Backwash and rinse all filter pumps")
            st.checkbox("Do any specific task for today")
            st.subheader("Brookestone(Boulder Flats)")
            st.image(f"Brookestone_Boulder_Flats.png", caption="Brookestone(Boulder Flats)", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat water feature", key="treat_water_feature_2")
            st.checkbox("Remove debris from water feature", key="remove_debris_2")
            st.checkbox("Clean out all pump strainers", key="clean_pump_strain_2")
            st.checkbox("Backwash and rinse all filter pumps", key="backwash_pump_strain_2")
            st.checkbox("Do any specific task for today", key="specific_task_2")
        elif page == "Map":
            st.subheader("Evans Road")
            st.write("5149 Evans Rd, San Antonio, TX 78261")
            m = folium.Map(location=[29.6425694, -98.3885825], zoom_start=12)
            folium.Marker(location=[29.6425694, -98.3885825], popup="Brookestone(Evans)",
            icon=folium.Icon(color="blue", icon="tint")).add_to(m)
            st_folium(m)
            st.subheader("Boulder Flats")
            st.write("Boulder Flts, San Antonio, TX 78266")
            m = folium.Map(location=[29.6409731, -98.3820970], zoom_start=12)
            folium.Marker(location=[29.6409731, -98.3820970], popup="Brookestone(Boulder Flats)", icon=folium.Icon(color="blue", icon="tint")).add_to(m)
            st_folium(m)
        elif page == "Water quality levels":
            pH = st.number_input("Enter the  pH: ")
            chlorine = st.number_input("Enter TC and FC: ")
            stabilizer = st.number_input("Enter stabilizer: ")
            if 7.2 <= pH <= 7.8:
                st.write(f"No muriatic acid is needed.")
            elif pH < 7.1:
                st.write(f"No muriatic acid is needed.")
            else:
                st.write(f"pH is high. Add 2 gallon of muriatic acid.")

            if chlorine <= 0.9:
                st.write(f"Add 10 tabs of chlorine.")
            elif 1 <= chlorine <= 5:
                st.write(f"Total and Free Chlorine is good. Chlorine tabs or liquid chlorine is NOT needed.")
            else:
                st.write(f"Total and Free Chlorine is high. No chemical needed.")

            if stabilizer <= 29:
                st.write(f"Add 5 pounds of Stabilizer.")
            elif 30 <= stabilizer <= 50 or 30 <= stabilizer <= 100:
                st.write(f"Stabilizer is ideal. Stabilizer is NOT needed in this water feature.")
            elif stabilizer > 101:
                st.write(f"Stabilizer is HIGH. Stabilizer is NOT needed in this water feature.")
            else:
                st.write(f"Stabilizer is HIGH.")
        elif page == "Report Generator":
            st.header("Task")

            # sump_clean = st.checkbox("Sump Cleaning")
            Starter = st.checkbox("Starter")
            Water_test_treatment = st.checkbox("Water test treatment")
            Trash_pump_strainer= st.checkbox("Trash pump strainer")
            Filter_pump= st.checkbox("Filter pump")
            Water_pump_removal = st.checkbox("Water Pump removal")
            Vacuum = st.checkbox("Vacuum")
            Nozzles_Valve_bodies = st.checkbox("Nozzles and Valve bodies")
            Water_filling = st.checkbox("Water filling")
            Damaged_pipe = st.checkbox("Damaged pipe and fixed")
            Sump_clean = st.checkbox("Sump clean")
            Motor_nonOperational = st.checkbox("Motor nonoperational")
            Motor_removal = st.checkbox("Motor removal")
            Motor_Reinstalled = st.checkbox("Motor re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")
            Ending = st.checkbox("Ending")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Starter:
                report.append("Today we perform routine maintenance on all water features. An inspection was conducted to assess current conditions and maintenance needs. After the inspection,")
            if Water_test_treatment:
                report.append("The water quality was tested and the water feature(s) was treated with chemical accordingly. An inspection was conducted to asses current conditions and maintenance needs. After the inspection,")
            if Trash_pump_strainer:
                report.append("Trash/debris was removed from the water feature and from the pump strainers.")
            if Filter_pump:
                report.append("The filter pump was backwashed and rinsed.")
            if Water_pump_removal:
                report.append("The submersible water pump was found to be non-operational and was removed from the water feature for further inspection and service.")
            if Vacuum:
                report.append("The water feature was vacuumed to removed buildup debris on the hardscape of the water feature.")
            if Nozzles_Valve_bodies:
                report.append("Debris was removed from the main water feature's nozzles and vale bodies to restore proper water flow and improve the water effects.")
            if Water_filling:
                report.append("The water feature (all basins) was filled back to its optimal water level.")
            if Damaged_pipe:
                report.append("A damaged section of pipe was removed and replaced to restore proper water flow and prevent leakage.")
            if Sump_clean:
                report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")
            if Motor_nonOperational:
                report.append("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
            if Motor_removal:
                report.append("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if Motor_Reinstalled:
                report.append("The motor was reinstalled, tested, and is fully operational at this time.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash/debris was removed from the water feature.")
            if Ending:
                report.append("Both water features were left in good conditions at the time of departure.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)


elif side == "Lake":
    site = st.selectbox("Choose pond", ["Search", "Falcon Pointe", "Berry Springs", "Hidden Oaks", "San Gabriel", "Camden Shadow Brooke", "Easton Park", "Wilder", "Blanco Vista", "Rosenbusch", "Hawkes Landing", "Lakeside Crossing", "Valley Ranch", "Red Bird Ranch", "Hunters Pond", "DR Horton", "Rhine Valley", "Whisper Falls", "Sundance Crossing", "Woods of Alon", "Cowboy Cabin", "The Willows HOA", "River Bend", "Preserve", "Green Lake", "Willow's Creek", "Wasser Ranch", "The Reserve at Lake Travis", "Crystal Village", "Versante", "South Grove Condominiums", "Austin East Parke HOA", "Edgewick HOA", "Alta Vista", "Mayfield", "Hidden Oaks at Berry Springs"])

    if site == "Falcon Pointe":
        page = st.radio("Select", ["Tasks", "Plant ID & Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("Secluded Willows")
            st.image(f"secluded_willows.png", caption="Secluded Willows", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Fountain inspection and testing")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
            st.subheader("Central Park")
            st.image(f"Falcon_Pointe.png", caption="Central Park", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat", key = "Treat_1")
            st.checkbox("Fountain inspection and testing", key = "Fountain_Inspection_Testing_1")
            st.checkbox("Pick up trash", key = "Pick_up_trash_1")
            st.checkbox("Do any specific task for today", key = "Specific_Task_1")
            st.subheader("Prim Rose")
            st.image(f"Prim_Rose.png", caption="Prim Rose", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat", key = "Treat_2")
            st.checkbox("Fountain inspection and testing", key = "Fountain_Inspection_Testing_2")
            st.checkbox("Pick up trash", key = "Pick_up_trash_2")
            st.checkbox("Do any specific task for today", key = "Specific_Task_2")
        elif page == "Plant ID & Treatment":
            #st.markdown("### Treatment")
            #st.checkbox("100 lbs copper sulfate (broadcast)") #Filamentous Algae control
            #st.checkbox("2 jugs of argos (spray)") #Filamentous Algae when bloom
            st.subheader("Secluded Willows")
            vegetation = None
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.image("filamentous_algae.png", use_container_width=True)
                if st.button("Filamentous Algae"):
                    vegetation = "Filamentous Algae"
            with col2:
                st.image("bushy_pondweed.png", use_container_width=True)
                if st.button("Bushy Pondweed"):
                    vegetation = "Bushy Pondweed"
            with col3:
                st.image("cat_tail.png", use_container_width=True)
                if st.button("Cattail"):
                    vegetation = "Cattail"
            with col4:
                st.image("arrow_head.png", use_container_width=True)
                if st.button("Arrowhead"):
                    vegetation = "Arrowhead"
            # Row 2
            col5, col6, col7, col8 = st.columns(4)
            with col5:
                st.image("prim_rose_plant.png", use_container_width=True)
                if st.button("Primrose"):
                    vegetation = "Primrose"
            with col6:
                st.image("lily.png", use_container_width=True)
                if st.button("Lily"):
                    vegetation = "Lily"
            with col7:
                st.image("alligator_weed.png", use_container_width=True)
                if st.button("Alligator Weed"):
                    vegetation = "Alligator Weed"
            with col8:
                st.image("american_weed.png", use_container_width=True)
                if st.button("American Pondweed"):
                    vegetation = "American Pondweed"

            if vegetation == "Filamentous Algae":
                st.markdown("### Treatment")
                st.write("Argos - Spray")
            elif vegetation == "Bushy Pondweed":
                st.markdown("### Treatment")
                st.write("Current - Spray")
            elif vegetation == "Cattail":
                st.markdown("### Treatment")
                st.write("Aquaneat - Spray")
            elif vegetation == "Arrowhead":
                st.markdown("### Treatment")
                st.write("Aquaneat - Spray")
            elif vegetation == "Primrose":
                st.markdown("### Treatment")
                st.write("Aquaneat - Spray")
            elif vegetation == "Lily":
                st.markdown("### Treatment")
                st.write("Aquaneat - Spray")
            elif vegetation == "Alligator Weed":
                st.markdown("### Treatment")
                st.write("Aquamaster - Spray")
            elif vegetation == "American Pondweed":
                st.markdown("### Treatment")
                st.write("Aquathol K Liquid - Spray or Aquathol K Granular - Broadcast")

            st.write("### Algae Control Treatment")
            st.write("50 lbs (whole bag) copper sulfate")
            st.subheader("Central Park")
            st.image(f"Falcon_Pointe.png", caption="Central Park", use_container_width=True)
            vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Argos - Spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
                # st.write("### Routine Treatment")
                # st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquathol K - spray")
            st.subheader("Prim Rose")
            st.image(f"Prim_Rose.png", caption="Prim Rose", use_container_width=True)
            st.write("### Algae Control Treatment")
            vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"], key = "vegetation_type_2")
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Argos - Spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
                # st.write("### Routine Treatment")
                # st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquathol K - spray")
            st.write("50 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
        elif page == "Map":
            m = folium.Map(location=[30.46, -97.58], zoom_start=12)
            folium.TileLayer("Esri.WorldImagery").add_to(m)

            folium.Marker([30.4717253, -97.5894210], popup="Secluded Willows", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            folium.Marker([30.4573293, -97.5840429], popup="Central Park",icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            folium.Marker([30.4517623, -97.5886834], popup="Prim Rose", icon=folium.Icon(color="green", icon="leaf")).add_to(m)

            folium.LayerControl().add_to(m)
            st_folium(m)
            #st.subheader("Secluded Willows")
            #st.write("1742 Secluded Willow Cove, Pflugerville, Texas 78660")
            #m = folium.Map(location=[30.4717253, -97.5894210], zoom_start=12)
            #folium.Marker(location=[30.4717253, -97.5894210], popup="Secluded Willows",icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            #st_folium(m)
            #folium.TileLayer("Esri.WorldImagery").add_to(m)
            #folium.LayerControl().add_to(m)
            #st.subheader("Central Park")
            #st.write("2708-2812 Standing Juniper Ct, Pflugerville, TX 78660")
            #m = folium.Map(location=[30.4573293, -97.5840429], zoom_start=12)
            #folium.Marker(location=[30.4573293, -97.5840429], popup="Falcon Pointe", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            #st_folium(m)
            #st.subheader("Prim Rose")
            #st.write("17829 Colorado Sand Dr, Pflugerville, Texas 78660")
            #m = folium.Map(location=[30.4517623, -97.5886834], zoom_start=12)
            #folium.Marker(location=[30.4517623, -97.5886834], popup="Prim Rose", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            #st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Starter = st.checkbox("Starter")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_Removal_Central = st.checkbox("Fountain removal Central")
            Fountain_Removal_Willows = st.checkbox("Fountain removal Willows")
            Fountain_Removal_Primrose = st.checkbox("Fountain removal Primrose")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Fountain_Lens = st.checkbox("Fountain lens")
            Fountain_lights = st.checkbox("Fountain lights")
            Motor_nonOperational = st.checkbox("Motor nonoperational")
            Motor_removal = st.checkbox("Motor removal")
            Motor_Reinstalled = st.checkbox("Motor re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")
            Ending = st.checkbox("Ending")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Starter:
                report.append("Today we perform routine maintenance on Secluded Willows, Central Park Pond and Primrose School Park. An inspection was conducted to assess current conditions and maintenance needs. After the inspection,")
            if Mow:
                report.append(
                    "the pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("the fountains on all ponds appear to be fully operational at this time including the lights, GFCI and the motor.")
            if Fountain_Removal_Willows:
                report.append(
                    "the fountain on Secluded Willows was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_Removal_Central:
                report.append(
                    "the fountain on Central Park Pond was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_Removal_Primrose:
                report.append("the fountain on Primrose School Park was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Fountain_lights:
                report.append(
                    "one of the fountain lights were replaced and tested to ensure proper illumination and operation.")
            if Fountain_Lens:
                report.append(
                    "the fountain light lens was replaced and the lighting system was tested to ensure porper operation.")
            if Chemical:
                report.append(
                    "the ponds were treated with chemical to control -plant species- growth and support overall water quality.")
            if Motor_nonOperational:
                report.append(
                    "the pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
            if Motor_removal:
                report.append(
                    "the pump motor was found to be non-operational and was removed from site for further inspection.")
            if Motor_Reinstalled:
                report.append("the motor was reinstalled, tested, and is fully operational at this time.")
            if Pressure_wash:
                report.append(
                    "the waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("the well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("the water level in [X] is [X] inches above from its optimal level.")
            if Water_level_decrease:
                report.append("the water level in [X] is [X] inches below from its optimal level.")
            if Trash:
                report.append("trash on all ponds were collected and properly disposed of to maintain the areas clean and accessible.")
            if Ending:
                report.append("All the ponds were left in good conditions at the time of departure.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Berry Springs":
        page = st.radio("Select", ["Tasks", "Plant ID & Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("Berry Springs")
            st.image(f"berry_springs.png", caption="Berry Springs", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Plant ID & Treatment":
            vegetation = None
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.image("filamentous_algae.png", use_container_width=True)
                if st.button("Filamentous Algae"):
                    vegetation = "Filamentous Algae"
            with col2:
                st.image("bushy_pondweed.png", use_container_width=True)
                if st.button("Bushy Pondweed"):
                    vegetation = "Bushy Pondweed"
            with col3:
                st.image("cat_tail.png", use_container_width=True)
                if st.button("Cattail"):
                    vegetation = "Cattail"
            with col4:
                st.image("arrow_head.png", use_container_width=True)
                if st.button("Arrowhead"):
                    vegetation = "Arrowhead"
            # Row 2
            col5, col6, col7, col8 = st.columns(4)
            with col5:
                st.image("prim_rose_plant.png", use_container_width=True)
                if st.button("Primrose"):
                    vegetation = "Primrose"
            with col6:
                st.image("lily.png", use_container_width=True)
                if st.button("Lily"):
                    vegetation = "Lily"
            with col7:
                st.image("alligator_weed.png", use_container_width=True)
                if st.button("Alligator Weed"):
                    vegetation = "Alligator Weed"
            with col8:
                st.image("american_weed.png", use_container_width=True)
                if st.button("American Pondweed"):
                    vegetation = "American Pondweed"

            if vegetation == "Filamentous Algae":
                st.markdown("### Treatment")
                st.write("Argos - Spray")
            elif vegetation == "Bushy Pondweed":
                st.markdown("### Treatment")
                st.write("Current - Spray")
            elif vegetation == "Cattail":
                st.markdown("### Treatment")
                st.write("Aquaneat - Spray")
            elif vegetation == "Arrowhead":
                st.markdown("### Treatment")
                st.write("Aquaneat - Spray")
            elif vegetation == "Primrose":
                st.markdown("### Treatment")
                st.write("Aquaneat - Spray")
            elif vegetation == "Lily":
                st.markdown("### Treatment")
                st.write("Aquaneat - Spray")
            elif vegetation == "Alligator Weed":
                st.markdown("### Treatment")
                st.write("Aquamaster - Spray")
            elif vegetation == "American Pondweed":
                st.markdown("### Treatment")
                st.write("Aquathol K Liquid - Spray or Aquathol K Granular - Broadcast")

            st.write("### Algae Control Treatment")
            st.write("50 lbs (whole bag) copper sulfate")



            #st.markdown("### Treatment")
            #st.checkbox("100 lbs copper sulfate (broadcast)") #Filamentous Algae control
            #st.checkbox("2 jugs of argos (spray)") #Filamentous Algae when bloom
            #vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #if vegetation == "Filamentous Algae":
            #    st.image("filamentous_algae.png", use_container_width=True)
             #   st.markdown("### Treatment")
              #  st.write("Argos - Spray")
            #if vegetation == "Bushy Pondweed":
             #   st.image("bushy_pondweed.png", use_container_width=True)
              #  st.markdown("### Treatment")
               # st.write("Current - Spray")
            #if vegetation == "Cattail":
             #   st.image("cat_tail.png", use_container_width=True)
              #  st.markdown("### Treatment")
               # st.write("Phase & Aquaneat - spray")
            #if vegetation == "Arrowhead":
             #   st.image("arrow_head.png", use_container_width=True)
             #   st.markdown("### Treatment")
              #  st.write("Phase & Aquaneat - spray")
            #if vegetation == "Primrose":
             #   st.image("prim_rose_plant.png", use_container_width=True)
              #  st.markdown("### Treatment")
               # st.write("Phase & Aquaneat - spray")
            #if vegetation == "Lily":
             #   st.image("lily.png", use_container_width=True)
              #  st.markdown("### Treatment")
               # st.write("Phase & Aquaneat - spray")
            #if vegetation == "Alligator Weed":
             #   st.image("alligator_weed.png", use_container_width=True)
              #  st.markdown("### Treatment")
               # st.write("Aquamaster - spray")
                # st.write("### Routine Treatment")
                # st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            #if vegetation == "American Pondweed":
             #   st.image("american_weed.png", use_container_width=True)
              #  st.markdown("### Treatment")
               # st.write("Aquathol K - spray")
            #st.write("### Algae Control Treatment")
            #st.write("50 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
        elif page == "Map":
            st.write("1136 Loganberry Dr, Georgetown, Texas 78626")
            m = folium.Map(location=[30.6647654, -97.6450196], zoom_start=12)
            folium.Marker(location=[30.6647654, -97.6450196], popup="Berry Springs",icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Starter = st.checkbox("Starter")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Fountain_Lens = st.checkbox("Fountain lens")
            Fountain_lights = st.checkbox("Fountain lights")
            Motor_nonOperational = st.checkbox("Motor nonoperational")
            Motor_removal = st.checkbox("Motor removal")
            Motor_Reinstalled = st.checkbox("Motor re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")
            Ending = st.checkbox("Ending")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Starter:
                report.append("Today we perform routine maintenance on the pond. An inspection was conducted to assess current conditions and maintenance needs. After the inspection,")
            if Mow:
                report.append(
                    "the pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain appear to be fully operational at this time including the lights, GFCI and the motor.")
            if Fountain_Removal:
                report.append(
                    "the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Fountain_lights:
                report.append(
                    "one of the fountain lights were replaced and tested to ensure proper illumination and operation.")
            if Fountain_Lens:
                report.append(
                    "the fountain light lens was replaced and the lighting system was tested to ensure porper operation.")
            if Chemical:
                report.append(
                    "the pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Motor_nonOperational:
                report.append(
                    "the pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
            if Motor_removal:
                report.append(
                    "the pump motor was found to be non-operational and was removed from site for further inspection.")
            if Motor_Reinstalled:
                report.append("the motor was reinstalled, tested, and is fully operational at this time.")
            if Pressure_wash:
                report.append(
                    "the waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("the well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("the water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("the water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("all visible trash/debris was collected and properly disposed of to maintain an accessible and a neat environment.")
            if Ending:
                report.append("The pond was left in good conditions at the time of departure.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Hidden Oaks":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("Hidden Oaks")
            st.image(f"hidden_oaks_1.png", caption="Hidden Oaks 1", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
            st.image(f"hidden_oaks_2.png", caption="Hidden Oaks 2", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat", key = "treat_1")
            st.checkbox("Pick up trash", key = "trash_1")
            st.checkbox("Take a picture")
            st.checkbox("Do any specific task for today", key = "specific_task_1")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            st.image(f"hidden_oaks_1.png", caption="Hidden Oaks 1", use_container_width=True)
            vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 jug of argo (spray) - Filamentous Algae when bloom")
                st.checkbox("1 pound and half (1 cup adn a half) of Aquathol K - spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
            # st.write("### Routine Treatment")
            # st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 and a half pound (1 cup and half) of Aquathol K")
            st.write("### Algae Control Treatment")
            st.write("50 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            st.image(f"hidden_oaks_2.png", caption="Hidden Oaks 2", use_container_width=True)
            vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"], key = "vegetation_1")
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 jug of argo (spray) - Filamentous Algae when bloom")
                st.checkbox("1 pound and half (1 cup adn a half) of Aquathol K - spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
            # st.write("### Routine Treatment")
            # st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 and a half pound (1 cup and half) of Aquathol K")
        elif page == "Map":
            st.subheader("Hidden Oaks 1")
            st.write("234 Sun Daisy Rd, Georgetown, Tx 78626")
            m = folium.Map(location=[30.5939999, -97.6645092], zoom_start=12)
            folium.Marker(location=[30.5939999, -97.6645092], popup="Hidden Oaks 1",icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
            st.subheader("Hidden Oaks 2")
            st.write("302 Georgia Lace Trail, Georgetown, Tx 78626")
            m = folium.Map(location=[30.5935153, -97.6615795], zoom_start=12)
            folium.Marker(location=[30.5935153, -97.6615795], popup="Hidden Oaks 2", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Starter = st.checkbox("Starter")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Fountain_Lens = st.checkbox("Fountain lens")
            Fountain_lights = st.checkbox("Fountain lights")
            Motor_nonOperational = st.checkbox("Motor nonoperational")
            Motor_removal = st.checkbox("Motor removal")
            Motor_Reinstalled = st.checkbox("Motor re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")
            Ending = st.checkbox("Ending")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Starter:
                report.append("Today we perform routine maintenance on both ponds. An inspection was conducted to assess current conditions and maintenance needs. After the inspection,")
            if Mow:
                report.append(
                    "The pond basin and surrounding areas in Hidden Oaks 2 was mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Fountain_lights:
                report.append(
                    "One of the fountain lights were replaced and tested to ensure proper illumination and operation.")
            if Fountain_Lens:
                report.append(
                    "The fountain light lens was replaced and the lighting system was tested to ensure porper operation.")
            if Chemical:
                report.append(
                    "Hidden Oaks pond 1 was treated with chemical to control -plant species- growth and support overall water quality.")
            if Motor_nonOperational:
                report.append(
                    "The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
            if Motor_removal:
                report.append(
                    "The pump motor was found to be non-operational and was removed from site for further inspection.")
            if Motor_Reinstalled:
                report.append("The motor was reinstalled, tested, and is fully operational at this time.")
            if Pressure_wash:
                report.append(
                    "The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level in [X] is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level in [X] is [X] inches above from its optimal level.")
            if Trash:
                report.append("All visible trash/debris was collected and properly disposed of to improve site appearance.")
            if Ending:
                report.append("Both ponds were left in good conditions at the time of departure.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "San Gabriel":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("San Gabriel")
            st.image(f"san_gabriel.png", caption="San Gabriel", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            # st.markdown("### Treatment")
            # st.checkbox("100 lbs copper sulfate (broadcast)") #Filamentous Algae control
            # st.checkbox("2 jugs of argos (spray)") #Filamentous Algae when bloom
            vegetation = st.selectbox("Choose vegetation type:",
                                      ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead",
                                       "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Argos - Spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Aquamaster - spray")
                # st.write("### Routine Treatment")
                # st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Aquathol K - spray")
            st.write("### Algae Control Treatment")
            st.write("50 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
        elif page == "Map":
            st.write("Red Berry Pass, Georgetown, Texas 78628")
            m = folium.Map(location=[30.6239602, -97.7695834], zoom_start=12)
            folium.Marker(location=[30.6239602, -97.7695834], popup="San Gabriel", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Starter = st.checkbox("Starter")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Fountain_Lens = st.checkbox("Fountain lens")
            Fountain_lights = st.checkbox("Fountain lights")
            Motor_nonOperational = st.checkbox("Motor nonoperational")
            Motor_removal = st.checkbox("Motor removal")
            Motor_Reinstalled = st.checkbox("Motor re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")
            Ending = st.checkbox("Ending")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Starter:
                report.append("Today we perform routine maintenance on the pond. An inspection was conducted to assess current conditions and maintenance needs. After the inspection,")
            if Mow:
                report.append(
                    "the pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append(
                    "The fountain appear to be fully operational at this time including the lights, GFCI and the motor.")
            if Fountain_Removal:
                report.append(
                    "the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Fountain_lights:
                report.append(
                    "one of the fountain lights were replaced and tested to ensure proper illumination and operation.")
            if Fountain_Lens:
                report.append(
                    "the fountain light lens was replaced and the lighting system was tested to ensure porper operation.")
            if Chemical:
                report.append(
                    "the pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Motor_nonOperational:
                report.append(
                    "the pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
            if Motor_removal:
                report.append(
                    "the pump motor was found to be non-operational and was removed from site for further inspection.")
            if Motor_Reinstalled:
                report.append("the motor was reinstalled, tested, and is fully operational at this time.")
            if Pressure_wash:
                report.append(
                    "the waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("the well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("the water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("the water level is [X] inches above from its optimal level.")
            if Trash:
                report.append(
                    "all visible trash/debris was collected and properly disposed of to maintain an accessible and a neat environment.")
            if Ending:
                report.append("The pond was left in good conditions at the time of departure.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Camden Shadow Brooke":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("Camden Shadow Brooke")
            st.image(f"cammden.png", caption="Camden Shadow Brooke", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Fountain Inspection")
            st.checkbox("Treat")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            # st.markdown("### Treatment")
            # st.checkbox("100 lbs copper sulfate (broadcast)") #Filamentous Algae control
            # st.checkbox("2 jugs of argos (spray)") #Filamentous Algae when bloom
            vegetation = st.selectbox("Choose vegetation type:",
                                      ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead",
                                       "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Argos - Spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Aquamaster - spray")
                # st.write("### Routine Treatment")
                # st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Aquathol K - spray")
            st.write("### Algae Control Treatment")
            st.write("30 lbs. Cutrine Plus")
        elif page == "Map":
            st.write("Camden Shadow Brook Apartments, Austin, Texas 78748")
            m = folium.Map(location=[30.1724075, -97.8035975], zoom_start=12)
            folium.Marker(location=[30.1724075, -97.8035975], popup="Camden Shadow Brooke", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Starter = st.checkbox("Starter")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Fountain_Lens = st.checkbox("Fountain lens")
            Fountain_lights = st.checkbox("Fountain lights")
            Motor_nonOperational = st.checkbox("Motor nonoperational")
            Motor_removal = st.checkbox("Motor removal")
            Motor_Reinstalled = st.checkbox("Motor re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")
            Ending = st.checkbox("Ending")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Starter:
                report.append("Today we perform routine maintenance on the pond. An inspection was conducted to assess current conditions and maintenance needs. After the inspection,")
            if Mow:
                report.append(
                    "the pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append(
                    "The fountain appear to be fully operational at this time including the lights, GFCI and the motor.")
            if Fountain_Removal:
                report.append(
                    "the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Fountain_lights:
                report.append(
                    "one of the fountain lights were replaced and tested to ensure proper illumination and operation.")
            if Fountain_Lens:
                report.append(
                    "the fountain light lens was replaced and the lighting system was tested to ensure porper operation.")
            if Chemical:
                report.append(
                    "the pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Motor_nonOperational:
                report.append(
                    "the pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
            if Motor_removal:
                report.append(
                    "the pump motor was found to be non-operational and was removed from site for further inspection.")
            if Motor_Reinstalled:
                report.append("the motor was reinstalled, tested, and is fully operational at this time.")
            if Pressure_wash:
                report.append(
                    "the waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("the well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("the water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("the water level is [X] inches above from its optimal level.")
            if Trash:
                report.append(
                    "all visible trash/debris was collected and properly disposed of to maintain an accessible and a neat environment.")
            if Ending:
                report.append("The pond was left in good conditions at the time of departure.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Easton Park":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("Easton Park")
            st.image(f"easton_park.png", caption="Falcon Pointe", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Fountain inspection and testing")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 jug of argo (spray) - Filamentous Algae when bloom")
                st.checkbox("1 pound and half (1 cup adn a half) of Aquathol K - spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
            # st.write("### Routine Treatment")
            # st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 and a half pound (1 cup and half) of Aquathol K")
            st.write("### Algae Control Treatment")
            st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
        elif page == "Map":
            m = folium.Map(location=[30.157468, -97.717157], zoom_start=12)
            folium.Marker(location=[30.157468, -97.717157], popup="Easton Park",icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Fountain_Lens = st.checkbox("Fountain lens")
            Fountain_lights = st.checkbox("Fountain lights")
            Motor_nonOperational = st.checkbox("Motor nonoperational")
            Motor_removal = st.checkbox("Motor removal")
            Motor_Reinstalled = st.checkbox("Motor re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Mow:
                report.append(
                    "The pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Fountain_lights:
                report.append(
                    "One of the fountain lights were replaced and tested to ensure proper illumination and operation.")
            if Fountain_Lens:
                report.append(
                    "The fountain light lens was replaced and the lighting system was tested to ensure porper operation.")
            if Chemical:
                report.append(
                    "The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Motor_nonOperational:
                report.append(
                    "The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
            if Motor_removal:
                report.append(
                    "The pump motor was found to be non-operational and was removed from site for further inspection.")
            if Motor_Reinstalled:
                report.append("The motor was reinstalled, tested, and is fully operational at this time.")
            if Pressure_wash:
                report.append(
                    "The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash was collected and properly disposed of to improve site appearance.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Wilder":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("Blanco Vista")
            st.image(f"wilder.png", caption="Wilder", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:",
                                      ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead",
                                       "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 jug of argo (spray) - Filamentous Algae when bloom")
                st.checkbox("1 pound and half (1 cup adn a half) of Aquathol K - spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
            #st.write("### Routine Treatment")
            #st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 and a half pound (1 cup and half) of Aquathol K")
            st.write("### Algae Control Treatment")
            st.write("50 lbs of copper sulfate (broadcast using boat) to control filamentous algae")
        elif page == "Map":
            st.write("Near 10530 Waterfowl, Adkins, TX 78101")
            m = folium.Map(location=[29.4339995, -98.2781728], zoom_start=12)
            folium.Marker(location=[29.4339995, -98.2781728], popup="Wilder",icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Starter = st.checkbox("Starter")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Fountain_Lens = st.checkbox("Fountain lens")
            Fountain_lights = st.checkbox("Fountain lights")
            Motor_nonOperational = st.checkbox("Motor nonoperational")
            Motor_removal = st.checkbox("Motor removal")
            Motor_Reinstalled = st.checkbox("Motor re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")
            Ending = st.checkbox("Ending")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Starter:
                report.append(
                    "Today we perform routine maintenance on the pond. An inspection was conducted to assess current conditions and maintenance needs. After the inspection,")
            if Mow:
                report.append(
                    "the pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append(
                    "The fountain appear to be fully operational at this time including the lights, GFCI and the motor.")
            if Fountain_Removal:
                report.append(
                    "the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Fountain_lights:
                report.append(
                    "one of the fountain lights were replaced and tested to ensure proper illumination and operation.")
            if Fountain_Lens:
                report.append(
                    "the fountain light lens was replaced and the lighting system was tested to ensure porper operation.")
            if Chemical:
                report.append(
                    "the pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Motor_nonOperational:
                report.append(
                    "the pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
            if Motor_removal:
                report.append(
                    "the pump motor was found to be non-operational and was removed from site for further inspection.")
            if Motor_Reinstalled:
                report.append("the motor was reinstalled, tested, and is fully operational at this time.")
            if Pressure_wash:
                report.append(
                    "the waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("the well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("the water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("the water level is [X] inches above from its optimal level.")
            if Trash:
                report.append(
                    "all visible trash/debris was collected and properly disposed of to maintain an accessible and a neat environment.")
            if Ending:
                report.append("The pond was left in good conditions at the time of departure.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Blanco Vista":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("Blanco Vista")
            st.image(f"blanco_vista.png", caption="Blanco Vista", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Fountain inspection and testing")
            st.checkbox("Check for Well Reading")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:",
                                      ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead",
                                       "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 jug of argo (spray) - Filamentous Algae when bloom")
                st.checkbox("1 pound and half (1 cup adn a half) of Aquathol K - spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
            #st.write("### Routine Treatment")
            #st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 and a half pound (1 cup and half) of Aquathol K")
            st.write("### Algae Control Treatment")
            st.write("100 lbs of copper sulfate (broadcast using boat) to control filamentous algae")
        elif page == "Map":
            st.write("413 Lacey Oak Lp, San Marcos, TX")
            m = folium.Map(location=[29.940703, -97.894674], zoom_start=12)
            folium.Marker(location=[29.940703, -97.894674], popup="Blanco Vista",icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Starter = st.checkbox("Starter")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Fountain_Lens = st.checkbox("Fountain lens")
            Fountain_lights = st.checkbox("Fountain lights")
            Motor_nonOperational = st.checkbox("Motor nonoperational")
            Motor_removal = st.checkbox("Motor removal")
            Motor_Reinstalled = st.checkbox("Motor re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")
            Ending = st.checkbox("Ending")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Starter:
                report.append(
                    "Today we perform routine maintenance on the pond. An inspection was conducted to assess current conditions and maintenance needs. After the inspection,")
            if Mow:
                report.append(
                    "the pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append(
                    "The fountain appear to be fully operational at this time including the lights, GFCI and the motor.")
            if Fountain_Removal:
                report.append(
                    "the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Fountain_lights:
                report.append(
                    "one of the fountain lights were replaced and tested to ensure proper illumination and operation.")
            if Fountain_Lens:
                report.append(
                    "the fountain light lens was replaced and the lighting system was tested to ensure porper operation.")
            if Chemical:
                report.append(
                    "the pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Motor_nonOperational:
                report.append(
                    "the pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
            if Motor_removal:
                report.append(
                    "the pump motor was found to be non-operational and was removed from site for further inspection.")
            if Motor_Reinstalled:
                report.append("the motor was reinstalled, tested, and is fully operational at this time.")
            if Pressure_wash:
                report.append(
                    "the waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("the well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("the water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("the water level is [X] inches above from its optimal level.")
            if Trash:
                report.append(
                    "all visible trash/debris was collected and properly disposed of to maintain an accessible and a neat environment.")
            if Ending:
                report.append("The pond was left in good conditions at the time of departure.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Rosenbusch":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.header("Rosenbusch")
            st.subheader("Pond 1")
            st.image(f"rosenbusch_1.png", caption="Rosenbusch", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Well Reading")
            st.checkbox("Treat", key="treat_1")
            st.checkbox("Pick up trash", key="pickup_trash_1")
            st.checkbox("Do any specific task for today", key="specific_task_1")
        if page == "Tasks":
            st.subheader("Pond 2")
            st.image(f"rosenbusch_2.png", caption="Rosenbusch 2", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat", key="treat_2")
            st.checkbox("Pick up trash", key="pickup_trash_2")
            st.checkbox("Do any specific task for today", key="specific_task_2")
        if page == "Tasks":
            st.subheader("Pond 3")
            st.image(f"rosenbusch_3.png", caption="Rosenbusch 3", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Pick up trash", key="pickup_trash_3")
            st.checkbox("Mow", key="mow_3")
            st.checkbox("Do any specific task for today", key="specific_task_3")
        if page == "Tasks":
            st.subheader("Pond 4")
            st.image(f"rosenbusch_4.png", caption="Alta Vista 4", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Pick up trash", key="pickup_trash_4")
            st.checkbox("Mow", key="mow_4")
            st.checkbox("Do any specific task for today", key="specific_task_4")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:",
                                      ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead",
                                       "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Argo - Spray")
                st.checkbox("Aquathol K - spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
            # st.write("### Routine Treatment")
            # st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquathol K")
        elif page == "Map":
            st.subheader("Pond 1")
            st.write("2090 Vis Rdg, Leander, TX 78641")
            m = folium.Map(location=[30.5627719, -97.8817885], zoom_start=12)
            folium.Marker(location=[30.5627719, -97.8817885], popup="Rosenbusch 1", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
            st.subheader("Pond 2")
            st.write("2090 Vis Rdg, Leander, TX 78641")
            m = folium.Map(location=[30.5630797, -97.8809534], zoom_start=12)
            folium.Marker(location=[30.5630797, -97.8809534], popup="Rosenbusch 2", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
            st.subheader("Pond 3")
            st.write("324 Wildhorse St, Leander, TX 78641")
            m = folium.Map(location=[30.5653202, -97.8824826], zoom_start=12)
            folium.Marker(location=[30.5653202, -97.8824826], popup="Rosenbusch 3", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
            st.subheader("Pond 4")
            st.write("Near 332-320, Eagle Cyn Dr, Leander, TX 78641")
            m = folium.Map(location=[30.5665506, -97.8785001], zoom_start=12)
            folium.Marker(location=[30.5665506, -97.8785001], popup="Rosenbusch 4", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            #sump_clean = st.checkbox("Sump Cleaning")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")

            report = []

            #if sump_clean:
                #report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Mow:
                report.append("The pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append("Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append("Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Chemical:
                report.append("The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Pressure_wash:
                report.append("The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash was collected and properly disposed of to improve site appearance.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Hawkes Landing":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.header("Hawkes Landing")
            st.subheader("Pond 1")
            st.image(f"hawkes_1.png", caption="Hawkes Landing", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Fountain inspection")
            st.checkbox("Treat", key="treat_1")
            st.checkbox("Pick up trash", key="pickup_trash_1")
            st.checkbox("Do any specific task for today", key="specific_task_1")
        if page == "Tasks":
            st.subheader("Pond 4")
            st.image(f"hawkes_4.png", use_container_width=True)
            st.image(f"hawkes_44.png", caption="Hawkes Landing 4", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Mow")
            st.checkbox("Treat", key="treat_2")
            st.checkbox("Pick up trash", key="pickup_trash_2")
            st.checkbox("Do any specific task for today", key="specific_task_2")
        if page == "Tasks":
            st.subheader("Pond 5")
            st.image(f"hawkes_5.png", use_container_width=True)
            st.image(f"hawkes_55.png", caption="Hawkes Landing 5", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Pick up trash", key="pickup_trash_3")
            st.checkbox("Mow", key="mow_3")
            st.checkbox("Do any specific task for today", key="specific_task_3")
        if page == "Tasks":
            st.subheader("Pond 6")
            st.image(f"hawkes_6.png", caption="Hawkes Landing 6", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Pick up trash", key="pickup_trash_4")
            st.checkbox("Mow", key="mow_4")
            st.checkbox("Do any specific task for today", key="specific_task_4")
        if page == "Tasks":
            st.subheader("Pond 7")
            st.image(f"hawkes_7.png", caption="Hawkes Landing 7", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Pick up trash", key="pickup_trash_5")
            st.checkbox("Mow", key="mow_5")
            st.checkbox("Do any specific task for today", key="specific_task_5")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:",
                                      ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead",
                                       "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Argo - Spray")
                st.checkbox("Aquathol K - spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
            # st.write("### Routine Treatment")
            # st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquathol K")
        elif page == "Map":
            st.subheader("Pond 1")
            st.write("298 Sebastians Run, Lakeway, TX 78738")
            m = folium.Map(location=[30.3381135, -97.9602324], zoom_start=12)
            folium.Marker(location=[30.3381135, -97.9602324], popup="Alta Vista 1", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
            st.subheader("Pond 2")
            st.write("102 Lakota Pass, Lakeway, TX 78738")
            m = folium.Map(location=[30.3383132, -97.9555818], zoom_start=12)
            folium.Marker(location=[30.3383132, -97.9555818], popup="Alta Vista 2", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
            st.subheader("Pond 3")
            st.write("116 Burgess Cove, Lakeway, TX 78738")
            m = folium.Map(location=[30.3354030, -97.9550993], zoom_start=12)
            folium.Marker(location=[30.3354030, -97.9550993], popup="Alta Vista 3", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
            st.subheader("Pond 4")
            st.write("199 Vailco Ln, Lakeway, TX 78738")
            m = folium.Map(location=[30.3359224, -97.9505711], zoom_start=12)
            folium.Marker(location=[30.3359224, -97.9505711], popup="Alta Vista 4", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            #sump_clean = st.checkbox("Sump Cleaning")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")

            report = []

            #if sump_clean:
                #report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Mow:
                report.append("The pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append("Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append("Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Chemical:
                report.append("The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Pressure_wash:
                report.append("The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash was collected and properly disposed of to improve site appearance.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Lakeside Crossing":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("Lakeside Crossing")
            st.image(f"lakeside_crossing.png", caption="Lakeside Crossing", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Fountain inspection and testing")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 jug of argo (spray) - Filamentous Algae when bloom")
                st.checkbox("1 pound and half (1 cup adn a half) of Aquathol K - spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
            #st.write("### Routine Treatment")
            #st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 and a half pound (1 cup and half) of Aquathol K")
            st.write("### Algae Control Treatment")
            st.write("50 lbs of copper sulfate")
        elif page == "Map":
            st.write("229 Fountain Grove Dr, Kyle, TX")
            m = folium.Map(location=[30.016148, -97.844254], zoom_start=12)
            folium.Marker(location=[30.016148, -97.844254], popup="Lakeside Crossing",icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Fountain_Lens = st.checkbox("Fountain lens")
            Fountain_lights = st.checkbox("Fountain lights")
            Motor_nonOperational = st.checkbox("Motor nonoperational")
            Motor_removal = st.checkbox("Motor removal")
            Motor_Reinstalled = st.checkbox("Motor re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Mow:
                report.append(
                    "The pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Fountain_lights:
                report.append(
                    "One of the fountain lights were replaced and tested to ensure proper illumination and operation.")
            if Fountain_Lens:
                report.append(
                    "The fountain light lens was replaced and the lighting system was tested to ensure porper operation.")
            if Chemical:
                report.append(
                    "The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Motor_nonOperational:
                report.append(
                    "The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
            if Motor_removal:
                report.append(
                    "The pump motor was found to be non-operational and was removed from site for further inspection.")
            if Motor_Reinstalled:
                report.append("The motor was reinstalled, tested, and is fully operational at this time.")
            if Pressure_wash:
                report.append(
                    "The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash was collected and properly disposed of to improve site appearance.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Valley Ranch":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("Valley Ranch")
            st.image(f"valley_ranch.png", caption="Valley Ranch", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Fountain inspection and testing")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 jug of argo (spray) - Filamentous Algae when bloom")
                st.checkbox("1 pound and half (1 cup adn a half) of Aquathol K - spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
            #st.write("### Routine Treatment")
            #st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 and a half pound (1 cup and half) of Aquathol K")
            st.write("### Algae Control Treatment")
            st.write("50 lbs of copper sulfate")
        elif page == "Map":
            st.write("13639 Valley Lk, San Antonio, TX")
            m = folium.Map(location=[29.519325, -98.765837], zoom_start=12)
            folium.Marker(location=[29.519325, -98.765837], popup="Park near the entrance, next to trash container",icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Fountain_Lens = st.checkbox("Fountain lens")
            Fountain_lights = st.checkbox("Fountain lights")
            Motor_nonOperational = st.checkbox("Motor nonoperational")
            Motor_removal = st.checkbox("Motor removal")
            Motor_Reinstalled = st.checkbox("Motor re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Mow:
                report.append("The pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append("Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append("Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Fountain_lights:
                report.append("One of the fountain lights were replaced and tested to ensure proper illumination and operation.")
            if Fountain_Lens:
                report.append("The fountain light lens was replaced and the lighting system was tested to ensure porper operation.")
            if Chemical:
                report.append("The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Motor_nonOperational:
                report.append("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
            if Motor_removal:
                report.append("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if Motor_Reinstalled:
                report.append("The motor was reinstalled, tested, and is fully operational at this time.")
            if Pressure_wash:
                report.append("The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash was collected and properly disposed of to improve site appearance.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Red Bird Ranch":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
                st.subheader("Red Bird Ranch")
                st.image(f"red_bird_ranch.png", caption="Red Bird Ranch", use_container_width=True)
                st.markdown("### Tasks")
                st.checkbox("Treat")
                st.checkbox("Pick up trash")
                st.checkbox("Do any specific task for today")
        elif page == "Treatment":
                    # st.markdown("### Treatment")
                    # st.checkbox("100 lbs copper sulfate (broadcast)") #Filamentous Algae control
                    # st.checkbox("2 jugs of argos (spray)") #Filamentous Algae when bloom
                vegetation = st.selectbox("Choose vegetation type:",
                                              ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead",
                                               "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
                if vegetation == "Filamentous Algae":
                    st.image("filamentous_algae.png", use_container_width=True)
                    st.markdown("### Treatment")
                    st.write("Argos - Spray")
                if vegetation == "Bushy Pondweed":
                    st.image("bushy_pondweed.png", use_container_width=True)
                    st.markdown("### Treatment")
                    st.write("Current - Spray")
                if vegetation == "Cattail":
                    st.image("cat_tail.png", use_container_width=True)
                    st.markdown("### Treatment")
                    st.write("Phase & Aquaneat - spray")
                if vegetation == "Arrowhead":
                    st.image("arrow_head.png", use_container_width=True)
                    st.markdown("### Treatment")
                    st.write("Phase & Aquaneat - spray")
                if vegetation == "Primrose":
                    st.image("prim_rose_plant.png", use_container_width=True)
                    st.markdown("### Treatment")
                    st.write("Phase & Aquaneat - spray")
                if vegetation == "Lily":
                    st.image("lily.png", use_container_width=True)
                    st.markdown("### Treatment")
                    st.write("Phase & Aquaneat - spray")
                if vegetation == "Alligator Weed":
                    st.image("alligator_weed.png", use_container_width=True)
                    st.markdown("### Treatment")
                    st.write("Aquamaster - spray")
                        # st.write("### Routine Treatment")
                        # st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
                if vegetation == "American Pondweed":
                    st.image("american_weed.png", use_container_width=True)
                    st.markdown("### Treatment")
                    st.write("Aquathol K - spray")
                st.write("### Algae Control Treatment")
                st.write("150 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
        elif page == "Map":
                st.write("163 Garden Emerald, San Antonio, Texas 78253")
                m = folium.Map(location=[29.4387324, -98.8065347], zoom_start=12)
                folium.Marker(location=[29.4387324, -98.8065347], popup="Red Bird Ranch", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
                st_folium(m)
        elif page == "Report Generator":
                st.header("Test")

                    # sump_clean = st.checkbox("Sump Cleaning")
                Starter = st.checkbox("Starter")
                Mow = st.checkbox("Mow")
                Chemical = st.checkbox("Chemical")
                Fountain_Operational = st.checkbox("Fountain operational")
                Fountain_NonOperational = st.checkbox("Fountain non-operational")
                Fountain_Removal = st.checkbox("Fountain removal")
                Fountain_Reinstalled = st.checkbox("Fountain re-installed")
                Fountain_Lens = st.checkbox("Fountain lens")
                Fountain_lights = st.checkbox("Fountain lights")
                Motor_nonOperational = st.checkbox("Motor nonoperational")
                Motor_removal = st.checkbox("Motor removal")
                Motor_Reinstalled = st.checkbox("Motor re-installed")
                Well_reading = st.checkbox("Well reading")
                Pressure_wash = st.checkbox("Pressure wash")
                Trash = st.checkbox("Trash")
                Water_level_increase = st.checkbox("Water level increase")
                Water_level_decrease = st.checkbox("Water level decrease")
                Ending = st.checkbox("Ending")

                report = []

                    # if sump_clean:
                    # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

                if Starter:
                    report.append(
                            "Today we perform routine maintenance on the pond. An inspection was conducted to assess current conditions and maintenance needs. After the inspection,")
                if Mow:
                    report.append(
                            "the pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
                if Fountain_Operational:
                    report.append(
                            "The fountain appear to be fully operational at this time including the lights, GFCI and the motor.")
                if Fountain_Removal:
                    report.append(
                            "the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
                if Fountain_NonOperational:
                    report.append(
                            "the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
                if Fountain_Reinstalled:
                    report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
                if Fountain_lights:
                    report.append(
                            "one of the fountain lights were replaced and tested to ensure proper illumination and operation.")
                if Fountain_Lens:
                    report.append(
                            "the fountain light lens was replaced and the lighting system was tested to ensure porper operation.")
                if Chemical:
                    report.append(
                            "the pond was treated with chemical to control -plant species- growth and support overall water quality.")
                if Motor_nonOperational:
                    report.append(
                            "the pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
                if Motor_removal:
                    report.append(
                            "the pump motor was found to be non-operational and was removed from site for further inspection.")
                if Motor_Reinstalled:
                    report.append("the motor was reinstalled, tested, and is fully operational at this time.")
                if Pressure_wash:
                    report.append(
                            "the waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
                if Well_reading:
                    report.append("the well reading was inspected at -time-, with a measurement of ###.")
                if Water_level_increase:
                    report.append("the water level is [X] inches below from its optimal level.")
                if Water_level_decrease:
                    report.append("the water level is [X] inches above from its optimal level.")
                if Trash:
                    report.append(
                            "all visible trash/debris was collected and properly disposed of to maintain an accessible and a neat environment.")
                if Ending:
                    report.append("The pond was left in good conditions at the time of departure.")

                st.header("Generated Report")

                if report:
                    final_report = " ".join(report)
                    st.write(final_report)

    if site == "Hunters Pond":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("Hunters Pond")
            st.image(f"hunters_pond.png", caption="Hunters Pond", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 jug of argo (spray) - Filamentous Algae when bloom")
                st.checkbox("1 pound and half (1 cup adn a half) of Aquathol K - spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
            #st.write("### Routine Treatment")
            #st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 and a half pound (1 cup and half) of Aquathol K")
            st.write("### Algae Control Treatment")
            st.write("100 lbs of copper sulfate")
        elif page == "Map":
            st.write("9942 Hunters Pond, San Antonio, TX")
            m = folium.Map(location=[29.317733, -98.543061], zoom_start=12)
            folium.Marker(location=[29.317733, -98.543061], popup="Hunters Pond", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Mow:
                report.append(
                    "The pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Chemical:
                report.append(
                    "The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Pressure_wash:
                report.append(
                    "The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash was collected and properly disposed of to improve site appearance.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "DR Horton":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("DR Horton")
            st.image(f"drr_horton.png", caption="DR Horton", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Fountain inspection and testing")
            st.checkbox("Get Well Reading")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 jug of argo (spray) - Filamentous Algae when bloom")
                st.checkbox("1 pound and half (1 cup adn a half) of Aquathol K - spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
            #st.write("### Routine Treatment")
            #st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 and a half pound (1 cup and half) of Aquathol K")
            st.write("### Algae Control Treatment")
            st.write("50 lbs of copper sulfate")
        elif page == "Map":
            st.write("Near D.R. Horton San Antonio Division Office, San Antonio, TX")
            m = folium.Map(location=[29.603528, -98.382056], zoom_start=12)
            folium.Marker(location=[29.603528, -98.382056], popup="DR Horton", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")
            Trash = st.checkbox("Trash")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Mow:
                report.append(
                    "The pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Chemical:
                report.append(
                    "The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Pressure_wash:
                report.append(
                    "The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash was collected and properly disposed of to improve site appearance.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Rhine Valley":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("Rhine Valley")
            st.image(f"rhine_valley.png", caption="Rhine Valley", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Argo (spray) - Filamentous Algae when bloom")
                st.write("Aquathol K - broadcast")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Aquamaster - spray")
            #st.write("### Routine Treatment")
            #st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Aquathol K")
            st.write("### Algae Control Treatment")
            st.write("100 lbs of copper sulfate")
        elif page == "Map":
            st.write("9984 Sarrebourg Street, Schertz, TX")
            m = folium.Map(location=[29.5269856, -98.2348819], zoom_start=12)
            folium.Marker(location=[29.5269856, -98.2348819], popup="two sites", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Mow:
                report.append(
                    "The pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Chemical:
                report.append(
                    "The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Pressure_wash:
                report.append(
                    "The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash was collected and properly disposed of to improve site appearance.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)
    if site == "Whisper Falls":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("Whisper Falls 1")
            st.image(f"whisper_falls.png", caption="Whisper Falls 1", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat", key="treat_1")
            st.checkbox("Test Autofill", key="test_autofill_1")
            st.checkbox("Fountain inspection and testing", key="found_inspection_1")
            st.checkbox("Pick up trash", key="pick_up_trash_1")
            st.checkbox("Do any specific task for today", key="specific_task_1")
        if page == "Tasks":
            st.subheader("Whisper Falls 2")
            st.image(f"whisper_falls2.png", caption="Whisper Falls 2", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Test Autofill")
            st.checkbox("Fountain inspection and testing")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            st.subheader("Site 1")
            st.image(f"whisper_falls.png", caption="Whisper Falls", use_container_width=True)
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Argo (spray) - Filamentous Algae when bloom")
                st.write("Aquathol K - broadcast")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Aquamaster - spray")
            #st.write("### Routine Treatment")
            #st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Aquathol K")
            st.write("### Algae Control Treatment")
            st.write("30 lbs of Cutrine Plus")
            st.subheader("Site 2")
            st.image(f"whisper_falls2.png", caption="Whisper Falls", use_container_width=True)
            vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"], key="vegetation_select_1")
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Argo (spray) - Filamentous Algae when bloom")
                st.write("Aquathol K - broadcast")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Aquamaster - spray")
            # st.write("### Routine Treatment")
            # st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Aquathol K")
            st.write("### Algae Control Treatment")
            st.write("30 lbs of Cutrine Plus")
        elif page == "Map":
            st.write("13125 Tremolo Echo, San Antonio, TX")
            m = folium.Map(location=[29.372891, -98.753637], zoom_start=12)
            folium.Marker(location=[29.372891, -98.753637], popup="Whisper Falls", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Mow:
                report.append(
                    "The pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Chemical:
                report.append(
                    "The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Pressure_wash:
                report.append(
                    "The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash was collected and properly disposed of to improve site appearance.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)
    if site == "Sundance Crossing":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("Sundance Crossing")
            st.image(f"sundance_crossing1.png", caption="Sundance Crossing 1", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            st.subheader("Site 1")
            st.image(f"sundance_crossing1.png", caption="Sundance Crossing 1", use_container_width=True)
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentods Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Argo (spray) - Filamentous Algae when bloom")
                st.write("Aquathol K - broadcast")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Aquamaster - spray")
            #st.write("### Routine Treatment")
            #st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Aquathol K")
            st.write("### Algae Control Treatment")
            st.write("25 lbs of Copper Sulfate")
            st.subheader("Site 2")
            st.image(f"sundance_crossing2.png", caption="Sundance Crossing 2", use_container_width=True)
            vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"], key="vegetation_select_2")
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Argo (spray) - Filamentous Algae when bloom")
                st.write("Aquathol K - broadcast")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Aquamaster - spray")
            # st.write("### Routine Treatment")
            # st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Aquathol K")
            st.write("### Algae Control Treatment")
            st.write("25 lbs of Copper Sulfate")
            st.subheader("Site 3")
            st.image(f"sundance_crossing3.png", caption="Sundance Crossing 3", use_container_width=True)
        elif page == "Map":
            st.subheader("Site 1 and 2")
            st.write("12105 Western Mail Wy, Austin, TX")
            m = folium.Map(location=[30.1653377, -97.634716], zoom_start=12)
            folium.Marker(location=[30.1653377, -97.634716], popup="Sundance Crossing", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
            st.subheader("Site 3")
            st.write("6516 Albany Sleigh Dr, Austin, TX")
            m = folium.Map(location=[30.162739, -97.633859], zoom_start=12)
            folium.Marker(location=[30.162739, -97.633859], popup="Sundance Crossing", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Mow:
                report.append(
                    "The pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Chemical:
                report.append(
                    "The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Pressure_wash:
                report.append(
                    "The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash was collected and properly disposed of to improve site appearance.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Woods of Alon":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("Woods of Alon")
            st.image(f"woods_alon.png", caption="Woods of Alon", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Fountain Inspection")
            st.checkbox("Treat")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            # st.markdown("### Treatment")
            # st.checkbox("100 lbs copper sulfate (broadcast)") #Filamentous Algae control
            # st.checkbox("2 jugs of argos (spray)") #Filamentous Algae when bloom
            vegetation = st.selectbox("Choose vegetation type:",
                                      ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead",
                                       "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Argos - Spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Aquamaster - spray")
                # st.write("### Routine Treatment")
                # st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Aquathol K - spray")
            st.write("### Algae Control Treatment")
            st.write("60 lbs Cutrine Plus")
        elif page == "Map":
            st.write("2906 Zurich, San Antonio, Texas 78230")
            m = folium.Map(location=[29.549143, -98.534438], zoom_start=12)
            folium.Marker(location=[29.549143, -98.534438], popup="Woods of Alon", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Starter = st.checkbox("Starter")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Fountain_Lens = st.checkbox("Fountain lens")
            Fountain_lights = st.checkbox("Fountain lights")
            Motor_nonOperational = st.checkbox("Motor nonoperational")
            Motor_removal = st.checkbox("Motor removal")
            Motor_Reinstalled = st.checkbox("Motor re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")
            Ending = st.checkbox("Ending")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Starter:
                report.append(
                    "Today we perform routine maintenance on the pond. An inspection was conducted to assess current conditions and maintenance needs. After the inspection,")
            if Mow:
                report.append(
                    "the pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append(
                    "The fountain appear to be fully operational at this time including the lights, GFCI and the motor.")
            if Fountain_Removal:
                report.append(
                    "the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Fountain_lights:
                report.append(
                    "one of the fountain lights were replaced and tested to ensure proper illumination and operation.")
            if Fountain_Lens:
                report.append(
                    "the fountain light lens was replaced and the lighting system was tested to ensure porper operation.")
            if Chemical:
                report.append(
                    "the pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Motor_nonOperational:
                report.append(
                    "the pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
            if Motor_removal:
                report.append(
                    "the pump motor was found to be non-operational and was removed from site for further inspection.")
            if Motor_Reinstalled:
                report.append("the motor was reinstalled, tested, and is fully operational at this time.")
            if Pressure_wash:
                report.append(
                    "the waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("the well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("the water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("the water level is [X] inches above from its optimal level.")
            if Trash:
                report.append(
                    "all visible trash/debris was collected and properly disposed of to maintain an accessible and a neat environment.")
            if Ending:
                report.append("The pond was left in good conditions at the time of departure.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Cowboy Cabin":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("Cowboy Cabin")
            st.image(f"cowboy_cabin.png", caption="Cowboy Cabin", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Fountain inspection and testing:6018")
            #st.checkbox("Pick up trash")
            #st.checkbox("Do any specific task for today")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Argo (spray) - Filamentous Algae when bloom")
                st.write("Aquathol K - broadcast")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Aquamaster - spray")
            # st.write("### Routine Treatment")
            # st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.write("Aquathol K")
            st.write("### Algae Control Treatment")
            st.write("30 lbs of Cutrine Plus")
        elif page == "Map":
            st.write("10281 FM 20, Lockhart, TX")
            m = folium.Map(location=[29.786919, -97.734721], zoom_start=12)
            folium.Marker(location=[29.786919, -97.734721], popup="Cowboy Cabin", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Mow:
                report.append(
                    "The pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Chemical:
                report.append(
                    "The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Pressure_wash:
                report.append(
                    "The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash was collected and properly disposed of to improve site appearance.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "The Willows HOA":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("The Willows HOA")
            st.image(f"willows_hoa.png", caption="The Willows HOA", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Argo - Spray")
                st.checkbox("Aquathol K - spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
            #st.write("### Routine Treatment")
            #st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 and a half pound (1 cup and half) of Aquathol K")
            st.write("### Algae Control Treatment")
            st.write("100 lbs of copper sulfate")
        elif page == "Map":
            st.write("4985 Lakeshore Dr, Killeen, TX")
            m = folium.Map(location=[31.086025, -97.680181], zoom_start=12)
            folium.Marker(location=[31.086025, -97.680181], popup="The Willows HOA", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Mow:
                report.append(
                    "The pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Chemical:
                report.append(
                    "The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Pressure_wash:
                report.append(
                    "The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash was collected and properly disposed of to improve site appearance.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "River Bend":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("River Bend")
            st.image(f"river_bend.png", caption="River Bend", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Argo - Spray")
                st.checkbox("Aquathol K - spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
            #st.write("### Routine Treatment")
            #st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquathol K")
            st.write("### Algae Control Treatment")
            st.write("30 lbs of Cutrine Plus")
        elif page == "Map":
            st.write("105 Whitewing Way, Floresville, TX")
            m = folium.Map(location=[29.156680, -98.182802], zoom_start=12)
            folium.Marker(location=[29.156680, -98.182802], popup="River Bend", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Mow:
                report.append(
                    "The pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Chemical:
                report.append(
                    "The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Pressure_wash:
                report.append(
                    "The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash was collected and properly disposed of to improve site appearance.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Preserve":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("Preserve")
            st.image(f"preserve.png", caption="Preserve", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Clean pump strainers - 3030 lock code")
            st.checkbox("Treat")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:",
                                      ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead",
                                       "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Argo - Spray")
                st.checkbox("Aquathol K - spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
            # st.write("### Routine Treatment")
            # st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquathol K")
        elif page == "Map":
            st.write("Near New Braunfels, TX 78132")
            m = folium.Map(location=[29.7099256, -98.1997875], zoom_start=12)
            folium.Marker(location=[29.7099256, -98.1997875], popup="Preserve", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Mow:
                report.append(
                    "The pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Chemical:
                report.append(
                    "The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Pressure_wash:
                report.append(
                    "The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash was collected and properly disposed of to improve site appearance.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Wasser Ranch":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("Wasser Ranch")
            st.image(f"wasser_ranch.png", caption="Wasser Ranch", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Fountain inspection")
            st.checkbox("Pick up trash")
            st.checkbox("Well Reading")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 jug of argo (spray) - Filamentous Algae when bloom")
                st.checkbox("1 pound and half (1 cup adn a half) of Aquathol K - spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
            # st.write("### Routine Treatment")
            # st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 and a half pound (1 cup and half) of Aquathol K")
            st.write("### Algae Control Treatment")
            st.write("50 lbs. Copper Sulfate")
        elif page == "Map":
            st.subheader("Wasser Ranch")
            st.write("630 Pader, New Braunfels, Texas 78130")
            m = folium.Map(location=[29.7502488, -98.073824], zoom_start=12)
            folium.Marker(location=[29.7502488, -98.073824], popup="Wasser Ranch",icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Starter = st.checkbox("Starter")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Fountain_Lens = st.checkbox("Fountain lens")
            Fountain_lights = st.checkbox("Fountain lights")
            Motor_nonOperational = st.checkbox("Motor nonoperational")
            Motor_removal = st.checkbox("Motor removal")
            Motor_Reinstalled = st.checkbox("Motor re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")
            Ending = st.checkbox("Ending")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Starter:
                report.append("Today we perform routine maintenance on both ponds. An inspection was conducted to assess current conditions and maintenance needs. After the inspection,")
            if Mow:
                report.append(
                    "The pond basin and surrounding areas in Hidden Oaks 2 was mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Fountain_lights:
                report.append(
                    "One of the fountain lights were replaced and tested to ensure proper illumination and operation.")
            if Fountain_Lens:
                report.append(
                    "The fountain light lens was replaced and the lighting system was tested to ensure porper operation.")
            if Chemical:
                report.append(
                    "Hidden Oaks pond 1 was treated with chemical to control -plant species- growth and support overall water quality.")
            if Motor_nonOperational:
                report.append(
                    "The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
            if Motor_removal:
                report.append(
                    "The pump motor was found to be non-operational and was removed from site for further inspection.")
            if Motor_Reinstalled:
                report.append("The motor was reinstalled, tested, and is fully operational at this time.")
            if Pressure_wash:
                report.append(
                    "The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level in [X] is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level in [X] is [X] inches above from its optimal level.")
            if Trash:
                report.append("All visible trash/debris was collected and properly disposed of to improve site appearance.")
            if Ending:
                report.append("Both ponds were left in good conditions at the time of departure.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "The Reserve at Lake Travis":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("The Reserve at Lake Travis")
            st.image(f"lake_travis.png", caption="The Reserve at Lake Travis", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Fountain inspection")
            st.checkbox("Treat")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 jug of argo (spray) - Filamentous Algae when bloom")
                st.checkbox("1 pound and half (1 cup adn a half) of Aquathol K - spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
            # st.write("### Routine Treatment")
            # st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 and a half pound (1 cup and half) of Aquathol K")
            st.write("### Algae Control Treatment")
            st.write("30 lbs. Cutrine Plus")
        elif page == "Map":
            st.subheader("The Reserve at Lake Travis")
            st.write("The Reserve At Lake Travis, Briarcliff, TX 78669")
            m = folium.Map(location=[30.4086077, -97.9965388], zoom_start=12)
            folium.Marker(location=[30.4086077, -97.9965388], popup="The Reserve at Lake Travis",icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Starter = st.checkbox("Starter")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Fountain_Lens = st.checkbox("Fountain lens")
            Fountain_lights = st.checkbox("Fountain lights")
            Motor_nonOperational = st.checkbox("Motor nonoperational")
            Motor_removal = st.checkbox("Motor removal")
            Motor_Reinstalled = st.checkbox("Motor re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")
            Ending = st.checkbox("Ending")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Starter:
                report.append("Today we perform routine maintenance on both ponds. An inspection was conducted to assess current conditions and maintenance needs. After the inspection,")
            if Mow:
                report.append(
                    "The pond basin and surrounding areas in Hidden Oaks 2 was mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Fountain_lights:
                report.append(
                    "One of the fountain lights were replaced and tested to ensure proper illumination and operation.")
            if Fountain_Lens:
                report.append(
                    "The fountain light lens was replaced and the lighting system was tested to ensure porper operation.")
            if Chemical:
                report.append(
                    "Hidden Oaks pond 1 was treated with chemical to control -plant species- growth and support overall water quality.")
            if Motor_nonOperational:
                report.append(
                    "The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
            if Motor_removal:
                report.append(
                    "The pump motor was found to be non-operational and was removed from site for further inspection.")
            if Motor_Reinstalled:
                report.append("The motor was reinstalled, tested, and is fully operational at this time.")
            if Pressure_wash:
                report.append(
                    "The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level in [X] is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level in [X] is [X] inches above from its optimal level.")
            if Trash:
                report.append("All visible trash/debris was collected and properly disposed of to improve site appearance.")
            if Ending:
                report.append("Both ponds were left in good conditions at the time of departure.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Crystal Village":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("Crystal Village")
            st.image(f"crystal_village.png", caption="Crystal Village", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 jug of argo (spray) - Filamentous Algae when bloom")
                st.checkbox("1 pound and half (1 cup adn a half) of Aquathol K - spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
            # st.write("### Routine Treatment")
            # st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("1 and a half pound (1 cup and half) of Aquathol K")
            st.write("### Algae Control Treatment")
            st.write("30 lbs. Cutrine Plus")
        elif page == "Map":
            st.subheader("Crystal Village")
            st.write("Near 2051 Raider Way, Leander, Texas 78641")
            m = folium.Map(location=[30.5599216, -97.8209852], zoom_start=12)
            folium.Marker(location=[30.5599216, -97.8209852], popup="Crystal Village",icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Starter = st.checkbox("Starter")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Fountain_Lens = st.checkbox("Fountain lens")
            Fountain_lights = st.checkbox("Fountain lights")
            Motor_nonOperational = st.checkbox("Motor nonoperational")
            Motor_removal = st.checkbox("Motor removal")
            Motor_Reinstalled = st.checkbox("Motor re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")
            Ending = st.checkbox("Ending")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Starter:
                report.append("Today we perform routine maintenance on both ponds. An inspection was conducted to assess current conditions and maintenance needs. After the inspection,")
            if Mow:
                report.append(
                    "The pond basin and surrounding areas in Hidden Oaks 2 was mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Fountain_lights:
                report.append(
                    "One of the fountain lights were replaced and tested to ensure proper illumination and operation.")
            if Fountain_Lens:
                report.append(
                    "The fountain light lens was replaced and the lighting system was tested to ensure porper operation.")
            if Chemical:
                report.append(
                    "Hidden Oaks pond 1 was treated with chemical to control -plant species- growth and support overall water quality.")
            if Motor_nonOperational:
                report.append(
                    "The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
            if Motor_removal:
                report.append(
                    "The pump motor was found to be non-operational and was removed from site for further inspection.")
            if Motor_Reinstalled:
                report.append("The motor was reinstalled, tested, and is fully operational at this time.")
            if Pressure_wash:
                report.append(
                    "The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level in [X] is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level in [X] is [X] inches above from its optimal level.")
            if Trash:
                report.append("All visible trash/debris was collected and properly disposed of to improve site appearance.")
            if Ending:
                report.append("Both ponds were left in good conditions at the time of departure.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Green Lake":
        page = st.radio("Select", ["Tasks", "Treatment", "Map"], horizontal=True)

        m = folium.Map(location=[29.309109, -98.386129], zoom_start=12)
        folium.Marker(location=[29.309109, -98.386129], popup="Green Lake",icon=folium.Icon(color="green", icon="leaf")).add_to(m)
        st_folium(m)

    if site == "Willow's Creek":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("Willow's Creek")
            st.image(f"willow_creek.png", caption="Willow's Creek", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Argo - Spray")
                st.checkbox("Aquathol K - spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
            #st.write("### Routine Treatment")
            #st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquathol K")
            st.write("### Algae Control Treatment")
            st.write("30 lbs of Cutrine Plus")
        elif page == "Map":
            st.write("105 Whitewing Way, Floresville, TX")
            m = folium.Map(location=[29.860380, -97.972922], zoom_start=12)
            folium.Marker(location=[29.860380, -97.972922], popup="Willow Creek", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Mow:
                report.append(
                    "The pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Chemical:
                report.append(
                    "The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Pressure_wash:
                report.append(
                    "The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash was collected and properly disposed of to improve site appearance.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Versante":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.header("Versante")
            st.subheader("Pond 1")
            st.image(f"versante11.png", caption="Versante 1", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat", key="Treat_1")
            st.checkbox("Pick up trash", key="pickup_trash_1")
            st.checkbox("Mow", key="mow_1")
            st.checkbox("Do any specific task for today", key="specific_task_1")
        if page == "Tasks":
            st.subheader("Pond 2")
            st.image(f"versante2.png", caption="Versante 2", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Pick up trash", key="pickup_trash_2")
            st.checkbox("Mow", key="mow_2")
            st.checkbox("Do any specific task for today", key="specific_task_2")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:",
                                      ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead",
                                       "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Argo - Spray")
                st.checkbox("Aquathol K - spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
            # st.write("### Routine Treatment")
            # st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquathol K")
        elif page == "Map":
            st.subheader("Pond 1")
            st.write("9201 Villa Norte Dr, Austin, TX 78726")
            m = folium.Map(location=[30.4317645, -97.8443623], zoom_start=12)
            folium.Marker(location=[30.4317645, -97.8443623], popup="Versante 1", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
            st.subheader("Pond 2")
            st.write("Near 12000 Terraza Cir, Austin, TX 78726")
            m = folium.Map(location=[30.4290936, -97.8455958], zoom_start=12)
            folium.Marker(location=[30.4290936, -97.8455958], popup="Versante 2", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Mow:
                report.append(
                    "The pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Chemical:
                report.append(
                    "The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Pressure_wash:
                report.append(
                    "The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash was collected and properly disposed of to improve site appearance.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "South Grove Condominiums":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("South Grove Condominiums")
            st.image(f"south_grove.png", caption="South Grove Condominiums", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Mow")
            st.checkbox("Treat")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Argo - Spray")
                st.checkbox("Aquathol K - spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
            #st.write("### Routine Treatment")
            #st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquathol K")
        elif page == "Map":
            st.write("320 Promenade Ct, Austin, TX 78652")
            m = folium.Map(location=[30.1387111, -97.8047448], zoom_start=12)
            folium.Marker(location=[30.1387111, -97.8047448], popup="South Grove Condominiums", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Mow:
                report.append(
                    "The pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Chemical:
                report.append(
                    "The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Pressure_wash:
                report.append(
                    "The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash was collected and properly disposed of to improve site appearance.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Austin East Parke HOA":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("Austin East Parke HOA")
            st.image(f"austin_eastparke.png", caption="Austin East Parke HOA", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Mow")
            st.checkbox("Treat")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Argo - Spray")
                st.checkbox("Aquathol K - spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
            #st.write("### Routine Treatment")
            #st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquathol K")
        elif page == "Map":
            st.write("5504 Coolbrook Dr, Austin, TX 78724")
            m = folium.Map(location=[30.3058572, -97.6581587], zoom_start=12)
            folium.Marker(location=[30.3058572, -97.6581587], popup="Austin East Parke HOA", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Mow:
                report.append(
                    "The pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Chemical:
                report.append(
                    "The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Pressure_wash:
                report.append(
                    "The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash was collected and properly disposed of to improve site appearance.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Alta Vista":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.header("Alta Vista")
            st.subheader("Pond 1")
            st.image(f"alta_vista1.png", caption="Alta Vista 1", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Pick up trash", key="pickup_trash_1")
            st.checkbox("Mow", key="mow_1")
            st.checkbox("Do any specific task for today", key="specific_task_1")
        if page == "Tasks":
            st.subheader("Pond 2")
            st.image(f"alta_vista2.png", caption="Alta Vista 2", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Pick up trash", key="pickup_trash_2")
            st.checkbox("Mow", key="mow_2")
            st.checkbox("Do any specific task for today", key="specific_task_2")
        if page == "Tasks":
            st.subheader("Pond 3")
            st.image(f"alta_vista3.png", caption="Alta Vista 3", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Pick up trash", key="pickup_trash_3")
            st.checkbox("Mow", key="mow_3")
            st.checkbox("Do any specific task for today", key="specific_task_3")
        if page == "Tasks":
            st.subheader("Pond 4")
            st.image(f"alta_vista4.png", caption="Alta Vista 4", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Pick up trash", key="pickup_trash_4")
            st.checkbox("Mow", key="mow_4")
            st.checkbox("Do any specific task for today", key="specific_task_4")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:",
                                      ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead",
                                       "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Argo - Spray")
                st.checkbox("Aquathol K - spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
            # st.write("### Routine Treatment")
            # st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquathol K")
        elif page == "Map":
            st.subheader("Pond 1")
            st.write("298 Sebastians Run, Lakeway, TX 78738")
            m = folium.Map(location=[30.3381135, -97.9602324], zoom_start=12)
            folium.Marker(location=[30.3381135, -97.9602324], popup="Alta Vista 1", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
            st.subheader("Pond 2")
            st.write("102 Lakota Pass, Lakeway, TX 78738")
            m = folium.Map(location=[30.3383132, -97.9555818], zoom_start=12)
            folium.Marker(location=[30.3383132, -97.9555818], popup="Alta Vista 2", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
            st.subheader("Pond 3")
            st.write("116 Burgess Cove, Lakeway, TX 78738")
            m = folium.Map(location=[30.3354030, -97.9550993], zoom_start=12)
            folium.Marker(location=[30.3354030, -97.9550993], popup="Alta Vista 3", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
            st.subheader("Pond 4")
            st.write("199 Vailco Ln, Lakeway, TX 78738")
            m = folium.Map(location=[30.3359224, -97.9505711], zoom_start=12)
            folium.Marker(location=[30.3359224, -97.9505711], popup="Alta Vista 4", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            #sump_clean = st.checkbox("Sump Cleaning")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")

            report = []

            #if sump_clean:
                #report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Mow:
                report.append("The pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append("Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append("Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Chemical:
                report.append("The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Pressure_wash:
                report.append("The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash was collected and properly disposed of to improve site appearance.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Edgewick HOA":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.subheader("Edgewick HOA (3)")
            st.image(f"edgewick_hoa.png", caption="Edgewick HOA", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Mow")
            st.checkbox("Treat")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:", ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Argo - Spray")
                st.checkbox("Aquathol K - spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
            #st.write("### Routine Treatment")
            #st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquathol K")
        elif page == "Map":
            st.write("2633 Witsome Loop, Austin, TX 78741")
            m = folium.Map(location=[30.2273486, -97.7387500], zoom_start=12)
            folium.Marker(location=[30.2273486, -97.7387500], popup="Edgewick HOA", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            # sump_clean = st.checkbox("Sump Cleaning")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")

            report = []

            # if sump_clean:
            # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Mow:
                report.append(
                    "The pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append(
                    "Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Chemical:
                report.append(
                    "The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Pressure_wash:
                report.append(
                    "The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash was collected and properly disposed of to improve site appearance.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

    if site == "Hidden Oaks at Berry Springs":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
        if page == "Tasks":
            st.header("Hidden Oaks at Berry Springs")
            st.subheader("Site 1")
            st.image(f"hidden_springs_1.png", caption="Hidden Oaks at Berry Springs 1", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Pick up trash", key="pickup_trash_1")
            st.checkbox("Mow", key="mow_1")
            st.checkbox("Do any specific task for today", key="specific_task_1")
        if page == "Tasks":
            st.subheader("Site 2")
            st.image(f"hidden_springs_2.png", caption="Hidden Oaks at Berry Springs 2", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat", key="treat_2")
            st.checkbox("Pick up trash", key="pickup_trash_2")
            st.checkbox("Mow", key="mow_2")
            st.checkbox("Do any specific task for today", key="specific_task_2")
        if page == "Tasks":
            st.subheader("Site 3")
            st.image(f"hidden_springs_3.png", caption="Hidden Oaks at Berry Springs 3", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat", key="treat_3")
            st.checkbox("Pick up trash", key="pickup_trash_3")
            st.checkbox("Mow", key="mow_3")
            st.checkbox("Do any specific task for today", key="specific_task_3")
        elif page == "Treatment":
            #    st.write("### Routine Treatment")
            #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            vegetation = st.selectbox("Choose vegetation type:",
                                      ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead",
                                       "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
            #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
            if vegetation == "Filamentous Algae":
                st.image("filamentous_algae.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Argo - Spray")
                st.checkbox("Aquathol K - spray")
            if vegetation == "Bushy Pondweed":
                st.image("bushy_pondweed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Current - Spray")
            if vegetation == "Cattail":
                st.image("cat_tail.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Arrowhead":
                st.image("arrow_head.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Primrose":
                st.image("prim_rose_plant.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Lily":
                st.image("lily.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Phase & Aquaneat - spray")
            if vegetation == "Alligator Weed":
                st.image("alligator_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquamaster - spray")
            # st.write("### Routine Treatment")
            # st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
            if vegetation == "American Pondweed":
                st.image("american_weed.png", use_container_width=True)
                st.markdown("### Treatment")
                st.checkbox("Aquathol K")
        elif page == "Map":
            st.subheader("Site 1")
            st.write("116 Fairway Ln, Georgetown, TX 78628")
            m = folium.Map(location=[30.7163279, -97.6690273], zoom_start=12)
            folium.Marker(location=[30.7163279, -97.6690273], popup="Hidden Oaks at Berry Springs 1", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
            st.subheader("Site 2")
            st.write("217 Tovas Secret Cv, Georgetown, TX 78628")
            m = folium.Map(location=[30.7157857, -97.6700674], zoom_start=12)
            folium.Marker(location=[30.7157857, -97.6700674], popup="Hidden Oaks at Berry Springs 2", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
            st.subheader("Site 3")
            st.write("Near 109 Stately Oak Dr, Georgetown, TX 78628")
            m = folium.Map(location=[30.7164853, -97.6706776], zoom_start=12)
            folium.Marker(location=[30.7164853, -97.6706776], popup="Hidden Oaks at Berry Springs 3", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Generator":
            st.header("Test")

            #sump_clean = st.checkbox("Sump Cleaning")
            Mow = st.checkbox("Mow")
            Chemical = st.checkbox("Chemical")
            Fountain_Operational = st.checkbox("Fountain operational")
            Fountain_NonOperational = st.checkbox("Fountain non-operational")
            Fountain_Removal = st.checkbox("Fountain removal")
            Fountain_Reinstalled = st.checkbox("Fountain re-installed")
            Well_reading = st.checkbox("Well reading")
            Pressure_wash = st.checkbox("Pressure wash")
            Trash = st.checkbox("Trash")
            Water_level_increase = st.checkbox("Water level increase")
            Water_level_decrease = st.checkbox("Water level decrease")

            report = []

            #if sump_clean:
                #report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

            if Mow:
                report.append("The pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
            if Fountain_Operational:
                report.append("The fountain was inspected and tested and is currently fully operational.")
            if Fountain_Removal:
                report.append("Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
            if Fountain_NonOperational:
                report.append("Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if Fountain_Reinstalled:
                report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
            if Chemical:
                report.append("The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if Pressure_wash:
                report.append("The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
            if Well_reading:
                report.append("The well reading was inspected at -time-, with a measurement of ###.")
            if Water_level_increase:
                report.append("The water level is [X] inches below from its optimal level.")
            if Water_level_decrease:
                report.append("The water level is [X] inches above from its optimal level.")
            if Trash:
                report.append("Trash was collected and properly disposed of to improve site appearance.")

            st.header("Generated Report")

            if report:
                final_report = " ".join(report)
                st.write(final_report)

        if site == "Alta Vista":
            page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Generator"], horizontal=True)
            if page == "Tasks":
                st.header("Alta Vista")
                st.subheader("Pond 1")
                st.image(f"alta_vista1.png", caption="Alta Vista 1", use_container_width=True)
                st.markdown("### Tasks")
                st.checkbox("Treat")
                st.checkbox("Pick up trash", key="pickup_trash_1")
                st.checkbox("Mow", key="mow_1")
                st.checkbox("Do any specific task for today", key="specific_task_1")
            if page == "Tasks":
                st.subheader("Pond 2")
                st.image(f"alta_vista2.png", caption="Alta Vista 2", use_container_width=True)
                st.markdown("### Tasks")
                st.checkbox("Pick up trash", key="pickup_trash_2")
                st.checkbox("Mow", key="mow_2")
                st.checkbox("Do any specific task for today", key="specific_task_2")
            if page == "Tasks":
                st.subheader("Pond 3")
                st.image(f"alta_vista3.png", caption="Alta Vista 3", use_container_width=True)
                st.markdown("### Tasks")
                st.checkbox("Pick up trash", key="pickup_trash_3")
                st.checkbox("Mow", key="mow_3")
                st.checkbox("Do any specific task for today", key="specific_task_3")
            if page == "Tasks":
                st.subheader("Pond 4")
                st.image(f"alta_vista4.png", caption="Alta Vista 4", use_container_width=True)
                st.markdown("### Tasks")
                st.checkbox("Pick up trash", key="pickup_trash_4")
                st.checkbox("Mow", key="mow_4")
                st.checkbox("Do any specific task for today", key="specific_task_4")
            elif page == "Treatment":
                #    st.write("### Routine Treatment")
                #    st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
                vegetation = st.selectbox("Choose vegetation type:",
                                          ["Select", "Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead",
                                           "Primrose", "Lily", "Alligator Weed", "American Pondweed"])
                #         vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily", "American Pondweed"])
                if vegetation == "Filamentous Algae":
                    st.image("filamentous_algae.png", use_container_width=True)
                    st.markdown("### Treatment")
                    st.checkbox("Argo - Spray")
                    st.checkbox("Aquathol K - spray")
                if vegetation == "Bushy Pondweed":
                    st.image("bushy_pondweed.png", use_container_width=True)
                    st.markdown("### Treatment")
                    st.checkbox("Current - Spray")
                if vegetation == "Cattail":
                    st.image("cat_tail.png", use_container_width=True)
                    st.markdown("### Treatment")
                    st.checkbox("Phase & Aquaneat - spray")
                if vegetation == "Arrowhead":
                    st.image("arrow_head.png", use_container_width=True)
                    st.markdown("### Treatment")
                    st.checkbox("Phase & Aquaneat - spray")
                if vegetation == "Primrose":
                    st.image("prim_rose_plant.png", use_container_width=True)
                    st.markdown("### Treatment")
                    st.checkbox("Phase & Aquaneat - spray")
                if vegetation == "Lily":
                    st.image("lily.png", use_container_width=True)
                    st.markdown("### Treatment")
                    st.checkbox("Phase & Aquaneat - spray")
                if vegetation == "Alligator Weed":
                    st.image("alligator_weed.png", use_container_width=True)
                    st.markdown("### Treatment")
                    st.checkbox("Aquamaster - spray")
                # st.write("### Routine Treatment")
                # st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
                if vegetation == "American Pondweed":
                    st.image("american_weed.png", use_container_width=True)
                    st.markdown("### Treatment")
                    st.checkbox("Aquathol K")
            elif page == "Map":
                st.subheader("Pond 1")
                st.write("298 Sebastians Run, Lakeway, TX 78738")
                m = folium.Map(location=[30.3381135, -97.9602324], zoom_start=12)
                folium.Marker(location=[30.3381135, -97.9602324], popup="Alta Vista 1",
                              icon=folium.Icon(color="green", icon="leaf")).add_to(m)
                st_folium(m)
                st.subheader("Pond 2")
                st.write("102 Lakota Pass, Lakeway, TX 78738")
                m = folium.Map(location=[30.3383132, -97.9555818], zoom_start=12)
                folium.Marker(location=[30.3383132, -97.9555818], popup="Alta Vista 2",
                              icon=folium.Icon(color="green", icon="leaf")).add_to(m)
                st_folium(m)
                st.subheader("Pond 3")
                st.write("116 Burgess Cove, Lakeway, TX 78738")
                m = folium.Map(location=[30.3354030, -97.9550993], zoom_start=12)
                folium.Marker(location=[30.3354030, -97.9550993], popup="Alta Vista 3",
                              icon=folium.Icon(color="green", icon="leaf")).add_to(m)
                st_folium(m)
                st.subheader("Pond 4")
                st.write("199 Vailco Ln, Lakeway, TX 78738")
                m = folium.Map(location=[30.3359224, -97.9505711], zoom_start=12)
                folium.Marker(location=[30.3359224, -97.9505711], popup="Alta Vista 4",
                              icon=folium.Icon(color="green", icon="leaf")).add_to(m)
                st_folium(m)
            elif page == "Report Generator":
                st.header("Test")

                # sump_clean = st.checkbox("Sump Cleaning")
                Mow = st.checkbox("Mow")
                Chemical = st.checkbox("Chemical")
                Fountain_Operational = st.checkbox("Fountain operational")
                Fountain_NonOperational = st.checkbox("Fountain non-operational")
                Fountain_Removal = st.checkbox("Fountain removal")
                Fountain_Reinstalled = st.checkbox("Fountain re-installed")
                Well_reading = st.checkbox("Well reading")
                Pressure_wash = st.checkbox("Pressure wash")
                Trash = st.checkbox("Trash")
                Water_level_increase = st.checkbox("Water level increase")
                Water_level_decrease = st.checkbox("Water level decrease")

                report = []

                # if sump_clean:
                # report.append("The sump basin was cleaned and cleared of accumulated debris to ensure proper pump operation.")

                if Mow:
                    report.append(
                        "The pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
                if Fountain_Operational:
                    report.append("The fountain was inspected and tested and is currently fully operational.")
                if Fountain_Removal:
                    report.append(
                        "Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance.")
                if Fountain_NonOperational:
                    report.append(
                        "Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
                if Fountain_Reinstalled:
                    report.append("The fountain was reinstalled, tested, and is fully operational at this time.")
                if Chemical:
                    report.append(
                        "The pond was treated with chemical to control -plant species- growth and support overall water quality.")
                if Pressure_wash:
                    report.append(
                        "The waterfall structure was pressure washed to remove buildup debris and improve overall appearance.")
                if Well_reading:
                    report.append("The well reading was inspected at -time-, with a measurement of ###.")
                if Water_level_increase:
                    report.append("The water level is [X] inches below from its optimal level.")
                if Water_level_decrease:
                    report.append("The water level is [X] inches above from its optimal level.")
                if Trash:
                    report.append("Trash was collected and properly disposed of to improve site appearance.")

                st.header("Generated Report")

                if report:
                    final_report = " ".join(report)
                    st.write(final_report)









        #elif page == "Treatment":
         #   vegetation = st.radio("Select vegetation type:", ["Filamentous Algae", "Bushy Pondweed", "Cattail", "Arrowhead", "Primrose", "Lily"])
          #  if vegetation == "Filamentous Algae":
           #     st.image("filamentous_algae.png", use_container_width=True)
            #st.markdown("### Treatment")
            #st.checkbox("100 lbs copper sulfate (broadcast) - Filamentous Algae control")  # Filamentous Algae control
            #st.checkbox("2 jugs of argos (spray) - Filamentous Algae when bloom")  #


#site = st.selectbox("Choose a site:", ["River View", "Winding Creek", "Steele Creek", "Redbird", "Alamo Ranch", "Creekside"])

#if site == "river view":
        #m = folium.Map(location=[30.632489, -97.735146], zoom_start=12)
        #folium.Marker(location=[30.632489, -97.735146], popup="River View", icon=folium.Icon(color="blue", icon="tint")).add_to(
        #m)
        #st_folium(m)

#if site == "River View":
    #m = folium.Map(location=[30.632489, -97.735146], zoom_start=12)
    #folium.Marker(location=[30.632489, -97.735146], popup = "River View", icon=folium.Icon(color="blue", icon="tint")).add_to(m)
    #st_folium(m)

#if site == "Winding Creek":
    #m = folium.Map(location=[29.623099, -98.125060], zoom_start=12)
    #folium.Marker(location=[29.623099, -98.125060], popup = "Winding Creek", icon=folium.Icon(color="blue", icon="tint")).add_to(m)
    #st_folium(m)

#if site == "Steele Creek":
    #m = folium.Map(location=[29.572180, -98.218894], zoom_start=12)
    #folium.Marker(location=[29.572180, -98.218894], popup = "Steele Creek", icon=folium.Icon(color="blue", icon="tint")).add_to(m)
    #st_folium(m)

#if site == "Redbird":
    #m = folium.Map(location=[29.431115, -98.798014], zoom_start=12)
    #folium.Marker(location=[29.431115, -98.798014], popup = "Redbird", icon=folium.Icon(color="blue", icon="tint")).add_to(m)
    #st_folium(m)

#if site == "Alamo Ranch":
    #m = folium.Map(location=[29.4834609, -98.7338868], zoom_start=12)
    #folium.Marker(location=[29.4834609, -98.7338868], popup = "Alamo Ranch", icon=folium.Icon(color="blue", icon="tint")).add_to(m)
    #st_folium(m)

#if site == "Creekside":
    #m = folium.Map(location=[29.7298477, -98.0750534], zoom_start=12)
    #folium.Marker(location=[29.7298477, -98.0750534], popup = "Creekside", icon=folium.Icon(color="blue", icon="tint")).add_to(m)
    #st_folium(m)

#If you want to post all in once:

# m = folium.Map(location=[###,###], zoom_start=#)

#folium.Marker([29.72, -98.1], popup="River View").add_to(m)
#folium.Marker([29.74, -98.15], popup="Lake Park").add_to(m)
#folium.Marker([29.70, -98.05], popup="Creek Side").add_to(m)
#etc.










