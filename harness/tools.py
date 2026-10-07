import subprocess
from pathlib import Path

# 工具注册表
TOOLS = {}

def tool(name, description, parameters):
    """工具装饰器：将函数注册为 Agent 可调用的工具"""
    def decorator(func):
        TOOLS[name] = {
            "type": "function",
            "function": {
                "name": name,
                "description": description,
                "parameters": parameters
            }
        }
        func.tool_name = name
        return func
    return decorator

@tool(
    name="read_file",
    description="读取指定路径的文件内容",
    parameters={
        "type": "object",
        "properties": {
            "path": {"type": "string", "description": "文件路径"}
        },
        "required": ["path"]
    }
)
def read_file(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")

@tool(
    name="write_file",
    description="将内容写入指定路径的文件",
    parameters={
        "type": "object",
        "properties": {
            "path": {"type": "string", "description": "文件路径"},
            "content": {"type": "string", "description": "要写入的内容"}
        },
        "required": ["path", "content"]
    }
)
def write_file(path: str, content: str) -> str:
    Path(path).write_text(content, encoding="utf-8")
    return f"已写入 {path}"

@tool(
    name="bash",
    description="执行 shell 命令并返回输出",
    parameters={
        "type": "object",
        "properties": {
            "command": {"type": "string", "description": "要执行的命令"}
        },
        "required": ["command"]
    }
)
def bash(command: str) -> str:
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout + result.stderr

def get_tool_schemas():
    """返回所有工具的定义，供 LLM 使用"""
    return list(TOOLS.values())

def execute_tool(name, args):
    """执行指定工具"""
    func = globals().get(name)
    if func and callable(func):
        return func(**args)
    return f"未知工具: {name}"