def main():
    content = (
        '"Not all those who wander are lost." - Bilbo Baggins\n'
        '"All\'s well that ends better." - Hamfast Gamgee\n'
    )

    with open("lotr_quotes.txt", "a") as file:
        file.write(content)

if __name__ == "__main__":
    main()