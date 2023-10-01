import sys
import requests
import pyfiglet
print(pyfiglet.figlet_format("PANSCANNER"))
if __name__ == "__main__":
    banner = """
    Aswin kumar
    Pavan
    nishanth babu
    """
    print(banner)
# Define ANSI color codes
RED = '\033[0;31m'
NC = '\033[0m'  # No Color

# Function to display help information
def display_help():
    print("Usage: {} [-u URL] [-list FILE_PATH]".format(sys.argv[0]))
    print("Check for parameter-based open redirects in a single URL or a list of URLs.")
    print("\nOptions:")
    print("  -u URL          The URL to check for open redirects.")
    print("  -list FILE_PATH Specify a file containing a list of URLs to check.")
    print("  --help          Display this help message.")

# Function to check for parameter-based open redirects
def check_parameter_redirect(url):
    param_name = "url"  # Change this to the parameter you want to test

    response = requests.head(url, allow_redirects=True)

    if "location" in response.headers and param_name in response.url:
        print(f"{RED}Parameter-based open redirect found at: {url}")
        print(f"Redirects to: {response.url}{NC}")
    else:
        print(f"No parameter-based open redirect found at: {url}")

# If no arguments are provided, display help
if len(sys.argv) == 1:
    display_help()
    sys.exit(0)

# Parse command line options
i = 1
while i < len(sys.argv):
    if sys.argv[i] == "-u":
        single_url = sys.argv[i + 1]
        check_parameter_redirect(single_url)
        i += 2
    elif sys.argv[i] == "-list":
        file_path = input("Please provide the path to the file containing URLs:\n")
        try:
            with open(file_path, "r") as file:
                for url in file.readlines():
                    check_parameter_redirect(url.strip())
        except FileNotFoundError:
            print("Invalid file path.")
            sys.exit(1)
        i += 1
    elif sys.argv[i] == "--help":
        display_help()
        sys.exit(0)
    else:
        print("Invalid option. Use --help for usage information.")
        sys.exit(1)
