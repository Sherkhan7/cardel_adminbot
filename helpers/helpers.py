def wrap_tags(*args):
    symbol = ' ' if len(args) > 1 else ''
    return f'<b><i><u>{symbol.join(args)}</u></i></b>'
