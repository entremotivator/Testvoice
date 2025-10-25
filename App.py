import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AI Voice Assistant (Mic Checker)", page_icon="🎙️", layout="wide")

st.sidebar.title("🎧 AI Voice Assistant")
st.sidebar.info("Make sure to allow microphone access when prompted (Browser + macOS settings).")

# VAPI widget HTML (sidebar) - Fixed version
vapi_widget_html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100vh;
            overflow: hidden;
            background: transparent;
        }
        #vapi-container {
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
        }
    </style>
</head>
<body>
    <div id="vapi-container">
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
    </div>
    
    <!-- Load VAPI SDK Script -->
    <script src="https://unpkg.com/@vapi-ai/client-sdk-react/dist/embed/widget.umd.js" type="text/javascript"></script>
    
    <script>
        // Wait for script to load and initialize
        window.addEventListener('load', function() {
            console.log('VAPI widget loaded');
            
            // Give the widget time to initialize
            setTimeout(function() {
                const widget = document.querySelector('vapi-widget');
                if (widget) {
                    console.log('VAPI widget found:', widget);
                } else {
                    console.error('VAPI widget element not found');
                }
            }, 1000);
        });
        
        // Handle errors
        window.addEventListener('error', function(e) {
            console.error('Error loading VAPI:', e);
        });
    </script>
</body>
</html>
"""

with st.sidebar:
    components.html(vapi_widget_html, height=600, scrolling=False)

# Main content
st.markdown("## 🧠 AI Voice Assistant — Microphone Permission Checker")
st.markdown(
    "This page checks microphone permission and shows an actionable alert if access is blocked. "
    "Use the **Enable Mic** button to request mic access, or follow the macOS steps if your browser is blocked."
)

st.info(
    "If you previously denied mic access, open **System Settings → Privacy & Security → Microphone** and enable your browser (Chrome/Safari)."
)

# JS snippet that checks mic permission and shows overlay in the main Streamlit page
mic_check_html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        /* overlay styling */
        #mic-overlay {
            position: fixed;
            left: 0;
            right: 0;
            top: 12px;
            margin: 0 auto;
            max-width: 900px;
            z-index: 9999;
            background: linear-gradient(90deg, rgba(255,0,27,0.95), rgba(0,0,0,0.95));
            color: white;
            border-radius: 10px;
            padding: 14px;
            display: flex;
            gap: 12px;
            align-items: center;
            box-shadow: 0 8px 30px rgba(0,0,0,0.5);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial;
        }
        #mic-overlay .title { font-weight: 700; margin-right: 8px; }
        #mic-overlay .msg { flex: 1; font-size: 14px; line-height: 1.2; }
        #mic-overlay .btn {
            background: white;
            color: #000;
            border: none;
            padding: 8px 12px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
        }
        #mic-overlay .btn:hover {
            background: #f0f0f0;
        }
        #mic-overlay .btn.secondary {
            background: transparent;
            color: white;
            border: 1px solid rgba(255,255,255,0.3);
        }
        #mic-overlay .btn.secondary:hover {
            background: rgba(255,255,255,0.1);
        }
        #mic-overlay.hidden { display: none !important; }
    </style>
</head>
<body>
    <div id="mic-overlay" class="hidden" role="alert">
        <div style="display:flex; align-items:center;">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" style="margin-right:8px">
                <path d="M12 14c1.657 0 3-1.343 3-3V5c0-1.657-1.343-3-3-3s-3 1.343-3 3v6c0 1.657 1.343 3 3 3z" fill="#fff"/>
                <path d="M19 11a1 1 0 10-2 0c0 3.866-3.134 7-7 7s-7-3.134-7-7a1 1 0 10-2 0c0 4.971 4.029 9 9 9s9-4.029 9-9z" fill="#fff"/>
            </svg>
        </div>

        <div class="msg">
            <div class="title">Microphone access required</div>
            <div id="mic-msg-text">This app needs your microphone. Click "Enable Mic" to allow access, or open your browser/macOS settings if you previously denied permission.</div>
        </div>

        <div style="display:flex; gap:8px; align-items:center;">
            <button class="btn" id="enable-mic-btn">Enable Mic</button>
            <button class="btn secondary" id="reload-btn">Reload</button>
        </div>
    </div>

    <script>
    (function() {
        const overlay = document.getElementById('mic-overlay');
        const msgText = document.getElementById('mic-msg-text');
        const enableBtn = document.getElementById('enable-mic-btn');
        const reloadBtn = document.getElementById('reload-btn');

        async function showOverlay(reason) {
            if (reason) {
                msgText.innerText = reason;
            }
            overlay.classList.remove('hidden');
        }
        
        function hideOverlay() {
            overlay.classList.add('hidden');
        }

        // try Permissions API first
        async function checkPermission() {
            if (!navigator.permissions || !navigator.permissions.query) {
                // fallback to attempting to getUserMedia without prompting if possible
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                    stream.getTracks().forEach(track => track.stop()); // Stop the stream immediately
                    hideOverlay();
                } catch (err) {
                    showOverlay("Microphone blocked or not available. Click 'Enable Mic' to allow microphone access.");
                }
                return;
            }

            try {
                const status = await navigator.permissions.query({ name: 'microphone' });
                handleState(status.state);
                // listen for changes
                status.onchange = () => handleState(status.state);
            } catch (e) {
                // some browsers (older Safari) may not support query({name:'microphone'})
                console.log('Permission query not supported, trying getUserMedia');
                try {
                    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                    stream.getTracks().forEach(track => track.stop());
                    hideOverlay();
                } catch (err) {
                    showOverlay("Microphone blocked or not available. Click 'Enable Mic' to allow microphone access.");
                }
            }
        }

        function handleState(state) {
            console.log('Microphone permission state:', state);
            if (state === 'granted') {
                hideOverlay();
            } else if (state === 'prompt') {
                // user hasn't decided — show a gentle prompt
                showOverlay("Microphone permission not yet granted. Click 'Enable Mic' to trigger the browser permission prompt.");
            } else if (state === 'denied') {
                showOverlay("Microphone permission is blocked. Open your browser or macOS privacy settings and enable microphone access for this browser, then click Reload.");
            } else {
                showOverlay("Microphone status: " + state + ". Click 'Enable Mic' to try again.");
            }
        }

        // request microphone (triggers browser prompt)
        async function requestMicrophone() {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                // success - stop the stream immediately as we just needed permission
                stream.getTracks().forEach(track => track.stop());
                hideOverlay();
                alert('Microphone access granted! You can now use the voice assistant in the sidebar.');
            } catch (err) {
                // user denied or error
                showOverlay("Permission denied or microphone unavailable. If you previously denied, open macOS → System Settings → Privacy & Security → Microphone and enable your browser, then click Reload.");
                console.warn("getUserMedia error:", err);
            }
        }

        enableBtn.addEventListener('click', requestMicrophone);
        reloadBtn.addEventListener('click', () => location.reload());

        // initial check
        checkPermission();

        // Additional fallback: detect devices list change (some browsers update)
        if (navigator.mediaDevices && navigator.mediaDevices.addEventListener) {
            navigator.mediaDevices.addEventListener('devicechange', checkPermission);
        }
    })();
    </script>
</body>
</html>
"""

# Render the mic-checker HTML (full width at top of page)
components.html(mic_check_html, height=140, scrolling=False)
