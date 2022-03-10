def count_words(input_str: str) -> dict:
    diced: list[str] = input_str.split()  # get the individual words to count
    counted_words: dict = {}
    for word in diced:
        if word in counted_words:  # increase the count
            counted_words[word] += 1
        else:  # new discovery, add it to the dictionary
            counted_words[word] = 1
    return counted_words


with open('document.txt') as f:  # open and close the file safely
    vals = count_words(f.read())  # pass a string version of file contents into the function
    print("")  # format the output
    # sort from most to least first(negative) then by lexicographic order in tuple
    sorted_words = sorted(vals.items(), key=lambda val: (-val[1], val[0]))
    for i in range(0, 5):
        print(f"{sorted_words[i][0]}: {sorted_words[i][1]}")
