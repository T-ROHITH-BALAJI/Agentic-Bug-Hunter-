def locate_bug(parsed_code):
    buggy = parsed_code["buggy_lines"]
    correct = parsed_code["correct_lines"]

    min_len = min(len(buggy), len(correct))

    for i in range(min_len):
        if buggy[i].strip() != correct[i].strip():
            return i + 1  # line numbers start at 1

    # fallback if no difference found
    return 1
