import pysrt
import string
import random

forbidden_list = ["fuck", "fucking", "shit", "dog", "fuck off"]

subs = pysrt.open("assets/sub.srt")
translator = str.maketrans("", "", string.punctuation)

result_words = []

arr = []


def extract_sub():
    for sub in subs:
        arr.append(sub.text)
    return arr


arr = extract_sub()


def select_random_string_pos(word):
    get_length_of_word = len(word)
    print(get_length_of_word)
    print(word)
    x_num = random.randint(0, 2)
    return x_num


for subs_text in arr:
    words = subs_text.split()

    for i in range(len(words)):
        clean_words = words[i].translate(translator)

        if clean_words.lower() in forbidden_list:
            words[i] = (
                words[i][: select_random_string_pos(words[i])]
                + "xx"
                + words[i][select_random_string_pos(words[i]) :]
            )

    new_sub_text = " ".join(words)
    result_words.append(new_sub_text)

for sub_text in result_words:
    print(sub_text)
