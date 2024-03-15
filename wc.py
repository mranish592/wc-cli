import sys

print("hello world from wc cli")

def parse_arguments(argv):
    if(argv[1] != '-c'):
        print("Incorrect usage. The syntax is: ")
        print("python wc.py -c <filename>")
        exit()
    return ['c', argv[2]]

def read_binary(filepath):
    file = open(filepath, "rb")
    line = file.readline()

    line_count = 0
    byte_count = 0
    word_count = 0
    while(line):
        line_count = line_count + 1
        byte_count = byte_count + len(line)
        words = line.strip().split()
        word_count = word_count + len(words)
        line = file.readline()
    
    file.close()
    print("lines: ", line_count)
    print("bytes: ", byte_count)
    print("words: ", word_count)

def read_text(filepath):
    file = open(filepath)
    line = file.readline()

    line_count = 0
    char_count = 0
    word_count = 0
    while(line):
        line_count = line_count + 1
        char_count = char_count + len(line) + 1
        words = line.strip().split()
        word_count = word_count + len(words)
        line = file.readline()
    
    file.close()
    print("lines: ", line_count)
    print("characters: ", char_count)
    print("words: ", word_count)

print(sys.argv)
[options, filepath] = parse_arguments(sys.argv)
print("options: ", options)
print("filename: ", filepath)

read_binary(filepath)
read_text(filepath)


