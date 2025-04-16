import os
from pathlib import Path
import pytest
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from dir_size import get_dir_size

@pytest.fixture
def setup_test_dir(tmp_path):
    """Set up a temporary directory with test files."""
    test_dir = tmp_path / "test_files"
    test_dir.mkdir()
    (test_dir / "file1.txt").write_text("Hello")
    (test_dir / "file2.txt").write_text("World")
    return test_dir

def test_get_dir_size(setup_test_dir):
    """Test directory size calculation."""
    size = get_dir_size(str(setup_test_dir))
    assert size == 10  # "Hello" (5 bytes) + "World" (5 bytes)