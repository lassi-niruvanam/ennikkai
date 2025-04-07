from புதுப்பிப்பி import புதுப்பிப்பி
from constellationpy.client import Client


class விண்மீன்_புதுப்பிப்பி(புதுப்பிப்பி):
    def __init__(தன், விண்மீன்: Client):
        தன்.விண்மீன் = விண்மீன்

    async def தகவட்களைப்_பின்பற்று(தன்):
        return await தன்.விண்மீன்.bds.suivreDonnéesTableau(

        )
