# Transformer from Scratch (Minimal Dataset) 
 **Self-attention please:** If it helped you — **consider leaving a ⭐. It motivates and helps others discover it!**

This project implements a Transformer model architecture **from scratch using PyTorch**, inspired by the original "Attention is All You Need" paper. It is trained on a **small dummy dataset** (few English to French sentence pairs) for the **purpose of testing architecture and understanding** — not production translation.

## Why this project matters

This project implements Transformer architecture from scratch (without Huggingface/nn.Transformer), showing step-by-step how attention, positional encoding, and decoding are used in a real translation task. Useful for learning and interview-ready understanding.


##  Files

- `transformers_archi.ipynb`: Contains architecture
- `Inference.ipynb`: For testing inference using trained weights contains training loop, and dummy dataset.
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

> 💡 If this repo helped you understand Transformers better, please consider leaving a ⭐!
