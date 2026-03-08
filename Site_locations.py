import streamlit as st
import folium
from streamlit_folium import st_folium

st.image("LMSS.png", width=450)
st.markdown("Lake & AWF Maintenance Dashboard for routine maintenance,treatment identification, and reporting.")

side = st.selectbox("Choose your side:", ["Select", "Lake", "AWF"])
#site = st.text_input("Enter site name")

if side == "AWF":
    site = st.selectbox("Choose water feature", ["Search", "River View", "Winding Creek", "Steele Creek", "Redbird", "Alamo Ranch", "Creekside", "Éilan", "Brookestone(Evans)", "Brookestone(Boulder Flats)"])

    if site == "River View":
        page = st.radio("Select", ["Routine Maintenance", "Water quality levels", "Map"], horizontal=True)
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

    if site == "Winding Creek":
        page = st.radio("Select", ["Routine Maintenance", "Water quality levels", "Map"], horizontal=True)
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


    if site == "Steele Creek":
        page = st.radio("Select", ["Routine Maintenance", "Water quality levels", "Map"], horizontal=True)
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

    if site == "Redbird":
        page = st.radio("Select", ["Routine Maintenance", "Water quality levels", "Map"], horizontal=True)
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

    if site == "Alamo Ranch":
        page = st.radio("Select", ["Routine Maintenance", "Water quality levels", "Map"], horizontal=True)
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

    if site == "Creekside":
        page = st.radio("Select", ["Routine Maintenance", "Water quality levels", "Map"], horizontal=True)
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

    if site == "Éilan":
        page = st.radio("Select", ["Routine Maintenance", "Water quality levels", "Map"], horizontal=True)
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

    if site == "Brookestone(Evans)":
        page = st.radio("Select", ["Routine Maintenance", "Water quality levels", "Map"], horizontal=True)
        if page == "Routine Maintenance":
            st.subheader("Brookestone(Evans)")
            st.image(f"Brookestone_Evans.png", caption="Brookestone(Evans)", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat water feature")
            st.checkbox("Remove debris from water feature")
            st.checkbox("Clean out all pump strainers")
            st.checkbox("Backwash and rinse all filter pumps")
            st.checkbox("Do any specific task for today")
        elif page == "Map":
            st.write("5149 Evans Rd, San Antonio, TX 78261")
            m = folium.Map(location=[29.6425694, -98.3885825], zoom_start=12)
            folium.Marker(location=[29.6425694, -98.3885825], popup="Brookestone(Evans)",
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

    if site == "Brookestone(Boulder Flats)":
        page = st.radio("Select", ["Routine Maintenance", "Water quality levels", "Map"], horizontal=True)
        if page == "Routine Maintenance":
            st.subheader("Brookestone(Boulder Flats)")
            st.image(f"Brookestone_Boulder_Flats.png", caption="Brookestone(Boulder Flats)", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat water feature")
            st.checkbox("Remove debris from water feature")
            st.checkbox("Clean out all pump strainers")
            st.checkbox("Backwash and rinse all filter pumps")
            st.checkbox("Do any specific task for today")
        elif page == "Map":
            st.write("Boulder Flts, San Antonio, TX 78266")
            m = folium.Map(location=[29.6409731, -98.3820970], zoom_start=12)
            folium.Marker(location=[29.6409731, -98.3820970], popup="Brookestone(Boulder Flats)",
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


elif side == "Lake":
    site = st.selectbox("Choose pond", ["Search", "Prim Rose", "Falcon Pointe", "Easton Park", "Blanco Vista", "Lakeside Crossing", "Valley Ranch", "Hunters Pond", "DR Horton", "Rhine Valley", "Whisper Falls", "Sundance Crossing", "Woods of Alon", "Cowboy Cabin", "The Willows HOA", "River Bend", "Green Lake", "Willow's Creek", "Versante", "Versante 2", "Mayfield"])

    if site == "Prim Rose":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Details"], horizontal=True)
        if page == "Tasks":
            st.subheader("Prim Rose")
            st.image(f"Prim_Rose.png", caption="Prim Rose", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Fountain inspection and testing")
            st.checkbox("Pick up trash")
            st.checkbox("Do any specific task for today")
        elif page == "Treatment":
            #st.markdown("### Treatment")
            #st.checkbox("100 lbs copper sulfate (broadcast)") #Filamentous Algae control
            #st.checkbox("2 jugs of argos (spray)") #Filamentous Algae when bloom
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
            st.write("### Algae Control Treatment")
            st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
        elif page == "Map":
            st.write("17829 Colorado Sand Dr, Pflugerville, Texas 78660")
            m = folium.Map(location=[30.4517623, -97.5886834], zoom_start=12)
            folium.Marker(location=[30.4517623, -97.5886834], popup="Prim Rose",icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Details":
            task = st.radio("Select", ["Chemical", "Fountain operational", "Trash", "Fountain non-operational", "Fountain removal", "Well reading", "Pressure wash", "Pump systems operational", "Pump systems non-operational", "Fountain reinstalled", "Motor removal", "Motor non-operational"])
            if task == "Chemical":
                st.write("The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if task == "Fountain operational":
                st.write("The fountain was inspected and tested and is fully operational at this time.")
            if task == "Trash":
                st.write("Trash was collected and properly disposed of to improve site appearance.")
            if task == "Fountain non-operational":
                st.write("Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if task == "Fountain removal":
                st.write("Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance at the shop.")
            if task == "Well reading":
                st.write("The well reading was inspected with a measurement of 1111.")
            if task == "Pressure wash":
                st.write("The waterfall structure was pressure washed to remove buildup and improve overall appearance.")
            if task == "Pump systems operational":
                st.write("The pump system was inspected and found to be operating properly at this time.")
            if task == "Pump systems non-operational":
                st.write("The pump system was inspected and found to be non-operational. Further evaluation and maintenance will be required.")
            if task == "Fountain reinstalled":
                st.write("The fountain was reinstalled, tested, and is fully operational at this time.")
            if task == "Motor removal":
                st.write("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if task == "Motor non-operational":
                st.write("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")


    if site == "Falcon Pointe":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Details"], horizontal=True)
        if page == "Tasks":
            st.subheader("Falcon Pointe")
            st.image(f"Falcon_Pointe.png", caption="Falcon Pointe", use_container_width=True)
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
            st.write("100 lbs (whole bag) copper sulfate (broadcast) to control filamentous algae")
        elif page == "Map":
            st.write("2708-2812 Standing Juniper Ct, Pflugerville, TX 78660")
            m = folium.Map(location=[30.4573293, -97.5840429], zoom_start=12)
            folium.Marker(location=[30.4573293, -97.5840429], popup="Falcon Pointe",icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Details":
            task = st.radio("Select", ["Chemical", "Fountain operational", "Trash", "Fountain non-operational", "Fountain removal", "Well reading", "Pressure wash", "Pump systems operational", "Pump systems non-operational", "Fountain reinstalled", "Motor removal", "Motor non-operational"])
            if task == "Chemical":
                st.write("The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if task == "Fountain operational":
                st.write("The fountain was inspected and tested and is fully operational at this time.")
            if task == "Trash":
                st.write("Trash was collected and properly disposed of to improve site appearance.")
            if task == "Fountain non-operational":
                st.write("Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if task == "Fountain removal":
                st.write("Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance at the shop.")
            if task == "Well reading":
                st.write("The well reading was inspected with a measurement of 1111.")
            if task == "Pressure wash":
                st.write("The waterfall structure was pressure washed to remove buildup and improve overall appearance.")
            if task == "Pump systems operational":
                st.write("The pump system was inspected and found to be operating properly at this time.")
            if task == "Pump systems non-operational":
                st.write("The pump system was inspected and found to be non-operational. Further evaluation and maintenance will be required.")
            if task == "Fountain reinstalled":
                st.write("The fountain was reinstalled, tested, and is fully operational at this time.")
            if task == "Motor removal":
                st.write("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if task == "Motor non-operational":
                st.write("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")


    if site == "Easton Park":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Details"], horizontal=True)
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
        elif page == "Report Details":
            task = st.radio("Select", ["Chemical", "Fountain operational", "Trash", "Fountain non-operational", "Fountain removal", "Well reading", "Pressure wash", "Pump systems operational", "Pump systems non-operational", "Fountain reinstalled", "Motor removal", "Motor non-operational"])
            if task == "Chemical":
                st.write("The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if task == "Fountain operational":
                st.write("The fountain was inspected and tested and is fully operational at this time.")
            if task == "Trash":
                st.write("Trash was collected and properly disposed of to improve site appearance.")
            if task == "Fountain non-operational":
                st.write("Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if task == "Fountain removal":
                st.write("Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance at the shop.")
            if task == "Well reading":
                st.write("The well reading was inspected with a measurement of 1111.")
            if task == "Pressure wash":
                st.write("The waterfall structure was pressure washed to remove buildup and improve overall appearance.")
            if task == "Pump systems operational":
                st.write("The pump system was inspected and found to be operating properly at this time.")
            if task == "Pump systems non-operational":
                st.write("The pump system was inspected and found to be non-operational. Further evaluation and maintenance will be required.")
            if task == "Fountain reinstalled":
                st.write("The fountain was reinstalled, tested, and is fully operational at this time.")
            if task == "Motor removal":
                st.write("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if task == "Motor non-operational":
                st.write("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")


    if site == "Blanco Vista":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Details"], horizontal=True)
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
        elif page == "Report Details":
            task = st.radio("Select", ["Chemical", "Fountain operational", "Trash", "Fountain non-operational", "Fountain removal", "Well reading", "Pressure wash", "Pump systems operational", "Pump systems non-operational", "Fountain reinstalled", "Motor removal", "Motor non-operational"])
            if task == "Chemical":
                st.write("The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if task == "Fountain operational":
                st.write("The fountain was inspected and tested and is fully operational at this time.")
            if task == "Trash":
                st.write("Trash was collected and properly disposed of to improve site appearance.")
            if task == "Fountain non-operational":
                st.write("Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if task == "Fountain removal":
                st.write("Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance at the shop.")
            if task == "Well reading":
                st.write("The well reading was inspected with a measurement of 1111.")
            if task == "Pressure wash":
                st.write("The waterfall structure was pressure washed to remove buildup and improve overall appearance.")
            if task == "Pump systems operational":
                st.write("The pump system was inspected and found to be operating properly at this time.")
            if task == "Pump systems non-operational":
                st.write("The pump system was inspected and found to be non-operational. Further evaluation and maintenance will be required.")
            if task == "Fountain reinstalled":
                st.write("The fountain was reinstalled, tested, and is fully operational at this time.")
            if task == "Motor removal":
                st.write("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if task == "Motor non-operational":
                st.write("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")

    if site == "Lakeside Crossing":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Details"], horizontal=True)
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
        elif page == "Report Details":
            task = st.radio("Select", ["Chemical", "Fountain operational", "Trash", "Fountain non-operational", "Fountain removal", "Fountain reinstalled", "Motor removal", "Motor non-operational"])
            if task == "Chemical":
                st.write("The pond was treated with chemical to control filamentous algae growth and support overall water quality.")
            if task == "Fountain operational":
                st.write("The fountain was inspected and tested and is fully operational at this time.")
            if task == "Trash":
                st.write("Trash was collected and properly disposed of to improve site appearance.")
            if task == "Fountain non-operational":
                st.write("Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if task == "Fountain removal":
                st.write("Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance at the shop.")
            if task == "Fountain reinstalled":
                st.write("The fountain was reinstalled, tested, and is fully operational at this time.")
            if task == "Motor removal":
                st.write("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if task == "Motor non-operational":
                st.write("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
            #if task == "Well Reading":
                #st.write("The well reading was inspected with a measurement of #####.)

    if site == "Valley Ranch":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Details"], horizontal=True)
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
        elif page == "Report Details":
            task = st.radio("Select", ["Chemical", "Fountain operational", "Trash", "Fountain non-operational", "Fountain removal", "Well reading", "Pressure wash", "Pump systems operational", "Pump systems non-operational", "Fountain reinstalled", "Motor removal", "Motor non-operational"])
            if task == "Chemical":
                st.write("The pond was treated with chemical to control filamentous algae growth and support overall water quality.")
            if task == "Fountain operational":
                st.write("The fountain was inspected and tested and is fully operational at this time.")
            if task == "Trash":
                st.write("Trash was collected and properly disposed of to improve site appearance.")
            if task == "Fountain non-operational":
                st.write("Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if task == "Fountain removal":
                st.write("Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance at the shop.")
            if task == "Well reading":
                st.write("The well reading was inspected with a measurement of 1111.")
            if task == "Pressure wash":
                st.write("The waterfall structure was pressure washed to remove buildup and improve overall appearance.")
            if task == "Pump systems operational":
                st.write("The pump system was inspected and found to be operating properly at this time.")
            if task == "Pump systems non-operational":
                st.write("The pump system was inspected and found to be non-operational. Further evaluation and maintenance will be required.")
            if task == "Fountain reinstalled":
                st.write("The fountain was reinstalled, tested, and is fully operational at this time.")
            if task == "Motor removal":
                st.write("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if task == "Motor non-operational":
                st.write("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")

    if site == "Hunters Pond":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Details"], horizontal=True)
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
        elif page == "Report Details":
            task = st.radio("Select", ["Chemical", "Fountain operational", "Trash", "Fountain non-operational", "Fountain removal", "Well reading", "Pressure wash", "Pump systems operational", "Pump systems non-operational", "Fountain reinstalled", "Motor removal", "Motor non-operational"])
            if task == "Chemical":
                st.write("The pond was treated with chemical to control filamentous algae growth and support overall water quality.")
            if task == "Fountain operational":
                st.write("The fountain was inspected and tested and is fully operational at this time.")
            if task == "Trash":
                st.write("Trash was collected and properly disposed of to improve site appearance.")
            if task == "Fountain non-operational":
                st.write("Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if task == "Fountain removal":
                st.write("Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance at the shop.")
            if task == "Well reading":
                st.write("The well reading was inspected with a measurement of 1111.")
            if task == "Pressure wash":
                st.write("The waterfall structure was pressure washed to remove buildup and improve overall appearance.")
            if task == "Pump systems operational":
                st.write("The pump system was inspected and found to be operating properly at this time.")
            if task == "Pump systems non-operational":
                st.write("The pump system was inspected and found to be non-operational. Further evaluation and maintenance will be required.")
            if task == "Fountain reinstalled":
                st.write("The fountain was reinstalled, tested, and is fully operational at this time.")
            if task == "Motor removal":
                st.write("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if task == "Motor non-operational":
                st.write("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")

    if site == "DR Horton":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Details"], horizontal=True)
        if page == "Tasks":
            st.subheader("DR Horton")
            st.image(f"drr_horton.png", caption="DR Horton", use_container_width=True)
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
            st.write("Near D.R. Horton San Antonio Division Office, San Antonio, TX")
            m = folium.Map(location=[29.603528, -98.382056], zoom_start=12)
            folium.Marker(location=[29.603528, -98.382056], popup="DR Horton", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Details":
            task = st.radio("Select", ["Chemical", "Fountain operational", "Trash", "Fountain non-operational", "Fountain removal", "Well reading", "Pressure wash", "Pump systems operational", "Pump systems non-operational", "Fountain reinstalled", "Motor removal", "Motor non-operational"])
            if task == "Chemical":
                st.write("The pond was treated with chemical to control filamentous algae growth and support overall water quality.")
            if task == "Fountain operational":
                st.write("The fountain was inspected and tested and is fully operational at this time.")
            if task == "Trash":
                st.write("Trash was collected and properly disposed of to improve site appearance.")
            if task == "Fountain non-operational":
                st.write("Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if task == "Fountain removal":
                st.write("Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance at the shop.")
            if task == "Well reading":
                st.write("The well reading was inspected with a measurement of 1111.")
            if task == "Pressure wash":
                st.write("The waterfall structure was pressure washed to remove buildup and improve overall appearance.")
            if task == "Pump systems operational":
                st.write("The pump system was inspected and found to be operating properly at this time.")
            if task == "Pump systems non-operational":
                st.write("The pump system was inspected and found to be non-operational. Further evaluation and maintenance will be required.")
            if task == "Fountain reinstalled":
                st.write("The fountain was reinstalled, tested, and is fully operational at this time.")
            if task == "Motor removal":
                st.write("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if task == "Motor non-operational":
                st.write("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")

    if site == "Rhine Valley":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Details"], horizontal=True)
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
        elif page == "Report Details":
            task = st.radio("Select", ["Chemical", "Fountain operational", "Trash", "Fountain non-operational", "Fountain removal", "Well reading", "Pressure wash", "Pump systems operational", "Pump systems non-operational", "Fountain reinstalled", "Motor removal", "Motor non-operational"])
            if task == "Chemical":
                st.write("The pond was treated with chemical to control filamentous algae growth and support overall water quality.")
            if task == "Fountain operational":
                st.write("The fountain was inspected and tested and is fully operational at this time.")
            if task == "Trash":
                st.write("Trash was collected and properly disposed of to improve site appearance.")
            if task == "Fountain non-operational":
                st.write("Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if task == "Fountain removal":
                st.write("Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance at the shop.")
            if task == "Well reading":
                st.write("The well reading was inspected with a measurement of 1111.")
            if task == "Pressure wash":
                st.write("The waterfall structure was pressure washed to remove buildup and improve overall appearance.")
            if task == "Pump systems operational":
                st.write("The pump system was inspected and found to be operating properly at this time.")
            if task == "Pump systems non-operational":
                st.write("The pump system was inspected and found to be non-operational. Further evaluation and maintenance will be required.")
            if task == "Fountain reinstalled":
                st.write("The fountain was reinstalled, tested, and is fully operational at this time.")
            if task == "Motor removal":
                st.write("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if task == "Motor non-operational":
                st.write("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")

    if site == "Whisper Falls":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Details"], horizontal=True)
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
        elif page == "Report Details":
            task = st.radio("Select", ["Chemical", "Fountain operational", "Trash", "Fountain non-operational", "Fountain removal", "Well reading", "Pressure wash", "Pump systems operational", "Pump systems non-operational", "Fountain reinstalled", "Motor removal", "Motor non-operational"])
            if task == "Chemical":
                st.write("The pond was treated with chemical to control filamentous algae growth and support overall water quality.")
            if task == "Fountain operational":
                st.write("The fountain was inspected and tested and is fully operational at this time.")
            if task == "Trash":
                st.write("Trash was collected and properly disposed of to improve site appearance.")
            if task == "Fountain non-operational":
                st.write("Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if task == "Fountain removal":
                st.write("Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance at the shop.")
            if task == "Well reading":
                st.write("The well reading was inspected with a measurement of 1111.")
            if task == "Pressure wash":
                st.write("The waterfall structure was pressure washed to remove buildup and improve overall appearance.")
            if task == "Pump systems operational":
                st.write("The pump system was inspected and found to be operating properly at this time.")
            if task == "Pump systems non-operational":
                st.write("The pump system was inspected and found to be non-operational. Further evaluation and maintenance will be required.")
            if task == "Fountain reinstalled":
                st.write("The fountain was reinstalled, tested, and is fully operational at this time.")
            if task == "Motor removal":
                st.write("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if task == "Motor non-operational":
                st.write("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")

    if site == "Sundance Crossing":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Details"], horizontal=True)
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
        elif page == "Report Details":
            task = st.radio("Select", ["Chemical", "Fountain operational", "Trash", "Fountain non-operational", "Fountain removal", "Well reading", "Pressure wash", "Pump systems operational", "Pump systems non-operational", "Fountain reinstalled", "Motor removal", "Motor non-operational"])
            if task == "Chemical":
                st.write("The pond was treated with chemical to control filamentous algae growth and support overall water quality.")
            if task == "Fountain operational":
                st.write("The fountain was inspected and tested and is fully operational at this time.")
            if task == "Trash":
                st.write("Trash was collected and properly disposed of to improve site appearance.")
            if task == "Fountain non-operational":
                st.write("Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if task == "Fountain removal":
                st.write("Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance at the shop.")
            if task == "Well reading":
                st.write("The well reading was inspected with a measurement of 1111.")
            if task == "Pressure wash":
                st.write("The waterfall structure was pressure washed to remove buildup and improve overall appearance.")
            if task == "Pump systems operational":
                st.write("The pump system was inspected and found to be operating properly at this time.")
            if task == "Pump systems non-operational":
                st.write("The pump system was inspected and found to be non-operational. Further evaluation and maintenance will be required.")
            if task == "Fountain reinstalled":
                st.write("The fountain was reinstalled, tested, and is fully operational at this time.")
            if task == "Motor removal":
                st.write("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if task == "Motor non-operational":
                st.write("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")

    if site == "Woods of Alon":
        page = st.radio("Select", ["Tasks", "Treatment", "Map"], horizontal=True)

        m = folium.Map(location=[29.549143, -98.534438], zoom_start=12)
        folium.Marker(location=[29.549143, -98.534438], popup="Woods of Alon",icon=folium.Icon(color="green", icon="leaf")).add_to(m)
        st_folium(m)

    if site == "Cowboy Cabin":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Details"], horizontal=True)
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
        elif page == "Report Details":
            task = st.radio("Select", ["Chemical", "Fountain operational", "Trash", "Fountain non-operational", "Fountain removal", "Well reading", "Pressure wash", "Pump systems operational", "Pump systems non-operational", "Fountain reinstalled", "Fountain Light", "Motor removal", "Motor non-operational"])
            if task == "Chemical":
                st.write("The pond was treated with chemical to control filamentous algae growth and support overall water quality.")
            if task == "Fountain operational":
                st.write("The fountain was inspected and tested and is fully operational at this time.")
            if task == "Trash":
                st.write("Trash was collected and properly disposed of to improve site appearance.")
            if task == "Fountain non-operational":
                st.write("Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if task == "Fountain removal":
                st.write("Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance at the shop.")
            if task == "Well reading":
                st.write("The well reading was inspected with a measurement of 1111.")
            if task == "Pressure wash":
                st.write("The waterfall structure was pressure washed to remove buildup and improve overall appearance.")
            if task == "Pump systems operational":
                st.write("The pump system was inspected and found to be operating properly at this time.")
            if task == "Pump systems non-operational":
                st.write("The pump system was inspected and found to be non-operational. Further evaluation and maintenance will be required.")
            if task == "Fountain reinstalled":
                st.write("The fountain was reinstalled, tested, and is fully operational at this time.")
            if task == "Fountain Light":
                st.write("The fountain light was replaced and tested to ensure proper operation.")
            if task == "Motor removal":
                st.write("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if task == "Motor non-operational":
                st.write("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")

    if site == "The Willows HOA":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Details"], horizontal=True)
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
        elif page == "Report Details":
            task = st.radio("Select", ["Chemical", "Fountain operational", "Trash", "Fountain non-operational", "Fountain removal", "Well reading", "Pressure wash", "Pump systems operational", "Pump systems non-operational", "Fountain reinstalled", "Motor removal", "Motor non-operational"])
            if task == "Chemical":
                st.write("The pond was treated with chemical to control filamentous algae growth and support overall water quality.")
            if task == "Fountain operational":
                st.write("The fountain was inspected and tested and is fully operational at this time.")
            if task == "Trash":
                st.write("Trash was collected and properly disposed of to improve site appearance.")
            if task == "Fountain non-operational":
                st.write("Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if task == "Fountain removal":
                st.write("Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance at the shop.")
            if task == "Well reading":
                st.write("The well reading was inspected with a measurement of 1111.")
            if task == "Pressure wash":
                st.write("The waterfall structure was pressure washed to remove buildup and improve overall appearance.")
            if task == "Pump systems operational":
                st.write("The pump system was inspected and found to be operating properly at this time.")
            if task == "Pump systems non-operational":
                st.write("The pump system was inspected and found to be non-operational. Further evaluation and maintenance will be required.")
            if task == "Fountain reinstalled":
                st.write("The fountain was reinstalled, tested, and is fully operational at this time.")
            if task == "Motor removal":
                st.write("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if task == "Motor non-operational":
                st.write("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")

    if site == "River Bend":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Details"], horizontal=True)
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
        elif page == "Report Details":
            task = st.radio("Select", ["Chemical", "Fountain operational", "Trash", "Fountain non-operational", "Fountain removal", "Well reading", "Pressure wash", "Pump systems operational", "Pump systems non-operational", "Fountain reinstalled", "Motor removal", "Motor non-operational"])
            if task == "Chemical":
                st.write("The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if task == "Fountain operational":
                st.write("The fountain was inspected and tested and is fully operational at this time.")
            if task == "Trash":
                st.write("Trash was collected and properly disposed of to improve site appearance.")
            if task == "Fountain non-operational":
                st.write("Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if task == "Fountain removal":
                st.write("Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance at the shop.")
            if task == "Well reading":
                st.write("The well reading was inspected with a measurement of 1111.")
            if task == "Pressure wash":
                st.write("The waterfall structure was pressure washed to remove buildup and improve overall appearance.")
            if task == "Pump systems operational":
                st.write("The pump system was inspected and found to be operating properly at this time.")
            if task == "Pump systems non-operational":
                st.write("The pump system was inspected and found to be non-operational. Further evaluation and maintenance will be required.")
            if task == "Fountain reinstalled":
                st.write("The fountain was reinstalled, tested, and is fully operational at this time.")
            if task == "Motor removal":
                st.write("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if task == "Motor non-operational":
                st.write("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")

    if site == "Green Lake":
        page = st.radio("Select", ["Tasks", "Treatment", "Map"], horizontal=True)

        m = folium.Map(location=[29.309109, -98.386129], zoom_start=12)
        folium.Marker(location=[29.309109, -98.386129], popup="Green Lake",icon=folium.Icon(color="green", icon="leaf")).add_to(m)
        st_folium(m)

    if site == "Willow's Creek":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Details"], horizontal=True)
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
        elif page == "Report Details":
            task = st.radio("Select", ["Chemical", "Fountain operational", "Trash", "Fountain non-operational", "Fountain removal", "Well reading", "Pressure wash", "Pump systems operational", "Pump systems non-operational", "Fountain reinstalled", "Motor removal", "Motor non-operational"])
            if task == "Chemical":
                st.write("The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if task == "Fountain operational":
                st.write("The fountain was inspected and tested and is fully operational at this time.")
            if task == "Trash":
                st.write("Trash was collected and properly disposed of to improve site appearance.")
            if task == "Fountain non-operational":
                st.write("Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if task == "Fountain removal":
                st.write("Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance at the shop.")
            if task == "Well reading":
                st.write("The well reading was inspected with a measurement of 1111.")
            if task == "Pressure wash":
                st.write("The waterfall structure was pressure washed to remove buildup and improve overall appearance.")
            if task == "Pump systems operational":
                st.write("The pump system was inspected and found to be operating properly at this time.")
            if task == "Pump systems non-operational":
                st.write("The pump system was inspected and found to be non-operational. Further evaluation and maintenance will be required.")
            if task == "Fountain reinstalled":
                st.write("The fountain was reinstalled, tested, and is fully operational at this time.")
            if task == "Motor removal":
                st.write("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if task == "Motor non-operational":
                st.write("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")

    if site == "Versante":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Details"], horizontal=True)
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
            m = folium.Map(location=[30.431707, -97.844185], zoom_start=12)
            folium.Marker(location=[30.431707, -97.844185], popup="Versante", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Details":
            task = st.radio("Select", ["Chemical", "Fountain operational", "Trash", "Fountain non-operational", "Fountain removal", "Well reading", "Pressure wash", "Pump systems operational", "Pump systems non-operational", "Fountain reinstalled", "Motor removal"])
            if task == "Chemical":
                st.write("The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if task == "Fountain operational":
                st.write("The fountain was inspected and tested and is fully operational at this time.")
            if task == "Trash":
                st.write("Trash was collected and properly disposed of to improve site appearance.")
            if task == "Fountain non-operational":
                st.write("Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if task == "Fountain removal":
                st.write("Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance at the shop.")
            if task == "Well reading":
                st.write("The well reading was inspected with a measurement of 1111.")
            if task == "Pressure wash":
                st.write("The waterfall structure was pressure washed to remove buildup and improve overall appearance.")
            if task == "Pump systems operational":
                st.write("The pump system was inspected and found to be operating properly at this time.")
            if task == "Pump systems non-operational":
                st.write("The pump system was inspected and found to be non-operational. Further evaluation and maintenance will be required.")
            if task == "Fountain reinstalled":
                st.write("The fountain was reinstalled, tested, and is fully operational at this time.")
            if task == "Motor removal":
                st.write("The pump motor was found to be non-operational and was removed from site for further inspection.")
            if task == "Motor non-operational":
                st.write("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")

    if site == "Versante 2":
        page = st.radio("Select", ["Tasks", "Treatment", "Map"], horizontal=True)

        m = folium.Map(location=[30.429038, -97.845580], zoom_start=12)
        folium.Marker(location=[30.429038, -97.845580], popup="Versante",icon=folium.Icon(color="green", icon="leaf")).add_to(m)
        st_folium(m)

    if site == "Mayfield":
        page = st.radio("Select", ["Tasks", "Treatment", "Map", "Report Details"], horizontal=True)
        if page == "Tasks":
            st.header("Mayfield")
            st.subheader("Site 1")
            st.image(f"mayfield_1.png", caption="Mayfield 1", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Treat")
            st.checkbox("Pick up trash", key="pickup_trash_1")
            st.checkbox("Mow", key="mow_1")
            st.checkbox("Do any specific task for today", key="specific_task_1")
        if page == "Tasks":
            st.subheader("Site 2")
            st.image(f"mayfield_22.png", caption="Mayfield 2", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Pick up trash", key="pickup_trash_2")
            st.checkbox("Mow", key="mow_2")
            st.checkbox("Do any specific task for today", key="specific_task_2")
        if page == "Tasks":
            st.subheader("Site 3")
            st.image(f"mayfield_3.png", caption="Mayfield 3", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Pick up trash", key="pickup_trash_3")
            st.checkbox("Mow", key="mow_3")
            st.checkbox("Do any specific task for today", key="specific_task_3")
        if page == "Tasks":
            st.subheader("Site 4")
            st.image(f"mayfield_4.png", caption="Mayfield 4", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Pick up trash", key="pickup_trash_4")
            st.checkbox("Mow", key="mow_4")
            st.checkbox("Do any specific task for today", key="specific_task_4")
        if page == "Tasks":
            st.subheader("Site 5")
            st.image(f"mayfield_5.png", caption="Mayfield 5", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Pick up trash", key="pickup_trash_5")
            st.checkbox("Mow",key="mow_5")
            st.checkbox("Do any specific task for today", key="specific_task_5")
        if page == "Tasks":
            st.subheader("Site 6")
            st.image(f"mayfield_6.png", caption="Mayfield 6", use_container_width=True)
            st.markdown("### Tasks")
            st.checkbox("Pick up trash", key="pickup_trash_6")
            st.checkbox("Mow",key="mow_6")
            st.checkbox("Do any specific task for today", key="specific_task_6")
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
            st.write("3826 Sebastian Cove, Round Rock, TX")
            m = folium.Map(location=[30.5512964, -97.7452443], zoom_start=12)
            folium.Marker(location=[30.5512964, -97.7452443], popup="Mayfield pond 1", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
            st.subheader("Site 2")
            st.write("3612 Pine Needle Cir, Round Rock, TX")
            m = folium.Map(location=[30.5543936, -97.7391661], zoom_start=12)
            folium.Marker(location=[30.5543936, -97.7391661], popup="Mayfield pond 2", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
            st.subheader("Site 3")
            st.write("3632 Fossilwood Way, Round Rock, TX")
            m = folium.Map(location=[30.5565555, -97.7408281], zoom_start=12)
            folium.Marker(location=[30.5565555, -97.7408281], popup="Mayfield pond 3", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
            st.subheader("Site 4")
            st.write("3800 Sapphire Ct, Round Rock, TX")
            m = folium.Map(location=[30.5600706, -97.7541087], zoom_start=12)
            folium.Marker(location=[30.5600706, -97.7541087], popup="Mayfield pond 4", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
            st.subheader("Site 5")
            st.write("4001 Massey Way, Round Rock, TX")
            m = folium.Map(location=[30.5575839, -97.7532584], zoom_start=12)
            folium.Marker(location=[30.5575839, -97.7532584], popup="Mayfield pond 5", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
            st.subheader("Site 6")
            st.write("3835 Lagoona Dr, Round Rock, TX")
            m = folium.Map(location=[30.5592073, -97.7499684], zoom_start=12)
            folium.Marker(location=[30.5592073, -97.7499684], popup="Mayfield pond 6", icon=folium.Icon(color="green", icon="leaf")).add_to(m)
            st_folium(m)
        elif page == "Report Details":
            task = st.radio("Select", ["Chemical", "Fountain operational", "Trash", "Fountain non-operational",
                                       "Fountain removal", "Well reading", "Pressure wash", "Pump systems operational",
                                       "Pump systems non-operational", "Fountain reinstalled", "Motor removal", "Mow"])
            if task == "Chemical":
                st.write(
                    "The pond was treated with chemical to control -plant species- growth and support overall water quality.")
            if task == "Fountain operational":
                st.write("The fountain was inspected and tested and is fully operational at this time.")
            if task == "Trash":
                st.write("Trash was collected and properly disposed of to improve site appearance.")
            if task == "Fountain non-operational":
                st.write(
                    "Upon arrival, the fountain was found to be non-operational. Further maintenance is required to restore proper function.")
            if task == "Fountain removal":
                st.write(
                    "Upon arrival, the fountain was found to be non-operational. The unit was removed from the pond for further evaluation and maintenance at the shop.")
            if task == "Well reading":
                st.write("The well reading was inspected with a measurement of 1111.")
            if task == "Pressure wash":
                st.write(
                    "The waterfall structure was pressure washed to remove buildup and improve overall appearance.")
            if task == "Pump systems operational":
                st.write("The pump system was inspected and found to be operating properly at this time.")
            if task == "Pump systems non-operational":
                st.write(
                    "The pump system was inspected and found to be non-operational. Further evaluation and maintenance will be required.")
            if task == "Fountain reinstalled":
                st.write("The fountain was reinstalled, tested, and is fully operational at this time.")
            if task == "Motor removal":
                st.write(
                    "The pump motor was found to be non-operational and was removed from site for further inspection.")
            if task == "Motor non-operational":
                st.write("The pump motor was inspected and fount to be non-operational. Further evaluation and maintenance will be required.")
            if task == "Mow":
                st.write("The pond basin and surrounding areas were mowed to control vegetation growth and maintain site appearance.")
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










