def main():
    content = (
        '"Not all those who wander are lost." - Bilbo Baggins\n'
        '"All\'s well that ends better." - Hamfast Gamgee\n'
    )

    with opem("lotr_quotes.txt", "w") as file:
        file.write(content)

if __name__ == "__main__":
    main()