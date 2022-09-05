with open('input.txt.txt', 'r', encoding="utf-8") as input_file:
    with open('output.txt.txt', 'w', encoding="utf-8") as output_file:
        for line in reversed(input_file.readlines()):
            output_file.write(line)
