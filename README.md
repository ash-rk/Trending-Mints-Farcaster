# Trending Mints Tracker

This project consists of a set of Python scripts designed to track and identify trending mint events on the Base blockchain Layer 2 (L2) over the last week. The purpose is to analyze and understand the activity related to ERC token mints and to identify any trends that may be valuable for collectors, traders, or researchers.

## Setup Instructions

1. Clone the repository to your local machine.
2. Create a `.env` file in the root directory of the project to store your secret key like so:
    ```
    SECRET_KEY=your_secret_key_here
    ```
   Make sure to replace `your_secret_key_here` with your actual API secret key.

3. Install the required dependencies using:
    ```
    pip install -r requirements.txt
    ```
   This step assumes that you have Python and pip already installed on your system.

## How to Run

1. Run `main.py` to collect data from the Base blockchain:
    ```
    python main.py
    ```
   This will execute a GraphQL query using the provided secret key in your `.env` file and store the results in `data.json`.

2. Once you have your data, run `data_formatter.py` to format the data into a CSV file:
    ```
    python data_formatter.py
    ```
   This script will read the data from `data.json`, process it, and output the trending mints to `trending_mints.csv` in a structured tabular format.

3. You can now open `trending_mints.csv` to analyze the trending mint events from the last week.

## Data Generated

- `data.json`: Raw JSON data retrieved from the Base blockchain API.
- `trending_mints.csv`: Formatted data in CSV format for easy analysis and visualization.

Please note that the scripts require network access to interact with the Base blockchain API.

## Contributing

If you wish to contribute to this project, please fork the repository and submit a pull request with your proposed changes.

## License

This project is licensed under the [MIT License](LICENSE.txt).
