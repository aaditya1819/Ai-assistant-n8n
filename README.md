# ⚡ Neural Logic AI Assistant

A high-end, professional AI Personal Assistant built with **Streamlit** and powered by **n8n Automation**. This assistant orchestrates complex workflows including web search, calendar management, email handling, and more through a sleek, modern interface.

![Modern UI](https://img.shields.io/badge/UI-Modern_Professional-blueviolet)
![Power](https://img.shields.io/badge/Powered_by-n8n-orange)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red)

## ✨ Key Features

*   **🌐 Real-time Web Search**: Access global information instantly via automated search nodes.
*   **📅 Precision Calendar**: Seamlessly manage meetings and events through Google Calendar integration.
*   **📧 Intelligent Inbox**: AI-powered email summarization and automated replies via Gmail.
*   **💰 Expense Tracking**: Automated monitoring and analysis of personal finances.
*   **📝 Neural Notes**: Rapid idea capture and organized note-taking.
*   **⚡ Workflow Orchestration**: Dynamic task creation and deletion across your preferred productivity apps.

## 🎨 Design Highlights

*   **Quantum Glassmorphism**: High-end translucent UI elements.
*   **Kinetic Hover Effects**: Animated, responsive capability cards in the sidebar.
*   **Animated Dynamics**: Smooth slide-in chat transitions and a "System Online" pulse indicator.
*   **Premium Typography**: Professional font pairing using *Outfit* and *Inter*.

## 🛠️ Tech Stack

*   **Frontend**: Streamlit
*   **Backend Automation**: n8n (self-hosted or cloud)
*   **Styling**: Custom Vanilla CSS with RGB-Glow Mesh Gradients
*   **API Management**: REST API via Python Requests

## 🚀 Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/aaditya1819/Ai-assistant-n8n.git
cd Ai-assistant-n8n
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Secrets
Create a `.streamlit/secrets.toml` file in the root directory:
```toml
N8N_WEBHOOK_URL = "your_n8n_webhook_url_here"
```

### 4. Launch the Assistant
```bash
streamlit run app.py
```

## 🔒 Security

This project uses Streamlit's native secrets management to ensure your n8n credentials remain private. Never commit your `secrets.toml` to version control.

---
Built with ❤️ by [Aaditya](https://github.com/aaditya1819)
