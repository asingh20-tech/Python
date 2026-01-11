def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    return input("what's you name? ")

def get_house():        
    return input("house: ")

if __name__ == "__main__":
    main() 