class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def vote(self):
        self.votes += 1

class VoteTally:
    def __init__(self):
        self.candidates = []

    def add_candidate(self, name):
        self.candidates.append(Candidate(name))

    def vote_for_candidate(self, name):
        candidate = next((c for c in self.candidates if c.name == name), None)
        if candidate:
            candidate.vote()

    def get_candidate_names(self):
        return [candidate.name for candidate in self.candidates]

    def get_candidate_votes(self):
        return [candidate.votes for candidate in self.candidates]

    def total_votes(self):
        return sum(self.get_candidate_votes())

    def get_winner(self):
        if not self.candidates:
            return None
        max_votes = max(self.get_candidate_votes())
        winners = [candidate for candidate in self.candidates if candidate.votes == max_votes]
        if len(winners) == 1:
            return winners[0].name
        else:
            return "Tie"

