from ai import call_gpt

def main():
    name = input("Enter your name:")
    topic = input("Enter a topic:")
    print("Creating your haiku...")
    response = call_gpt(name,topic)
    print(response)


if __name__ == "__main__":
    main()