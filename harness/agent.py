import json
from .llm import OllamaClient
from .tools import get_tool_schemas, execute_tool
from .memory import ConversationMemory

class Agent:
    def __init__(self, model="qwen2.5", max_turns=10):
        self.llm = OllamaClient(model=model)
        self.memory = ConversationMemory()
        self.max_turns = max_turns
        # 注入系统提示词
        self.memory.add("system", "你是一个AI助手，可以使用工具来完成任务。")

    def run(self, user_input):
        """Agent 主循环"""
        self.memory.add("user", user_input)
        tools = get_tool_schemas()

        for turn in range(self.max_turns):
            # 1. 调用模型
            response = self.llm.chat(self.memory.get_messages(), tools)
            
            # 2. 检查是否有工具调用
            if "tool_calls" in response and response["tool_calls"]:
                for tool_call in response["tool_calls"]:
                    name = tool_call["function"]["name"]
                    
                    # 3. 兼容 Ollama 格式和 OpenAI 格式的参数处理
                    raw_args = tool_call["function"]["arguments"]
                    if isinstance(raw_args, str):
                        args = json.loads(raw_args)
                    else:
                        args = raw_args
                        
                    print(f"  🔧 调用工具: {name}({args})")
                    result = execute_tool(name, args)
                    
                    # 将工具结果加入对话历史
                    self.memory.add("assistant", f"调用工具 {name}，参数 {args}")
                    self.memory.add("tool", str(result))
                continue  # 继续循环，让模型基于工具结果再推理
            else:
                # 4. 没有工具调用，输出最终答案
                answer = response["content"]
                self.memory.add("assistant", answer)
                return answer

        return "达到最大轮次限制，未完成任务。"