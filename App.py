import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="AI CEO Voice Assistant",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar widgets
st.sidebar.title("⚙️ Settings")
st.sidebar.markdown("---")

# Text input widget
user_name = st.sidebar.text_input("Your Name", placeholder="Enter your name")

# Select box widget
conversation_mode = st.sidebar.selectbox(
    "Conversation Mode",
    ["Voice", "Chat", "Both"]
)

# Slider widget
voice_speed = st.sidebar.slider("Voice Speed", 0.5, 2.0, 1.0, 0.1)

# Radio buttons
language = st.sidebar.radio(
    "Preferred Language",
    ["English", "Spanish", "French", "German"]
)

# Checkbox widget
show_transcript = st.sidebar.checkbox("Show Transcript", value=True)

# Color picker
accent_color = st.sidebar.color_picker("Accent Color", "#ff001b")

st.sidebar.markdown("---")

# Button widget
if st.sidebar.button("Reset Settings"):
    st.rerun()

# File uploader widget
uploaded_file = st.sidebar.file_uploader("Upload Document", type=["pdf", "txt", "docx"])

st.sidebar.markdown("---")
st.sidebar.info("💡 Use the voice assistant below to interact with AI CEO")

# Main content area
st.title("🎙️ AI CEO Voice Assistant")
st.markdown("### Welcome to the Interactive Voice Experience")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Active Users", "1,234", "+12%")
with col2:
    st.metric("Conversations", "5,678", "+23%")
with col3:
    st.metric("Satisfaction", "98%", "+2%")

st.markdown("---")

# Display user settings
if user_name:
    st.success(f"👋 Hello, {user_name}!")

st.write(f"**Current Mode:** {conversation_mode}")
st.write(f"**Voice Speed:** {voice_speed}x")
st.write(f"**Language:** {language}")

# Vapi Widget HTML
vapi_html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{
            margin: 0;
            padding: 20px;
            min-height: 600px;
        }}
    </style>
</head>
<body>
    <vapi-widget
        public-key="588f8e51-4057-4a7f-b247-28587afcf555"
        assistant-id="e092a75f-dcd8-4c16-8558-316542eb9c5e"
        mode="voice"
        theme="dark"
        base-bg-color="#000000"
        accent-color="{accent_color}"
        cta-button-color="#000000"
        cta-button-text-color="#ffffff"
        border-radius="large"
        size="full"
        position="bottom-right"
        title="TALK WITH AICEO"
        start-button-text="Start"
        end-button-text="End Call"
        chat-first-message="Hey, How can I help you today?"
        chat-placeholder="Type your message..."
        voice-show-transcript="{'true' if show_transcript else 'false'}"
        consent-required="true"
        consent-title="Terms and conditions"
        consent-content="By clicking "Agree," and each time I interact with this AI agent, I consent to the recording, storage, and sharing of my communications with third-party service providers, and as otherwise described in our Terms of Service."
        consent-storage-key="vapi_widget_consent"
    ></vapi-widget>
    
    <script src="https://unpkg.com/@vapi-ai/client-sdk-react/dist/embed/widget.umd.js" async type="text/javascript"></script>
</body>
</html>
"""

st.markdown("---")
st.subheader("🎯 Voice Assistant Interface")

# Embed the Vapi widget
components.html(vapi_html, height=650, scrolling=True)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        <p>Powered by Vapi AI | Built with Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)
