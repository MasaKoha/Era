#! /usr/local/bin/python
# coding=utf-8


def main():
    file_data = open("log.txt", "r")
    all_character = ""
    for line in file_data:
        all_character += line.encode().decode('unicode-escape')
    char_list = list(set(all_character))

    write_characters = ""
    for character in char_list:
        write_characters += character

    file_writer = open('use_character.txt', 'w')
    file_writer.write(write_characters)
    file_writer.close()
    print("Output File use_character.txt")


if __name__ == '__main__':
    main()
