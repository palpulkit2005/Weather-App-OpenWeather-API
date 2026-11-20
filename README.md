# Project 05 – Weather App with Live OpenWeather API

## Description
This is a Python-based Weather Application that fetches real-time weather information and a 5-day weather forecast for any city using the OpenWeather API.

## Features
- Fetches real-time weather information.
- Displays city name and temperature.
- Shows feels-like temperature.
- Displays humidity and weather conditions.
- Shows wind speed.
- Provides a 5-day weather forecast.
- Handles invalid city names and API errors.
- Uses environment variables to protect the API key.

## Technologies Used
- Python
- OpenWeather API
- Requests
- Python-dotenv

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## API Key Setup

1. Create an account on OpenWeather.
2. Generate an API key.
3. Create a `.env` file in the project folder.
4. Add your API key:

```text
API_KEY=your_api_key_here
```

**Note:** Never upload your actual API key to GitHub.

## How to Run

```bash
python3 main.py
```

Enter a city name to view its current weather and 5-day forecast.

## Project Files
- `main.py` – Main application code.
- `requirements.txt` – Required Python libraries.
- `.env` – Stores the API key (not uploaded to GitHub).
- `.gitignore` – Prevents sensitive files from being uploaded.

## Author
Pulkit Pal