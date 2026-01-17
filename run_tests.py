#!/usr/bin/env python3
"""Simple test runner for the FastAPI application"""

import sys
import os

# Add the current directory and src to Python path
current_dir = os.getcwd()
sys.path.insert(0, current_dir)
sys.path.insert(0, os.path.join(current_dir, 'src'))

try:
    import pytest
    # Run pytest on the tests directory
    sys.exit(pytest.main(['-v', 'tests/']))
except ImportError as e:
    print(f"Error: {e}")
    print("Please install pytest: pip install pytest")
    sys.exit(1)