def main():
    quotes_file = open("creative_quotes.txt", "r")
    for line in quotes_files:
        print(line, end='')
    quotes_file.close()

if __name__ == "__main__":
    main()