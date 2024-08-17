import streamlit as st

# Title of the form
st.title("Work Request Form")

# Date input
date = st.date_input("Select Date (DD/MM/YYYY)")

# Department dropdown
department = st.selectbox("Select Department", ["Engineering", "TRD", "SIG"])

# Section names dropdown
section = st.selectbox("Select Section", ["Section 1", "Section 2", "Section 3", "Section 4", "Section 5"])

# Block Section dropdown with indentation for Station/Section ID
st.markdown("### Block Section")
block_section = st.selectbox(" ", ["Station", "Section"])

if block_section == "Station":
    st.markdown("<div style='margin-left: 20px;'>", unsafe_allow_html=True)
    line = st.selectbox("Select Station ID", ["Station 1", "Station 2", "Station 3", "Station 4", "Station 5"])
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.markdown("<div style='margin-left: 20px;'>", unsafe_allow_html=True)
    line = st.selectbox("Select Section ID", ["Section 1", "Section 2", "Section 3", "Section 4", "Section 5"])
    st.markdown("</div>", unsafe_allow_html=True)

# Work Description dropdown with indentation for Mission/Non-Mission Block
st.markdown("### Work Description")
work_description_type = st.selectbox(" ", ["Mission Block", "Non-Mission Block"])

if work_description_type == "Mission Block":
    st.markdown("<div style='margin-left: 20px;'>", unsafe_allow_html=True)
    mission_block_description = st.selectbox("Select Mission Block Work Description", ["Mission Work 1", "Mission Work 2", "Mission Work 3"])
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.markdown("<div style='margin-left: 20px;'>", unsafe_allow_html=True)
    non_mission_block_description = st.selectbox("Select Non-Mission Block Work Description", ["Non-Mission Work 1", "Non-Mission Work 2", "Non-Mission Work 3"])
    st.markdown("</div>", unsafe_allow_html=True)

# Caution Required with indented options
st.markdown("### Caution Required")
caution_required = st.radio(" ", ["Yes", "No"], key="caution_required")

if caution_required == "Yes":
    st.markdown("<div style='margin-left: 20px;'>", unsafe_allow_html=True)
    speed = st.number_input("Enter the Speed of the Caution (in km/h)", min_value=0)
    location_from = st.text_input("Caution Location From (XXX/YY format)")
    location_to = st.text_input("Caution Location To (XXX/YY format)")
    st.markdown("</div>", unsafe_allow_html=True)

# Section location (where work is requested)
work_location_from = st.text_input("Work Location From (XXX/YY format)")
work_location_to = st.text_input("Work Location To (XXX/YY format)")

# Demand time
time_from = st.time_input("Demand Time From (HH:MM)")
time_to = st.time_input("Demand Time To (HH:MM)")

# SIG Disconnection
sig_disconnection = st.radio("SIG Disconnection?", ["Yes", "No"], key="sig_disconnection")

# OH Disconnection with indented options
st.markdown("### OH Disconnection")
oh_disconnection = st.radio(" ", ["Yes", "No"], key="oh_disconnection")

if oh_disconnection == "Yes":
    st.markdown("<div style='margin-left: 20px;'>", unsafe_allow_html=True)
    elementary_section_from = st.text_input("Elementary Section From (XXX/YY format)")
    elementary_section_to = st.text_input("Elementary Section To (XXX/YY format)")
    st.markdown("</div>", unsafe_allow_html=True)

# Number of lines affected (excluding the selected line)
all_lines = ["Station 1", "Station 2", "Station 3", "Station 4", "Station 5"] if block_section == "Station" else ["Section 1", "Section 2", "Section 3", "Section 4", "Section 5"]
lines_affected = st.multiselect("Select Other Lines Affected", [l for l in all_lines if l != line])

# Submit button
if st.button("Submit"):
    st.success("Form submitted successfully!")
    st.write("Date:", date)
    st.write("Department:", department)
    st.write("Section:", section)
    st.write("Block Section:", block_section)
    st.write("Selected Line:", line)
    st.write("Work Description Type:", work_description_type)
    if work_description_type == "Mission Block":
        st.write("Mission Block Work Description:", mission_block_description)
    else:
        st.write("Non-Mission Block Work Description:", non_mission_block_description)
    st.write("Caution Required:", caution_required)
    if caution_required == "Yes":
        st.write("Speed of Caution:", speed)
        st.write("Caution Location From:", location_from)
        st.write("Caution Location To:", location_to)
    st.write("Work Location From:", work_location_from)
    st.write("Work Location To:", work_location_to)
    st.write("Demand Time From:", time_from)
    st.write("Demand Time To:", time_to)
    st.write("SIG Disconnection:", sig_disconnection)
    st.write("OH Disconnection:", oh_disconnection)
    if oh_disconnection == "Yes":
        st.write("Elementary Section From:", elementary_section_from)
        st.write("Elementary Section To:", elementary_section_to)
    st.write("Lines Affected:", lines_affected)
