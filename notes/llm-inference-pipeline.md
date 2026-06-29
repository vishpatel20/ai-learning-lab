# LLM Inference Pipeline

## What Is Inference?

Inference is the process of using a trained Large Language Model (LLM) to generate a response from a user's input.

Unlike training, where the model learns from massive datasets, inference uses the already-trained model to make predictions.

Every time you interact with ChatGPT or another LLM, the model is performing inference.

---

## Step 1: User Prompt

Everything begins with a user entering a prompt.

Example:

> Explain quantum computing like I'm 10.

At this point, the model has not yet understood the text.

The prompt is simply a sequence of characters (letters, numbers, punctuation, and spaces).

Before the model can process it, the text must first be converted into tokens.


---

## Step 2: Tokenization

The application sends the user's raw text to a tokenizer.

The tokenizer converts the text into smaller pieces called tokens.

Example:

Input:

> Explain quantum computing like I'm 10.

Possible tokens:

- Explain
- quantum
- computing
- like
- I'm
- 10
- .

The exact tokens depend on the tokenizer used by the model.

At this stage, the model still does not understand the meaning of the text.

The tokenizer has only converted raw text into tokens.
