import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.generate_log import generate_log
from datetime import datetime

def test_valid_log_data():
    """Test that valid log data creates file with correct contents"""
    log_entries = ["Entry 1", "Entry 2", "Entry 3"]
    filename = generate_log(log_entries)
    expected_filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    assert filename == expected_filename, "Filename pattern incorrect"
    assert os.path.exists(filename), "File not created"
    
    with open(filename, "r") as f:
        contents = f.read().strip().split('\n')
    assert contents == log_entries, "File contents don't match"
    
    os.remove(filename)
    print("✓ test_valid_log_data passed")

def test_empty_list():
    """Test that empty list creates empty file without errors"""
    filename = generate_log([])
    assert os.path.exists(filename), "File not created for empty list"
    
    with open(filename, "r") as f:
        assert f.read() == "", "File should be empty"
    
    os.remove(filename)
    print("✓ test_empty_list passed")

def test_invalid_input():
    """Test that non-list input raises ValueError"""
    import pytest
    
    invalid_inputs = ["not a list", 123, None, {"key": "value"}]
    
    for invalid in invalid_inputs:
        try:
            generate_log(invalid)
            assert False, f"Should have raised ValueError for {type(invalid)}"
        except ValueError:
            pass
    
    print("✓ test_invalid_input passed")

def test_print_message():
    """Test that function prints confirmation message"""
    import io
    import sys
    
    # Capture print output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    filename = generate_log(["test"])
    sys.stdout = sys.__stdout__
    
    assert f"Log written to {filename}" in captured_output.getvalue()
    
    os.remove(filename)
    print("✓ test_print_message passed")

if __name__ == "__main__":
    print("Running tests for generate_log...")
    print("-" * 40)
    test_valid_log_data()
    test_empty_list()
    test_invalid_input()
    test_print_message()
    print("-" * 40)
    print("All tests passed! ✓")
