from setuptools import setup
from setuptools.command.install import install
import subprocess
import sys
import os


class CustomInstallCommand(install):
    def run(self):
        install.run(self)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        hello_file = os.path.join(current_dir, "hello_world.py")

        # Run during installation
        subprocess.call([sys.executable, hello_file])


setup(
    name="alertops",
    version="1.0",
    description="Recon Alert Plugin",
    author="nvk0x",
    py_modules=["alertops"],
    packages=["alertops"],
    entry_points={
        "console_scripts": [
            "alertops=alertops:main",
        ],
    },
    cmdclass={
        "install": CustomInstallCommand,
    },
)
