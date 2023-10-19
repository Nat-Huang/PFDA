def main():
    quotesdb = open("quotesdb.txt", 'r')
    quotes_list = list(quotesdb)
    print(quotes_list)

if __name__ == "__main__":
    main()