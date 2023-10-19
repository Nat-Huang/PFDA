def main():
    quotes_file = open("creative_quotes.txt", "r")
    print(quotes_file.readline())
    print(quotes_file.readline())
    quotes_file.close()

if __name__ == "__main__":
    main()