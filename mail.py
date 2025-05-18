import streamlit as st

st.title("Raft Foundation Design Tool")

length = st.number_input("Raft Length (m)")
width = st.number_input("Raft Width (m)")
load = st.number_input("Total Load (kN)")
soil_capacity = st.number_input("Soil Bearing Capacity (kN/m²)")

if st.button("Calculate"):
    area = length * width
    pressure = load / area
    st.write(f"Contact Pressure: {pressure:.2f} kN/m²")
    if pressure <= soil_capacity:
        st.success("Safe Design ✅")
    else:
        st.error("Unsafe Design ❌")
