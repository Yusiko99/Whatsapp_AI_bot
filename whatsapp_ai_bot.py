import pyautogui
import time
import requests
import pyperclip
import keyboard

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

GEMINI_API_KEY = "your_gemini_api_key_here"
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

def get_gemini_response(prompt):
    try:
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": f"You are responding as a friend. Be natural, friendly and helpful. Keep responses short and casual. Respond to: {prompt}"
                        }
                    ]
                }
            ],
            "generationConfig": {
                "temperature": 0.8,
                "topK": 40,
                "topP": 0.95,
                "maxOutputTokens": 300,
            }
        }

        response = requests.post(
            f"{API_URL}?key={GEMINI_API_KEY}",
            json=payload,
            headers={'Content-Type': 'application/json'},
            timeout=30
        )
        response.raise_for_status()

        result = response.json()
        if result and "candidates" in result and len(result["candidates"]) > 0:
            bot_text = result["candidates"][0]["content"]["parts"][0]["text"]
            return bot_text.strip()
        else:
            return "Hey! 😊"
    except Exception as e:
        print(f"[ERROR] Error with Gemini API: {e}")
        return "Sorry, I'm having trouble right now"

def send_message(message):
    try:
        pyautogui.typewrite(message)
        time.sleep(0.5)
        
        pyautogui.press('enter')
        time.sleep(1)
        
        print(f"[SENT] Sent: {message}")
        return True
        
    except Exception as e:
        print(f"[ERROR] Error sending message: {e}")
        return False

def main():
    print("[BOT] Simple WhatsApp Bot Starting...")
    print("=" * 60)
    print("[INFO] Instructions:")
    print("1. Open WhatsApp desktop app")
    print("2. Go to some chat")
    print("3. Click in the message input box")
    print("4. Run this bot")
    print("5. When your contact sends a message:")
    print("   - Select/highlight her message")
    print("   - Press Ctrl+C to copy it")
    print("   - The bot will automatically respond!")
    print()
    print("[STOP] Press Ctrl+c to stop the bot")
    print("=" * 60)
    
    input("Press Enter when you're ready (WhatsApp open, in some chat, cursor in message box)...")
    
    print("[OK] Bot is now active! Waiting for messages...")
    print("[TIP] Copy your contact's messages with Ctrl+C and I'll respond automatically!")
    
    last_message = ""
    message_count = 0
    
    keyboard.add_hotkey('ctrl+shift+q', lambda: exit())
    
    while True:
        try:
            current_clipboard = pyperclip.paste().strip()
            
            if (current_clipboard and 
                current_clipboard != last_message and 
                len(current_clipboard) > 0 and 
                len(current_clipboard) < 1000 and
                not current_clipboard.startswith('http')):
                
                last_message = current_clipboard
                message_count += 1
                
                print(f"\n[MSG] Message #{message_count} from Nəzi:")
                print(f"   '{current_clipboard}'")
                print("[BOT] Generating response...")
                
                bot_response = get_gemini_response(current_clipboard)
                
                time.sleep(1)
                
                if send_message(bot_response):
                    print("[OK] Response sent!")
                    print(f"[BOT] Bot said: '{bot_response}'")
                else:
                    print("[ERROR] Failed to send response")
                
                print("\n[WAIT] Waiting for next message... (copy with Ctrl+C)")
                time.sleep(2)
            
            time.sleep(1)
            
        except KeyboardInterrupt:
            print("\n[STOP] Bot stopped!")
            break
        except Exception as e:
            print(f"[WARNING] Error: {e}")
            time.sleep(2)

if __name__ == "__main__":
    main()
