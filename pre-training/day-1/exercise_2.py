"""
Exercise 2 — Control Flow That Does Something Real
A grade_classifier function tested against a list of scores.
"""


def grade_classifier(score):
    """Return a grade string based on numeric score."""
    if score >= 90:
        return "Distinction"
    elif score >= 60:
        return "Pass"
    else:
        return "Fail"


scores = [45, 72, 91, 60, 38, 85]

print(f"{'Score':>6}  {'Result'}") # reserves 6 spaces and pushes the text to the right
print("-" * 20)

for score in scores:
    result = grade_classifier(score)