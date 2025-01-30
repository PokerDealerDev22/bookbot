def sort_on(dict):
    return dict["num"]

def sort_alpha(text):
    alpha_count={}
    lowered_text=text.lower()
    word_count=len(text.split())
    for character in lowered_text:
        if character in alpha_count:
            alpha_count[character]+=1
        else:
            alpha_count[character]=1
    alpha_list=[]
    for key in alpha_count:
        if key.isalpha():
            char_dict= {"char": key, "num": alpha_count[key]}
            alpha_list.append(char_dict)
    alpha_list.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()

    for char_dict in alpha_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")

    print("--- End report ---")
    
    

def character_count(text):
    count={}
    lowered_text=text.lower()
    for character in lowered_text:
        if character in count:
            count[character]+=1
        else:
            count[character]=1
    return count


def word_count(text):
    count=len(text.split())
    return count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents= f.read()
        sort_alpha(file_contents)
main()
