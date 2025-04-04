import streamlit as st 
import pandas as pd # use for data display 

# ___________Page Configuration ______________######
# Must be first strwmlit command in your script
st.set_page_config(
    page_title = "MY Custom App",
    page_icon = "🚀",
    layout = "centered", # can be wide or centered
    initial_sidebar_state = "expanded", # it can be 'auto', ' expanded', ' collapsed'
)

# ___________Main App Content______________######

st.title("🌟 My Simple Customizable App")
st.write("Welcome! Lets Add some features.")

# ___________Basic Input Widget: Text Input______________######
user_name = st.text_input("What is your name?", " Curious User") # Second value is default value

# Basic Output
st.write(f"Hello,**{user_name}**! Nice to meet you.")

st.divider() # Add a divider line

st.header("Let's explore customization!")
st.markdown("Below, we will add different feature step by step.")

#___________Feature 1: Sidebar Navigation____________######
st.sidebar.header("App Options")
app_mode = st.sidebar.selectbox("Choose App Mode:", ["Greeting","Data Viewer", "Advanced Options" ])
st.sidebar.write(f"You Selected: {app_mode}")

#  Add some text to controlo the sidebar
st.sidebar.markdown("______") # Devide the sidebar
st.sidebar.button("Dummy Sidebar Button") # Dummy button to show the sidebar is working
st.sidebar.write("This is a dummy button")

# You can display the different things in the main area based on the sidebar section

if app_mode == "Greeting":
    st.info("Showing the Greeting section.")

elif app_mode == "Data Viewer":
    st.info("Showing the Data Viewer mode(content below).")

else:
    st.warning("Advanced Options Selected (no content defined yet)")

st.divider() # Add a divider line

# ___________Feature 2: Using Columns for Layout____________######
# Create two columns

st.header("Layout with Columns")
col1, col2, col3 = st.columns(3)

# Yuo can also specify widths of the columns
# col1, col2 = st.columns([2, 1]) # 2:1 ratio
# col1, col2 = st.columns([1, 2]) # 1:2 ratio

with col1:
    st.subheader("Column 1")
    st.write("Content for the first column.")
    if st.button("Button in col 1"):
        st.write("Col1 button Cliecked!")
with col2:
    st.subheader('Column 2')
    st.write("More content here.")
    # add another widget
    happiness  = st.slider("Rate your Happiness:", 0, 10, 5) # min, max, default values
    st.write(f"Your Happiness: {happiness}/10")

with col3:
    st.subheader("column 3")
    st.write("Final column.")
    st.image("https://static.streamlit.io/examples/cat.jpg", caption="A Cute Cat") # Excample Image

st.divider()

# ___________Adding More Widgets & Interactivity____________######
# Let's add checkboxes, radio buttons, and make a button perform a specific action using st.session_state.
# Modify the code: 
st.header("More Widgets")

# Checkbox
show_details = st.checkbox("Show Advanced Details")
if show_details:
    st.write("Here are the advance details you requested!")
    st.warning("Advanced details can be complex.")

# Radio Button
fav_color = st.radio(
    "What is your Favorite color?",
    ("Blue", "Green", "Red"),
    index = 0, # Default value is Blue
    horizontal=True, # Display horizontally
)

st.write(f"Your favorite color is: {fav_color}")

# Button with state (simple Counter example)
st.subheader("Button Interaction")
# initialize counter 
# Initialize the counter in session_state if it doesn't exist yet
if "count" not in st.session_state:
    st.session_state.count = 0

# Button to increase the counter
if st.button("➕ Increase"):
    st.session_state.count += 1

# Button to decrease the counter
if st.button("➖ Decrease"):
    st.session_state.count -= 1

# Show the counter value
st.write(f"Current Count: {st.session_state.count}")