import json as ஜேஸான்
from functools import lru_cache

from nuchabäl.rukux import chijun
from pkg_resources import resource_filename as கோப்புபெயர்

from .அடிமானம் import அடிமானம்
from .இடஞ்சார் import இடஞ்சார்

முறைமைகள் = {}

கோப்பு = கோப்புபெயர்('எண்ணிக்கை', 'தகவல்கள்.json')
with open(கோப்பு, encoding='utf8') as கோ:
    தகவல்கள் = ஜேஸான்.load(கோ)

for பெயர், விவரங்கள் in தகவல்கள்.items():

    வகை = விவரங்கள்['வகை']
    ஒருங்குறி = விவரங்கள்['ஒருங்குறி']
    பிரிப்பு = விவரங்கள்['பிரிப்பு'] if 'பிரிப்பு' in விவரங்கள் else '.'
    அடுக்குக்குறி = விவரங்கள்['அடுக்குக்குறி'] if 'அடுக்குக்குறி' in விவரங்கள் else 'e'
    குறிகள் = விவரங்கள்['குறிகள்']

    if வகை == 'இடஞ்சார்':
        முறைமைகள்[பெயர்] = இடஞ்சார்(
            பெயர், ஒருங்குறி=ஒருங்குறி, குறிகள்=குறிகள், பிரிப்பு=பிரிப்பு, அடுக்குக்குறி=அடுக்குக்குறி
        )
    elif வகை == 'அடிமானம்':
        அடிமானங்கள் = விவரங்கள்['அடிமானங்கள்']
        முறைமைகள்[பெயர்] = அடிமானம்(
            பெயர், ஒருங்குறி=ஒருங்குறி, அடிமானங்கள்=அடிமானங்கள், குறிகள்=குறிகள், பிரிப்பு=பிரிப்பு,
            அடுக்குக்குறி=அடுக்குக்குறி
        )
    else:
        raise ValueError(வகை)


@lru_cache()
def முறைமை_பேற்ற(மொழி, எல்லாம்=False):
    சாத்தியங்கள் = list(முறைமைகள்.values()) if மொழி is None else []
    if not சாத்தியங்கள் and மொழி in முறைமைகள்:
        சாத்தியங்கள் = [முறைமைகள்[மொழி]]
    if not சாத்தியங்கள்:
        சாத்தியங்கள் = [மு for மு in முறைமைகள்.values() if மு.ஒருங்குறி == மொழி]

    if not சாத்தியங்கள்:
        try:
            மொழி = chijun.rajilanïk(மொழி)
        except ValueError:
            pass

    if not சாத்தியங்கள்:
        raise ValueError(மொழி)

    if எல்லாம்:
        return சாத்தியங்கள்
    else:
        return சாத்தியங்கள்[0]
