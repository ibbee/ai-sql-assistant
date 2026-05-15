import ollama

def generate_sql(prompt):
    response = ollama.chat(
        model="mistral:latest",
        messages=[
            {"role": "system", "content": "You generate SQL queries."},
            {"role": "user", "content": prompt}
        ]
    )

    return response['message']['content']