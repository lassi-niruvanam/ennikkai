from abc import ABC, abstractmethod

from deepmerge import always_merger


class தகவல்_மூலம்(ABC):
    @abstractmethod
    def தகவல்களைப்_பெறு(தன்) -> dict:
        pass

    def __add__(தன், மற்ற: "தகவல்_மூலம்"):
        return இணைந்த_தகவல்கள்(தன், மற்ற)


class இணைந்த_தகவல்கள்(தகவல்_மூலம்):

    def __init__(தன், *மூலங்கள்: "தகவல்_மூலம்"):
        தன்.மூலங்கள் = மூலங்கள்

    def தகவல்களைப்_பெறு(தன்) -> dict:
        தகவல்கள் = {}

        for மூலம் in தன்.மூலங்கள்:
            always_merger.merge(தகவல்கள், மூலம்)

        return தகவல்கள்
