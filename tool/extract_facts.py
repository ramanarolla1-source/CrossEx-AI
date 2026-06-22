"""
CrossEx AI
Fact Extraction Module

Extracts material facts from witness
statements and affidavits.

Prototype implementation for the
Anna AI-Native App Hackathon.
"""

import re

def extract_facts(statement):
"""
Extract material facts from a witness statement.

```
Parameters
----------
statement : str

Returns
-------
dict
"""

facts = {
    "times": [],
    "locations": [],
    "observations": []
}

if not statement:
    return facts

# Extract times
time_pattern = r"\b\d{1,2}:\d{2}\s?(?:AM|PM|am|pm)\b"

facts["times"] = re.findall(
    time_pattern,
    statement
)

# Extract locations
location_keywords = [
    "intersection",
    "junction",
    "market plaza",
    "industrial estate",
    "premises",
    "parking area",
    "central junction"
]

lower_text = statement.lower()

for location in location_keywords:
    if location in lower_text:
        facts["locations"].append(
            location.title()
        )

# Extract observations
observation_patterns = [
    "collision involving two vehicles",
    "collision",
    "two individuals exiting",
    "vehicle crossing the signal",
    "observed a collision",
    "spoke to one driver"
]

for observation in observation_patterns:
    if observation.lower() in lower_text:
        facts["observations"].append(
            observation
        )

# Remove duplicates
facts["times"] = list(
    dict.fromkeys(facts["times"])
)

facts["locations"] = list(
    dict.fromkeys(facts["locations"])
)

facts["observations"] = list(
    dict.fromkeys(
        facts["observations"]
    )
)

return facts
```

if **name** == "**main**":

```
sample_statement = """
I arrived at the Central Junction
intersection at approximately
8:00 PM.

I observed a collision involving
two vehicles.
"""

extracted = extract_facts(
    sample_statement
)

print("\nEXTRACTED FACTS\n")
print(extracted)
```

