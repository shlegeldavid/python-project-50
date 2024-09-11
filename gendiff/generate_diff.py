import json


json1 = json.load(open('src/json_files/file1.json'))
json2 = json.load(open('src/json_files/file2.json'))


def diff(json1, json2):
    result = ''
    keys1 = []
    keys2 = []

    for key in json1:
        keys1.append(key)
    for key in json2:
        keys2.append(key)
    
    sorted1 = sorted(keys1)
    sorted2 = sorted(keys2)
    higher_len = 0
    i = 0

    if len(sorted1) > len(sorted2):
        higher_len += len(sorted1)
    else:
        higher_len += len(sorted2)
    
    while i < higher_len:
        if sorted1[i] in sorted2:
            if json1[sorted1[i]] == json2[sorted1[i]]:
                result += f'  {sorted1[i]}: {json1[sorted1[i]]}\n'
            else:
                result += f'- {sorted1[i]}: {json1[sorted1[i]]}\n'
                result += f'+ {sorted1[i]}: {json2[sorted1[i]]}\n'
        if sorted1[i] not in sorted2:
            result += f'- {sorted1[i]}: {json1[sorted1[i]]}\n'
        elif sorted2[i - 1] not in sorted1:
            result += f'+ {sorted2[i - 1]}: {json2[sorted2[i - 1]]}\n'
        i += 1
    formatted_result = '{\n' + result + '}'
    return formatted_result


print(diff(json1, json2))