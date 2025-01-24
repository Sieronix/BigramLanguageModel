# **Simple Bigram Language Model**

This project implements a **bigram language model** that predicts and generates text based on word pairs. It includes a **user-friendly GUI** for visualizing word probabilities and generating sentences interactively. The model is designed to be simple, lightweight, and easy to use, making it ideal for learning purposes or small-scale text generation tasks.

---

## **Key Features**

1. **Bigram Model**:
   - Predicts the next word based on the previous word using probability distributions.
   - Trains on a text dataset to learn word pair frequencies.

2. **Probability Table**:
   - Displays word pair probabilities in a structured table format.
   - Allows searching and filtering by specific words.

3. **Sentence Generation**:
   - Generates sentences starting with a user-provided word.
   - Stops generating at sentence-ending punctuation (`.`, `!`, `?`).

4. **Interactive GUI**:
   - Built with Tkinter for a seamless user experience.
   - Provides a clean interface for searching probabilities and generating sentences.

---

## **System Architecture**

The project is divided into three main components:

1. **Model Training**:
   - Reads text data from a file (`training_data.txt`).
   - Tokenizes the text and builds bigrams (pairs of consecutive words).
   - Calculates probabilities for each word pair.

2. **GUI Interface**:
   - Displays the probability table in a scrollable and searchable format.
   - Allows users to input a starting word and generate sentences.

3. **Text Generation**:
   - Uses the trained bigram model to predict and generate text iteratively.
   - Stops generation when sentence-ending punctuation is encountered.

---

## **Use Cases**

- **Educational Tool**: Learn how language models work by experimenting with bigrams.
- **Text Generation**: Generate simple sentences for creative writing or prototyping.
- **Probability Visualization**: Explore word pair probabilities in a structured format.

---

## **Requirements**

- Python 3.x
- Libraries: `tkinter`, `pandas`, `numpy`

---

## **Usage**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/simple-language-model.git
   cd simple-language-model
