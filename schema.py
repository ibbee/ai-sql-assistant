schema = """
Table: customers
- id (int, primary key)
- name (text, name of the customer)
- city (text, current city of customer)

Table: orders
- id (int, primary key)
- customer_id (int, foreign key -> customers.id)
- amount (float, price or amount of the order)
- order_date (date, stores exact order timestamp)
"""