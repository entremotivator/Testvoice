import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="AI CEO Voice Assistant",
    page_icon="🎙️",
    layout="wide"
)

# HTML with Vapi Widget and microphone access
vapi_html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            margin: 0;
            padding: 0;
            min-height: 100vh;
            background-color: #000000;
        }
    </style>
</head>
<body>
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
    
    <script>
        // Request microphone access when page loads
        window.addEventListener('load', async function() {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                console.log('Microphone access granted');
                // Keep the stream active
                window.audioStream = stream;
            } catch (error) {
                console.error('Microphone access denied:', error);
                alert('Please allow microphone access to use the voice assistant.');
            }
        });
    </script>
</body>
</html>
"""

# Render the widget
components.html(vapi_html, height=800, scrolling=False)
