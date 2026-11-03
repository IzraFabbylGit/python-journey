"""project phase 0 env_check.py"""

import platform
import sys


def check_environment():
    print(f"Python version: {sys.version}")
    print(f"Platform: {sys.platform}")
    print(f"Executable: {sys.executable}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")


if __name__ == "__main__":
    check_environment()
