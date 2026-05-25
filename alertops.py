import subprocess
import sys
import os


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    hello_file = os.path.join(current_dir, "hello_world.py")

    subprocess.call([sys.executable, hello_file])


if __name__ == "__main__":
    main()
