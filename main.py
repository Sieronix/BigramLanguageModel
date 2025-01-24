import pandas as pd
from collections import defaultdict, Counter
from visualize import launch_gui
import numpy as np

class BigramLanguageModel:
    def __init__(self):
        self.counts = defaultdict(Counter)
        self.vocab = set()

    def train(self, file_path):
        with open(file_path, "r") as file:
            text = file.read()

        words = text.split()

        for prev_word, next_word in zip(words[:-1], words[1:]):
            self.counts[prev_word][next_word] += 1
            self.vocab.add(prev_word)
            self.vocab.add(next_word)

    def predict_next_word(self, prev_word):
        if prev_word in self.counts:
            next_words = list(self.counts[prev_word].keys())
            probabilities = np.array(list(self.counts[prev_word].values())) / sum(self.counts[prev_word].values())
            return np.random.choice(next_words, p=probabilities)
        return None

    def generate_text(self, start_word, num_words=10):
        current_word = start_word
        text = [current_word]

        for _ in range(num_words - 1):
            next_word = self.predict_next_word(current_word)
            if next_word is None:
                break
            text.append(next_word)
            current_word = next_word

        return " ".join(text)

    def create_probability_table(self):
        data = []
        for prev_word, next_words in self.counts.items():
            total_count = sum(next_words.values())
            for next_word, count in next_words.items():
                prob = count / total_count
                data.append([prev_word, next_word, prob, count, total_count])

        return pd.DataFrame(data, columns=["Previous Word", "Next Word", "Probability", "Count", "Total Count"])


file_path = "..\\simple_language_model\\training_data.txt"
model = BigramLanguageModel()
model.train(file_path)
df = model.create_probability_table()

launch_gui(df, model)
