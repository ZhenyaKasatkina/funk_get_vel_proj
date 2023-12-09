
def get_val(collection, key, default='git'):
    """Функция возвращает значение из словаря
    по переданному ключу, если ключ существует.
    В ином случае возвращается значение default"""
    if collection == {}:
        return default
    else:
        for k_item, v_item in collection.items():
            if key == k_item:
                return v_item
            else:
                return default
