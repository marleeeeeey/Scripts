def examples(input_file):
    tree = ET.parse(input_file)
    root = tree.getroot()
    print('root.tag:', root.tag)
    print('root.attrib:', root.attrib)

    print('childs:')
    for child in root:
        print(child.tag, child.attrib)

    print('iter(neighbor):')
    for neighbor in root.iter('neighbor'):
        print(neighbor.attrib)

    print('findall(country):')
    for country in root.findall('country'):
        rank = country.find('rank').text
        name = country.get('name')
        print(name, rank)

    print('remove country rank < 50:')
    for country in root.findall('country'):
        rank = int(country.find('rank').text)
        if rank < 50:
            root.remove(country)

    tree.write('output.xml')
