import pysrt
import string


forbidden_list = ["fuck", "fucking", "shit", "dog", "fuck off"]

subs = pysrt.open("assets/sub.srt")
translator = str.maketrans("", "", string.punctuation)

result_words = []

arr = []


# more feature should be added
def censorhip(text):
    print(text)


def extract_sub():
    for sub in subs:
        arr.append(f"{sub.start} --> {sub.end}")
        arr.append(censorhip(sub.text))

    # return arr


arr = extract_sub()


# for sub in arr:
#     print(sub)


# for subs_text in arr:
#     words = subs_text.split()

#     for i in range(len(words)):
#         clean_words = words[i].translate(translator)

#         if clean_words.lower() in forbidden_list:

#             words[i] = words[i][:1] + "xx" + words[i][2:]

#     new_sub_text = " ".join(words)
#     result_words.append(new_sub_text)

# for sub_text in result_words:
#     print(sub_text)

# for i in range(len(result_words)):
#     print(result_words[i])
