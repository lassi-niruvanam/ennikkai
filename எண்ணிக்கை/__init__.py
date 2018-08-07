import os

from .மூலம் import எண்ணுக்கு, உரைக்கு, வழவெளி, நீட்டிப்பு_வார்ப்புரு, மொழிகள்

கோப்புரை = os.path.split(os.path.realpath(__file__))[0]
with open(os.path.join(கோப்புரை, 'புதிப்பு.txt')) as கோ:
    __புதிப்பு__ = __version__ = கோ.read().strip()
