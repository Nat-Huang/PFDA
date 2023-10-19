import random 

def main():
    quotesdb = open("quotesdb.txt", 'r')
    quotes_list = list(quotesdb)
    quotesdb.close()
    index = random.randrange(len(quotes_list))
    print(quotes_list)

if __name__ == "__main__":
    main()