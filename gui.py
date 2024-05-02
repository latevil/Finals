import tkinter as tk
from vote_tally import VoteTally


class VoteGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Vote Tally Program")
        self.vote_tally = VoteTally()
        self.vote_tally.add_candidate("John")  # Add John as a candidate
        self.vote_tally.add_candidate("Jane")  # Add Jane as a candidate

        self.candidate_label = tk.Label(master, text="Candidates:")
        self.candidate_label.pack()

        self.selected_candidate = tk.StringVar()
        self.create_candidate_radio_buttons()

        self.vote_button = tk.Button(master, text="Vote", command=self.vote)
        self.vote_button.pack()

        self.results_label = tk.Label(master, text="Vote Tally Results:")
        self.results_label.pack()

        self.results_text = tk.Text(master, height=10, width=40)
        self.results_text.pack()

    def create_candidate_radio_buttons(self):
        candidate_names = self.vote_tally.get_candidate_names()
        for name in candidate_names:
            rb = tk.Radiobutton(self.master, text=name, variable=self.selected_candidate, value=name)
            rb.pack()

    def vote(self):
        selected_candidate = self.selected_candidate.get()
        if not selected_candidate:
            self.display_error("Please select a candidate before voting.")
            return

        if selected_candidate not in self.vote_tally.get_candidate_names():
            self.display_error("Invalid candidate selection. Please choose a valid candidate.")
            return

        self.vote_tally.vote_for_candidate(selected_candidate)
        self.update_results_display()

    def update_results_display(self):
        self.results_text.delete('1.0', tk.END)
        results = ""
        for name, votes in zip(self.vote_tally.get_candidate_names(), self.vote_tally.get_candidate_votes()):
            results += f"{name}: {votes}\n"
        self.results_text.insert(tk.END, results)

    def display_error(self, message):
        error_label = tk.Label(self.master, text=message, fg="red")
        error_label.pack()


def main():
    root = tk.Tk()
    app = VoteGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

