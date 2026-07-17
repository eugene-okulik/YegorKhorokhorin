import argparse
import os
import re


def get_args():
    parser = argparse.ArgumentParser(description="Log analyzer")
    parser.add_argument("path", help="Path to log file or folder with logs")
    parser.add_argument("--text", required=True, help="Text to search in logs")
    return parser.parse_args()


def get_files(path):
    if os.path.isfile(path):
        return [path]

    if os.path.isdir(path):
        log_files = []

        for file_name in sorted(os.listdir(path)):
            file_path = os.path.join(path, file_name)

            if os.path.isfile(file_path):
                log_files.append(file_path)

        return log_files

    print("Path does not exist")
    return []


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def split_logs_into_blocks(content):
    blocks = []
    current_block = []
    current_time = None
    start_line = None

    time_pattern = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"

    lines = content.splitlines()

    for line_number, line in enumerate(lines, start=1):
        if re.match(time_pattern, line):
            if current_block:
                blocks.append({
                    "time": current_time,
                    "start_line": start_line,
                    "text": "\n".join(current_block)
                })

            current_time = line[:19]
            start_line = line_number
            current_block = [line]
        else:
            current_block.append(line)

    if current_block:
        blocks.append({
            "time": current_time,
            "start_line": start_line,
            "text": "\n".join(current_block)
        })

    return blocks


def get_context(block_text, search_text):
    words = block_text.split()
    search_text = search_text.lower()

    for index, word in enumerate(words):
        if search_text in word.lower():
            start = max(index - 5, 0)
            end = min(index + 6, len(words))
            return " ".join(words[start:end])

    return ""


def search_in_blocks(blocks, search_text):
    results = []
    search_text_lower = search_text.lower()

    for block in blocks:
        if search_text_lower in block["text"].lower():
            lines = block["text"].splitlines()
            found_line = None

            for index, line in enumerate(lines):
                if search_text_lower in line.lower():
                    found_line = block["start_line"] + index
                    break

            results.append({
                "time": block["time"],
                "line": found_line,
                "context": get_context(block["text"], search_text)
            })

    return results


def print_results(file_path, results):
    print("=" * 80)
    print(f"File: {file_path}")

    if not results:
        print("Nothing found")
        return

    print(f"Found: {len(results)}")

    for result in results:
        print("-" * 80)
        print(f"Warn time: {result['time']}")
        print(f"Found line: {result['line']}")
        print("Context:")
        print(result["context"])


def main():
    args = get_args()
    files = get_files(args.path)

    for file_path in files:
        content = read_file(file_path)
        blocks = split_logs_into_blocks(content)
        results = search_in_blocks(blocks, args.text)
        print_results(file_path, results)


main()
