import streamlit as st
import pandas as pd # use for data display
import time         # We'll use this for a demo later

# ___________Page Configuration ______________######
# Must be first streamlit command in your script
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
user_name = st.text_input("What is your name?", "Curious User") # Second value is default value

# Basic Output
st.write(f"Hello, **{user_name}**! Nice to meet you.")

st.divider() # Add a divider line


#___________Feature 1: Sidebar Navigation____________######
# Sidebar provides a dedicated place for controls or navigation
st.sidebar.header("App Options")
# The selectbox returns the chosen string, which we store in 'app_mode'
app_mode = st.sidebar.selectbox("Choose App Mode:",
                                ["Greeting", "Data Viewer", "More Widgets Demo", "File Uploader", "Advanced Options" ])
st.sidebar.write(f"You Selected: {app_mode}")

# Add some text to control the sidebar
st.sidebar.markdown("---") # Horizontal rule in sidebar
st.sidebar.button("Dummy Sidebar Button") # Dummy button to show the sidebar is interactive
st.sidebar.info("Sidebar can hold inputs, text, and navigation elements.")

# ___________Conditional Display Based on Sidebar Selection____________######
# We use the 'app_mode' variable to decide what to show in the main area.
# This makes the app feel like it has different 'pages' or sections.

if app_mode == "Greeting":
    st.header("👋 Greeting Section")
    st.info("Showing the Greeting section based on sidebar selection.")
    # We already have the greeting logic above, but you could add more here.
    st.write("This area changes based on what you pick in the sidebar!")

elif app_mode == "Data Viewer":
    st.header("📊 Data Viewer")
    st.info("Showing the Data Viewer mode.")
    # --- Feature 4: Displaying Data (added below) --- will appear here

elif app_mode == "More Widgets Demo":
    st.header("⚙️ More Widgets Demo")
    st.info("This section shows the Checkbox, Radio button, and Counter.")
    # --- Widgets Section (completed below) --- will appear here

elif app_mode == "File Uploader":
    st.header("📁 File Uploader")
    st.info("This section demonstrates the file uploader.")
    # --- Feature 5: File Uploader (added below) --- will appear here

else: # Corresponds to "Advanced Options"
    st.header("🛠️ Advanced Options")
    st.warning("Advanced Options Selected (no specific content defined yet)")
    st.write("You could add complex features or settings here.")

st.divider() # Add a divider line


# ___________Feature 2: Using Columns for Layout____________######
# Columns help organize content horizontally.
st.header("Layout with Columns")
col1, col2, col3 = st.columns(3) # Creates 3 columns of equal width

# You can also specify widths:
# col1, col2 = st.columns([2, 1]) # col1 is twice as wide as col2
# col1, col2 = st.columns([1, 2]) # col2 is twice as wide as col1

# Use 'with' statement to add content to each column
with col1:
    st.subheader("Column 1")
    st.write("Content for the first column.")
    if st.button("Button in Col 1"):
        st.success("Col 1 button Clicked!") # Use st.success for positive feedback
with col2:
    st.subheader('Column 2')
    st.write("More content here.")
    # Add another widget: A slider
    happiness = st.slider("Rate your Happiness:", 0, 10, 5) # min, max, default value
    st.write(f"Your Happiness: {happiness}/10 😊") # Added an emoji!

with col3:
    st.subheader("Column 3")
    st.write("Final column.")
    # Display an image from a URL
    st.image("https://static.streamlit.io/examples/cat.jpg", caption="A Cute Cat 🐈") # Example Image

st.divider()

# ___________Feature 3: More Widgets & Interactivity (Counter Completed)____________######
# We only show these widgets if the corresponding mode is selected in the sidebar
if app_mode == "More Widgets Demo":

    st.header("More Widgets & State")

    # Checkbox: Returns True if checked, False otherwise
    show_details = st.checkbox("Show Advanced Details")
    if show_details:
        st.write("Here are the advanced details you requested!")
        st.warning("Advanced details can be complex, proceed with caution!")

    # Radio Button: Returns the selected option
    fav_color = st.radio(
        "What is your Favorite color?",
        ("Blue 💙", "Green 💚", "Red ❤️"), # Added emojis
        index=0, # Default selection is the first item ("Blue")
        horizontal=True, # Display options side-by-side
    )
    st.write(f"Your favorite color is: {fav_color}")

    # --- Button with state (Counter example - Completed!) ---
    st.subheader("Button Interaction with Session State")
    st.write("This counter remembers its value even when other widgets change!")

    # Initialize the counter in st.session_state IF it doesn't exist yet
    # st.session_state is like a dictionary that persists across reruns
    if 'count' not in st.session_state:
        st.session_state.count = 0
        st.write("Counter Initialized!") # Show when it initializes

    # Create a button. The code inside the 'if' runs ONLY when the button is clicked.
    if st.button("Increment Counter"):
        st.session_state.count += 1 # Increase the value stored in session state
        st.success(f"Counter incremented to {st.session_state.count}") # Feedback

    # Display the current counter value (it reads from session_state)
    st.write(f"Button has been clicked **{st.session_state.count}** times.")

    # Add a reset button
    if st.button("Reset Counter"):
        st.session_state.count = 0 # Reset the value in session state
        st.info("Counter Reset!")
        # Optional: st.experimental_rerun() # Use if you need the display to update instantly after reset


# ___________Feature 4: Displaying Data with Pandas____________######
# This section will only be displayed if "Data Viewer" is selected in the sidebar
if app_mode == "Data Viewer":

    st.header("Displaying DataFrames")
    st.write("Streamlit works great with Pandas DataFrames!")

    # Create a sample DataFrame (Dictionary -> DataFrame)
    data = {
        'Column A': [1, 2, 3, 4, 5],
        'Column B': [10, 20, 30, 40, 50],
        'Column C': ['Apple', 'Banana', 'Orange', 'Grape', 'Mango']
    }
    df = pd.DataFrame(data)

    st.subheader("1. Interactive DataFrame (`st.dataframe`)")
    st.write("You can sort columns by clicking headers.")
    st.dataframe(df) # Displays the dataframe with scrolling and sorting

    st.subheader("2. Static Table (`st.table`)")
    st.write("Displays the entire table statically (good for small tables).")
    st.table(df.head(3)) # Display only the first 3 rows as a static table

    st.subheader("3. Write Command (`st.write`)")
    st.write("`st.write` can often figure out how to display things, including DataFrames:")
    st.write(df)


# ___________Feature 5: File Uploader____________######
# This section will only be displayed if "File Uploader" is selected
if app_mode == "File Uploader":

    st.header("File Upload Feature")
    st.write("Allow users to upload their own data (e.g., CSV).")

    # st.file_uploader returns None initially, or an UploadedFile object when a file is uploaded.
    # 'type' argument restricts allowed file extensions.
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # When a file is uploaded, uploaded_file is no longer None.
        st.success("File Uploaded Successfully!")
        st.write("Filename:", uploaded_file.name)
        st.write("File Type:", uploaded_file.type)
        st.write("File Size:", uploaded_file.size, "bytes")

        # Now, let's try to read it as a Pandas DataFrame
        try:
            df_uploaded = pd.read_csv(uploaded_file)
            st.write("Preview of the uploaded data:")
            st.dataframe(df_uploaded.head()) # Show the first 5 rows

            # You could add more features here, like showing statistics (df_uploaded.describe())
            # or letting the user select columns for plotting.

        except Exception as e:
            st.error(f"An error occurred while processing the file: {e}")
            st.warning("Please ensure the file is a valid CSV.")
    else:
        st.info("Upload a CSV file to see its contents here.")


# ___________Bonus Feature: Caching Example (Illustrative)____________######
st.divider()
st.header("Bonus: Function Caching")
st.write("Use `@st.cache_data` to speed up apps by storing results of expensive functions.")

@st.cache_data # This decorator tells Streamlit to cache the output
def slow_calculation(input_number):
    st.write(f"Running the slow calculation for input: {input_number}...") # This will only print when the function actually runs
    time.sleep(2) # Simulate a time-consuming task
    result = input_number * input_number
    return result

cache_input = st.number_input("Enter a number for cached calculation", 1, 10, 3)

if st.button("Run Calculation"):
    with st.spinner("Calculating..."): # Shows a nice spinner animation
        output = slow_calculation(cache_input)
    st.write(f"The square of {cache_input} is: {output}")
    st.info("Try clicking 'Run Calculation' again with the same number. Notice it's instant and the 'Running...' message doesn't appear, because the result was cached!")

st.divider()
st.write("--- End of App ---")
st.balloons() # Add some fun at the end!

'''
Explanation of Added/Completed Features:

Feature 3: Counter (Completed)

st.session_state: This is Streamlit's way to store variables across user interactions or script reruns. When you click a button or change a widget, Streamlit often reruns your entire script from top to bottom. st.session_state acts like a persistent dictionary to hold values (like our counter) between these reruns.

Initialization (if 'count' not in st.session_state:): We need to check if the count variable already exists in the session state. If not, we initialize it to 0. This prevents the counter from resetting every time the script reruns for other reasons.

Button Logic (if st.button(...)): The code inside this if block only runs when that specific button is clicked. Here, we increment st.session_state.count.

Displaying: We display the current value directly from st.session_state.count.

Feature 4: Displaying Data

Pandas Integration: Streamlit works seamlessly with Pandas DataFrames.

Sample Data: We create a simple DataFrame using pd.DataFrame().

st.dataframe(df): This displays the DataFrame as an interactive table where users can scroll and sort columns. Best for larger datasets.

st.table(df): This displays the DataFrame as a static table (no scrolling, all rows shown). Good for small summaries.

st.write(df): Often, st.write is smart enough to figure out how to display common objects like DataFrames, usually defaulting to st.dataframe.

Conditional Display: This whole section is wrapped in if app_mode == "Data Viewer": so it only shows when that mode is selected in the sidebar.

Feature 5: File Uploader

st.file_uploader(...): This widget allows users to browse and upload files from their computer.

type="csv": Restricts uploads to only files with the .csv extension. You can specify other types like ["csv", "txt", "xlsx"].

Checking for Upload (if uploaded_file is not None:): The widget returns None until a file is uploaded. We use this if check to proceed only after a file is present.

File Object: The uploaded_file object contains information like the filename, type, size, and importantly, the file's content (which you can read).

Reading the File (pd.read_csv(uploaded_file)): Pandas can directly read the uploaded file object.

Error Handling (try...except): It's good practice to wrap file processing in a try...except block in case the user uploads a corrupted or incorrectly formatted file.

Conditional Display: Again, wrapped in if app_mode == "File Uploader":.

Bonus: Caching

@st.cache_data: This is a "decorator". You put it right before a function definition (def ...:). It tells Streamlit: "If this function is called with the same input arguments as before, don't actually run the function again. Instead, just return the result you stored last time."

Why Cache?: Useful for functions that are slow (like loading a large dataset, running a complex calculation, or fetching data from an API). It makes your app much faster on subsequent runs with the same inputs.

Demonstration: The slow_calculation function has a time.sleep(2) to simulate slowness and a st.write message inside. When you run it with the same number multiple times, you'll see the 2-second delay and the message only the first time. Subsequent clicks are instant.

Feel free to run this code, play with the different modes in the sidebar, upload a sample CSV, and observe how the counter and caching work! This should give you a solid foundation for adding more complex features.
'''