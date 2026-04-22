# 🤖 Gemini Chatbot

A sleek, full-stack AI chatbot web application powered by **Google Gemini 2.5 Flash**, built with **Flask** and a custom dark-themed frontend.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?style=flat-square&logo=flask)
![Gemini](https://img.shields.io/badge/Google%20Gemini-2.5%20Flash-4285F4?style=flat-square&logo=google)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## ✨ Features

- 💬 Real-time conversational AI using Google Gemini 2.5 Flash
- 🎨 Beautiful dark UI with ambient glow effects and smooth animations
- ⌨️ Auto-growing textarea with `Enter` to send, `Shift+Enter` for new line
- 💡 Suggestion chips on the welcome screen for quick prompts
- ⏳ Animated typing indicator while waiting for a response
- 🕐 Timestamped message bubbles for user and AI
- 🔌 Simple REST API backend (`/chat` endpoint) via Flask

---

## 📁 Project Structure

```
Chatbot/
├── app.py                  # Flask backend & Gemini API integration
├── requirements.txt        # Python dependencies
├── .gitignore
└── templates/
    └── index.html          # Frontend UI (HTML/CSS/JS)
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/kadirivinodkumar/Chatbot.git
cd Chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Activate it:
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Get your free API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_api_key_here
```

Then update `app.py` to load it securely:

```python
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
```

Install python-dotenv:

```bash
pip install python-dotenv
```

### 5. Run the app

```bash
python app.py
```

Open your browser and go to: **http://localhost:2005**

---

## 🖥️ How It Works

```
User types a message
        │
        ▼
  POST /chat  (JSON: { "message": "..." })
        │
        ▼
  Flask backend receives the message
        │
        ▼
  Google Gemini 2.5 Flash generates a response
        │
        ▼
  Response returned as JSON: { "reply": "..." }
        │
        ▼
  Frontend renders the AI reply in the chat UI
```

---

## 🔌 API Reference

### `POST /chat`

**Request body:**
```json
{
  "message": "What is machine learning?"
}
```

**Response:**
```json
{
  "reply": "Machine learning is a subset of AI that enables systems to learn from data..."
}
```

**Error response:**
```json
{
  "reply": "Gemini error"
}
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| AI Model | Google Gemini 2.5 Flash (`google-genai`) |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Fonts | Syne (display), DM Mono (body) |

---

## 📦 Dependencies

```
flask
google-genai
python-dotenv
```

---

## ⚠️ Security Note

Never commit your API key directly in source code. Always use environment variables or a `.env` file, and make sure `.env` is listed in your `.gitignore`.

---

## 🙋‍♂️ Author

**Kadiri Vinod Kumar**  
[GitHub](https://github.com/kadirivinodkumar)

---

*⭐ If you found this helpful, consider starring the repo!*
