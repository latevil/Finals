def vote_menu() -> str:
    """Display the vote menu and return the user's selection."""
    while True:
        option = input("V: Vote\nX: Exit\nOption: ").strip().lower()
        if option in ('v', 'x'):
            return option
        print("Invalid (v/x):", option)


def candidate_menu() -> int:
    """Display the candidate menu and return the user's selection."""
    candidates = {'1': 'john', '2': 'jane'}
    while True:
        candidate = input("Candidate Menu\n1: John\n2: Jane\nCandidate: ").strip()
        if candidate in candidates:
            return int(candidate)
        print("Invalid (1/2):", candidate)


def main():
    """Keep track of the vote count and display the final output."""
    vote_counts = {'john': 0, 'jane': 0}

    while True:
        option = vote_menu()

        if option == 'x':
            break

        candidate = candidate_menu()
        candidate_name = 'john' if candidate == 1 else 'jane'
        vote_counts[candidate_name] += 1

        print(f"Voted {candidate_name.capitalize()}")

    total_votes = sum(vote_counts.values())
    print(f"John - {vote_counts['john']}, Jane - {vote_counts['jane']}, Total - {total_votes}")


if __name__ == "__main__":
    main()

