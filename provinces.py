
def main():
    provinces = read("provinces.txt")
    print(provinces)
    provinces.pop(0)
    provinces.pop()
    for i in range(len(provinces)):
        if provinces[i] == "AB":
            provinces[i] = "Alberta" 
    total = provinces.count("Alberta")
    
    print(f"\nAlberta occurs {total} times in the modified list.")   


def read(provinces_file):
    list = []
    with open(provinces_file, "rt") as file:
        for text in file:
            just_text = text.strip()
            list.append(just_text)
    return list

if __name__ == "__main__":
    main()