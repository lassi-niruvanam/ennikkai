import type { bds, ClientConstellation } from "@constl/ipa";
import { கிளி } from "@lassi-js/kili";

import {
  எண்ணிக்கை_சிறப்பு_சொல்,
  அட்டவணை_சாபி,
  முறைமை_குறியீடு_நெடுவரிசை_குறியீடு,
  முறைமை_வகை_நெடுவரிசை_குறியீடு,
  முறைமை_ஒருங்குறி_குறியீடு_நெடுவரிசை_குறியீடு,
  முறைமை_குறிகள்_நெடுவரிசை_குறியீடு,
  முறைமை_அடுக்குக்குறி_நெடுவரிசை_குறியீடு,
  முறைமை_அடிமானங்கள்_நெடுவரிசை_குறியீடு,
  முறைமை_பிரிப்பு_நெடுவரிசை_குறியீடு,
  முறைமை_குறியீடு_மாறி_குறியீடு,
  முறைமை_வகை_மாறி_குறியீடு,
  முறைமை_ஒருங்குறி_குறியீடு_மாறி_குறியீடு,
  முறைமை_குறிகள்_மாறி_குறியீடு,
  முறைமை_அடுக்குக்குறி_மாறி_குறியீடு,
  முறைமை_அடிமானங்கள்_மாறி_குறியீடு,
  முறைமை_பிரிப்பு_மாறி_குறியீடு,
  கிளி_குழு_அடையாளம்,
} from "@/மாறிலிகள்.js";

const தரவுத்தள_வார்ப்புரு: bds.schémaSpécificationBd = {
  licence: "ODbl-1_0",
  motsClefs: [எண்ணிக்கை_சிறப்பு_சொல்],
  tableaux: [
    {
      cols: [
        {
          idColonne: முறைமை_குறியீடு_நெடுவரிசை_குறியீடு,
          idVariable: முறைமை_குறியீடு_மாறி_குறியீடு,
          index: true,
        },
        {
          idColonne: முறைமை_வகை_நெடுவரிசை_குறியீடு,
          idVariable: முறைமை_வகை_மாறி_குறியீடு,
        },
        {
          idColonne: முறைமை_ஒருங்குறி_குறியீடு_நெடுவரிசை_குறியீடு,
          idVariable: முறைமை_ஒருங்குறி_குறியீடு_மாறி_குறியீடு,
        },
        {
          idColonne: முறைமை_குறிகள்_நெடுவரிசை_குறியீடு,
          idVariable: முறைமை_குறிகள்_மாறி_குறியீடு,
        },
        {
          idColonne: முறைமை_அடுக்குக்குறி_நெடுவரிசை_குறியீடு,
          idVariable: முறைமை_அடுக்குக்குறி_மாறி_குறியீடு,
        },
        {
          idColonne: முறைமை_அடிமானங்கள்_நெடுவரிசை_குறியீடு,
          idVariable: முறைமை_அடிமானங்கள்_மாறி_குறியீடு,
        },
        {
          idColonne: முறைமை_பிரிப்பு_நெடுவரிசை_குறியீடு,
          idVariable: முறைமை_பிரிப்பு_மாறி_குறியீடு,
        },
      ],
      clef: அட்டவணை_சாபி,
    },
  ],
};

export type முறைமை_தகவல்_வரிசை = {
  [முறைமை_குறியீடு_நெடுவரிசை_குறியீடு]: string;
  [முறைமை_வகை_நெடுவரிசை_குறியீடு]: string;
  [முறைமை_ஒருங்குறி_குறியீடு_நெடுவரிசை_குறியீடு]?: string;
  [முறைமை_குறிகள்_நெடுவரிசை_குறியீடு]: string;
  [முறைமை_அடுக்குக்குறி_நெடுவரிசை_குறியீடு]?: string;
  [முறைமை_அடிமானங்கள்_நெடுவரிசை_குறியீடு]?: string;
  [முறைமை_பிரிப்பு_நெடுவரிசை_குறியீடு]?: string;
};

export type எண்ணிக்கை_கிளி = கிளி<முறைமை_தகவல்_வரிசை>;

export const கிளி_தயாரிப்பு = ({
  விண்மீன்,
}: {
  விண்மீன்: ClientConstellation;
}): எண்ணிக்கை_கிளி => {
  return new கிளி<முறைமை_தகவல்_வரிசை>({
    விண்மீன்: விண்மீன்,
    அட்டவணை_சாபி,
    வார்ப்புரு: தரவுத்தள_வார்ப்புரு,
    குழு_அடையாளம்: கிளி_குழு_அடையாளம்,
  });
};
