
# 💱 Conversor de Moedas em Tempo Real

Este é um projeto completo de **Conversor de Moedas** feito com **Python (Flask)** no backend e **HTML, CSS e JavaScript** no frontend.  
O objetivo é permitir a conversão de valores entre diversas moedas em tempo real utilizando uma API externa de câmbio.

---

## 🚀 Funcionalidades

- Conversão em tempo real entre múltiplas moedas
- Conexão com API pública de taxas de câmbio
- Interface simples e intuitiva em HTML/CSS
- Comunicação entre frontend e backend via `fetch`
- Tratamento de erros e validação de dados
- Resolução de CORS configurada no Flask

---

## 🛠️ Tecnologias utilizadas

### Backend
- Python 3.x
- Flask
- Requests
- Flask-CORS

### Frontend
- HTML5
- CSS3
- JavaScript (Fetch API)

---

## 📂 Estrutura do Projeto

```
conversor-moeda/
├─ backend/           # Código do servidor Flask
│   └─ app.py
├─ frontend/          # Interface do usuário
│   ├─ index.html
│   ├─ style.css
│   └─ script.js
├─ .gitignore
├─ requirements.txt   # Lista de dependências
└─ README.md
```

---

## ⚙️ Como rodar o projeto localmente

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/conversor-moeda.git
cd conversor-moeda
```

### 2️⃣ Criar e ativar o ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate  # no Mac/Linux
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Rodar o backend

```bash
cd backend
python app.py
```

### 5️⃣ Rodar o frontend

Abra o arquivo `frontend/index.html` com **Live Server** no VS Code.

---

## 🌐 API utilizada

Este projeto utiliza a API pública de câmbio [ExchangeRate-API](https://www.exchangerate-api.com/) para buscar valores atualizados das moedas.

---

## 📸 Exemplo de uso

```
http://127.0.0.1:5000/convert?from=USD&to=BRL&amount=100
```

**Resposta:**

```json
{
  "from": "USD",
  "to": "BRL",
  "amount": 100.0,
  "converted_amount": 553.21,
  "rate": 5.5321
}
```

---

## ✍️ Autor

Desenvolvido por **Gabriel Scandiuzzi** 🚀  
📍 Projeto de portfólio - Engenharia de Software
