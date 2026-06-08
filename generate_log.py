from datetime import datetime
import sys

def generate_log(log_data):
    """
    Creates a log file with timestamped filename and writes log entries.
    
    Args:
        log_data: A list of strings to write to the log file
        
    Returns:
        str: The filename that was created
        
    Raises:
        ValueError: If log_data is not a list
    """
    # Check if log_data is a list
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")
    
    # Create timestamped filename (format: log_YYYYMMDD.txt)
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    # Write each log entry to the file
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")
    
    # Print confirmation message
    print(f"Log written to {filename}")
    
    return filename

def fetch_api_data():
    """
    Optional: Fetch data from an API using requests library
    """
    import requests
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

if __name__ == "__main__":
    # Example usage for testing
    log_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_data)
    
    # Optional: Test the API fetch
    # post = fetch_api_data()
    # print("Fetched Post Title:", post.get("title", "No title found"))
