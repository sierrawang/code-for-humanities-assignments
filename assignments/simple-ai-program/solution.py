from ai import call_gpt

def main():
    query = input("Query: ")
    response = call_gpt(query)
    print(f"Response: {response}")

if __name__ == "__main__":
    main()