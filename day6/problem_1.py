def treat(file):
    buffer = []
    for i, char in enumerate(file.read()):
        if len(buffer) < 13:
            buffer.append(char)
        else:
            if valid_buffer(buffer) and char not in buffer:
                print(buffer)
                print(char)
                print(i + 1)
                return
            else:
                buffer.pop(0)
                buffer.append(char)


def valid_buffer(buffer):
    return len(buffer) == len(set(buffer))


with open("day6/input") as file:
    treat(file)
