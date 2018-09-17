# எண்ணிக்கை
எல்லாம் உலகத்தின் மொழிகளில் எண்களின் படிப்புதல் மற்றும் எழுதல்.

## நிலை
[![Build Status](https://travis-ci.org/julienmalard/ennikkai.svg?branch=master)](https://travis-ci.org/julienmalard/ennikkai)
[![Build status](https://ci.appveyor.com/api/projects/status/06m0e097gahel2ij?svg=true)](https://ci.appveyor.com/project/julienmalard/ennikkai)
[![Coverage Status](https://coveralls.io/repos/github/julienmalard/ennikkai/badge.svg?branch=master)](https://coveralls.io/github/julienmalard/ennikkai?branch=master)

## பயன்பாடு
பைதான் எண் மூலம் எதாவது மொழியின் எண் கிடைக்கும்.

```python
from எண்ணிக்கை import உரைக்கு 

உரைக்கு(123.456, 'த')  # தமிழ்
# '௱௨௰௩.௪௫௬'

உரைக்கு(123.456, 'த', தளம்=False)  # பதின்மம் தமிழ்
# '௧௨௩.௪௫௬'

உரைக்கு(123.456, 'ߒߞߏ‎')  # ந்கோ மொழி
# '߁߂߃.߄߅߆'

```

எதாவது மொழி மூலம் வேறு மொழிக்கு மொழிபெயர்ப்பு செய்யலாம்.

```python
from எண்ணிக்கை import உரைக்கு

உரைக்கு('૧૨૩૪.૫૬', 'த‎')  # குஜராதீ மூலம் தமிழ்
# '௲௨௱௩௰௪.௫௬'
``` 

எதாவது மொழி மூலம் பைத்தான் எண் வரை மாற்றலாம்.

```python
from எண்ணிக்கை import எண்ணுக்கு, உரைக்கு

எண்ணுக்கு('一百二十三。四五六')  # சினீ மொழி
# 123.456

அ = எண்ணுக்கு('߁߂߃') * எண்ணுக்கு('௰')
ஆ = எண்ணுக்கு('૪')
இ = அ + ஆ
print(உரைக்கு(இ, 'ار'))
# ۱۲۳۴
```

## நிறுவல்
    pip install ennikkai

## சோர்க்கப்பட்ட மொழிகள்

எண்ணிக்கையால் **எல்லா மொழிகளின்** எண்களை மொழிபெயர்ப்பு செய்ய முடியும். 

எதாவது ஒரு மொழியை மறந்து விட்டோம என்றால், எண்களுக்கு [சொல்லவும்](https://github.com/julienmalard/ennikkai/issues). நாங்கள் அதை சேர்வோம்.

#### பதினமம் எண் அமைப்பமுறைகள்
* தமிழ்
* Latin
* देवनागरी
* ਪੰਜਾਬੀ
* ગુજરાતી
* മലയാളം
* اردو - فارسی - پنجابی
* العربية
* ଓଡ଼ିଆ 
* ಕನ್ನಡ 
* తెలుగు 
* 汉语 - 日本語
* ߒߞߏ‎
* বাংলা
* සිංහල
* ภาษาไทย
* ພາສາລາວ
* བོད་ཡིག
* လိၵ်ႈတႆး
* ꕙꔤ

#### வேறு எண் அமைப்பமுறைகள்
* Romanum
* Mayab'
