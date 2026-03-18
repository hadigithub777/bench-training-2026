# Day 2 — Functions, Lists, Dicts

Focused on writing reusable functions and working with Python's two most common data structures.

## Scripts

### exercise_1.py — Word Frequency Counter
- `word_frequency(text)` strips punctuation, lowercases everything, and returns a `{word: count}` dict.
- Prints the top 5 most common words from a hardcoded paragraph using `sorted()`.

### exercise_2.py — Grade Book System
- 5 students stored as a list of dicts, each with name, scores, and subject.
- `calculate_average()`, `get_grade()`, `class_topper()` functions.
- Prints a formatted report sorted by average (descending). Top scorer is marked.

## How to Run

```bash
python3 exercise_1.py
python3 exercise_2.py
```

## Lists vs Dicts — When to Use Each

A list is for when you have a bunch of items and the order matters. Like a list of scores — you don't need to name each one, you just care about the sequence. You access stuff by position (index 0, 1, 2...).

A dict is for when each piece of data has a label. Like a student record — you want to look up "name" or "scores" by key, not by remembering that name is at index 0 and scores is at index 1. That would be fragile and confusing.

In practice I ended up using both together a lot. The grade book exercise is a good example: the students list is a *list* (because I have multiple students in order), but each student is a *dict* (because each one has named fields like name, scores, subject). That combo — list of dicts — comes up all the time.
