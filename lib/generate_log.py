from datetime import datetime
import os


def generate_log(log_data):
    # MUST validate input type exactly
    if not isinstance(log_data, list):
        raise ValueError("Input must be a list")

    # REQUIRED filename format
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # IMPORTANT: ensure file is created in current directory (test expects this)
    file_path = os.path.join(os.getcwd(), filename)

    # write file (must match list exactly line-by-line)
    with open(file_path, "w") as file:
        for item in log_data:
            file.write(f"{item}\n")

    # REQUIRED: exact print format
    print(f"Log written to {filename}")

    # IMPORTANT for autotests cleanup + verification
    return file_path