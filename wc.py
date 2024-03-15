import sys

print("hello world from wc cli")

def print_wc_output(counts, filepath):
    spacing = "    "
    for count in counts:
        print(spacing + str(count), end="")
        spacing = spacing[:-1]
    print(" " + filepath)

def parse_arguments(argv):
    argv.pop(0)
    print(argv)
    file = ""
    useDefaultOptions = True
    options = {'c': False, 'm': False, 'l': False, 'w': False}
    for arg in argv:
        if (arg.startswith("-")):
            useDefaultOptions = False
            optionsToAdd = list(arg[1:])
            print("optionsToAdd: ", optionsToAdd)
            for option in optionsToAdd:
                if(option == 'c'): options['m'] = False
                elif (option == 'm'): options['c'] = False
                elif (option != 'w' and option != 'l'):
                    print("wc-cli: illegal option -- " + option)
                    print("usage: wc [-clmw] [file ...] ")
                    exit()
                options[option] = True
        else: 
            file = arg
            print("file: ", arg)
    
    if(useDefaultOptions):
        options = {'c': True, 'm': False, 'l': True, 'w': True}

    return [options, file]

def read_binary(filepath, options):
    try: 
        file = open(filepath, "rb")

        line_count = 0
        byte_count = 0
        word_count = 0

        line = file.readline()
        while(line):
            if(options['l']): line_count = line_count + 1
            if(options['c']): byte_count = byte_count + len(line)
            if(options['w']): 
                words = line.strip().split()
                word_count = word_count + len(words)
            line = file.readline()
        
        file.close()
        counts = []
        if(options['l']): counts.append(line_count)
        if(options['w']): counts.append(word_count)
        if(options['c']): counts.append(byte_count)
        
        print_wc_output(counts, filepath)

    except Exception as e: 
        print("wc-cli: " + filepath + ": " + e.args[1])
        exit()


def read_text(filepath, options):
    try: 
        file = open(filepath)
        line = file.readline()

        line_count = 0
        char_count = 0
        word_count = 0
        while(line):
            if(options['l']): line_count = line_count + 1
            if(options['m']): char_count = char_count + len(line) + 1
            if(options['w']): 
                words = line.strip().split()
                word_count = word_count + len(words)
            line = file.readline()
        
        file.close()
        counts = []
        if(options['l']): counts.append(line_count)
        if(options['w']): counts.append(word_count)
        if(options['m']): counts.append(char_count)
        
        print_wc_output(counts, filepath)

    except Exception as e: 
        print("wc-cli: " + filepath + ": " + e.args[1])
        exit()

print(sys.argv)
[options, filepath] = parse_arguments(sys.argv)
print("options: ", options)
print("filename: ", filepath)

if(options['m']):
    read_text(filepath, options)
else:
    read_binary(filepath, options)


