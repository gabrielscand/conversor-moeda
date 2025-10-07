async function convert() {
  const amount = document.getElementById("amount").value;
  const from = document.getElementById("from").value;
  const to = document.getElementById("to").value;

  if (!amount) {
    alert("Digite um valor para converter!");
    return;
  }

  try {
    const response = await fetch(`http://127.0.0.1:5000/convert?from=${from}&to=${to}&amount=${amount}`);
    const data = await response.json();

    if (data.error) {
      document.getElementById("result").innerText = `❌ Erro: ${data.error}`;
    } else {
      document.getElementById("result").innerText = `${data.amount} ${data.from} = ${data.converted_amount} ${data.to}`;
    }
  } catch (error) {
    document.getElementById("result").innerText = "❌ Erro ao conectar com o servidor.";
  }
}
