# List of input file names
input_files = ['ybmebd.txt', 'csjebd.txt']

# Initialize merged content with the first file's content (including header)
merged_content = []
with open(input_files[0], 'r') as first_file:
    merged_content = first_file.readlines()

# Read the content from the remaining files and append to merged content
for input_file in input_files[1:]:
    with open(input_file, 'r') as file:
        content = file.readlines()
        merged_content.extend(content[1:])  # Skip the header in subsequent files

# Write the merged content to a new file
with open('ebd.txt', 'w') as merged_file:
    for line in merged_content:
        merged_file.write(line)
