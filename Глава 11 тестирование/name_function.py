
def get_formatted_name(*first_middle_last):
    """Строит отформатированное полное имя."""
    s = []
    for str in first_middle_last:
        s.append(str.strip())
    full_name = s[0]
    full_name += f' {s[1]}' if len(s)>1 and s[1] else ''
    full_name += f' {s[2]}' if len(s)>2 and s[2] else '' 
    return full_name.title()