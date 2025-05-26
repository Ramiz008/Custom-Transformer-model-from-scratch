# Transformer from Scratch (Minimal Dataset)

This project implements a Transformer model architecture **from scratch using PyTorch**, inspired by the original "Attention is All You Need" paper. It is trained on a **small dummy dataset** (few English to French sentence pairs) for the **purpose of testing architecture and understanding** — not production translation.

##  Files

- `Transformer_Training.ipynb`: Contains architecture, training loop, and dummy dataset.
- `Transformer_Inference.ipynb`: For testing inference using trained weights.
- `requirements.txt`: List of dependencies used.

##  Highlights

- Encoder-decoder architecture with custom Multi-Head Attention.
- Positional encoding, masking, and custom training loop implemented.
- Fully implemented in PyTorch without using high-level libraries like HuggingFace.

##  Note

- The model is trained on **very limited data**, so output is random/meaningless.
- Purpose is to demonstrate **working knowledge of Transformers**, not build a production translation system.


---

## 💡 Example Output

> Input: `hello world`  
> Output: `- de en▁are cette in leur leur de en` _(random dummy tokens)_

## 📌 Author

Made with 💻 by [Ramiz Raza]

