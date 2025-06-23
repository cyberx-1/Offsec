# -------------------------------
# 👤 Coded by: Mohammad Almahamid
# 🐦 Twitter: @j6_mu
# -------------------------------

import time
import requests
import random

def generate_random_username(length):
    letters = "qwertyuioplkjhgfdsazxcvbnm._"
    return ''.join(random.choice(letters) for _ in range(length))

def send_to_telegram(bot_token, chat_id, message):
    if not bot_token or not chat_id:
        print("❌ Bot token or chat ID not provided.")
        return

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {'chat_id': chat_id, 'text': message}
    try:
        response = requests.post(url, data=data)
        if response.status_code != 200:
            print(f"❌ Failed to send to Telegram: {response.text}")
    except Exception as e:
        print(f"❌ Error sending to Telegram: {e}")

def user_ins(num_users, username_length, bot_token, chat_id):
    url = 'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/'
    
    for _ in range(num_users):
        user = generate_random_username(username_length)

        headers = {
            'Host': 'www.instagram.com',
            'Cookie': 'csrftoken=vB0rkDeOJWDh2ctPFiXRjMJzRMbR0wV7; wd=375x640;',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X)',
            'Referer': 'https://www.instagram.com/accounts/signup/username/',
            'X-IG-App-ID': '1217981644879628',
            'X-ASBD-ID': '129477',
            'X-CSRFToken': 'vB0rkDeOJWDh2ctPFiXRjMJzRMbR0wV7',
            'Origin': 'https://www.instagram.com',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Site': 'same-origin',
            'X-Instagram-AJAX': '1015625738',
            'Accept-Language': 'ar',
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Encoding': 'gzip, deflate, br',
            'Sec-Fetch-Mode': 'cors'
        }

        data = {
            'enc_password': '',
            'username': user,
            'email': '',
            'client_id': 'Zrnm6AAAAAGrhVCY-4iexGkrQafH',
            'seamless_login_enabled': '1',
            'tos_version': 'row',
            'force_sign_up_code': ''
        }

        try:
            response = requests.post(url, headers=headers, data=data)
            if response.status_code == 200:
                result = response.json()
                if 'errors' in result and 'username' in result['errors']:
                    print(f"❌ Username not available: {user}")
                else:
                    print(f"✅ Available: {user}")
                    send_to_telegram(bot_token, chat_id, f"✅ Available: {user}")
            else:
                print(f"⚠️ HTTP Error: {response.status_code}")
        except Exception as e:
            print(f"❌ Request Error: {e}")
        
        time.sleep(4)

# === MAIN ===
bot_token = input("Enter your Telegram bot token: ").strip()
chat_id = input("Enter your Telegram chat ID: ").strip()

try:
    num_users = int(input("How many usernames to check?: "))
    username_length = int(input("Length of each username: "))
except ValueError:
    print("❌ Please enter valid numbers.")
    exit()

user_ins(num_users, username_length, bot_token, chat_id)