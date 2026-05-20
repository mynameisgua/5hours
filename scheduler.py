import anthropic
import schedule
import time
from datetime import datetime

client = anthropic.Anthropic()  # 會自動讀取環境變數 ANTHROPIC_API_KEY

def say_hi():
    print(f"\n[{datetime.now()}] 開新 session...")
    
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=200,
        messages=[{"role": "user", "content": "嗨！"}]
    )
    
    print(f"Claude 回覆：{response.content[0].text}")

schedule.every(5).hours.do(say_hi)

say_hi()  # 啟動時先跑一次

print("Scheduler 啟動，每 5 小時會開新 session...")

while True:
    schedule.run_pending()
    time.sleep(60)