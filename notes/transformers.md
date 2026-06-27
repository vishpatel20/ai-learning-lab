# Transformers

## What Is a Transformer?

A transformer is a neural network architecture designed to understand relationships between tokens in a sequence.

Instead of reading text one word at a time, transformers look at many tokens together and decide which tokens are most important to each other.

This is what allows modern AI models to understand context.

## Why Transformers Matter

Transformers are the foundation of modern large language models.

They are important because they allow models to:
- Understand context
- Track relationships between words
- Handle long sequences of text
- Learn meaning from large amounts of data

## Simple Example

Sentence:

> The dog chased the ball because it was excited.

A transformer helps the model understand that “it” most likely refers to “the dog,” not “the ball.”

This happens through a mechanism called attention.

## Key Idea

Transformers do not just look at words.

They look at how words relate to each other.


## Attention

Attention is the mechanism that allows a transformer to determine which tokens are most important when processing a particular token.

For every token, the model asks:

> Which other tokens should I pay attention to?

The model assigns different importance (weights) to other tokens in the sequence.

Example:

Sentence:

> The dog chased the ball because it was excited.

When processing the token "it", attention may determine:

- dog → high importance
- ball → low importance

This allows the model to understand that "it" refers to the dog.


## Self-Attention

Self-attention is the mechanism that allows each token in a sequence to examine every other token in the same sequence.

For every token, the model asks:

> Which other tokens in this sentence are important to me?

The model then assigns weights to all other tokens and combines this information to produce a richer understanding of the token.

Example:

Sentence:

> The dog chased the ball.

When processing the token "dog", the model may pay attention to:

- chased
- ball
- The

This process helps the model understand context and relationships within the sentence.

Self-attention is one of the core innovations that made transformers successful.
