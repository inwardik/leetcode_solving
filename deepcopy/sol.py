def deepcopy(it):
    if isinstance(it, list):
        copy_it = []
        for element in it:
            if not hasattr(element, '__len__'):
                copy_it.append(element)
            else:
                copy_it.append(deepcopy(element))
        return copy_it
    elif isinstance(it, set):
        copy_it = set()
        for element in it:
            if not hasattr(element, '__len__'):
                copy_it.add(element)
            else:
                copy_it.add(deepcopy(element))
        return copy_it
    elif isinstance(it, dict):
        copy_it = {}
        for key, value in it.items():
            if not hasattr(value, '__len__'):
                copy_it[key] = value
            else:
                copy_it[key] = deepcopy(value)
        return copy_it