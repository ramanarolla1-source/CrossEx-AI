"""
CrossEx AI
Contradiction Analysis Module

Detects simple inconsistencies within
witness statements and affidavits.

This is a prototype implementation for
the Anna AI-Native App Hackathon.
"""

def detect_contradictions(statement):
"""
Analyze a witness statement and
identify potential contradictions.

```
Parameters
----------
statement : str

Returns
-------
list
    List of detected contradictions.
"""

contradictions = []

text = statement.lower()

# Timeline contradiction example
if "8:00 pm" in text and "7:45 pm" in text:
    contradictions.append({
        "type": "Timeline Inconsistency",
        "description": (
            "Multiple arrival times detected "
            "(8:00 PM and 7:45 PM)."
        )
    })

# Affidavit contradiction example
if (
    "no persons entered or exited" in text
    and "two individuals exiting" in text
):
    contradictions.append({
        "type": "Affidavit Inconsistency",
        "description": (
            "Witness states that no persons "
            "entered or exited the premises, "
            "but later reports observing two "
            "individuals exiting."
        )
    })

# Observation reliability issue
if (
    "clear view" in text
    and "blocked my view" in text
):
    contradictions.append({
        "type": "Observation Reliability",
        "description": (
            "Witness claims a clear view of the "
            "incident but later reports an "
            "obstructed line of sight."
        )
    })

return contradictions
```

if **name** == "**main**":

```
sample_statement = """
I arrived at the intersection at 8:00 PM.

Later I recalled arriving at 7:45 PM.
"""

results = detect_contradictions(
    sample_statement
)

print("Detected Contradictions:")

for item in results:
    print(item)
```

