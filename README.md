# OpenAI Tokenizer for CodeGPT

This repository contains an OpenAI tokenizer that interacts with OpenAI models (GPT-3.5, GPT-4, etc.) using the tiktoken library. The tokenizer provides a standard way to break down any AI-generated code the user inserts and returns a breakdown of tokens used and effective token ratio.

## Prerequisites

Before running the code, make sure you have the following:

- Python 3 installed
- `tiktoken` library installed

Optional: 
Create a CodeGPT Plus account to test a wider range of AI models: https://account.codegpt.co

## Installation

Clone the repository:

```bash
https://github.com/noorkaur5/tokencalculations
```

### Install the required libraries:

```bash
pip install tiktoken
```

Make sure Python and Tiktoken are installed in the same virtual environment to avoid any issue of not being able to detect imports.

### Choose Your Script:

There are two scripts you can choose from.
| Script Name        | Tokenization              | Meaningfulness Judgment                                  | Summary                                                                                                |
|---------------------|---------------------------|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| `manual_etr.py`    | Automated (via tiktoken) | Manual (e.g., human labels each token as meaningful or not) | Gives transparency, useful for benchmarking regex logic                                                 |
| `automated_etr.py` | Automated (via tiktoken) | Automated (e.g., uses regex to classify tokens)         | Scalable and faster, but depends on the quality of heuristics                                          |

## Copy and Paste any code from an AI model into the Script:

### Example: manual_etr.py
```bash
# Example: simulate a model's completion
completion_text = "Here is the Python function:\n```python\ndef square(n): return n * n\n```"
```
### Your result will be:
Prompt tokens: 29
--- Prompt breakdown ---
[system] You are a helpful assistant.
Tokens: [2675, 527, 264, 11190, 18328, 13]
Pieces: ['You', ' are', ' a', ' helpful', ' assistant', '.']

[user] Write a Python function that returns the square of a number.
Tokens: [8144, 264, 13325, 734, 430, 4780, 279, 9518, 315, 264, 1396, 13]
Pieces: ['Write', ' a', ' Python', ' function', ' that', ' returns', ' the', ' square', ' of', ' a', ' number', '.']

Completion tokens: 19
--- Completion breakdown ---
Tokens: [8586, 374, 279, 13325, 734, 512, 74694, 12958, 198, 755, 9518, 1471, 1680, 471, 308, 353, 308, 198, 74694]
Pieces: ['Here', ' is', ' the', ' Python', ' function', ':\n', '```', 'python', '\n', 'def', ' square', '(n', '):', ' return', ' n', ' *', ' n', '\n', '```']
Total tokens: 48

### Example: automated_etr.py
```bash
# Example completion text
completion = """
Optimizing the Sum List Function in Python
Here's the original function:

python
def sum_list(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    return total
Optimized Solutions (from fastest to slowest):
1. Using Built-in sum() Function
python
def sum_list(lst):
    return sum(lst)
This is the most efficient solution as Python's built-in sum() function is implemented in C and highly optimized.

2. Using Direct Iteration
python
def sum_list(lst):
    total = 0
    for item in lst:
        total += item
    return total
If you can't use the built-in sum() function, direct iteration is more efficient than using indices because:

It avoids the overhead of index lookups
It eliminates the need for the range() function and length calculation
3. Using NumPy (for numerical arrays)
python
import numpy as np

def sum_list(lst):
    return np.sum(lst)
This is extremely fast for large numerical arrays but has the overhead of importing NumPy.

Performance Comparison:
For a list with 10 million integers:

Method	Relative Speed
Built-in sum()	Fastest (baseline)
Direct iteration	~1.5x slower
Original function	~2x slower
NumPy sum	Fastest for large arrays, but has import overhead
Why These Optimizations Work:
Built-in functions are implemented in C and highly optimized
Direct iteration avoids index lookups and range generation
NumPy uses vectorized operations and is optimized for numerical computations
The original function was inefficient because it:

Used unnecessary indexing
Created a range object with the length of the list
Performed repeated lookups into the list
For most Python applications, the built-in sum() function is the best choice for summing a list.
"""
```

### Your result will be:
Total tokens: 377
Meaningful tokens: 21
Effective Token Ratio (ETR): 0.06
