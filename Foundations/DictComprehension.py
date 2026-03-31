# Dict Comprehemnsion

word_len = {word: len(word) for word in ["cat", "elephant", "Ox"]}

print(word_len)


score = 78
# if score >= 90:
#     grade = "A"
# elif score >= 75:
#     grade = "B"
# else:
#     grade = "C"
# Ternary (one-liner if/else)
status = "pass" if score >= 60 else "fail"