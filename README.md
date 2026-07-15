# Daily Digest CLI

A simple command-line Python application that fetches a random cat fact from a free public API, displays it in the terminal, and saves a daily report to a text file.

Built as part of a Python Bootcamp mini-project to practice working with functions, APIs, HTTP requests, JSON, and file handling.

## Features

- Fetches live data from the [Cat Fact API](https://catfact.ninja/) using the `requests` library
- Parses the JSON response into a Python dictionary
- Displays the retrieved fact in the terminal
- Generates a `daily_report.txt` file containing the date, API name, and retrieved information
- Handles network errors (no internet, timeouts, bad responses) gracefully instead of crashing

## Tech Stack

- Python 3
- [`requests`](https://pypi.org/project/requests/) library

## Project Structure

```
daily-digest-cli/
├── daily_digest_cli.py   # main source code
├── requirements.txt      # project dependencies
├── daily_report.txt      # sample generated report
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.7 or higher installed
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/daily-digest-cli.git
   cd daily-digest-cli
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

Run the program:

```bash
python daily_digest_cli.py
```

Example output:

```
Fetching today's cat fact...

===== Daily Digest: Cat Fact =====
Date: 2026-07-15
Fact: Cats sleep 70% of their lives.
(Fact length: 30 characters)
===================================

Report saved successfully to 'daily_report.txt'.
```

A `daily_report.txt` file will be created (or overwritten) in the project folder with the same information.

## How It Works

1. `fetch_cat_fact()` sends a GET request to the Cat Fact API and converts the JSON response into a Python dictionary.
2. `display_fact()` prints the date and the fact to the terminal.
3. `save_report()` writes a formatted report to `daily_report.txt`.
4. `main()` ties the above steps together and handles the case where the API call fails.

## Error Handling

The program gracefully handles:
- No internet connection
- Request timeouts
- Invalid API responses

If any of these occur, a clear message is printed instead of the program crashing.

## Author

Noor Fatima — Python Bootcamp Mini Project

## License

This project is for educational purposes as part of a Python Bootcamp assignment.
