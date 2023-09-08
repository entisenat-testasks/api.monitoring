import requests
import time

# Configuration for API
BLOCKLIST_DE_API_URL = "https://api.blocklist.de/getlast.php"

# Define the Splunk input
SPLUNK_TCP_HOST = "127.0.0.1"
SPLUNK_TCP_PORT = 8000

def collect_blocklist_data():
    try:
        response = requests.get(BLOCKLIST_DE_API_URL)
        response.raise_for_status()

        data = response.text

        splunk_connection = (SPLUNK_TCP_HOST, SPLUNK_TCP_PORT)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(splunk_connection)
            s.sendall(data.encode())

        print("Data successfully ingested")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    while True:
        collect_blocklist_data()
        # Sleep for 1 hour
        time.sleep(3600)