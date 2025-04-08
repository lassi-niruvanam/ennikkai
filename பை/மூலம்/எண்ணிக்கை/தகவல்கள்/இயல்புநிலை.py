import json
from importlib import resources
from typing import Optional

from .தகவல்கள் import தகவல்_மூலம்


class இயல்புநிலை_தகவல்கள்(தகவல்_மூலம்):

    def __init__(தன், தகவல்_கோப்பு: Optional[str] = None):
        super().__init__()
        தகவல்_கோப்பு = தகவல்_கோப்பு or resources.files("எண்ணிக்கை.வளங்கள்").joinpath("தகவல்கள்.json")
        with open(தகவல்_கோப்பு, encoding='utf8') as கோ:
            தன்.தகவல்கள் = json.load(கோ)

    def தகவல்களைப்_பெறு(தன்) -> dict:
        return தன்.தகவல்கள்
