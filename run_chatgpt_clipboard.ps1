# Get the directory of the script
$scriptDir = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent

# Change to the script's directory
Set-Location $scriptDir

# Define the virtual environment and Python script paths (relative to the script location)
$venvPath = Join-Path $scriptDir "venv"  # Adjust if your virtual environment folder is named differently
$scriptPath = Join-Path $scriptDir "./chatgpt_clipboard.py"  # Adjust to your Python script's name

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
