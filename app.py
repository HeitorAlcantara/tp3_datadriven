import streamlit as st
import os
from dotenv import load_dotenv

# LLM
from langchain_google_genai import ChatGoogleGenerativeAI
# Agent
from langchain.agents import AgentExecutor, Tool, create_react_agent
# Prompt
from langchain.prompts import PromptTemplate 
# Memory
from langchain.memory import ConversationBufferMemory
from langchain_community.callbacks.streamlit import (
    StreamlitCallbackHandler,
)
# Tools
from langchain_experimental.tools import PythonREPLTool
from langchain_community.tools.wolfram_alpha import WolframAlphaQueryRun
# Utilities
from langchain_community.utilities.wolfram_alpha import WolframAlphaAPIWrapper

load_dotenv()
python_repl = PythonREPLTool()

st.title("🐍 Code and Science!")

def load_agent():
    """
    """
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    tools = tools = [
    Tool(
        name="wolfram_alpha",
        description="A wrapper around Wolfram Alpha. Useful for when you need to answer questions about Math, Science, Technology, Culture, Society and Everyday Life. Input should be a search query.",
        func=WolframAlphaQueryRun(api_wrapper=WolframAlphaAPIWrapper()).run,
    ),
    Tool(
        name="python_repl",
        description="A Python shell. Use this to execute python commands."
        " Input should be a valid python command. If you want to see"
        " the output of a value, you should print it out with `print(...)`.",
        func=python_repl.run,
    )
]
    
    prompt = """
        You are a helpful AI assistant that solves and create questions about math and science.

        If the input is on how to solve a question about math or science problem, you should solve and anwser the question. If the input is to create a question, there is no need to python code.

        Example:

        (How to solve a question)
        Input: What is 2x+5 = -3x + 7?
        Input: A bag contains 5 red marbles, 3 blue marbles, and 2 green marbles. If you randomly select two marbles without replacement, what is the probability that both marbles are red?
        Input: Find the derivative of the function f(x) = 3x² - 4x + 6

        (Create a question)
        Input: Create a mathematical question about first degree equations.
        Input: Give me 3 different math problems.
        Input: Create a physics question about Newton's second law of motion.

        You have the following tools at your disposal: {tool_names}.
        Description of the tools: {tools}.

        To use a tool, respond exactly in this format:
            Thought: [Your reasoning about that action to take next]
            Action: [The name of the tool to use next]
            Action Input: [The input to the action]
            Observation: [Observe whether the question is anwsered after the action is made]

        If the input is how to solve a question and the questions was awnsered, respond:
            Thought: The question was awnsered. I should create the python code.
            Final Answer: The final answer to the original input question and the python code.

        If the input is to create a question and the questions was created, respond:
            Thought: The question was created.
            Final Answer: The final answer to the original input.

        Input: {input}

        {agent_scratchpad}
        """
    prompt_template = PromptTemplate(
    input_variable=["input", "tool_names", "tools", "agent_scratchpad"],
    template=prompt
)
    agent = create_react_agent(llm=llm, prompt=prompt_template, tools=tools)
    return AgentExecutor(agent=agent,
                         tools=tools,
                         handle_parsing_errors=True,
                         verbose=True)


MEMORY = ConversationBufferMemory(
    memory_key="chat_history", return_messages=True, output_key="answer"
)

avatars = {
    "human": "user",
    "ai": "assistant"
}
for msg in MEMORY.chat_memory.messages:
    st.chat_message(avatars[msg.type]).write(msg.content)

agent_chain = load_agent()


# response = agent_executor.invoke({
#     "input": "What is 2x+5 = -3x + 7?",
#     "tool_names": [tool.name for tool in tools],
#     "tools": [tool.description for tool in tools],
# })

# print()
# print(response)

if prompt := st.chat_input(placeholder="Qual a sua dúvida?"):
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())
        response = agent_chain.invoke(
            {"input": prompt},
            {"callbacks": [st_callback]}
        )
        st.write(response["output"])