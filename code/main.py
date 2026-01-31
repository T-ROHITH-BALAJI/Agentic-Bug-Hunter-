from utils.csv_utils import read_input_csv, write_output_csv
from agents.parsing_agent import parse_code
from agents.bug_localization_agent import locate_bug
from agents.bug_match_agent import match_bug
from agents.explanation_agent import generate_explanation

def main():
    rows = read_input_csv("samples.csv")
    output_rows = []

    for row in rows:
        code_id = row["ID"]
        buggy_code = row["Code"]
        correct_code = row["Correct Code"]
        context = row["Context"]

        parsed = parse_code(buggy_code, correct_code)
        bug_line = locate_bug(parsed)
        bug_info = match_bug(context)
        explanation = generate_explanation(bug_info)

        output_rows.append({
            "ID": code_id,
            "Bug Line": bug_line,
            "Explanation": explanation
        })


    write_output_csv("output.csv", output_rows)

if __name__ == "__main__":
    main()
