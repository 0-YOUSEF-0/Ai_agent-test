import argparse
from dotenv import load_dotenv
import os
from openai import OpenAI
from prompts import system_prompt
from call_function import available_functions, call_function
import json

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise RuntimeError("OPENAI_API_KEY environment variable is not set")

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
)

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
]

response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages,
    tools=available_functions,
    temperature=0,
)



if response.usage is None:
    raise RuntimeError("Response usage is None")

if args.verbose:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")

message = response.choices[0].message

if message.tool_calls:
    for tool_call in message.tool_calls:
        result_message = call_function(tool_call, args.verbose)

        if not result_message["content"]:
            raise RuntimeError("Function call returned empty content")

        if args.verbose:
            print(f"-> {result_message['content']}")
else:
    print(message.content)
