from setuptools import setup
from setuptools.command.install import install
import subprocess
import sys
import os


class CustomInstall(install):
    def run(self):
        install.run(self)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        hello_file = os.path.join(current_dir, "hello_world.py")

        subprocess.call([sys.executable, hello_file])


setup(
    name="alertops",
    version="1.0",
    py_modules=["alertops"],
    entry_points={
        "console_scripts": [
            "alertops=alertops:main",
        ],
    },
    cmdclass={
        "install": CustomInstall,
    },
)
