def parse_code(buggy_code, correct_code):
    return {
        "buggy_lines": buggy_code.splitlines(),
        "correct_lines": correct_code.splitlines()
    }
