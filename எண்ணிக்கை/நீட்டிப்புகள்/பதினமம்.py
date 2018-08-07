import json as ஜேஸான்
import re
from math import floor

from pkg_resources import resource_filename as கோப்புபெயர்

from ..மூலம் import நீட்டிப்பு_வார்ப்புரு

கோப்பு_தகவல்கள் = கோப்புபெயர்('எண்ணிக்கை.நீட்டிப்புகள்', 'பதின்மம்_தகவல்கள்.json')
with open(கோப்பு_தகவல்கள், encoding='utf8') as கோ:
    தகவல்_அகராதி = ஜேஸான்.load(கோ)


class பதினமம்(நீட்டிப்பு_வார்ப்புரு):

    def __init__(தன், தகவல்கள்=None):
        தன்.தகவல்கள் = தகவல்_அகராதி

        if தகவல்கள் is not None:
            தன்.தகவல்கள்.update(தகவல்கள்)
        for மொ, அக in தன்.தகவல்கள்.items():
            if 'தசம' not in அக:
                அக['தசம'] = ['.']
            elif '.' not in 'தசம':
                அக['தசம'].append('.')
        தன்.தொகுப்பி = {மொ: _தொகுப்பி_உருவாக்கு(தன்.தகவல்கள்[மொ]) for மொ in தன்.தகவல்கள்}
        தன்.மறு_தொகுப்பி = {மொ: _தொகுப்பி_உருவாக்கு(தன்.தகவல்கள்[மொ], மறு=True) for மொ in தன்.தகவல்கள்}
        தன்.கூடிய_எழுத்து = {மொ: அக['எண்கள்'] + அக['தசம'] + ['-'] for மொ, அக in தன்.தகவல்கள்.items()}
        தன்.கூடிய_எழுத்து_களம் = {
            மொ: ப + [இர[1] for இர in தன்.தகவல்கள்[மொ]["தளம்"]]
            for மொ, ப in தன்.கூடிய_எழுத்து.items() if "தளம்" in தன்.தகவல்கள்[மொ]
        }

    def எண்ணுக்கு(தன், உரை, மொழி=None):
        if மொழி is None:
            மொழி = தன்.மொழிகள்()
        elif isinstance(மொழி, str):
            மொழி = [மொழி]

        தக = தன்.தகவல்கள்

        for மொ in மொழி:
            if all(x in தன்.கூடிய_எழுத்து[மொ] for x in உரை):
                return float(தன்.தொகுப்பி[மொ](உரை))
            if மொ in தன்.கூடிய_எழுத்து_களம் and all(x in தன்.கூடிய_எழுத்து_களம்[மொ] for x in உரை):
                return _தளம்_படிப்பு(உரை, தக[மொ]["தளம்"], தன்.தொகுப்பி[மொ], தக[மொ]["தசம"])
        raise ValueError

    def உரைக்கு(தன், எண், மொழி, மொழி_மூலம்=None, தளம்=None):

        தக = தன்.தகவல்கள்
        if isinstance(எண், str):
            எண் = தன்.எண்ணுக்கு(எண், மொழி=மொழி_மூலம்)

        if தளம் is None:
            தளம் = மொழி in தன்.கூடிய_எழுத்து_களம்

        if not தளம்:
            return தன்.மறு_தொகுப்பி[மொழி](str(எண்))
        else:
            if மொழி not in தன்.கூடிய_எழுத்து_களம்:
                raise ValueError('தளம்', மொழி)
            return _தளம்_எழுதல்(எண், தக[மொழி]["தளம்"], தன்.மறு_தொகுப்பி[மொழி], தக[மொழி]["தசம"][0])

    def மொழிகள்(தன்):
        return list(தன்.தகவல்கள்)

    def வழவெளி(தன், மொழி=None):
        # ''.join(['\\u%04x' % x for x in தகவல்_அகராதி[மொழி]['எண்கள்']])
        pass


def _தொகுப்பி_உருவாக்கு(தகவல்கள், மறு=False):
    if மறு:
        அக = {str(i): x for i, x in enumerate(தகவல்கள்['எண்கள்'])}
        தசம = next((த for த in தகவல்கள்['தசம'] if த != '.'), None)
        if தசம:
            அக.update({'.': தசம})
    else:
        அக = {x: str(i) for i, x in enumerate(தகவல்கள்['எண்கள்'])}
        அக.update({த: '.' for த in தகவல்கள்['தசம'] if த != '.'})

    வழ = re.compile('|'.join(map(re.escape, அக)))

    def பொருந்தும்(பொ):
        return அக[பொ.group(0)]

    return lambda அ: வழ.sub(பொருந்தும், அ)


def _தளம்_படிப்பு(உரை, தளங்கள், தொகுப்பி, தசம_பிரிய):
    அக_தளங்கள் = {தளம்: மதிப்பு for மதிப்பு, தளம் in தளங்கள்}
    neg = உரை.startswith('-')
    if neg:
        உரை = உரை[1:]
    dec = None
    ent = உரை
    for d in தசம_பிரிய:
        try:
            ent, dec = உரை.split(d)
            break
        except ValueError:
            pass

    எண் = 0
    v = 1
    b = b0 = None
    for x in ent:
        try:
            b = அக_தளங்கள்[x]
            if b0 is None or b < b0:
                எண் += b*v
            else:
                எண் += v
                எண் *= b
            b0 = b
            v = 0
        except KeyError:
            v = int(தொகுப்பி(x))

    if dec:
        எண் += float('.' + தொகுப்பி(dec))
    if neg:
        எண் *= -1
    return எண்


def _தளம்_எழுதல்(எண், தளங்கள், தொகுப்பி, தசம_பிரிய):
    neg = எண் < 0
    எண் = abs(எண்)
    ent = floor(எண்)
    try:
        dec = int(str(எண்).split('.')[1])
    except IndexError:
        dec = None
    reste = ent
    உரை = ''
    for மதிப்பு, தளம் in reversed(தளங்கள்):
        s = int(reste // மதிப்பு)
        if s:
            reste -= s * மதிப்பு
            if s != 1:
                உரை += _தளம்_எழுதல்(s, தளங்கள், தொகுப்பி, தசம_பிரிய) + தளம்
            else:
                உரை += தளம்
    if reste:
        உரை += தொகுப்பி(str(reste))
    if neg:
        உரை = '-' + உரை
    if dec:
        உரை += தசம_பிரிய + தொகுப்பி(str(dec))
    return உரை
