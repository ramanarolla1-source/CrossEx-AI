"""
CrossEx AI
Fact Extraction Tests

These tests validate extraction of
material facts from witness statements.
"""

from app.tool.extract_facts import extract_facts

def test_extract_arrival_time():
statement = """
I arrived at the intersection at approximately 8:00 PM.
"""

```
facts = extract_facts(statement)

assert "8:00 PM" in facts["times"]
```

def test_extract_location():
statement = """
I arrived at the Central Junction intersection.
"""

```
facts = extract_facts(statement)

assert "Central Junction intersection" in facts["locations"]
```

def test_extract_observation():
statement = """
I observed a collision involving two vehicles.
"""

```
facts = extract_facts(statement)

assert "collision involving two vehicles" in facts["observations"]
```

def test_extract_multiple_facts():
statement = """
I arrived at the Central Junction intersection
at approximately 8:00 PM.

```
I observed a collision involving two vehicles.
"""

facts = extract_facts(statement)

assert len(facts["times"]) == 1
assert len(facts["locations"]) == 1
assert len(facts["observations"]) == 1
```

def test_empty_statement():
facts = extract_facts("")

```
assert facts["times"] == []
assert facts["locations"] == []
assert facts["observations"] == []
```

def test_no_recognized_facts():
statement = """
This sentence contains no recognizable
witness-related information.
"""

```
facts = extract_facts(statement)

assert isinstance(facts, dict)
assert "times" in facts
assert "locations" in facts
assert "observations" in facts
```

