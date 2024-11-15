#!/bin/sh

# Get the directory where the script is located
SCRIPT_DIR=$(dirname "$(realpath "$0")")
notify-send "running" -t 100

# Navigate to the project directory
cd "$SCRIPT_DIR"

# Activate the virtual environment
source venv/bin/activate

# Run the Python script (replace 'your_script.py' with your actual script filename)
python ./chatgpt_clipboard.py

notify-send "done" -t 100

# Deactivate the virtual environment after the script is done
deactivate
