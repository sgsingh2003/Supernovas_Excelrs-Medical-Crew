function analyzeCase() {
  const initialProblem = document.getElementById("initialProblem").value;
  const additionalDetails = document.getElementById("additionalDetails").value;
  const resultBox = document.getElementById("resultContent");

  resultBox.innerText = "⏳ Analyzing case...";

  fetch("/analyze", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      problem: initialProblem + ". " + additionalDetails
    })
  })
    .then(res => res.json())
    .then(data => {
      if (data.error) {
        resultBox.innerText = data.error;
      } else {
        resultBox.innerText =
          "STATUS:\n" + data.status + "\n\n" +
          "AGENT STEPS:\n" + data.agent_steps.join("\n") + "\n\n" +
          "MEDICAL REPORT:\n" + data.medical_report;
      }
    })
    .catch(err => {
      console.error(err);
      resultBox.innerText = "❌ Server error";
    });
}