"""
Exercise 1 — Word Frequency Counter
Takes a paragraph, counts how often each word appears, prints the top 5.
"""

import string


def word_frequency(text):
    text = text.lower()

    # strip out punctuation so "world." and "world" count the same
    for ch in string.punctuation:
        text = text.replace(ch, "")

    words = text.split()
    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1

    return freq


paragraph = (
    "Python is a great language for beginners and experts alike. "
    "Many people learn Python as their first language because the syntax "
    "is clean and easy to read. Once you learn the basics of Python you "
    "can build web apps, scripts, data pipelines, and more. The community "
    "around Python is huge and there are thousands of libraries to help "
    "you get things done. Learning a language is not just about syntax "
    "though — you need to practice writing real code every single day."
)

counts = word_frequency(paragraph)

# sort by count descending, grab top 5
top_5 = sorted(counts.items(), key=lambda item: item[1], reverse=True)[:5]

print("Top 5 most common words:")
print("-" * 25)
for rank, (word, count) in enumerate(top_5, start=1):
    print(f"  {rank}. {word:>10} — {count} times")
