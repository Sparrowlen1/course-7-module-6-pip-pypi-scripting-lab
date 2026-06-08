from datetime import datetime

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


if __name__ == "__main__":
    # Example usage for testing
    log_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_data)
