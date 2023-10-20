def main():
    filename = "test.txt"
    try:
            file = open(filename, "r")
            print("File opened for reading.")
            print(file.readliness())
    except FileNotFoundError:
        file = open(filename, "w")
        print("File not found. Creating a new {filename} instead.")
    finally:
        file.close()
        print("File closed.")

if __name__ == "__main__":
    main()