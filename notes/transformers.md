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


## Attention Weights

Attention does not treat all tokens equally.

For every token being processed, the transformer assigns a numerical importance score (weight) to every other token.

Higher weights mean:

> "This token is important for understanding the current token."

Lower weights mean:

> "This token is less important."

Example:

Sentence:

> The dog chased the ball because it was excited.

When processing "it":

- dog → 0.80
- ball → 0.10
- chased → 0.05
- The → 0.05

Because "dog" receives the highest attention weight, the model determines that "it" most likely refers to the dog.

Attention weights allow transformers to capture context and relationships between tokens.

## Multi-Head Attention

A transformer does not perform attention only once.

Instead, it performs multiple attention operations in parallel. Each of these operations is called an attention head.

Each attention head can learn different relationships between tokens.

For example, one head may learn:

- Subject → Verb relationships

Another head may learn:

- Pronoun → Object relationships

Another head may learn:

- Long-range dependencies between distant tokens

Because multiple heads examine the same sentence from different perspectives, the transformer gains a richer understanding of the text.

This process is called Multi-Head Attention.

Example:

Sentence:

> Sarah gave John a book because he asked for it.

Different attention heads may learn:

- "he" → John
- "it" → book
- "gave" → Sarah

Using multiple attention heads allows transformers to capture many different relationships simultaneously.

## Positional Encoding

Transformers process tokens in parallel rather than one at a time.

Because of this, transformers do not inherently understand the order of words.

Positional encoding provides information about the position of each token in a sequence.

This allows the model to distinguish between sentences such as:

> Dog bites man.

and

> Man bites dog.

Although both sentences contain the same tokens, their meanings are very different because of word order.

Positional information is added to token embeddings before they are passed into the transformer.

Without positional encoding, a transformer would treat:

- "dog bites man"
- "man bites dog"

as nearly identical.

Positional encoding allows transformers to understand sequence order and preserve meaning.

### Embeddings vs. Positional Encoding

- Embeddings tell the model **what** a token means.
- Positional encoding tells the model **where** the token appears in the sequence.

The transformer uses both together to understand language accurately.
