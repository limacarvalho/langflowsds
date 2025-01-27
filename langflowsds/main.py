import os
import sys
import subprocess

def main():
    # Check if the port number is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 run_langflow.py <TCP_PORT>")
        sys.exit(1)
    
    # Get the TCP_PORT from command-line arguments
    tcp_port = sys.argv[1].strip()

    # Validate that the TCP_PORT is a valid number
    if not tcp_port.isdigit():
        print("Error: TCP_PORT must be a valid number.")
        sys.exit(1)
    
    # Construct the bash command
    langflow_command = [
        # uv run --directory $HOME/.aitools langflow
        "/opt/conda/envs/default/bin/uv",
        "run",
        "--directory",
        "/home/joaoc/.aitools",
        "langflow",
        "run",
        "--host", "0.0.0.0",
        "--port", tcp_port,
        "--log-level", "info",
        "--auto-saving"
    ]

    # Run the command as a subprocess
    try:
        subprocess.run(langflow_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")
    except FileNotFoundError:
        print("Error: langflow command not found. Check the installation path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
