import argparse
from itertools import product


def main(place_val: int):
    """
    Main function to generate and store digits
    """
    digits = "0123456789"
    file_name = f"digits-{place_val}.txt"
    combination_list = ["".join(d) for d in product(digits, repeat=place_val)]
    combinations = "\n".join(combination_list)

    with open(file_name, 'w+') as f:
        f.write(combinations)
        f.close()

    print(f"Generated combinations saved to {file_name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A script that count digits")

    # Place value
    default_place_value = 4
    parser.add_argument(
        "--place-value",
        type=int,
        help="Length of digits to generate",
        default=default_place_value
    )
    args = parser.parse_args()

    main(args.place_value)
