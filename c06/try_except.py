def main():
    filename = "test.txt"
    with open(filename, 'r') as file:
        print(file.readliness())
except FileNotFoundError as err:
    msg: f"Oops! We couldn't find the file "{filename}""
    print(msg)
    print(err)

if __name__ == "__main__":
    main()