import string

# CLEAN FUNCTION: Clean txt file into a word list.
def clean_txt(raw_text):
    text = raw_text.replace("-", " ")
    text = text.replace("/", " ")

    words = text.split()

    cleaned_list = []

    for word in words:
        word = word.strip(string.punctuation).lower()
        if word.isdigit():
            continue
        if word.endswith("'s"):
            word = word[:-2]
        if word == "":
            continue
        cleaned_list.append(word)

    return cleaned_list