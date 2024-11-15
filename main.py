import string

def total_words(s: str) -> int:
    """Return the total word count of a string."""
    return len(s.split())

def count_chars(s: str) -> dict[str, int]:
    """Return a frequency table containing the counts of each 
    character in the string."""
    counts = {c: 0 for c in string.ascii_lowercase}
    for char in s.lower():
        if char in string.ascii_lowercase:
            counts[char] += 1
    return counts

def print_report(counts: dict[str, int], num_words: int, filepath: str) -> None:
    print(f"--- Begin report of {filepath} ---")
    print(f"{num_words} words found in the document\n")
    for char, count in counts.items():
        print(f"The {char} character was found {count} times")
    print("--- End report ---")

def main() -> None:
    filepath = "books/frankenstein.txt"
    with open(filepath, "r") as f:
        contents = f.read()
        num_words = total_words(contents)
        char_counts = count_chars(contents)
        print_report(char_counts, num_words, filepath)

if __name__ == "__main__":
    main()
