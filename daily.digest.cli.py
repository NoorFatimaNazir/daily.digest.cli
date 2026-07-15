"""
Project 2: Daily Digest CLI
-----------------------------
A command-line program that:
  1. Fetches data from a free public API (Cat Fact API - no key needed).
  2. Converts the JSON response into a Python dictionary.
  3. Prints the info to the terminal.
  4. Saves a report to daily_report.txt

API used: https://catfact.ninja/fact
  - Free, no sign-up, no API key required.
  - Returns JSON like: {"fact": "Cats sleep 70% of their lives.", "length": 30}

Before running, install the 'requests' library if you don't have it:
    pip install requests
"""

import requests          # lets us make HTTP requests to the API
import datetime          # lets us get today's date for the report
import json              # not strictly required (requests parses JSON for us)
                          # but shown here since JSON handling is a listed concept


# ---------------------------------------------------------------
# STEP 1: Fetch data from the API
# ---------------------------------------------------------------
def fetch_cat_fact():
    """
    Calls the Cat Fact API and returns the JSON response as a
    Python dictionary. Returns None if something goes wrong
    (no internet, API is down, bad response, etc).
    """
    url = "https://catfact.ninja/fact"

    try:
        # timeout=10 means: if the server doesn't respond in 10 seconds, give up
        response = requests.get(url, timeout=10)

        # raise_for_status() throws an error if the API returned
        # something like 404 or 500 (i.e. request failed)
        response.raise_for_status()

        # .json() converts the raw JSON text into a Python dict/list
        data = response.json()
        return data

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the internet. Please check your connection.")
        return None
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again.")
        return None
    except requests.exceptions.HTTPError as err:
        print(f"Error: The API returned an error: {err}")
        return None
    except requests.exceptions.RequestException as err:
        # This catches any other requests-related error we didn't
        # specifically plan for, so the program never crashes ugly.
        print(f"Error: Something went wrong while fetching data: {err}")
        return None


# ---------------------------------------------------------------
# STEP 2: Display the info in the terminal
# ---------------------------------------------------------------
def display_fact(fact_data):
    """Prints the fetched cat fact nicely in the terminal."""
    print("\n===== Daily Digest: Cat Fact =====")
    print(f"Date: {datetime.date.today()}")
    print(f"Fact: {fact_data['fact']}")
    print(f"(Fact length: {fact_data['length']} characters)")
    print("===================================\n")


# ---------------------------------------------------------------
# STEP 3: Save the report to a text file
# ---------------------------------------------------------------
def save_report(fact_data, filename="daily_report.txt"):
    """
    Writes a formatted report to daily_report.txt containing:
    - Current Date
    - API Name
    - Retrieved Information
    """
    today = datetime.date.today()

    # "w" mode = write (overwrites the file each time the program runs)
    with open(filename, "w", encoding="utf-8") as report_file:
        report_file.write("DAILY DIGEST REPORT\n")
        report_file.write("=====================\n")
        report_file.write(f"Date: {today}\n")
        report_file.write("API Name: Cat Fact API (https://catfact.ninja)\n")
        report_file.write(f"Retrieved Information: {fact_data['fact']}\n")

    print(f"Report saved successfully to '{filename}'.")


# ---------------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------------
def main():
    print("Fetching today's cat fact...")

    fact_data = fetch_cat_fact()

    # If fetch_cat_fact() failed (returned None), stop here gracefully
    # instead of crashing when we try to use fact_data.
    if fact_data is None:
        print("Could not generate today's report. Please try again later.")
        return

    display_fact(fact_data)
    save_report(fact_data)


if __name__ == "__main__":
    main()
