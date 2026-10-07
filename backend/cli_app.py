
import requests
import json

# ⚠️ 这里替换成你刚才复制的 API Key
API_KEY = "app-xxxxxxxxxx" 
BASE_URL = "http://localhost/v1"

def chat(query):
    resp = requests.post(
        f"{BASE_URL}/chat-messages",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "query": query,
            "inputs": {},
            "user": "cli-user",
            "response_mode": "streaming"
        },
        stream=True
    )
    
    for line in resp.iter_lines(decode_unicode=True):
        if line and line.startswith("data: "):
            event = json.loads(line[6:])
            if event.get("event") == "message":
                print(event["answer"], end="", flush=True)

if __name__ == "__main__":
    print("Dify CLI 已启动，输入 exit 退出。")
    while True:
        q = input("\n你: ")
        if q == "exit": break
        print("AI: ", end="")
        chat(q)
