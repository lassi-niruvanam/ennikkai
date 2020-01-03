import re


class எண்குறிமுறைமை(object):
    def __init__(தன், பெயர், ஒருங்குறி):
        தன்.பெயர் = பெயர்
        தன்.ஒருங்குறி = ஒருங்குறி

    def எண்ணுக்கு(தன், உரை):
        raise NotImplementedError

    def உரைக்கு(தன், எண்):
        raise NotImplementedError

    def சுருங்குறித்தொடர்(தன், வடிவம்):
        raise NotImplementedError

    def சரிபார்ப்பு(தன், உரை):
        return re.fullmatch(தன்.சுருங்குறித்தொடர்(), உரை) is not None
