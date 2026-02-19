import streamlit as st
import requests
import time

# Page configuration
st.set_page_config(
    page_title="Personal AI Assistant | Pro",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Advanced CSS for High-End Professional UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&family=Inter:wght@300;400;600&display=swap');
    
    :root {
        --primary: #6366f1;
        --primary-glow: rgba(99, 102, 241, 0.4);
        --secondary: #a855f7;
        --bg-dark: #020617;
        --card-bg: rgba(30, 41, 59, 0.7);
        --accent: #22d3ee;
    }

    /* Global Styles */
    .stApp {
        background: radial-gradient(circle at top right, #1e1b4b, transparent),
                    radial-gradient(circle at bottom left, #0f172a, #020617);
        color: #e2e8f0;
        font-family: 'Inter', sans-serif;
    }

    h1, h2, h3 {
        font-family: 'Outfit', sans-serif !important;
    }

    /* Sidebar Glassmorphism */
    section[data-testid="stSidebar"] {
        background: rgba(15, 23, 42, 0.6) !important;
        backdrop-filter: blur(20px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
    }

    /* Modern Title with Animation */
    .hero-title {
        background: linear-gradient(to right, #6366f1, #a855f7, #22d3ee);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 3.5rem;
        letter-spacing: -0.02em;
        margin-bottom: 0px;
        animation: fadeIn 1s ease-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Feature Cards with Hover Effects */
    .feature-card {
        background: var(--card-bg);
        padding: 1.2rem;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        margin-bottom: 1rem;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: default;
        position: relative;
        overflow: hidden;
    }

    .feature-card:hover {
        transform: translateY(-5px) scale(1.02);
        border-color: var(--primary);
        box-shadow: 0 10px 30px -10px var(--primary-glow);
        background: rgba(30, 41, 59, 0.9);
    }

    /* Animated Status Dot */
    .status-container {
        display: flex;
        align-items: center;
        gap: 8px;
        background: rgba(34, 211, 238, 0.1);
        padding: 4px 12px;
        border-radius: 20px;
        width: fit-content;
        margin-bottom: 20px;
        border: 1px solid rgba(34, 211, 238, 0.2);
    }

    .dot {
        height: 8px;
        width: 8px;
        background-color: #22d3ee;
        border-radius: 50%;
        display: inline-block;
        box-shadow: 0 0 12px #22d3ee;
        animation: pulse 2s infinite;
    }

    @keyframes pulse {
        0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(34, 211, 238, 0.7); }
        70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(34, 211, 238, 0); }
        100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(34, 211, 238, 0); }
    }

    /* Chat Styling */
    .stChatMessage {
        background: rgba(15, 23, 42, 0.4) !important;
        border-radius: 20px !important;
        padding: 1.5rem !important;
        margin-bottom: 1.2rem !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        animation: slideIn 0.4s ease-out;
    }

    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-10px); }
        to { opacity: 1; transform: translateX(0); }
    }

    .stChatMessage[data-testid="stChatMessageAssistant"] {
        border-left: 4px solid var(--primary) !important;
        background: rgba(99, 102, 241, 0.05) !important;
    }

    /* Chat Input Bar */
    .stChatInputContainer {
        border-radius: 24px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        background: rgba(15, 23, 42, 0.8) !important;
        padding: 5px !important;
        backdrop-filter: blur(10px);
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: transparent;
    }
    ::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(255, 255, 255, 0.2);
    }
    
    /* Hide Default Header */
    header { visibility: hidden; }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='color: white; margin-bottom: 5px;'>⚡ Quantum AI</h2>", unsafe_allow_html=True)
    
    # Status Indicator
    st.markdown("""
    <div class="status-container">
        <span class="dot"></span>
        <span style="color: #22d3ee; font-size: 0.8rem; font-weight: 600;">System Online</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='color: #94a3b8; font-size: 0.9rem;'>Connected to n8n Engine</p>", unsafe_allow_html=True)
    
    st.divider()
    
    # Capability Cards
    caps = [
        ("🌐", "Web Search", "Real-time global information access."),
        ("📅", "Calendar Access", "Precision event syncing & management."),
        ("📧", "Gmail Access", "Intelligent email orchestration & replies."),
        ("💰", "Expense Tracking", "Neural financial monitoring & analysis."),
        ("📝", "Notes Creation", "Instant idea capture & organization."),
        ("⚡", "Task Management", "Dynamic creation & deletion of workflows."),
    ]
    
    for icon, title, desc in caps:
        st.markdown(f"""
        <div class="feature-card">
            <div style="font-size: 1.4rem; margin-bottom: 8px;">{icon}</div>
            <div style="font-weight: 600; color: white;">{title}</div>
            <div style="font-size: 0.8rem; color: #94a3b8; line-height: 1.4;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
    if st.button("🗑️ Clear Neural Memory", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# --- MAIN UI ---
st.markdown('<h1 class="hero-title">Neural Logic Assistant</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #64748b; font-size: 1.2rem; margin-top: -10px; margin-bottom: 40px;">Next-generation workflow automation</p>', unsafe_allow_html=True)

# Message History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- INPUT & RESPONSE ---
if prompt := st.chat_input("Command your assistant..."):
    # Length check for stability
    if len(prompt) > 15000:
        st.warning("⚠️ Oversized Command: This prompt is exceptionally large and may cause the neural link to fail. Consider breaking it into smaller commands.")
    
    # Display user input
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)


    # Bot response
    with st.chat_message("assistant"):
        msg_area = st.empty()
        msg_area.markdown("""
        <div style="display: flex; align-items: center; gap: 10px;">
            <div class="dot" style="margin: 0;"></div>
            <span style="color: #94a3b8; font-style: italic;">Synchronizing with neural nodes...</span>
        </div>
        """, unsafe_allow_html=True)
        
        try:
            # Use Streamlit secrets for deployment, fallback to env for local
            n8n_url = st.secrets.get("N8N_WEBHOOK_URL", "https://aaditya1819k.app.n8n.cloud/webhook/5cf15705-3cc7-47fc-b5db-c829151b435d")
            
            response = requests.post(
                n8n_url,
                json={"message": prompt},
                timeout=60 # Increased timeout for larger prompts
            )
            
            if response.status_code == 200:
                if not response.text:
                    ans = "No response received from the neural node. The prompt might be too large or the workflow didn't return data."
                else:
                    try:
                        data = response.json()
                        # Determine response content
                        if isinstance(data, list) and len(data) > 0 and "output" in data[0]:
                            ans = data[0]["output"]
                        elif isinstance(data, dict) and "output" in data:
                            ans = data["output"]
                        else:
                            ans = f"Signal acquired, but data format is irregular. Response: {response.text[:200]}"
                    except ValueError:
                        ans = f"The neural node returned a non-JSON response: {response.text[:500]}"
                
                # Update UI
                msg_area.markdown(ans)
                st.session_state.messages.append({"role": "assistant", "content": ans})
            elif response.status_code == 413:
                msg_area.error("⚠️ Payload Too Large: The prompt you provided is too big for the neural connection.")
            elif response.status_code == 504:
                msg_area.error("⚠️ Gateway Timeout: The neural node took too long to process this large request.")
            else:
                msg_area.error(f"⚠️ Node Connection Error: Code {response.status_code}. Details: {response.text[:200]}")
        
        except requests.exceptions.Timeout:
            msg_area.error("🕒 Neural Request Timed Out: The process took too long. Try a shorter prompt.")
        except Exception as e:
            msg_area.error(f"🚫 Neural Link Failed: {str(e)}")


# Bottom Spacer
st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)