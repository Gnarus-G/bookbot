def count_words(text):
    return len(text.split())

def count_chars(text):
    counts = {}
    for char in text:
        c = char.lower()
        counts[c] = counts.get(c, 0) + 1
    return counts

def main():
    filename = "books/frankenstein.txt"
    print(f"--- Begining report of {filename} ---")

    with open(filename) as f:
        contents = f.read()
        wordcount = count_words(contents)
        print(f"{wordcount} words found in the document")
        print()

        charcount = count_chars(contents)

        counts = list(map(lambda tupl: ({"name":tupl[0],"count": tupl[1]}), charcount.items()))

        counts.sort(reverse=True, key=lambda value: value["count"])

        for value in counts:
            char = value["name"]
            if char.isalpha():
                print(f"The '{char}' character was found {value["count"]} times")

        print("-- End Report --")



main()
