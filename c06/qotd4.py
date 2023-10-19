import random 

def main():
    with open("quotesdb.txt", 'r') as quotesdb:
        quotes_list = list(quotesdb)
    print(random.choice(quotes_list), end='')

if __name__ == "__main__":
    main()