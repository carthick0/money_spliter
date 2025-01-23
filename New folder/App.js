document.getElementById("calculate").addEventListener("click", () => {
    const names = document.getElementById("names").value.split(",").map(name => name.trim());
    const totalExpense = parseFloat(document.getElementById("total").value);
  
    if (names.length === 0 || isNaN(totalExpense)) {
      alert("Please enter valid names and total expense.");
      return;
    }
  
    const share = (totalExpense / names.length).toFixed(2);
    const resultDiv = document.getElementById("result");
  
    resultDiv.innerHTML = `<p>Total Expense: $${totalExpense}</p>`;
    resultDiv.innerHTML += `<p>Each Person Pays: $${share}</p>`;
    resultDiv.innerHTML += `<ul>${names.map(name => `<li>${name}: $${share}</li>`).join("")}</ul>`;
  });
  