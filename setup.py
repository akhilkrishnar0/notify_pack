from setuptools import setup, find_packages

setup(
    name="notify_package",
    version="0.1",
    packages=find_packages(),
    install_requires=["plyer"],
    entry_points={
        "console_scripts": [
            "notify=notify_package.notifier:send_notification",
        ],
    },
    author="Your Name",
    description="A simple Python package to send notifications.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)