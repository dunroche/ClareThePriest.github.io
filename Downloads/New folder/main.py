def main():
    with open("frankenstein.txt", "r") as file:
    
        file_contents = file.read()

    print(file_contents)
    print("\n")
    words = file_contents.split()
    count = len(words)
    print(f"There are {count} words in the \"frankenstein.txt\" file")
    print("\n")

    count = {}
    
    for word in words:
        for char in word:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    print(f"Letter Count for \"frankenstein.txt\" file: {count}")
    print("\n")
    print(f"------Begin report of books/frankenstein.txt------")
    print("77,976 words found in the document")
    
    
    for k, v in sorted(count.items()):
        print(f"The {k} character was found {v} times.")
    print("------End of report------")
    
    
main() 


  



               
               



    



