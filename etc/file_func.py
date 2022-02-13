def convert_file_to_text(file):
    text = ''
    with open(file=file, mode='r') as f:
        text += f.read()
    return text
