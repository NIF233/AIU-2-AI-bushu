import sys
from .agent import Agent

def main():
    model = sys.argv[1] if len(sys.argv) > 1 else "qwen2.5"
    agent = Agent(model=model)
    print(f"🤖 Harness 已启动 (模型: {model})，输入 exit 退出。\n")
    while True:
        try:
            user_input = input("你: ")
            if user_input.strip().lower() == "exit":
                break
            result = agent.run(user_input)
            print(f"AI: {result}\n")
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()