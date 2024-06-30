#MAR 2024

import sys

def read_a3m(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    headers = []
    sequences = []
    seq_dict = {}
    current_header = None

    for line in lines:
        if line.startswith('>'):
            current_header = line.strip()
            headers.append(current_header)
            seq_dict[current_header] = []
        else:
            seq_dict[current_header].append(line.strip())

    for header in headers:
        sequences.append((header, ''.join(seq_dict[header])))

    return sequences

def write_combined_a3m(file1_sequences, file2_sequences, output_file):
    with open(output_file, 'w') as file:
        # Calculate sequence lengths and create header
        len1 = len(file1_sequences[0][1])
        len2 = len(file2_sequences[0][1])
        header = f"#{len1},{len2}\t1,1\n"
        file.write(header)
        
        # Write sequences from the first file
        for header, sequence in file1_sequences:
            file.write(f"{header}_1\n")
            file.write(sequence + '\n')
        
        # Write sequences from the second file
        for header, sequence in file2_sequences:
            file.write(f"{header}_2\n")
            file.write(sequence + '\n')

def main():
    if len(sys.argv) != 4:
        print("Usage: python combine_a3m.py <file1.a3m> <file2.a3m> <output.a3m>")
        sys.exit(1)
    
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    output_file = sys.argv[3]
    
    file1_sequences = read_a3m(file1)
    file2_sequences = read_a3m(file2)
    
    write_combined_a3m(file1_sequences, file2_sequences, output_file)

if __name__ == "__main__":
    main()