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

### Copy and paste any code from an AI model into the script:

```bash
"“Optimize this function for performance in Python:”

def sum_list(lst): total = 0 for i in range(len(lst)): total += lst[i] return total"
"""
```
