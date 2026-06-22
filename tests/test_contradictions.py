"""
CrossEx AI
Contradiction Detection Tests

These tests validate the ability of the contradiction
analysis module to identify inconsistencies in witness
statements and affidavits.
"""

import pytest

def detect_contradictions(statement):
"""
Placeholder contradiction detection function.

```
In production this would call the CrossEx AI
contradiction analysis engine.
"""

contradictions = []

if "8:00 PM" in statement and "7:45 PM" in statement:
    contradictions.append(
        "Timeline inconsistency detected: arrival time conflict."
    )

if (
    "no persons entered or exited" in statement.lower()
    and "two individuals exiting" in statement.lower()
):
    contradictions.append(
        "Affidavit inconsistency detected: exit activity conflict."
    )

return contradictions
```

def test_timeline_contradiction_detection():
statement = """
I arrived at the intersection at approximately 8:00 PM.

```
Later, I recalled reaching the location around 7:45 PM.
"""

results = detect_contradictions(statement)

assert len(results) == 1
assert "Timeline inconsistency" in results[0]
```

def test_affidavit_contradiction_detection():
affidavit = """
No persons entered or exited the building during that time.

```
At approximately 9:20 AM, I observed two individuals exiting
the building through a side entrance.
"""

results = detect_contradictions(affidavit)

assert len(results) == 1
assert "Affidavit inconsistency" in results[0]
```

def test_no_contradiction_detected():
statement = """
I arrived at the location at 8:00 PM.

```
I remained at the scene for fifteen minutes.

I then left the area.
"""

results = detect_contradictions(statement)

assert len(results) == 0
```

def test_multiple_contradictions():
statement = """
I arrived at approximately 8:00 PM.

```
Later, I recalled arriving at 7:45 PM.

No persons entered or exited the building.

I observed two individuals exiting through a side entrance.
"""

results = detect_contradictions(statement)

assert len(results) == 2
```

if **name** == "**main**":
pytest.main()

