# 🤖 WhatsApp AI Bot

<div align="center">

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

*An intelligent WhatsApp bot powered by Google's Gemini AI that automatically responds to messages with natural, friendly conversations.*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Configuration](#-configuration) • [Contributing](#-contributing)

</div>

---

## 🌟 Features

- **🧠 AI-Powered Responses**: Uses Google's Gemini 1.5 Flash model for intelligent, contextual replies
- **💬 Natural Conversations**: Responds like a friendly human with casual, helpful messages
- **⚡ Real-time Processing**: Automatically detects new messages and responds instantly
- **🎯 Smart Filtering**: Ignores URLs and overly long messages to maintain conversation quality
- **🔧 Easy Setup**: Simple configuration with minimal dependencies
- **⌨️ Hotkey Controls**: Quick stop functionality with Ctrl+Shift+Q
- **📊 Message Tracking**: Counts and logs all processed messages

## 🚀 How It Works

1. **Message Detection**: Monitors clipboard for copied WhatsApp messages
2. **AI Processing**: Sends messages to Gemini AI for natural response generation
3. **Auto-Reply**: Types and sends AI-generated responses automatically
4. **Continuous Loop**: Keeps running until manually stopped

## 📋 Prerequisites

- Python 3.7 or higher
- WhatsApp Desktop application
- Google Gemini API key
- Windows/macOS/Linux (tested on Windows)

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Yusiko99/Whatsapp_AI_bot.git
cd whatsapp-ai-bot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Get Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Replace the API key in `whatsapp_ai_bot.py`:
```python
GEMINI_API_KEY = "your-api-key-here"
```

## 🎯 Usage

### Quick Start

1. **Open WhatsApp Desktop**
   - Launch the WhatsApp desktop application
   - Navigate to the chat where you want the bot to respond

2. **Position Your Cursor**
   - Click in the message input box
   - Make sure the cursor is ready to type

3. **Run the Bot**
   ```bash
   python whatsapp_ai_bot.py
   ```

4. **Start Chatting**
   - When someone sends a message, select/highlight it
   - Press `Ctrl+C` to copy the message
   - The bot will automatically generate and send a response!

### Controls

- **Stop Bot**: Press `Ctrl+Shift+Q` at any time
- **Copy Message**: Use `Ctrl+C` to copy messages for the bot to respond to

## ⚙️ Configuration

### AI Response Settings

You can customize the AI behavior by modifying these parameters in the `get_gemini_response()` function:

```python
"generationConfig": {
    "temperature": 0.8,      # Creativity level (0.0-1.0)
    "topK": 40,             # Token selection diversity
    "topP": 0.95,           # Nucleus sampling
    "maxOutputTokens": 300, # Maximum response length
}
```

### Message Filtering

The bot automatically filters messages based on:
- **Length**: Ignores messages over 1000 characters
- **Content**: Skips URLs and links
- **Duplicates**: Won't respond to the same message twice

## 📁 Project Structure

```
whatsapp-ai-bot/
│
├── whatsapp_ai_bot.py    # Main bot script
├── requirements.txt      # Python dependencies
└── README.md            # Project documentation
```

## 🔧 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `pyautogui` | 0.9.54 | GUI automation for typing and clicking |
| `requests` | 2.31.0 | HTTP requests to Gemini API |
| `pyperclip` | 1.8.2 | Clipboard monitoring and management |
| `keyboard` | 0.13.5 | Global hotkey detection |

## 🚨 Important Notes

### Security
- **API Key**: Keep your Gemini API key secure and never commit it to version control
- **Permissions**: The bot requires accessibility permissions on macOS

### Usage Guidelines
- **Rate Limits**: Be mindful of Gemini API rate limits
- **Privacy**: Only use in chats where all participants consent
- **Testing**: Test thoroughly before using in important conversations

### Troubleshooting

**Bot not responding?**
- Ensure WhatsApp Desktop is open and focused
- Check that the cursor is in the message input box
- Verify your API key is valid

**Messages not being detected?**
- Make sure you're copying messages with `Ctrl+C`
- Check that the copied text isn't too long (>1000 chars)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This bot is for educational and personal use only. Please:
- Respect WhatsApp's Terms of Service
- Use responsibly and ethically
- Obtain consent from chat participants
- Be mindful of privacy and data protection
---

<div align="center">

**Made by Yusikome and Python**

*If you found this project helpful, please consider giving it a ⭐!*

</div>
