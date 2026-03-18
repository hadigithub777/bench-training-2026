"""
Exercise 2 — Grade Book System
5 students stored as list of dicts, with average, grade, and a formatted report.
"""


def calculate_average(scores):
    return sum(scores) / len(scores)


def get_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"


def class_topper(students):
    best = students[0]
    for s in students[1:]:
        if calculate_average(s["scores"]) > calculate_average(best["scores"]):
            best = s
    return best["name"]


students = [
    {"name": "Ayesha",  "scores": [88, 76, 95, 82], "subject": "CS"},
    {"name": "Bilal",   "scores": [72, 68, 74, 80], "subject": "CS"},
    {"name": "Fatima",  "scores": [91, 94, 89, 97], "subject": "CS"},
    {"name": "Omar",    "scores": [55, 63, 58, 60], "subject": "CS"},
    {"name": "Zainab",  "scores": [80, 85, 78, 90], "subject": "CS"},
]

topper = class_topper(students)

# build report rows without touching the original list
rows = []
for s in students:
    avg = calculate_average(s["scores"])
    grade = get_grade(avg)
    label = " *** TOP ***" if s["name"] == topper else ""
    rows.append((s["name"], avg, grade, label))

# sort by avg descending
rows_sorted = sorted(rows, key=lambda r: r[1], reverse=True)

print(f"{'Student':<12} {'Avg':>6}  {'Grade':<5}")
print("-" * 32)
for name, avg, grade, label in rows_sorted:
    print(f"{name:<12} {avg:>6.1f}  {grade:<5}{label}")
