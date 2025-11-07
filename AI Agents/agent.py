# pip install langchain langchain-openai
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent
import glob

@tool
def find_text_files() -> str:
    """Return a comma-separated string of all files ending with .txt in the current directory."""
    txt_files = glob.glob("*.txt")
    return ', '.join(txt_files)

@tool
def read_text_file(file: str) -> str:
    """Read the text from a text file."""
    f = open(file, mode='r')
    return f.read()

@tool
def write_text_file(file: str, text: str) -> str:
    """Write text to a text file."""
    f = open(file, mode='w')
    f.write(text)

tools = [find_text_files ,write_text_file, read_text_file]
model = ChatOpenAI(model="gpt-5", api_key='')
system_prompt = ("You are a helpful assistant that reads the contents of text files in the current directory, and then shares your analysis of these contents in an output text file")
agent = create_agent(model=model, tools=tools, system_prompt=system_prompt)
   
human_prompt = input("Give the AI Agent instructions: \n")
result = agent.invoke({"messages": [{"role": "user", "content": human_prompt}]})
agent_response =  result['messages'][-1].content 
print(f"AI Agent: {agent_response}")