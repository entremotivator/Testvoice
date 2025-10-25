import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="AI Voice Assistant",
    page_icon="🎙️",
    layout="wide",
)

# Sidebar Header
st.sidebar.title("🎧 AI Voice Assistant")

# Add some optional sidebar widgets
st.sidebar.text_input("Your Name")
st.sidebar.selectbox("Topic", ["General Inquiry", "Support", "Sales", "Other"])
st.sidebar.button("Submit")

# Embed the VAPI widget inside sidebar
vapi_widget_html = """
<vapi-widget
  public-key="588f8e51-4057-4a7f-b247-28587afcf555"
  assistant-id="e092a75f-dcd8-4c16-8558-316542eb9c5e"
  mode="voice"
  theme="dark"
  base-bg-color="#000000"
  accent-color="#ff001b"
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
  voice-show-transcript="true"
  consent-required="true"
  consent-title="Terms and conditions"
  consent-content="By clicking 'Agree,' and each time I interact with this AI agent, I consent to the recording, storage, and sharing of my communications with third-party service providers, and as otherwise described in our Terms of Service."
  consent-storage-key="vapi_widget_consent"
></vapi-widget>

<script src="https://unpkg.com/@vapi-ai/client-sdk-react/dist/embed/widget.umd.js" async type="text/javascript"></script>
"""

# Render widget inside sidebar
with st.sidebar:
    components.html(vapi_widget_html, height=500)

# Main page content
st.markdown("## 🧠 Welcome to the AI Voice Assistant Demo")
st.markdown("""
This demo integrates the **VAPI voice agent** directly inside the Streamlit sidebar.  
You can interact with it by voice or chat — click **Start** to begin talking!
""")

st.info("Try switching topics from the sidebar to guide your conversation.")

