import re

# function to remove 3rd column from each line of train.txt file
# input - input file name, train.txt 
# output - output file name
def preprocess(input_file, output_file):
  with open(input_file, 'r') as f, open(output_file, 'w') as out:
    for line in f:
        # Ignore the lines that separate sentences in the file
        # match the pattern of a line ending with "O" and not containing any other English alphabet
        if re.match(r'^[^\w]*[oO][^\w]*$', line):
            line = line.strip()
            cols = line.split()
            out.write(' '.join(cols) + '\n')
        else:
          line = line.strip()
          cols = line.split()
          out.write(' '.join(cols[:2]) + '\n')