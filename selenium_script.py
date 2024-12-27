import os
import time
import uuid
from datetime import datetime
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType

# MongoDB Configuration
MONGO_URI = "mongodb://localhost:27017"  # Replace with your MongoDB URI
DB_NAME = "TwitterData"
COLLECTION_NAME = "TrendingTopics"

# ProxyMesh Configuration
proxy_host = "proxy-ip-address.proxy-mesh.com"  # Replace with your ProxyMesh endpoint
proxy_port = "31280"  # Replace with your ProxyMesh port
proxy_credentials = f"username:password"  # Replace with your ProxyMesh credentials

# Twitter Credentials
username = os.getenv("TWITTER_USERNAME")
password = os.getenv("TWITTER_PASSWORD")
if not username or not password:
    raise ValueError("Twitter credentials not set in environment variables!")

def configure_proxy(chrome_options):
    """Configures proxy settings for Chrome."""
    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = f"{proxy_host}:{proxy_port}"
    proxy.ssl_proxy = f"{proxy_host}:{proxy_port}"
    proxy.add_to_capabilities(webdriver.DesiredCapabilities.CHROME)
    chrome_options.add_argument(f"--proxy-server=http://{proxy_credentials}@{proxy_host}:{proxy_port}")

def save_to_mongo(data):
    """Saves data to MongoDB."""
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    collection.insert_one(data)
    print("Data saved to MongoDB successfully!")

def fetch_trending_topics():
    """Fetch trending topics and store the result in MongoDB."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    configure_proxy(chrome_options)

    # Set up the driver
    driver_path = "C:\Program Files\Google\Chrome\Application"  # Replace with the path to your ChromeDriver
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Open Twitter's login page
        driver.get("https://twitter.com/login")
        time.sleep(5)  # Wait for the login page to load

        # Input username
        username_input = driver.find_element(By.NAME, "text")
        username_input.send_keys(username)
        driver.find_element(By.XPATH, '//div[contains(text(), "Next")]').click()
        time.sleep(3)

        # Input password
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(password)
        driver.find_element(By.XPATH, '//div[contains(text(), "Log in")]').click()
        time.sleep(5)

        # Locate the "What’s Happening" section
        trends_section = driver.find_element(By.XPATH, '//section[@aria-labelledby="accessible-list-0"]')
        trends = trends_section.find_elements(By.XPATH, './/span[contains(@class, "css-901oao")]')

        # Fetch top 5 trending topics
        top_trends = [trend.text for trend in trends[:5]]

        # Generate unique ID
        unique_id = str(uuid.uuid4())

        # Capture date and time
        end_time = datetime.now()

        # Get IP address (used in the proxy)
        ip_address = proxy_host

        # Prepare data for MongoDB
        data = {
            "unique_id": unique_id,
            "trend1": top_trends[0] if len(top_trends) > 0 else None,
            "trend2": top_trends[1] if len(top_trends) > 1 else None,
            "trend3": top_trends[2] if len(top_trends) > 2 else None,
            "trend4": top_trends[3] if len(top_trends) > 3 else None,
            "trend5": top_trends[4] if len(top_trends) > 4 else None,
            "end_time": end_time,
            "ip_address": ip_address
        }

        # Save data to MongoDB
        save_to_mongo(data)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()

# Call the function to fetch trending topics
fetch_trending_topics()
