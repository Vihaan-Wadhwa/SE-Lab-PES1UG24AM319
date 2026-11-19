import re

# SRN format, e.g. PES1UG23CS123: campus, 2-letter programme, 2-digit year,
# 2-letter department, 3-digit roll number. Digits are ASCII-only on purpose.
SRN_PATTERN = re.compile(r"(PES[0-9])([A-Z]{2})([0-9]{2})([A-Z]{2})([0-9]{3})")


def average_marks(marks_csv):
    """Return the average of comma-separated integer marks, rounded to 2 dp.

    Returns None if the input is not a string, is empty, or contains
    anything that is not an integer.
    """
    if not isinstance(marks_csv, str):
        return None
    try:
        marks = [int(m) for m in marks_csv.split(',')]  # int() ignores spaces
        return round(sum(marks) / len(marks), 2)
    except (ValueError, OverflowError):
        # ValueError: '', 'abc', '1,,3', or an absurdly long digit string
        # OverflowError: sum too large to convert to float
        return None


def parse_srn(srn):
    """Return (campus, year, dept) from an SRN like PES1UG23CS123.

    Returns None if the SRN is not a string or does not match the format.
    """
    if not isinstance(srn, str):
        return None
    match = SRN_PATTERN.fullmatch(srn.strip())
    if match is None:
        return None
    campus, _programme, year, dept, _roll = match.groups()
    return campus, int(year), dept


def short_name(full_name):
    """Return 'R. Kumar' for 'ravi kumar'.

    Returns None if the input is not a string or is not exactly two words.
    """
    if not isinstance(full_name, str):
        return None
    parts = full_name.split()
    if len(parts) != 2:
        return None
    first, last = parts
    return first[0].upper() + ". " + last.capitalize()


def main():
    print("==== Running average_marks ====")
    user_input = input("Enter marks as CSV (e.g. 78,85,92): ")
    result = average_marks(user_input)
    if result is None:
        print("Invalid input: enter whole numbers separated by commas.")
    else:
        print("Average Marks:", result)

    print("\n==== Running parse_srn ====")
    user_input = input("Enter an SRN (e.g. PES1UG23CS123): ")
    result = parse_srn(user_input)
    if result is None:
        print("Invalid input: SRN must look like PES1UG23CS123.")
    else:
        print("Campus, Year and Dept:", result)

    print("\n==== Running short_name ====")
    user_input = input("Enter first and last name (e.g. ravi kumar): ")
    result = short_name(user_input)
    if result is None:
        print("Invalid input: enter exactly two words, first and last name.")
    else:
        print("Short Name:", result)


if __name__ == "__main__":
    main()
