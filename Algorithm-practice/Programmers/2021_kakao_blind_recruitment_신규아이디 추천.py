def solution(new_id):
    new_id = new_id.lower()

    possible_char = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'
    i = 0
    while True:
        size = len(new_id)
        if i == size:
            break
        if new_id[i] not in possible_char:
            new_id = new_id.replace(new_id[i], '')
            continue
        i += 1
    
    i = 0
    while True:
        if i == len(new_id):
            break

        if new_id[i] == '.':
            j = i
            while j < len(new_id) and new_id[j] == '.':
                j += 1
            new_id = new_id.replace(new_id[i:j], '.')
        i += 1
    
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
    
    if not new_id:
        new_id = 'a'
    
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    while len(new_id) < 3:
        new_id = new_id + new_id[-1]

    return new_id