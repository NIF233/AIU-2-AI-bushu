class ConversationMemory:
    def __init__(self, max_messages=50):
        self.messages = []
        self.max_messages = max_messages

    def add(self, role, content):
        self.messages.append({"role": role, "content": content})

    def get_messages(self):
        return self.messages

    def maybe_compress(self, llm_client):
        """当消息过多时，压缩旧消息（简化版）"""
        if len(self.messages) > self.max_messages:
            # 保留最近 10 条，其余压缩为摘要
            old = self.messages[:-10]
            summary = llm_client.chat([
                {"role": "user", "content": f"用一句话总结以下对话：{old}"}
            ])["content"]
            self.messages = [
                {"role": "system", "content": f"之前的对话摘要：{summary}"}
            ] + self.messages[-10:]