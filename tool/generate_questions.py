"""
CrossEx AI
Question Generation Module

Generates structured cross-examination
questions based on extracted facts and
detected contradictions.

Prototype implementation for the
Anna AI-Native App Hackathon.
"""

def generate_questions(
facts,
contradictions
):
"""
Generate cross-examination questions.

```
Parameters
----------
facts : dict
contradictions : list

Returns
-------
list
    Generated questions.
"""

questions = []

# Fact confirmation questions
for time in facts.get("times", []):
    questions.append(
        f"Can you confirm the significance of the time '{time}' mentioned in your statement?"
    )

for location in facts.get(
    "locations",
    []
):
    questions.append(
        f"Can you confirm your presence at '{location}' on the relevant date?"
    )

# Contradiction-focused questions
for contradiction in contradictions:

    if isinstance(
        contradiction,
        dict
    ):

        contradiction_type = contradiction.get(
            "type",
            ""
        )

        if contradiction_type == "Timeline Inconsistency":

            questions.append(
                "You have provided multiple arrival times. Which arrival time is accurate?"
            )

            questions.append(
                "Can you explain the difference between the reported arrival times?"
            )

        elif contradiction_type == "Affidavit Inconsistency":

            questions.append(
                "You stated that no persons entered or exited the premises. How do you reconcile that statement with your observation of individuals exiting the building?"
            )

        elif contradiction_type == "Observation Reliability":

            questions.append(
                "You initially stated that you had a clear view of the incident. Can you explain how an obstructed view may have affected your observations?"
            )

# Generic credibility questions
if contradictions:

    questions.append(
        "How confident are you in the accuracy of your recollection of events?"
    )

    questions.append(
        "Did you review any documents or discuss the incident with anyone before making this statement?"
    )

# Default fallback question
if not questions:

    questions.append(
        "Can you describe the events in the order in which they occurred?"
    )

return questions
```

if **name** == "**main**":

```
sample_facts = {
    "times": [
        "8:00 PM",
        "7:45 PM"
    ],
    "locations": [
        "Central Junction"
    ],
    "observations": [
        "collision involving two vehicles"
    ]
}

sample_contradictions = [
    {
        "type":
        "Timeline Inconsistency",
        "description":
        "Multiple arrival times detected."
    }
]

questions = generate_questions(
    sample_facts,
    sample_contradictions
)

print(
    "\nGENERATED CROSS-EXAMINATION QUESTIONS\n"
)

for idx, question in enumerate(
    questions,
    start=1
):
    print(
        f"{idx}. {question}"
    )
```

