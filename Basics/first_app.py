import streamlit as st 

# Add title
st.title("My First Streamlit App")

# Add text
st.write("Hello. This is my first Streamlit app!")

# add a header
st.header("This Is a Header")

# add some markdown text
st.markdown("This is some **Hello AI Universe!** text.")

# 4. Core Concepts: Widgets & Display

# Streamlit works by running your Python script from top to bottom whenever something changes (like user input).

# Displaying Data:

# st.write(): A versatile command that can display text, numbers, DataFrames, plots, and more.

# st.markdown(): Display text formatted using Markdown.

# st.title(), st.header(), st.subheader(): Display text in different heading sizes.

# st.code(): Display code blocks.

# st.latex(): Display mathematical formulas.

# st.dataframe(), st.table(): Display tables (e.g., Pandas DataFrames).

# Interactive Widgets (Input): These allow users to interact with your app.

# st.button(): Creates a button. Returns True when clicked.

# st.text_input(): A single-line text input box.

# st.text_area(): A multi-line text input box.

# st.number_input(): Input for numerical values.

# st.selectbox(): A dropdown selection box.

# st.checkbox(): A checkbox.

# st.radio(): Radio buttons for selecting one option.

# st.slider(): A slider for selecting a range or value.

# st.file_uploader(): For uploading files.

# st.chat_input(): Specifically designed for chatbot input! (We'll use this later).

# Example: Try adding a text input and button to my_first_app.py: 


st.title("Interactive App")

# Get user input using a text input box
user_name = st.text_input("Enter your name:")

# Deisplay  a greeting if name is entered

if user_name:
    st.write(f"hello,{user_name}!")

# Add a button
if st.button("Click Me!"):
    st.write("How are you?")
else:
    st.write("waiting for you to click...")

# 5. Layout & Structure

# Organize your app's appearance:

# st.sidebar: Creates a collapsible sidebar on the left. 
# Great for options, navigation, or information that doesn't
#  need to be in the main area. 



#put the element on the side bar
add_selectbox = st.sidebar.selectbox(
    "How would you like to select your favorite device?",
    ("Mobile", "Laptop", "Tablet", "Desktop")
)

st.sidebar.write("You selected:", add_selectbox)
# Main area are here
st.title("Main app Area")
st.write("Content goes here.")


########## st.columns: Place elements side-by-side. ###############

col1,col2,col3 = st.columns(3) # create 3 equal width columns
with col1:
   st.header("Column 1")
   st.write("Content for column 1.")

with col2:
    st.header("Column 2")
    st.write("Button in Col 2.")

with col3:
    st.header("Colukmn 3")
    st.text_input("Enter something in column 3:")

######### st.exdpander: Create collapsible sections in the main area

with st.expander("Clecdi to see details."):
    st.write("Here is some detailed information inside the expander.")
    st.image("https://static.streamlit.io/examples/owl.jpg") # Example image
    # st.write("You can add any Streamlit component inside an expander.")
    # st.container(): Create an invisible container to group elements or insert elements 
    # out of order (useful for dynamic content like chat history).

############################################################################
# 6. State Management (Crucial for Chatbots!)

# The Problem: Every time you interact with a widget, Streamlit reruns your entire script from top to bottom. Local variables are reset on each rerun. How do you remember things like previous chat messages?

# The Solution: st.session_state

# st.session_state is a dictionary-like object that persists across reruns within a single user session.

# You can use it to store information like chat history, user login status, model parameters, etc.

# Example: A simple counter

# import streamlit as st

st.title("Session state Counter")

# Initiaslize the coount in the session state if it does not exist.
if 'couint' not in st.session_state:
    st.session_state.count = 0

# Increement button
if st.button("Increement"):
    st.session_state.count += 1

# display the current count
st.write("Count = ", st.session_state.count)



###########################################################
