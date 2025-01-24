Simple Bigram Language Model
This project implements a bigram language model that predicts and generates text based on word pairs. It includes a user-friendly GUI for visualizing word probabilities and generating sentences interactively.

Features
Bigram Model: Predicts the next word based on the previous word using probability distributions.

Probability Table: Displays word pair probabilities in a structured table format.

Sentence Generation: Generates sentences starting with a user-provided word, stopping at sentence-ending punctuation (., !, ?).

Interactive GUI: Built with Tkinter, allowing users to search the probability table and generate sentences dynamically.

How It Works
Training:

The model reads text data from a file (training_data.txt).

It tokenizes the text into words and builds bigrams (pairs of consecutive words).

It calculates probabilities for each word pair.

GUI:

Search: Users can search the probability table for specific words.

Generate Sentences: Users can input a starting word, and the model generates a sentence based on the learned probabilities.

Text Generation:

The model generates sentences by predicting the next word iteratively.

It stops generating when it encounters sentence-ending punctuation (., !, ?).

Requirements
Python 3.x

Libraries: tkinter, pandas, numpy
