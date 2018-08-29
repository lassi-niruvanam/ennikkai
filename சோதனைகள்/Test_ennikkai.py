import unittest
from எண்ணிக்கை import உரைக்கு, எண்ணுக்கு, மொழிகள்


class Test_மாற்றம்(unittest.TestCase):
    def _எண்_பரிசோதனை(தன், எண்):

        for மொ in மொழிகள்():
            with தன்.subTest(மொழி=மொ):
                உ = உரைக்கு(எண், மொ, தளம்=False)
                உ_௨ = உரைக்கு(எண், மொ, தளம்=None)
                வே = எண்ணுக்கு(உ)
                வே_௨ = எண்ணுக்கு(உ_௨)

                தன்.assertIsInstance(வே, type(எண்))
                தன்.assertEqual(வே, எண், உ)
                if உ != உ_௨:
                    தன்.assertIsInstance(வே_௨, type(எண்))
                    தன்.assertEqual(வே_௨, எண், உ_௨)

    def test_முழு_எண்(தன்):
        தன்._எண்_பரிசோதனை(123)

    def test_முழு_எண்_பதி(தன்):
        தன்._எண்_பரிசோதனை(123.)

    def test_vérifier_décimal(தன்):
        தன்._எண்_பரிசோதனை(0.1)

    def test_vérifier_décimal_début(தன்):
        தன்._எண்_பரிசோதனை(.123)

    def test_vérifier_décimal_0_début_multiple_0(தன்):
        தன்._எண்_பரிசோதனை(0.0000123)

    def test_vérifier_décimal_début_multiple_0(தன்):
        தன்._எண்_பரிசோதனை(.0000123)

    def test_vérifier_décimal_multiple_0(தன்):
        தன்._எண்_பரிசோதனை(12.0000123)

    def test_vérifier_négatif(தன்):
        தன்._எண்_பரிசோதனை(-1.23)

    def test_vérifier_négatif_déc_début(தன்):
        தன்._எண்_பரிசோதனை(-.101)

    def test_vérifier_tout(தன்):
        தன்._எண்_பரிசோதனை(-123456789.00012345678900)
