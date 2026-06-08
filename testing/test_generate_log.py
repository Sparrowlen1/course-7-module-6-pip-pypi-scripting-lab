import os
import sys
# Add the parent directory to path so we can import from lib
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.generate_log import generate_log
from datetime import datetime

def test_valid_log_data():
    """Test that valid log data creates file with correct contents"""
    print("Test 1: Valid log data...")
    log_entries = ["Entry 1", "Entry 2", "Entry 3"]
    filename = generate_log(log_entries)
    expected_filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    assert filename == expected_filename, "Filename pattern incorrect"
    assert os.path.exists(filename), "File not created"
    
    with open(filename, "r") as f:
        contents = f.read().strip().split('\n')
    assert contents == log_entries, "File contents don't match"
    
    os.remove(filename)
    print("✓ Passed\n")

def test_empty_list():
    """Test that empty list creates empty file without errors"""
    print("Test 2: Empty list...")
    filename = generate_log([])
    assert os.path.exists(filename), "File not created for empty list"
    
    with open(filename, "r") as f:
        content = f.read()
        assert content == "", "File should be empty"
    
    os.remove(filename)
    print("✓ Passed\n")

def test_invalid_input():
    """Test that non-list input raises ValueError"""
    print("Test 3: Invalid input (should raise ValueError)...")
    invalid_inputs = ["not a list", 123, None, {"key": "value"}]
    
    for invalid in invalid_inputs:
        try:
            generate_log(invalid)
            print(f"✗ Failed - Should have raised ValueError for {type(invalid)}")
            assert False
        except ValueError:
            print(f"✓ Correctly raised ValueError for {type(invalid)}")
    
    print("✓ All invalid input tests passed\n")

def test_confirmation_message():
    """Test that function prints confirmation message"""
    print("Test 4: Confirmation message...")
    import io
    import sys
    
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    filename = generate_log(["test message"])
    
    sys.stdout = sys.__stdout__
    
    assert f"Log written to {filename}" in captured_output.getvalue()
    
    os.remove(filename)
    print("✓ Passed\n")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("Running generate_log Tests")
    print("="*50 + "\n")
    
    test_valid_log_data()
    test_empty_list()
    test_invalid_input()
    test_confirmation_message()
    
    print("="*50)
    print("✅ ALL TESTS PASSED!")
    print("="*50)
