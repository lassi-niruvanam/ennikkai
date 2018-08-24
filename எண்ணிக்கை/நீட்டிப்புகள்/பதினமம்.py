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
            if all(அ in தன்.கூடிய_எழுத்து[மொ] for அ in உரை):
                எண் = தன்.தொகுப்பி[மொ](உரை)
                if '.' in எண்:
                    return float(எண்)
                else:
                    return int(எண்)
            if மொ in தன்.கூடிய_எழுத்து_களம் and all(அ in தன்.கூடிய_எழுத்து_களம்[மொ] for அ in உரை):
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
        எண்கள் = தகவல்_அகராதி[மொழி]['எண்கள்']
        
        வழவெளி= {
            'எண்கள்': ['\\u%04x' % அ for அ in எண்கள்],
            'தசம': ['\\u%04x' % அ for அ in தகவல்_அகராதி[மொழி]['தசம']]
        }
        
        try:
            வழவெளி += [அ[1] for அ in தகவல்_அகராதி[மொழி]['தளம்']]
        except KeyError:
            pass
        
        return வழவெளி


def _தொகுப்பி_உருவாக்கு(தகவல்கள், மறு=False):
    if மறு:
        அக = {str(எ): அ for எ, அ in enumerate(தகவல்கள்['எண்கள்'])}
        தசம = next((த for த in தகவல்கள்['தசம'] if த != '.'), None)
        if தசம:
            அக.update({'.': தசம})
    else:
        அக = {அ: str(எ) for எ, அ in enumerate(தகவல்கள்['எண்கள்'])}
        அக.update({த: '.' for த in தகவல்கள்['தசம'] if த != '.'})

    வழ = re.compile('|'.join(map(re.escape, அக)))

    def பொருந்தும்(பொ):
        return அக[பொ.group(0)]

    return lambda அ: வழ.sub(பொருந்தும், அ)


def _தளம்_படிப்பு(உரை, தளங்கள், தொகுப்பி, தசம_பிரிய):
    அக_தளங்கள் = {தளம்: மதிப்பு for மதிப்பு, தளம் in தளங்கள்}
    எதிர் = உரை.startswith('-')
    if எதிர்:
        உரை = உரை[1:]
    தசம = None
    முழு = உரை
    for பி in தசம_பிரிய:
        try:
            முழு, தசம = உரை.split(பி)
            break
        except ValueError:
            pass

    எண் = 0
    ம = 1
    த_முன் = None
    for அ in முழு:
        try:
            த = அக_தளங்கள்[அ]
            if த_முன் is None or த < த_முன்:
                எண் += த * ம
            else:
                எண் += ம
                எண் *= த
            த_முன் = த
            ம = 0
        except KeyError:
            ம = int(தொகுப்பி(அ))

    if தசம:
        எண் += float('.' + தொகுப்பி(தசம))
    if எதிர்:
        எண் *= -1
    return எண்


def _தளம்_எழுதல்(எண், தளங்கள், தொகுப்பி, தசம_பிரிய):
    எதிர் = எண் < 0
    எண் = abs(எண்)
    முழு = floor(எண்)
    try:
        தசம = int(str(எண்).split('.')[1])
    except IndexError:
        தசம = None
    மீதி = முழு
    உரை = ''
    for மதிப்பு, தளம் in reversed(தளங்கள்):
        ம = int(மீதி // மதிப்பு)
        if ம:
            மீதி -= ம * மதிப்பு
            if ம != 1:
                உரை += _தளம்_எழுதல்(ம, தளங்கள், தொகுப்பி, தசம_பிரிய) + தளம்
            else:
                உரை += தளம்
    if மீதி:
        உரை += தொகுப்பி(str(மீதி))
    if எதிர்:
        உரை = '-' + உரை
    if தசம:
        உரை += தசம_பிரிய + தொகுப்பி(str(தசம))
    return உரை
