from gendiff.parser import loader


def generate_a_difference(path1, path2):
    dict1 = loader(path1)
    dict2 = loader(path2)
    keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    dict_diff = []

    for key in keys:
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                dict_diff.append(f'    {key}: {dict1[key]}')
            else:
                dict_diff.append(f'  - {key}: {dict1[key]}')
                dict_diff.append(f'  + {key}: {dict2[key]}')

        elif key in dict1 and key not in dict2:
            dict_diff.append(f'  - {key}: {dict1[key]}')
        elif key in dict2 and key not in dict1:
            dict_diff.append(f'  + {key}: {dict2[key]}')

    return '{\n' + '\n'.join(dict_diff) + '\n}'
