import re

from எண்ணிக்கை import எண்ணிக்கை

எழுதல் = {
    'ஓன்று': {'எண்': 1, 'latin': '1', 'ગુજરાતી': '૧', 'தமிழ்': '௧', "Mayab'": '𝋡', 'ግዕዝ': '፩'},
    'பத்து': {'எண்': 10, 'latin': '10', 'ગુજરાતી': '૧૦', 'தமிழ்': '௰', "Mayab'": '𝋪', 'ግዕዝ': '፲'},
    'நூறு': {'எண்': 100, 'latin': '100', 'ગુજરાતી': '૧૦૦', 'தமிழ்': '௱', "Mayab'": '𝋥𝋠', 'ግዕዝ': '፻'},
    'நூற்று பத்து': {'எண்': 110, 'latin': '110', 'ગુજરાતી': '૧૧૦', 'தமிழ்': '௱௰', "Mayab'": '𝋥𝋪', 'ግዕዝ': '፻፲'},
    'ஆயிரம்': {'எண்': 1000, 'latin': '1000', 'ગુજરાતી': '૧૦૦૦', 'தமிழ்': '௲', "Mayab'": '𝋢𝋪𝋠', 'ግዕዝ': '፲፻'},
    'பத்தாயிறம்': {'எண்': 10000, 'latin': '10000', 'ગુજરાતી': '૧૦૦૦૦', 'தமிழ்': '௰௲', "Mayab'": '𝋡𝋥𝋠𝋠', 'ግዕዝ': '፼'},
    'பத்தினொன்றாயிறம்': {
        'எண்': 11000, 'latin': '11000', 'ગુજરાતી': '૧૧૦૦૦', 'தமிழ்': '௰௧௲', "Mayab'": '𝋡𝋧𝋪𝋠', 'ግዕዝ': '፼፲፻'
    },
    'லச்சியம்': {
        'எண்': 100000, 'latin': '100000', 'ગુજરાતી': '૧૦૦૦૦૦', 'தமிழ்': '௱௲', "Mayab'": '𝋬𝋪𝋠𝋠', 'ግዕዝ': '፲፼'
    },
    'கோடி': {
        'எண்': 10000000, 'latin': '10000000', 'ગુજરાતી': '૧૦૦૦૦૦૦૦', 'தமிழ்': '௰௲௲', "Mayab'": '𝋣𝋢𝋪𝋠𝋠𝋠',
        'ግዕዝ': '፲፻፼'
    },
    'முழு_எண்': {'எண்': 123, 'latin': '123', 'ગુજરાતી': '૧૨૩', 'தமிழ்': '௱௨௰௩', "Mayab'": '𝋦𝋣', 'ግዕዝ': '፻፳፫'},
    'முழு_எண்_பதி': {'எண்': 123., 'latin': '123.', 'ગુજરાતી': '૧૨૩.', 'தமிழ்': '௱௨௰௩.', "Mayab'": '𝋦𝋣.',
                     'ግዕዝ': '፻፳፫.'},
    'பதின்மம்': {
        'எண்': 0.123456789, 'latin': '0.123456789', 'ગુજરાતી': '૦.૧૨૩૪૫૬૭૮૯', 'தமிழ்': '௦.௧௨௩௪௫௬௭௮௯',
        "Mayab'": '𝋠.𝋢𝋩𝋧𝋭𝋡𝋮𝋩𝋲𝋨', 'ግዕዝ': '0.፩፪፫፬፭፮፯፰፱'},
    'புதியம்_பதின்மம்_பல_புதியம்': {
        'எண்': 0.0000123, 'latin': '0.0000123', 'ગુજરાતી': '૦.૦૦૦૦૧૨૩',
        'தமிழ்': '௦.௦௦௦௦௧௨௩', "Mayab'": '𝋠.𝋠𝋠𝋠𝋡𝋳𝋧𝋤', 'ግዕዝ': '0.0000፩፪፫'
    },
    'பதின்மம்_பல_புதியம்': {
        'எண்': 12.0000123, 'latin': '12.0000123', 'ગુજરાતી': '૧૨.૦૦૦૦૧૨૩', 'தமிழ்': '௰௨.௦௦௦௦௧௨௩',
        "Mayab'": '𝋬.𝋠𝋠𝋠𝋡𝋳𝋧𝋤', 'ግዕዝ': '፲፪.0000፩፪፫'
    },
    'எதிர்': {
        'எண்': -1.23, 'latin': '-1.23', 'ગુજરાતી': '-૧.૨૩', 'தமிழ்': '-௧.௨௩', "Mayab'": '-𝋡.𝋤𝋬', 'ግዕዝ': '-፩.፪፫'
    },
    'எல்லாம்': {
        'எண்': -123456789.00012345678900, 'latin': '-123456789.00012345678900',
        'ગુજરાતી': '-૧૨૩૪૫૬૭૮૯.૦૦૦૧૨૩૪૫૬૭૮૯૦૦', 'ግዕዝ': '-፼፳፫፻፵፭፼፷፯፻፹፱.000፩፪፫፬፭፮፯፰፱00'
    },
    'புஜியம்': {'எண்': 0, 'latin': '0', 'ગુજરાતી': '૦', 'தமிழ்': '௦', "Mayab'": '𝋠'},

    'புஜியம்_பதின்மம்_புஜியம்': {'எண்': 0.0, 'latin': '0.0', 'ગુજરાતી': '૦.૦', 'தமிழ்': '௦.௦', "Mayab'": '𝋠.𝋠'},
    'பெரிய என்': {
        'எண்': 12000000000000000., 'latin': '12000000000000000.', 'ગુજરાતી': '૧૨૦૦૦૦૦૦૦૦૦૦૦૦૦૦૦.',
        'தமிழ்': '௰௨௲௲௲௲௲.', "Mayab'": '𝋢𝋲𝋫𝋱𝋪𝋠𝋠𝋠𝋠𝋠𝋠𝋠𝋠.', 'ግዕዝ': '፼፳፻፼፼፼.'
    }
}

படித்தல் = {
    'பதின்மம்_ஆரம்பு': {'எண்': .123, 'latin': '.123', 'ગુજરાતી': '.૧૨૩', 'தமிழ்': '.௧௨௩', "Mayab'": '.𝋢𝋩𝋤'},
    'பதின்மம்_ஆரம்பு_பல_புதியம்': {
        'எண்': .0000123, 'latin': '.0000123', 'ગુજરાતી': '.૦૦૦૦૧૨૩', 'தமிழ்': '.௦௦௦௦௧௨௩', "Mayab'": '.𝋠𝋠𝋠𝋡𝋳𝋧𝋤'
    },
    'எதிர்_பதின்மம்_ஆரம்பு': {
        'எண்': -.101, 'latin': '-.101', 'ગુજરાતી': '-.૧૦૧', 'தமிழ்': '-.௧௦௧', "Mayab'": '-.𝋢𝋠𝋨'
    },
    'புஜியம்_பதின்மம்': {'எண்': 0., 'latin': '0.', 'ગુજરાતી': '૦.', 'தமிழ்': '௦.', "Mayab'": '𝋠.'},
}
படித்தல்.update(எழுதல்)


def மாற்றம்_சோதி():
    சோதனை_எண்ணிக்கை = எண்ணிக்கை()
    for பயர், தகவல்கள் in படித்தல்.items():
        for மொ in சோதனை_எண்ணிக்கை.முறைமைகள்:
            எண் = தகவல்கள்['எண்']
            உ = சோதனை_எண்ணிக்கை.உரைக்கு(எண், மொ)
            எ = சோதனை_எண்ணிக்கை.எண்ணுக்கு(உ, மொழி=மொ)
            assert isinstance(எ, type(எண்)), உ
            assert எ == எண், உ


def படித்தலைச்_சோதி():
    சோதனை_எண்ணிக்கை = எண்ணிக்கை()
    for பயர், தகவல்கள் in படித்தல்.items():
        எண் = தகவல்கள்['எண்']
        for மொ in தகவல்கள்:
            if மொ == 'எண்':
                continue
            உ = தகவல்கள்[மொ]
            எ = சோதனை_எண்ணிக்கை.எண்ணுக்கு(உ, மொழி=மொ)
            assert isinstance(எ, type(எண்)), உ
            assert எ == எண், உ


def சுருங்குறித்தொடர்_சோதி():
    சோதனை_எண்ணிக்கை = எண்ணிக்கை()
    for மொழி in சோதனை_எண்ணிக்கை.முறைமைகள்:
        சுருங்குறி = சோதனை_எண்ணிக்கை.சுருங்குறித்தொடர்(மொழி)
        for பயர், தகவல்கள் in படித்தல்.items():
            எண் = தகவல்கள்['எண்']
            உரை = சோதனை_எண்ணிக்கை.உரைக்கு(எண், மொழி)
            குழு = re.fullmatch(சுருங்குறி, உரை)
            assert குழு is not None, உரை
