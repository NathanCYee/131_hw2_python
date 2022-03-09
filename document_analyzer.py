def count_words(input_str: str) -> dict:
    diced: list[str] = input_str.split()
    counted_words: dict = {}
    for word in diced:
        # actual_word = ''.join([c for c in word if c.isalnum()]).lower()  # remove all nonalphanumeric chars
        if word in counted_words:
            counted_words[word] += 1
        else:
            counted_words[word] = 1
    return counted_words


with open('document.txt') as f:  # open the file
    vals = count_words(f.read())
    # sort from most to least first(negative) then by lexicographic order in tuple
    sorted_words = sorted(vals.items(), key=lambda val: (-val[1], val[0]))
    for i in range(0, 5):
        print(f"{sorted_words[i][0]}: {sorted_words[i][1]}")
