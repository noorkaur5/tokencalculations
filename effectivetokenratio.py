import tiktoken
import re

# Example completion text
completion = """
def hello_world():
    print("Hello, world!")
    return 0
"""

# Choose the correct model tokenizer
encoding = tiktoken.encoding_for_model("gpt-4")

# Encode and get tokens/pieces
token_ids = encoding.encode(completion)
token_pieces = [encoding.decode([tid]) for tid in token_ids]

# Define regex patterns for meaningful content
meaningful_patterns = [
    r"^def\b",
    r"\breturn\b",
    r"\bif\b",
    r"\belse\b",
    r"[a-zA-Z_]+\(",   # function calls
    r"\*\b",           # operators
    r"=",
    r"\d+",            # numbers
]

compiled_patterns = [re.compile(p) for p in meaningful_patterns]

# Check each token piece
meaningful_tokens = 0
for piece in token_pieces:
    if any(p.search(piece.strip()) for p in compiled_patterns):
        meaningful_tokens += 1

total_tokens = len(token_pieces)
etr = meaningful_tokens / total_tokens if total_tokens > 0 else 0

print(f"Total tokens: {total_tokens}")
print(f"Meaningful tokens: {meaningful_tokens}")
print(f"Effective Token Ratio (ETR): {etr:.2f}")