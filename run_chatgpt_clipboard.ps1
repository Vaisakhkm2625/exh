# Define the path to the virtual environment
$venvPath = ".\venv"  # Change this to your virtual environment folder
$scriptPath = ".\main.py"  # Path to your Python script

# Check if the virtual environment exists
if (-Not (Test-Path $venvPath)) {
    Write-Error "Virtual environment not found at $venvPath"
    exit 1
}

# Activate the virtual environment
$activateScript = Join-Path $venvPath "Scripts\Activate.ps1"
if (-Not (Test-Path $activateScript)) {
    Write-Error "Activation script not found: $activateScript"
    exit 1
}

# Run the activation script
& $activateScript

# Run the Python script
if (Test-Path $scriptPath) {
    python $scriptPath
} else {
    Write-Error "Python script not found: $scriptPath"
}

# Deactivate the virtual environment
deactivate
