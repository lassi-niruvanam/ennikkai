import os
import shutil
from time import sleep, time

import லஸ்ஸி

source = 'மூலம்'
dist = 'விநியோகம்'

extensions = {
    ".பை": ".py"
}
langue_source = 'த'

_dates_erreurs = {}


def lassifier(text, de, à):
    if not text.endswith('\n'):
        text += "\n"
    return லஸ்ஸி.மொழியாக்கம்(
        உரை=text,
        நிரல்மொழி='python', மொழி=à, மூல்மொழி=de
    )


def plus_récent(f_source, f_comp):
    if f_source in _dates_erreurs:
        return os.path.getmtime(f_source) > _dates_erreurs[f_source]
    return os.path.getmtime(f_source) > os.path.getmtime(f_comp)


def recompiler(dir_source, dir_dist):
    for racine, dossiers, fichiers in os.walk(dir_source):
        for f in fichiers:
            f_orig = os.path.join(racine, f)
            nom, ext = os.path.splitext(f)
            nom_comp = nom + extensions[ext] if ext in extensions else f
            f_comp = dir_dist + os.path.join(racine, nom_comp)[len(dir_source):]
            if '__pycache__' in f_orig or f_orig.startswith('.'):
                continue
            doisje_recompiler = not os.path.isfile(f_comp) or plus_récent(f_orig, f_comp)
            if doisje_recompiler:
                dir_comp = os.path.split(f_comp)[0]
                if not os.path.isdir(dir_comp):
                    os.makedirs(dir_comp)

                if ext in extensions:
                    with open(f_orig, 'r', encoding='utf8') as d:
                        text_orig = d.read()
                    try:
                        print('On compile... ', f_orig)
                        text_comp = lassifier(text_orig, langue_source, à='en')
                        with open(f_comp, 'w', encoding='utf8') as d:
                            d.write(text_comp)
                        print('On à compilé... ', f_orig)
                        if f_orig in _dates_erreurs:
                            _dates_erreurs.pop(f_orig)
                    except Exception as e:
                        print(e)
                        _dates_erreurs[f_orig] = time()
                else:
                    shutil.copyfile(f_orig, f_comp)


if __name__ == '__main__':
    while True:
        recompiler(source, dist)
        sleep(1)
