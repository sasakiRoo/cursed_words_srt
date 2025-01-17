import pysrt

listOfWords = ["fuck", "fucking", "shit", "dog", "fuck off"]

subs = pysrt.open("assets/sub.srt")

for sub in subs:
    # print(f"{sub.index} --> {sub.start} to {sub.end}")
    arrs = []
    arrs.append(sub.text)
    for i in arrs:
        print(i)
    print(arrs)
