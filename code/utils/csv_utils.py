import csv

def read_input_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

def write_output_csv(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "ID",
                "Bug Line",
                "Explanation"
            ]
        )
        writer.writeheader()
        writer.writerows(rows)
