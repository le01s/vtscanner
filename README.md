# VirusTotal Domain Check Script

This script is used to check domain names using the VirusTotal API. It sends a request to the API and outputs the results in JSON format, utilizing `pprint` for a structured and readable display.

## Installation and Setup

### 1. Clone the repository

Clone the repository to your local machine:

```bash
git clone https://github.com/le01s/vtscanner.git
cd vtscanner
```

### 2. Install dependencies

Use pip to install the required dependencies:

```bash
pip install -r requirements.txt
```


### 3. Get your API Key

Sign up at VirusTotal and obtain your API key.
Create a .env file in the project's root directory and add your API key in the following format:

```dotenv
VTKEY=your_virustotal_api_key
```

### 4. Run the script

Run the script using Python:

```bash
python vtscanner.py
```