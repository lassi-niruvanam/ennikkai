from .பிழைகள் import மொழிபெயர்ப்புபிழை
from .முறைமைகள் import முறைமை_பேற்ற


def எண்ணுக்கு(உரை, மொழி=None):
    முறைமைகள் = முறைமை_பேற்ற(மொழி, எல்லாம்=True)

    for முறை in முறைமைகள்:
        if முறை.சரிபார்ப்பு(உரை):
            return முறை.எண்ணுக்கு(உரை)

    raise மொழிபெயர்ப்புபிழை(உரை)


def உரைக்கு(எண், மொழி, மொழி_மூலம்=None):
    முறைமை = முறைமை_பேற்ற(மொழி)

    if isinstance(எண், str):
        எண் = எண்ணுக்கு(எண், மொழி=மொழி_மூலம்)

    return முறைமை.உரைக்கு(எண்)


def சுருங்குறித்தொடர்(மொழி):
    முறைமை = முறைமை_பேற்ற(மொழி)
    return முறைமை.சுருங்குறித்தொடர்()
