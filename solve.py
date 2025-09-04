import sys
from collections import Counter


def parse_row(line: str):
    # Support comma or whitespace separated
    if "," in line:
        parts = [p.strip() for p in line.strip().split(",") if p.strip()]
    else:
        parts = line.strip().split()
    try:
        return [int(x) for x in parts]
    except ValueError:
        return None


def row_matches_six_numbers(numbers: list[int]) -> bool:
    if len(numbers) != 6:
        return False
    counts = Counter(numbers)
    # Exactly one number occurs three times
    repeated_candidates = [value for value, count in counts.items() if count == 3]
    if len(repeated_candidates) != 1:
        return False
    # The remaining three numbers must be distinct and occur once each
    ones = [value for value, count in counts.items() if count == 1]
    if len(ones) != 3:
        return False
    repeated_value = repeated_candidates[0]
    avg_unique = sum(ones) / 3
    return repeated_value > avg_unique


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python solve.py <path_to_file>")
        sys.exit(1)

    path = sys.argv[1]

    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except OSError as e:
        print(f"Error: cannot open file: {e}")
        sys.exit(1)

    max_row_index = 0  # 1-based index, 0 if no row matches
    for idx, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        numbers = parse_row(line)
        if numbers is None:
            continue
        if row_matches_six_numbers(numbers):
            max_row_index = idx

    print(max_row_index)


if __name__ == "__main__":
    main()

