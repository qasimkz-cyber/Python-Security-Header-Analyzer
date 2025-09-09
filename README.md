# Python Security Header Analyzer 🛡️

A command-line tool built in Python to analyze the HTTP security headers of a given URL. This script helps assess a website's security posture by checking for key headers like `Content-Security-Policy` (CSP) and `Strict-Transport-Security` (HSTS) that are crucial for defending against common web vulnerabilities.

## Features
* Analyzes any given URL for the presence of important security headers.
* Provides clear, color-coded output for found (✅ Green) and missing (❌ Red) headers.
* Handles connection errors and bad server responses gracefully.
* Accepts the target URL as a simple command-line argument.

## Requirements
* Python 3.x

## Setup & Installation

1.  **Clone the repository (replace `your-username` with your actual GitHub username):**
    ```bash
    git clone [https://github.com/your-username/Python-Security-Header-Analyzer.git](https://github.com/your-username/Python-Security-Header-Analyzer.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd Python-Security-Header-Analyzer
    ```

3.  **Create and activate a virtual environment:**
    ```bash
    # Create the venv
    python -m venv venv

    # Activate on Windows
    .\venv\Scripts\activate

    # Activate on Mac/Linux
    source venv/bin/activate
    ```

4.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script from your terminal, followed by the full URL you want to analyze.

```bash
python analyzer.py <url>
Examples
Analyzing a secure site:

Bash

$ python analyzer.py [https://github.com](https://github.com)

✅ Success! Connected to [https://github.com](https://github.com) (Status Code: 200)

--- Security Header Analysis ---
✅ [FOUND]   Content-Security-Policy
✅ [FOUND]   Strict-Transport-Security

--- Summary ---
✅ Secure: All critical security headers were found.
Analyzing a less secure site:

Bash

$ python analyzer.py [http://example.com](http://example.com)

✅ Success! Connected to [http://example.com](http://example.com) (Status Code: 200)

--- Security Header Analysis ---
❌ [MISSING] Content-Security-Policy
❌ [MISSING] Strict-Transport-Security

--- Summary ---
❌ Not Secure: One or more critical security headers are missing.
Handling user error:

Bash

$ python analyzer.py

Usage: python analyzer.py <url>
