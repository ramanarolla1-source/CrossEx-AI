/*
CrossEx AI
Frontend Workflow Controller

Anna AI-Native App Hackathon
*/

class CrossExApp {

```
constructor() {

    this.statementInput =
        document.getElementById(
            "statementInput"
        );

    this.analyzeButton =
        document.getElementById(
            "analyzeBtn"
        );

    this.factsContainer =
        document.getElementById(
            "factsOutput"
        );

    this.contradictionsContainer =
        document.getElementById(
            "contradictionsOutput"
        );

    this.questionsContainer =
        document.getElementById(
            "questionsOutput"
        );

    this.initialize();
}

initialize() {

    this.analyzeButton.addEventListener(
        "click",
        () => this.runAnalysis()
    );
}

runAnalysis() {

    const statement =
        this.statementInput.value;

    if (!statement.trim()) {

        alert(
            "Please enter a witness statement."
        );

        return;
    }

    const results =
        this.mockAnalyze(
            statement
        );

    this.renderFacts(
        results.facts
    );

    this.renderContradictions(
        results.contradictions
    );

    this.renderQuestions(
        results.questions
    );
}

mockAnalyze(statement) {

    const facts = [];

    const contradictions = [];

    const questions = [];

    if (
        statement.includes("8:00 PM")
    ) {

        facts.push(
            "Arrival Time: 8:00 PM"
        );
    }

    if (
        statement.includes("7:45 PM")
    ) {

        facts.push(
            "Arrival Time: 7:45 PM"
        );
    }

    if (
        statement
            .toLowerCase()
            .includes("collision")
    ) {

        facts.push(
            "Observation: Collision"
        );
    }

    if (
        statement.includes("8:00 PM")
        &&
        statement.includes("7:45 PM")
    ) {

        contradictions.push(
            "Timeline inconsistency detected."
        );

        questions.push(
            "Why did you state two different arrival times?"
        );

        questions.push(
            "Which arrival time is accurate?"
        );
    }

    if (
        questions.length === 0
    ) {

        questions.push(
            "Can you describe the events in chronological order?"
        );
    }

    return {
        facts,
        contradictions,
        questions
    };
}

renderFacts(facts) {

    this.factsContainer.innerHTML =
        facts.map(
            item =>
            `<li>${item}</li>`
        ).join("");
}

renderContradictions(
    contradictions
) {

    if (
        contradictions.length === 0
    ) {

        this.contradictionsContainer.innerHTML =
            "<li>No contradictions detected.</li>";

        return;
    }

    this.contradictionsContainer.innerHTML =
        contradictions.map(
            item =>
            `<li>${item}</li>`
        ).join("");
}

renderQuestions(
    questions
) {

    this.questionsContainer.innerHTML =
        questions.map(
            item =>
            `<li>${item}</li>`
        ).join("");
}
```

}

document.addEventListener(
"DOMContentLoaded",
() => {
new CrossExApp();
}
);

