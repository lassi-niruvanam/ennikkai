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
