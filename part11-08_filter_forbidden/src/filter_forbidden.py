def filter_forbidden(string: str, forbidden: str):
    filtered = [character for character in string if character not in forbidden]
    return ''.join(filtered)