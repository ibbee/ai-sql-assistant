from schema import schema
from prompts import build_prompt
from llm import generate_sql
import json
from validator import validate_groupby
import re

FORBIDDEN = ["DROP", "DELETE", "ALTER", "TRUNCATE"]

def validate_sql(sql):
    upper_sql = sql.upper()

    for keyword in FORBIDDEN:
        if re.search(rf"\\b{keyword}\\b", upper_sql):
            return False

    return True

def parse_response(response):
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return None

def main():
    print("AI SQL Assistant (type 'exit' to quit)\n")

    while True:
        user_query = input("Ask: ")

        if user_query.lower() == "exit":
            break

        if not user_query.strip():
            continue

        prompt = build_prompt(schema, user_query)
        parsed = None
        for _ in range(2):
            raw = generate_sql(prompt)
            parsed = parse_response(raw)

            if parsed:
                break

        if parsed:
            if not validate_sql(parsed["query"]):
                print("⚠️ Unsafe query detected!")
                
            issues = validate_groupby(parsed["query"])

            if issues:
                print("\n⚠️ GROUP BY Warning:")
                print("Columns missing from GROUP BY:", issues)

            print("\n" + "="*50)
            print("SQL QUERY")
            print("="*50)
            print(parsed["query"])

            print("\nEXPLANATION")
            print("="*50)
            print(parsed["explanation"])
        else:
            print("\n" + "="*50)
            print("Failed to parse response.")
            print(raw)

if __name__ == "__main__":
    main()