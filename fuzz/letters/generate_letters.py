import argparse
from itertools import product


def main(repeat_value: int):
    """
    Main function to generate and store alphabets
    """
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    file_name = f"{repeat_value}-alpha-a-to-z.txt"
    combination_list = ["".join(d) for d in product(alphabets, repeat=repeat_value)]
    combinations = "\n".join(combination_list)

    with open(file_name, 'w+') as f:
        f.write(combinations)
        f.close()

    print(f"Generated combinations saved to {file_name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A script that generate alphabets in repeatable manner")

    # Place value
    default_repeat_value = 2
    parser.add_argument(
        "--order-pair",
        type=int,
        help="N number of order pairs",
        default=default_repeat_value
    )
    args = parser.parse_args()

    main(args.order_pair)
