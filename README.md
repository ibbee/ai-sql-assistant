# AI SQL Assistant

AI SQL Assistant is a command-line AI-powered application that converts natural language questions into PostgreSQL SQL queries using a local Large Language Model (LLM) via Ollama.

The project focuses on building a more reliable AI-assisted querying system by combining:
- prompt engineering
- structured JSON outputs
- validation layers
- lightweight guardrails

instead of relying purely on raw LLM generation.

---

# Features

- Natural language to SQL generation
- PostgreSQL-focused query generation
- Structured JSON responses
- Prompt-engineered constraints
- GROUP BY validation heuristics
- Unsafe query detection
- Lightweight SQL guardrails
- Modular architecture

---

# Project Architecture

User Query
    ↓
Prompt Builder
    ↓
LLM Generation (Mistral via Ollama)
    ↓
JSON Parsing
    ↓
Validation Layer
    ↓
Final SQL Output

---

# Project Structure
'''
AI_SQL_assistant/
│
├── main.py
├── llm.py
├── prompts.py
├── schema.py
├── validator.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── Examples/
│   ├── sample_queries.txt
│   └── outputs.txt
│
└── screenshots/
    └── sample_output.png
'''
---

# How It Works

The application:
1. Accepts a natural language query
2. Builds a constrained prompt using schema context
3. Sends the prompt to a local LLM using Ollama
4. Parses the generated JSON response
5. Validates generated SQL using heuristic checks
6. Displays SQL query and explanation

---

# Example Queries

- Show all customers
- Customers with no orders
- Total sales per month
- Top customer in latest available year
- Highest selling city last quarter

---

# Example Output

## User Query
Top customer in latest available year

## Generated SQL

SELECT c.name, SUM(o.amount) AS total_sales
FROM customers c
JOIN orders o
ON c.id = o.customer_id
WHERE EXTRACT(YEAR FROM o.order_date) =
(
    SELECT MAX(EXTRACT(YEAR FROM order_date))
    FROM orders
)
GROUP BY c.id, c.name
ORDER BY total_sales DESC
LIMIT 1;

## Explanation

Finds the customer with the highest sales in the latest available year.

---

# Validation Layer

The project includes lightweight validation heuristics such as:
- detecting unsafe SQL keywords
- GROUP BY consistency checks
- warning generation for potentially invalid queries

The validator is intentionally lightweight and heuristic-based.

---

# Current Limitations

- No real database execution yet
- Validator uses regex heuristics instead of full SQL parsing
- Semantic ambiguity may still occur
- PostgreSQL dialect assumptions only
- Complex nested SQL may bypass validation checks

---

# Future Improvements

- Real database execution
- Semantic SQL validation
- Automatic schema ingestion
- Web-based UI
- Query correction loops
- Better SQL parsing engine
- Multi-database support

---

# Tech Stack

- Python
- Ollama
- Mistral LLM
- Regex-based validation

---

# Setup

## Install dependencies

pip install -r requirements.txt

## Start Ollama

Make sure Ollama is installed and running locally.

Pull the Mistral model:

ollama pull mistral

## Run the application

python main.py

---

# Learning Goals Behind This Project

This project was built as part of an AI engineering upskilling journey focused on:
- reliable AI systems
- prompt engineering
- LLM guardrails
- structured generation
- hybrid deterministic + probabilistic architectures

rather than simply wrapping an LLM API.

---

# Disclaimer

This project is intended for learning and experimentation purposes.
Generated SQL should always be reviewed before production usage.
