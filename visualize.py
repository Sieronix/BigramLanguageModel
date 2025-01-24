import tkinter as tk
from tkinter import ttk

class ProbabilityTableApp:
    def __init__(self, root, df, model):
        self.root = root
        self.df = df
        self.model = model

        self.root.title("Probability Table Viewer")
        self.root.geometry("1200x800")

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.search_label = tk.Label(root, text="Search:")
        self.search_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.search_entry = tk.Entry(root, width=50)
        self.search_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.search_entry.bind("<Return>", lambda event: self.search_table())

        self.search_button = tk.Button(root, text="Search", command=self.search_table)
        self.search_button.grid(row=0, column=2, padx=10, pady=10, sticky="e")

        self.tree = ttk.Treeview(root, columns=("Previous Word", "Next Word", "Probability", "Count", "Total Count"), show="headings")
        self.tree.heading("Previous Word", text="Previous Word")
        self.tree.heading("Next Word", text="Next Word")
        self.tree.heading("Probability", text="Probability (%)")
        self.tree.heading("Count", text="Count")
        self.tree.heading("Total Count", text="Total Count")
        self.tree.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.scrollbar.grid(row=1, column=3, sticky="ns")
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.load_table()

        self.sentence_frame = tk.Frame(root)
        self.sentence_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        self.sentence_label = tk.Label(self.sentence_frame, text="Generate a sentence starting with:")
        self.sentence_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.sentence_entry = tk.Entry(self.sentence_frame, width=50)
        self.sentence_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.sentence_entry.bind("<Return>", lambda event: self.generate_sentence())

        self.generate_button = tk.Button(self.sentence_frame, text="Generate", command=self.generate_sentence)
        self.generate_button.grid(row=0, column=2, padx=10, pady=10, sticky="e")

        self.sentence_output = tk.Text(self.sentence_frame, height=5, width=80, wrap="word")
        self.sentence_output.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

    def load_table(self):
        for _, row in self.df.iterrows():
            formatted_row = list(row)
            formatted_row[2] = f"{row.iloc[2] * 100:.2f}%"
            self.tree.insert("", "end", values=formatted_row)

    def search_table(self):
        search_term = self.search_entry.get().strip().lower()
        if not search_term:
            self.tree.delete(*self.tree.get_children())
            self.load_table()
            return

        filtered_df = self.df[self.df["Previous Word"].str.lower().str.contains(search_term)]

        self.tree.delete(*self.tree.get_children())
        for _, row in filtered_df.iterrows():
            formatted_row = list(row)
            formatted_row[2] = f"{row.iloc[2] * 100:.2f}%"
            self.tree.insert("", "end", values=formatted_row)

    def generate_sentence(self):
        start_word = self.sentence_entry.get().strip()
        if not start_word:
            self.sentence_output.delete(1.0, tk.END)
            self.sentence_output.insert(tk.END, "Please enter a word to start the sentence.")
            return

        generated_sentence = self.model.generate_text(start_word, num_words=20)
        self.sentence_output.delete(1.0, tk.END)
        self.sentence_output.insert(tk.END, generated_sentence)

def launch_gui(df, model):
    root = tk.Tk()
    ProbabilityTableApp(root, df, model)
    root.mainloop()
