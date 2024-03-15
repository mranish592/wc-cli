import sys

def print_wc_output(counts, filepath):
    for count in counts:
        spacing = " "*(8 - len(str(count)))
        print(spacing + str(count), end="")
    print(" " + filepath)

def parse_arguments(argv):
    argv.pop(0)
    files = []
    useDefaultOptions = True
    options = {'c': False, 'm': False, 'l': False, 'w': False}
    for arg in argv:
        if (arg.startswith("-")):
            useDefaultOptions = False
            optionsToAdd = list(arg[1:])
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
            files.append(file)
    
    if(useDefaultOptions):
        options = {'c': True, 'm': False, 'l': True, 'w': True}

    return [options, files]

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
        return counts

    except Exception as e: 
        print("wc-cli: " + filepath + ": " + e.args[1])
        return None



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
        return counts

    except Exception as e: 
        print("wc-cli: " + filepath + ": " + e.args[1])
        return None

[options, files] = parse_arguments(sys.argv)

all_counts = []
for filepath in files:
    counts = []
    if(options['m']):
        counts = read_text(filepath, options)
    else:
        counts = read_binary(filepath, options)
    all_counts.append(counts)

if(len(all_counts) > 1):
    all_counts = [counts for counts in all_counts if counts is not None]
    counts_len = len(all_counts[0])
    total_counts = []
    for i in range(counts_len):
        total_count = 0
        for counts in all_counts:
            total_count = total_count + counts[i]
        total_counts.append(total_count)
    
    print_wc_output(total_counts, "total")
    




