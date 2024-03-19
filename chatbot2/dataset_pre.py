with open('keti.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

rearranged_data = []

first_data = None
second_data = None

for line in lines:
    parts = line.strip().split('\t')
    data_number = parts[0]
    data_content = parts[1]
    if data_number == '1':
        if first_data is not None:
            rearranged_data.append((first_data, second_data, 0))
        first_data = data_content
    elif data_number == '2':
        second_data = data_content

# Add the last pair
if first_data is not None:
    rearranged_data.append((first_data, second_data, 0))

# Print or do something with rearranged_data
for data in rearranged_data:
    print(data)
