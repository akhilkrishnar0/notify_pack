## Notify Package

A simple Python package to display notifications when a script finishes.

## Installation

```bash

pip install git+https://github.com/akhilkrishnar0/notify_pack.git

```

## Usage

```bash
from notify_package import send_notification
```

## Example
```
from notify_pack import send_notification

# Your script logic
for i in range(10000):
    pass

send_notification(title="Task Completed", message="Your script has finished running!", timeout=120):
```
