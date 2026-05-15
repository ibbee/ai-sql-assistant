import re

AGG_FUNCS = ["SUM", "COUNT", "AVG", "MIN", "MAX"]

def extract_select_columns(sql):
    match = re.search(r"SELECT(.*?)FROM", sql, re.IGNORECASE | re.DOTALL)

    if not match:
        return []

    cols = match.group(1).split(",")

    cleaned = []

    for c in cols:
        c = c.strip()

        if any(func in c.upper() for func in AGG_FUNCS):
            continue

        cleaned.append(c)

    return cleaned


def extract_groupby_columns(sql):
    match = re.search(r"GROUP BY(.*?)(ORDER BY|LIMIT|$)", sql, re.IGNORECASE | re.DOTALL)

    if not match:
        return []

    cols = match.group(1).split(",")

    return [c.strip() for c in cols]


def validate_groupby(sql):
    select_cols = extract_select_columns(sql)
    group_cols = extract_groupby_columns(sql)

    missing = []

    for col in select_cols:
        if col not in group_cols:
            missing.append(col)

    return missing