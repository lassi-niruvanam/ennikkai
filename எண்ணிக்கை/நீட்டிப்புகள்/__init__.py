def _உரை(எண்):
    உ = str(எண்)
    if 'e' in உ:
        அ, ஆ = உ.split('e')
        அ = அ.replace('.', '')
        உ = '0.' + '0' * (-int(ஆ) - 1) + அ
    return உ


from . import பதினமம், மாயாப், ரோமீ
