# Pulse - Daily Summary Bot

Pulse is a Python automation project that generates a daily summary containing weather information and an inspirational quote. The project runs automatically using GitHub Actions and stores the generated summary as a workflow artifact.

## Features

* Fetches current weather information using wttr.in
* Retrieves a daily inspirational quote
* Generates a formatted daily summary report
* Saves the summary as a text file
* Automated execution using GitHub Actions
* Uploads generated summaries as workflow artifacts

## Tech Stack

* Python
* Requests
* GitHub Actions
* Git & GitHub

## Project Structure

folio
 ├── bot.py
 ├── requirements.txt
 ├── daily_summary.txt
 └── .github
     └── workflows
          └── daily.yml

## How It Works

1. The bot fetches weather data from wttr.in.
2. It retrieves a random inspirational quote.
3. A daily summary is generated and stored in `daily_summary.txt`.
4. GitHub Actions executes the workflow automatically on a schedule.
5. The generated summary is uploaded as a workflow artifact.

## Sample Output

```text
==================================
      PULSE - Daily Summary
==================================

WEATHER
Thiruvananthapuram: 🌦 +29°C

TODAY'S QUOTE
"Success is the sum of small efforts repeated day in and day out."
- Robert Collier

==================================
```

## Learning Outcomes

* Python automation
* API integration
* Exception handling
* File handling
* GitHub Actions workflows
* Scheduled task automation

## Author

Kritikaa
