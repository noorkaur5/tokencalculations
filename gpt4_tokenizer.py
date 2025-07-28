import tiktoken

# Example messages
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Write a Python function that returns the square of a number."}
]

# Example model (can also use "gpt-3.5-turbo")
model = "gpt-4"

encoding = tiktoken.encoding_for_model(model)

def count_message_tokens(messages, model="gpt-4"):
    encoding = tiktoken.encoding_for_model(model)
    tokens_per_message = 3  # includes role & formatting tokens
    tokens_per_name = 1     # if a name field is used
    total_tokens = 0
    for message in messages:
        total_tokens += tokens_per_message
        for key, value in message.items():
            total_tokens += len(encoding.encode(value))
            if key == "name":
                total_tokens += tokens_per_name
    total_tokens += 3  # priming
    return total_tokens

def breakdown_text(text):
    token_ids = encoding.encode(text)
    pieces = [encoding.decode([t]) for t in token_ids]
    return token_ids, pieces

prompt_tokens = count_message_tokens(messages)

print(f"Prompt tokens: {prompt_tokens}")
print("--- Prompt breakdown ---")
for msg in messages:
    print(f"[{msg['role']}] {msg['content']}")
    ids, pieces = breakdown_text(msg['content'])
    print(f"Tokens: {ids}")
    print(f"Pieces: {pieces}")
    print()

# Example: simulate a model's completion
completion_text = "Here is the Python function:\n```python\ndef square(n): return n * n\n```"

completion_token_ids, completion_pieces = breakdown_text(completion_text)
completion_tokens = len(completion_token_ids)

print(f"Completion tokens: {completion_tokens}")
print("--- Completion breakdown ---")
print(f"Tokens: {completion_token_ids}")
print(f"Pieces: {completion_pieces}")

total_tokens = prompt_tokens + completion_tokens
print(f"Total tokens: {total_tokens}")
