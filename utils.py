def read_file(filename):
    file_contents = open(filename, "r")
    return file_contents.readlines()

def read_files(filenames):
    all_lines = []
    for filename in filenames:
        file_contents = open(filename, "r")
        all_lines.append(file_contents.readlines())
    
    return all_lines