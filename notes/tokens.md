# Tokens 

## What is a token?

A token is the smallest piece of text that a Large Language Model (LLM) processes. 

A few examples would be: 
| Text | Possible Tokens |
|-------|----------------|
| Hello world | "Hello", " world" |
| ChatGPT is awesome | "Chat", "GPT", " is", " awesome" |

Models do not read words or sentences directly. They read tokens. 

---

## Why Are Tokens Important?

Tokens determine the following:
- How much information can fit into the model context window
- The cost of API calls
- How much memory is required

---

## What is a Context Window?

A contex window is the maximum number of tokens a model can remember during a conversation.

Example: If a model supports 128,000 tokens, anything beyond that limit may be forgetten. If you have one long chat with with a certain 
          AI engine going, at some point, it will not remember the whole conversation and it may even crash. 

## Key Takeaways 
- LLMs process tokens, not words
- Contect windows are measured in tokens
- More tokens generally means more cost and more memory usage 
