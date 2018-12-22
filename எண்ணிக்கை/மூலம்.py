import inspect
import os
from typing import List

from nuchabäl import chijun

_நீட்டிப்பு_பட்டியல் = []  # type: List[நீட்டிப்பு_வார்ப்புரு]


class நீட்டிப்பு_வார்ப்புரு(object):
    def எண்ணுக்கு(தன், உரை, மொழி=None):
        """

        Parameters
        ----------
        உரை : str
        மொழி : str

        Returns
        -------
        float | int
        """
        raise NotImplementedError

    def உரைக்கு(தன், எண், மொழி, மொழி_மூலம்=None, தளம்=None):
        """

        Parameters
        ----------
        எண் : str | float | int
        மொழி : str
        மொழி_மூலம் : str
        தளம் : bool

        Returns
        -------
        str
        """
        raise NotImplementedError

    def மொழிகள்(தன்):
        """

        Returns
        -------
        list
        """
        raise NotImplementedError

    def வழவெளி(தன், மொழி):
        """
        வழக்கமான வெளிப்பாடு பேற்றும்.

        Returns
        -------
        str
        """

        raise NotImplementedError


def நீட்டிப்பு_பதிவு(நீட்டிப்பு, ப=None, தோகுதி=None):
    if ப is None:
        ப = []
    if தோகுதி is None:
        தோகுதி = []
    if inspect.ismodule(நீட்டிப்பு):

        for ஆ in inspect.getmembers(நீட்டிப்பு):
            if inspect.isclass(ஆ[1]) and issubclass(ஆ[1], நீட்டிப்பு_வார்ப்புரு) and ஆ[1] is not நீட்டிப்பு_வார்ப்புரு:
                ப.append(ஆ[1]())
            elif isinstance(ஆ[1], நீட்டிப்பு_வார்ப்புரு):
                ப.append(ஆ[1])
            elif inspect.ismodule(ஆ[1]) and hasattr(ஆ[1], '__file__') and \
                    (os.path.split(os.path.relpath(நீட்டிப்பு.__file__, ஆ[1].__file__))[0] == '..'):
                if ஆ[1] not in தோகுதி:
                    தோகுதி.append(ஆ[1])
                    நீட்டிப்பு_பதிவு(ஆ[1], ப=ப, தோகுதி=தோகுதி)
    elif isinstance(நீட்டிப்பு, நீட்டிப்பு_வார்ப்புரு):
        ப = [நீட்டிப்பு]
    else:
        raise TypeError
    for நீ in ப:
        if நீ not in _நீட்டிப்பு_பட்டியல்:
            _நீட்டிப்பு_பட்டியல்.append(நீ)


def _நீட்டிப்பு_தேடல்(மொழி=None):

    if மொழி is not None:
        சாத்தியங்கள் = [நீ for நீ in _நீட்டிப்பு_பட்டியல் if மொழி in நீ.மொழிகள்()]  # எண் அமைப்புமுறை

        if not len(சாத்தியங்கள்):
            மொழி, குறி = _மொழி_சரிப்பார்க்க(மொழி)
            சாத்தியங்கள் += [நீ for நீ in _நீட்டிப்பு_பட்டியல் if மொழி in நீ.மொழிகள்() or குறி in நீ.மொழிகள்()]
    else:
        சாத்தியங்கள் = _நீட்டிப்பு_பட்டியல்

    return மொழி, சாத்தியங்கள்


def _மொழி_சரிப்பார்க்க(மொழி):
    if isinstance(மொழி, str):
        try:
            return chijun.rajilanïk(மொழி), மொழி
        except ValueError:
            try:
                return chijun.ruchabäl(மொழி), chijun.runuk(மொழி)
            except ValueError:
                return மொழி, None


def _மொழி_குறியீடு(மொழி):
    return


def எண்ணுக்கு(உரை, மொழி=None):
    """

    Parameters
    ----------
    உரை : str
    மொழி : str

    Returns
    -------
    int | float

    Examples
    --------
    >>> எண்ணுக்கு('१२३४५.६७')
    12345.67
    >>> எண்ணுக்கு('௱௨௰௩,௪')
    123.4

    """

    சாத்தியங்கள் = _நீட்டிப்பு_தேடல்(மொழி)[1]

    for நீ in சாத்தியங்கள்:
        try:
            return நீ.எண்ணுக்கு(உரை, மொழி=மொழி)
        except ValueError:
            pass
    raise ValueError(உரை)


def உரைக்கு(எண், மொழி, மொழி_மூலம்=None, தளம்=None):
    """

    Parameters
    ----------
    எண் : float | int | str
    மொழி : str
    மொழி_மூலம் : str
    தளம் :

    Returns
    -------

    Examples
    --------
    >>> உரைக்கு(1234, 'தமிழ்', தளம்=None)
    '௧௨௩௪'

    >>> உரைக்கு(123.456789, 'தமிழ்', தளம்=None)
    '௧௨௩.௪௫௬௭௮௯'

    >>> உரைக்கு(-123.456789, 'தமிழ்', தளம்=None)
    '-௧௨௩.௪௫௬௭௮௯'

    >>> உரைக்கு(123.456789, '汉语')
    '一二三.四五六七八九'

    >>> உரைக்கு(123.456789, 'ગુજરાતી')
    '૧૨૩.૪૫૬૭૮૯'

    """

    if isinstance(எண், str):
        மொழி_மூலம், சாத்தியங்கள் = _நீட்டிப்பு_தேடல்(மொழி_மூலம்)
        எண்_மூலம் = None
        for நீ in சாத்தியங்கள்:
            try:
                எண்_மூலம் = நீ.எண்ணுக்கு(எண், மொழி=மொழி_மூலம்)
                break
            except (ValueError, KeyError):
                pass
        if எண்_மூலம் is None:
            raise ValueError
    else:
        எண்_மூலம் = எண்

    மொழி, சாத்தியங்கள் = _நீட்டிப்பு_தேடல்(மொழி)
    for நீ in சாத்தியங்கள்:
        try:
            return நீ.உரைக்கு(எண்_மூலம், மொழி=மொழி, மொழி_மூலம்=மொழி_மூலம், தளம்=தளம்)
        except ValueError:
            pass
    raise ValueError(எண், மொழி)


def வழவெளி(மொழி=None):
    """

    Parameters
    ----------
    மொழி : str | list[str]

    Returns
    -------
    str
    """

    if isinstance(மொழி, str):
        மொழி = [மொழி]

    சாத்தியங்கள் = [_நீட்டிப்பு_தேடல்(மொ) for மொ in மொழி]

    return '|'.join(f'({நீ[0].வழவெளி(மொ)})' for மொ, நீ in சாத்தியங்கள்)


def மொழிகள்():
    return list({மொ for நீ in _நீட்டிப்பு_பட்டியல் for மொ in நீ.மொழிகள்() })


from . import நீட்டிப்புகள்
நீட்டிப்பு_பதிவு(நீட்டிப்புகள்)
