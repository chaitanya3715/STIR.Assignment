# Selenium Twitter Trending Topics Fetcher

This project demonstrates a Selenium-based web scraper that fetches the top 5 trending topics from Twitter's "What’s Happening" section. The results are stored in a MongoDB database along with metadata such as the execution time, IP address, and a unique ID for each run. The project also includes a Flask-based web interface to trigger the Selenium script and display results.

---

## Features

- Fetch top 5 trending topics from Twitter’s homepage.
- Store results in MongoDB with the following fields:
  - Unique ID
  - Names of trending topics
  - Date and time of execution
  - IP address used for the query
- Use ProxyMesh to rotate IP addresses for each request.
- Simple HTML interface to trigger the script and display results.
- JSON extract of the stored record shown on the webpage.

---

## Project Structure

```
.
├── app.py                # Flask application
├── selenium_script.py    # Selenium script to fetch trending topics
├── requirements.txt      # Python dependencies
├── templates
│   └── index.html        # HTML interface
├── static
│   └── style.css         # CSS styles (optional)
├── venv/                 # Python virtual environment
└── README.md             # Project documentation
```

---

## Prerequisites

- Python 3.7 or above
- Google Chrome browser installed
- ChromeDriver (compatible with your Chrome version)
- MongoDB running locally or remotely
- ProxyMesh credentials (for IP rotation)
- Twitter account credentials

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - **Windows**:
     ```bash
     .\venv\Scripts\Activate
     ```
   - **Linux/Mac**:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Download and configure ChromeDriver:
   - [Download ChromeDriver](https://chromedriver.chromium.org/downloads) matching your Chrome version.
   - Place the `chromedriver.exe` file in an accessible path.

6. Configure MongoDB:
   - Ensure MongoDB is running locally or remotely.
   - Update the MongoDB URI in `app.py`:
     ```python
     client = MongoClient("mongodb://localhost:27017/")
     ```

7. Set up environment variables for Twitter and ProxyMesh credentials:
   - **Windows**:
     ```bash
     set TWITTER_USERNAME=your_username
     set TWITTER_PASSWORD=your_password
     set PROXYMESH_URL=http://your_proxymesh_url
     ```
   - **Linux/Mac**:
     ```bash
     export TWITTER_USERNAME=your_username
     export TWITTER_PASSWORD=your_password
     export PROXYMESH_URL=http://your_proxymesh_url
     ```

---

## Usage

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

3. Click the button on the webpage to run the Selenium script.

4. View the trending topics, metadata, and JSON extract of the record on the webpage.

---

## Testing Selenium Script

To test the Selenium script independently:
```bash
python selenium_script.py
```

Ensure the browser opens and fetches the trending topics correctly.

---

## Dependencies

All dependencies are listed in `requirements.txt`:
```text
selenium
flask
pymongo
proxymesh
```

Install them using:
```bash
pip install -r requirements.txt
```

---

## Common Issues

1. **500 Internal Server Error**:
   - Check Flask logs for detailed errors.
   - Ensure all credentials and paths are correctly set.

2. **WebDriverException**:
   - Verify ChromeDriver is compatible with your Chrome version.

3. **Login Issues**:
   - Ensure Twitter credentials are correct.
   - Check if Twitter’s DOM structure has changed, which might require updating Selenium locators.

4. **MongoDB Connection Issues**:
   - Confirm MongoDB is running.
   - Verify the connection URI.

---

## Future Enhancements

- Add Docker support for easier setup.
- Implement better error handling and retries in Selenium.
- Enhance the UI for better visualization of results.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

