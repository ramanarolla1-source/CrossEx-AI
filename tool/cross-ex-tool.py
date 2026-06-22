"""
CrossEx AI
Main Workflow Tool

Orchestrates the complete witness
analysis workflow:

1. Fact Extraction
2. Contradiction Detection
3. Question Generation

Built for the Anna AI-Native App Hackathon.
"""

from extract_facts import extract_facts
from contradiction_analysis import detect_contradictions
from generate_questions import generate_questions

class CrossExTool:

```
def __init__(self):
    self.name = "CrossEx AI"

def analyze_statement(self, statement):
    """
    Execute the complete CrossEx AI workflow.
    """

    facts = extract_facts(statement)

    contradictions = detect_contradictions(
        statement
    )

    questions = generate_questions(
        facts,
        contradictions
    )

    return {
        "facts": facts,
        "contradictions": contradictions,
        "questions": questions
    }

def build_report(self, statement):
    """
    Generate a structured report.
    """

    results = self.analyze_statement(
        statement
    )

    report = {
        "Extracted Facts":
            results["facts"],

        "Potential Contradictions":
            results["contradictions"],

        "Suggested Questions":
            results["questions"],

        "Review Required":
            (
                "All generated outputs are "
                "subject to lawyer review "
                "and approval."
            )
    }

    return report
```

if **name** == "**main**":

```
sample_statement = """
I arrived at the intersection at
approximately 8:00 PM.

Later I recalled reaching the
location around 7:45 PM.

I observed a collision involving
two vehicles.
"""

tool = CrossExTool()

report = tool.build_report(
    sample_statement
)

print("\nCROSSEX AI REPORT\n")

for section, content in report.items():
    print(f"{section}:")
    print(content)
    print()
```

