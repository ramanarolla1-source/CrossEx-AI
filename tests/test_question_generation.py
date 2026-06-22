"""
CrossEx AI
Question Generation Tests

These tests validate generation of
cross-examination questions from
facts and detected contradictions.
"""

from app.tool.generate_questions import generate_questions

def test_generate_contradiction_question():
facts = {
"times": ["8:00 PM", "7:45 PM"]
}

```
contradictions = [
    "Timeline inconsistency detected."
]

questions = generate_questions(
    facts,
    contradictions
)

assert len(questions) > 0

assert any(
    "why" in q.lower()
    or "explain" in q.lower()
    for q in questions
)
```

def test_generate_fact_confirmation_question():
facts = {
"times": ["8:00 PM"]
}

```
contradictions = []

questions = generate_questions(
    facts,
    contradictions
)

assert len(questions) > 0

assert any(
    "confirm" in q.lower()
    for q in questions
)
```

def test_generate_timeline_question():
facts = {
"times": ["8:00 PM"]
}

```
contradictions = [
    "Timeline inconsistency detected."
]

questions = generate_questions(
    facts,
    contradictions
)

assert any(
    "time" in q.lower()
    or "arrival" in q.lower()
    for q in questions
)
```

def test_multiple_question_types():
facts = {
"times": ["8:00 PM", "7:45 PM"],
"locations": ["Central Junction"]
}

```
contradictions = [
    "Timeline inconsistency detected."
]

questions = generate_questions(
    facts,
    contradictions
)

assert len(questions) >= 3
```

def test_no_facts_no_contradictions():
facts = {}

```
contradictions = []

questions = generate_questions(
    facts,
    contradictions
)

assert isinstance(questions, list)
```

def test_output_is_list():
facts = {
"times": ["8:00 PM"]
}

```
contradictions = []

questions = generate_questions(
    facts,
    contradictions
)

assert isinstance(questions, list)
```

