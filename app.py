import subprocess

def run_command(command):
    # Vulnerable code: Command injection
    subprocess.call(command, shell=True)

user_input = input("Enter a command: ")
run_command(user_input)
