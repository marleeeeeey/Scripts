import argparse
import re


class Item:
    def __init__(self):
        self.word = ""
        self.meaning = ""
        self.example = ""

    def add_to_example(self, s):
        if self.example == "":
            self.example = s
        else:
            self.example += " " + s


def any_special_symbol_in_string(line):
    chars = set('{}():.,1234567890<>')
    return any((c in chars) for c in line)


def remove_numbers_from_string(line):
    result = ''.join([i for i in line if not i.isdigit()])
    return result


def append_lines_to_file(file_name, lines):
    with open(file_name, 'a') as the_file:
        for line in lines:
            the_file.write(line + '\n')


def number_words_in_string(line):
    line = remove_numbers_from_string(line)
    count = len(re.findall(r'\w+', line))
    return count


def truncate_line_to(line, size):
    return line[:size] + (line[size:] and '...')


def write_items_to_file(file_name, items):
    file = open(file_name, "w", encoding="utf8")
    for item in items:
        file.write(item.word)
        file.write("\n")
        file.write(item.meaning)
        file.write("\n")
        file.write(item.example)
        file.write("\n")
    file.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, default="", help="import file")
    parser.add_argument("-o", "--output", type=str, default="", help="output file")
    args = parser.parse_args()

    input_file_name = args.input
    output_file_name = args.output
    if input_file_name == "" or output_file_name == "":
        print("Provide all arguments to start conversion")
        return

    content = []
    with open(input_file_name, encoding="utf8") as f:
        content = f.readlines()

    items = []
    last_line = len(content)
    counter = 1
    curr_item = Item()
    for i in range(last_line):
        cur = content[i].rstrip()
        next = ""
        if (i + 1) < last_line:
            next = content[i + 1].rstrip()
        else:
            print("Last line is", cur)
            continue

        if counter == 2:  # Meaning
            if curr_item.word == "":
                raise Exception("Have a meaning but word is empty. Line", cur)
            else:
                curr_item.meaning = cur
                counter = 3
        elif counter == 3:  # Example
            curr_item.add_to_example(cur)
            counter = 4
        elif counter == 4:  # Example multiple lines
            if number_words_in_string(cur) == 1 and number_words_in_string(next) > 1 \
                    and not any_special_symbol_in_string(cur) and not cur == "template":
                items.append(curr_item)
                counter = 1
            else:
                curr_item.add_to_example(cur)

        if counter == 1:  # Word
            if number_words_in_string(cur) == 1:
                curr_item = Item()
                curr_item.word = cur
                counter = 2
            else:
                raise Exception("Word is not from one word. Line", cur)

    for item in items:
        print("WORD:", item.word)
        print("MEANING:", item.meaning)
        print("EXAMPLE:", item.example)

    print("Loaded", len(items), "words")

    write_items_to_file(output_file_name, items)

    return


main()
