import streamlit as st 
st.title("Chat App")

# 7. Building a Basic Chat Interface
# Now let's apply these concepts to a chat UI. We'll use st.chat_input for user messages and st.chat_message
#  to display messages with nice styling. 

# Initialize the chat history in the session state 
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Add Clear Button to Sidebar --- <<< NEW SECTION
# st.header("Chat Options") # Add a header for clarity
# Create the button. The code inside the 'if' block runs ONLY when the button is clicked.
if st.button("Clear Chat History", key="clear_button"):
    st.session_state.messages = [] # Reset the messages list to empty
    st.success("Chat history cleared!") # Optional: show a success message
    # st.rerun() # Usually not needed as session state change triggers rerun,
                 # but uncomment if the chat doesn't clear immediately.

# Display past messages
# st.chat_manage create a container for a message with an icon
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message['content']) # use markdown for potential formatting 

# get the user inpout using chat_input 
#  the prompt text is display in the input box
if prompt := st.chat_input("What's Up! "):
    # add user message ito chat history
    st.session_state.messages.append({"role":"user", "content": prompt})

    # display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # (Simulate AI Response - we will add this next)
    # for now just display a place holder or echo 
     # Simulate AI response (for now, echo back the prompt)
    ai_response = f"Echo: {prompt}"
    with st.chat_message("assistant"):
        st.markdown(ai_response)

    # Add assistant response to the chat history
    st.session_state.messages.append({'role': 'assistant', 'content': ai_response})

  # Note: Streamlit automatically reruns after handling the input,
    # so the new messages display automatically.

