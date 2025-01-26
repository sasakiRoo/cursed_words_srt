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

    positions = random.sample(range(len(word)), 2)
    return sorted(positions)


for subs_text in arr:
    words = subs_text.split()

    for i in range(len(words)):
        clean_words = words[i].translate(translator)

        if clean_words.lower() in forbidden_list:
            positions = select_random_string_pos(words[i])
            x = positions[0]
            y = positions[1]
            print("x: ", x, "y: ", y)

            words[i] = words[i][:x] + "xx" + words[i][y:]

    new_sub_text = " ".join(words)
    result_words.append(new_sub_text)

for sub_text in result_words:
    print(sub_text)
