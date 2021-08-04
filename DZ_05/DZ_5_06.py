subjects = {}
with open('Text_5_06.txt') as file:
    subject_info = file.readlines()
    for info in subject_info:
        elements = info.split()
        hours = 0
        for element in elements[1:]:
            if element != '-':
                counts = '0'
                for el in element:
                    if el.isdigit():
                        counts = el
                    else:
                        break
                hours += int(counts)
        subjects.update({elements[0].strip(':'): counts})
print(subjects)
