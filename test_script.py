import os
from generate_log import generate_log
from datetime import datetime

print("Testing generate_log function...")
print("-" * 40)

# Test 1: Valid log data
print("Test 1: Valid log data")
log_entries = ["Entry 1", "Entry 2", "Entry 3"]
filename = generate_log(log_entries)
expected_filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
assert filename == expected_filename, "Filename pattern incorrect"
assert os.path.exists(filename), "File not created"
print("✓ Filename pattern correct")
print("✓ File created")

# Check file contents
with open(filename, "r") as f:
    contents = f.read().strip().split('\n')
assert contents == log_entries, "File contents don't match"
print("✓ File contents match input list")
os.remove(filename)
print("✓ Test 1 passed\n")

# Test 2: Empty list
print("Test 2: Empty list")
filename = generate_log([])
assert os.path.exists(filename), "File not created for empty list"
with open(filename, "r") as f:
    assert f.read() == "", "File should be empty"
print("✓ Empty list handled correctly")
os.remove(filename)
print("✓ Test 2 passed\n")

# Test 3: ValueError for non-list input
print("Test 3: Invalid input handling")
try:
    generate_log("not a list")
    print("✗ Should have raised ValueError")
except ValueError as e:
    print("✓ ValueError raised for string input")

try:
    generate_log(123)
    print("✗ Should have raised ValueError")
except ValueError as e:
    print("✓ ValueError raised for integer input")

try:
    generate_log(None)
    print("✗ Should have raised ValueError")
except ValueError as e:
    print("✓ ValueError raised for None input")
print("✓ Test 3 passed\n")

print("-" * 40)
print("All tests passed! ✓")
