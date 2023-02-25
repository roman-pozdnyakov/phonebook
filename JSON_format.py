import json

def load(fname):                            # загрузить из json
    with open(fname, 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    print('БД успешно загружена')
    return data

def save(fname, data):                      # сохранить в json
    with open(fname, 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(data, ensure_ascii=False))
    print('БД успешно сохранена')



