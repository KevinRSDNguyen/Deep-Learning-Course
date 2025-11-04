# pip install langchain langchain-openai
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent

@tool
def write_text_file(file: str, text: str) -> str:
    """Write text to a text file."""
    f = open(file, mode='w')
    f.write(text)

@tool
def read_text_file(file: str) -> str:
    """Read the text from a text file."""
    f = open(file, mode='r')
    return f.read()

tools = [write_text_file, read_text_file]
model = ChatOpenAI(model="gpt-4", api_key='')
system_prompt = ("You are a helpful assistant that reads the contents of text files, and then shares your transformation of these contents in an output text file")
agent = create_agent(model=model, tools=tools, system_prompt=system_prompt)
   
human_prompt = input("Give the AI Agent instructions: \n")
result = agent.invoke({"messages": [{"role": "user", "content": human_prompt}]})
agent_response =  result['messages'][-1].content 
print(f"AI Agent: {agent_response}")