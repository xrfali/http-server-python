import sys
from server import Server

def main():
    args = sys.argv
    file_path = None
    if len(args) > 2:
        file_path = args[2]

    Server(file_path).start()

if __name__ == "__main__":
    main()