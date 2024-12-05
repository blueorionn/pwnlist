from datetime import datetime, timedelta
import argparse


def validate_date(date_string):
    """Validate and convert the input date string to a datetime object."""
    try:
        return datetime.strptime(date_string, "%d-%m-%Y").date()
    except ValueError:
        raise ValueError("Invalid date format. Please use 'day-month-year' (e.g., 01-01-2000).")


def main(sd_date_string: str, ed_date_string: str):
    """
    Main function to generate and store dates
    """

    # Extracting value
    start_date, end_date = validate_date(sd_date_string), validate_date(ed_date_string)
    file_name = f"{sd_date_string}-to-{ed_date_string}.txt"

    # dates list
    dates_list = []

    # enumerating dates
    current_date = start_date
    while current_date <= end_date:
        dates_list.append(current_date.strftime('%d-%m-%Y'))
        current_date += timedelta(days=1)

    # Storing dates
    with open(file_name, 'w+') as f:
        all_dates = '\n'.join(dates_list)
        f.write(all_dates)
        f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A script that count dates")

    # Start date
    default_sd_date = "01-01-1970"
    parser.add_argument(
        "--start-date",
        type=str,
        help="Start Date",
        default=default_sd_date
    )

    # End date
    default_ed_date = "31-12-2020"
    parser.add_argument(
        "--end-date",
        type=str,
        help="End Date",
        default=default_ed_date
    )
    args = parser.parse_args()

    main(args.start_date, args.end_date)