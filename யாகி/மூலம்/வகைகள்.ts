export type எண்_வகை = இடஞ்சார்_எண்_வகை | அடிமானம்_எண்_வகை  

export type இடஞ்சார்_எண்_வகை = {
    வகை: string
    குறிகள்: string
    ஒருங்குறி?: string
    பிரிப்பு?: string
    அடுக்குக்குறி?: string
}

export type அடிமானம்_எண்_வகை = இடஞ்சார்_எண்_வகை & {
    அடிமானங்கள்: {[இ: string]: number}
}
