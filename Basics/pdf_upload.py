import streamlit as st
import fitz  # PyMuPDF library
import io      # To handle byte stream for PyMuPDF

# --- Basic Setup ---
st.title("Chat & PDF App")

# Initialize chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []
# Initialize extracted PDF text if it doesn't exist
if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = None
# Initialize a flag to know if a PDF has been processed in this session
if "pdf_processed" not in st.session_state:
    st.session_state.pdf_processed = False

# --- PDF Upload Section in Main Area --- <<< MOVED HERE
st.subheader("Upload and Process PDF")

# Use columns for a cleaner layout: uploader on left, button on right
col1, col2 = st.columns([3, 1]) # Make first column wider

with col1:
    uploaded_pdf = st.file_uploader(
        "Upload your PDF here", type="pdf", key="pdf_uploader_main", label_visibility="collapsed" # Hide label if subheader is enough
    )

with col2:
    # Process PDF Button - appears next to the uploader
    process_button_clicked = st.button(
        "Process PDF",
        key="process_pdf_button_main",
        disabled=(uploaded_pdf is None), # Disable if no file is uploaded
        use_container_width=True # Make button fill column width
    )

# Processing logic remains largely the same, but uses st.* for messages
if process_button_clicked: # Check if the button in the main area was clicked
    if uploaded_pdf is not None:
        try:
            pdf_bytes = uploaded_pdf.getvalue()
            pdf_stream = io.BytesIO(pdf_bytes)

            with st.spinner(f"Processing '{uploaded_pdf.name}'..."):
                doc = fitz.open(stream=pdf_stream, filetype="pdf")
                extracted_text = ""
                for page_num in range(len(doc)):
                    page = doc.load_page(page_num)
                    extracted_text += page.get_text()
                doc.close()

            st.session_state.pdf_text = extracted_text
            st.session_state.pdf_processed = True
            st.success(f"Successfully processed '{uploaded_pdf.name}'!") # Use st.success
            st.info(f"Extracted {len(st.session_state.pdf_text)} characters.") # Use st.info
            st.session_state.messages = [{"role": "assistant", "content": "PDF processed. How can I help you with its content?"}]
            # Force a rerun to update the chat display immediately after processing
            st.rerun()

        except Exception as e:
            st.error(f"Error processing PDF: {e}") # Use st.error
            st.session_state.pdf_text = None
            st.session_state.pdf_processed = False
    # No need for an 'else' here as the button is disabled if uploaded_pdf is None

# --- Sidebar (Optional: Keep Clear Button Here) ---
st.sidebar.header("Chat Options")
# Clear Chat History Button (Keeping this in the sidebar for now)
if st.sidebar.button("Clear Chat History", key="clear_chat_sidebar"):
    st.session_state.messages = []
    st.session_state.pdf_text = None # Also clear PDF state if desired
    st.session_state.pdf_processed = False
    st.success("Chat history and PDF context cleared!")
    st.rerun() # Rerun to update UI immediately


# --- Display Chat History ---
st.subheader("Conversation")
# Display a message if PDF is processed but no messages yet
if st.session_state.pdf_processed and not st.session_state.messages:
     st.session_state.messages = [{"role": "assistant", "content": "PDF processed. How can I help you with its content?"}]

# Display all messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message['content'])

# --- Handle User Input ---
prompt = st.chat_input("Ask something about the PDF or chat normally...")

if prompt:
    # Add user message to history and display
    st.session_state.messages.append({"role":"user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- Simulate AI Response (Potentially using PDF context) ---
    ai_response = ""
    if st.session_state.pdf_processed and st.session_state.pdf_text:
        ai_response = f"Echo (with PDF context): {prompt}\n\n(Context length: {len(st.session_state.pdf_text)} chars)"
    else:
        ai_response = f"Echo: {prompt}"

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(ai_response)

    # Add AI response to history
    st.session_state.messages.append({'role': 'assistant', 'content': ai_response})

# Display info if PDF hasn't been uploaded/processed yet (adjust message slightly)
if not st.session_state.pdf_processed and uploaded_pdf is None:
     st.info("Upload a PDF above and click 'Process PDF' to chat about its content.")
elif not st.session_state.pdf_processed and uploaded_pdf is not None:
     st.info("Click the 'Process PDF' button above to analyze the uploaded file.")