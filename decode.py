def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    message_dict = {}
    for line in lines:
        parts = line.split()
        if len(parts) == 2:
            number, word = parts
            message_dict[int(number)] = word

    pyramid_numbers = []
    i = 1
    while i <= len(message_dict):
        pyramid_numbers.append(i)
        i += len(pyramid_numbers) + 1

    message = ' '.join([message_dict[number] for number in pyramid_numbers])

    return message

message_file = "decodethis.txt"
result = decode(message_file)
print(result)