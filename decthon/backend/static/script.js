function analyzeCase() {
    const initialProblem = document.getElementById("initialProblem").value;
    const additionalDetails = document.getElementById("additionalDetails").value;
    const resultBox = document.getElementById("resultContent");

    resultBox.innerHTML = "⏳ Analyzing case...";

    fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            initial_problem: initialProblem,
            additional_details: additionalDetails
        })
    })
    .then(res => res.json())
    .then(data => {
        resultBox.innerHTML = data.result;
    })
    .catch(err => {
        console.error(err);
        resultBox.innerHTML = "❌ Error connecting to server";
    });
}