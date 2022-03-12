import unittest

from .regex import match_pattern, match


class TestRegex(unittest.TestCase):
    # stage 1
    def test_1(self):
        self.assertTrue(match("a", "a"))  # "Two identical patterns should return True!"),

    def test_11(self):
        self.assertFalse(match("a", "b"))  # "Two different patterns should not return True!"),

    def test_12(self):
        self.assertTrue(match("7", "7"))  # "Two identical patterns should return True!"),

    def test_13(self):
        self.assertFalse(match("6", "7"))  # "Two different patterns should not return True!"),

    def test_14(self):
        self.assertTrue(match(".", "a"))  # "Don't forget that '.' is a wild-card that matches any single character."),

    def test_15(self):
        self.assertFalse(match("a", "."))  # "A period in the input string is still a literal!"),

    def test_16(self):
        self.assertTrue(match("", "a"))  # "An empty regex always returns True!"),

    def test_17(self):
        self.assertTrue(match("", ""))  # "An empty regex always returns True!"),

    def test_18(self):
        self.assertFalse(match("a", ""))  # "A non-empty regex and an empty input string always returns False!"),

    # stage 2
    def test_2(self):
        self.assertTrue(match("apple", "apple"))  # "Two identical equal-length patterns should return True!"),

    def test_21(self):
        self.assertTrue(match(".pple", "apple"))  # "The wild-card '.' should match any single character in a string."),

    def test_22(self):
        self.assertTrue(match("appl.", "apple"))  # "The wild-card '.' should match any single character in a string."),

    def test_23(self):
        self.assertTrue(match(".....", "apple"))  # "The wild-card '.' should match any single character in a string."),

    def test_24(self):
        self.assertTrue(match("", "apple"))  # "An empty regex always returns True!")

    def test_25(self):
        self.assertFalse(match("apple", ""))  # "A non-empty regex and an empty input string always returns False!"),

    def test_26(self):
        self.assertFalse(match("apple", "peach"))  # "Two different patterns should not return True!"),

    # stage 3
    def test_3(self):
        self.assertTrue(match("le", "apple"))  # "If the input string contains the regex, it should return True!"),

    def test_31(self):
        self.assertTrue(match("app", "apple"))  # "If the input string contains the regex, it should return True!"),

    def test_32(self):
        self.assertTrue(match("a", "apple"))  # "If the input string contains the regex, it should return True!"),

    def test_33(self):
        self.assertTrue(match(".", "apple"))  # "Even a single wild-card character '.' can produce a match!"),

    def test_34(self):
        self.assertFalse(match("apwle", "apple"))  # "Two different patterns should not return True!"),

    def test_35(self):
        self.assertFalse(match("peach", "apple"))  # "Two different patterns should not return True!"),

    # stage 4
    def test_4(self):
        self.assertTrue(match('^app', 'apple'))

    def test_41(self):
        self.assertTrue(match('le$', 'apple'))

    def test_42(self):
        self.assertTrue(match('^a', 'apple'))

    def test_43(self):
        self.assertTrue(match('.$', 'apple'))

    def test_44(self):
        self.assertTrue(match('apple$', 'tasty apple'))

    def test_45(self):
        self.assertTrue(match('^apple', 'apple pie'))

    def test_46(self):
        self.assertTrue(match('^apple$', 'apple'))

    def test_47(self):
        self.assertFalse(match('^apple$', 'tasty apple'))

    def test_48(self):
        self.assertFalse(match('^apple$', 'apple pie'))

    def test_49(self):
        self.assertFalse(match('app$', 'apple'))

    def test_410(self):
        self.assertFalse(match('^le', 'apple'))

    # stage 5
    def test_5(self):
        self.assertTrue(match("colou?r", "color"))

    def test_51(self):
        self.assertTrue(match("colou?r", "colour"))

    def test_52(self):
        self.assertFalse(match("colou?r", "colouur"))

    def test_53(self):
        self.assertTrue(match("colou*r", "color"))

    def test_54(self):
        self.assertTrue(match("colou*r", "colour"))

    def test_55(self):
        self.assertTrue(match("colou*r", "colouur"))

    def test_56(self):
        self.assertTrue(match("colou+r", "colour"))

    def test_57(self):
        self.assertFalse(match("colou+r", "color"))

    def test_58(self):
        self.assertTrue(match(".*", "aaa"))

    def test_59(self):
        self.assertTrue(match(".+", "aaa"))

    def test_510(self):
        self.assertTrue(match(".?", "aaa"))

    def test_511(self):
        self.assertFalse(match("no+$", "noooooooope"))

    def test_512(self):
        self.assertTrue(match("^no+", "noooooooope"))

    def test_513(self):
        self.assertTrue(match("^no+pe$", "noooooooope"))

    def test_514(self):
        self.assertTrue(match("^n.+pe$", "noooooooope"))

    def test_515(self):
        self.assertFalse(match("^n.+p$", "noooooooope"))

    def test_516(self):
        self.assertTrue(match('^.*c$', 'abcabc'))

    # stage 6
    def test_6(self):
        self.assertTrue(match("\\.$", "end."))

    def test_61(self):
        self.assertTrue(match("3\\+3", "3+3=6"))

    def test_62(self):
        self.assertTrue(match("\\?", "Is this working?"))

    def test_63(self):
        self.assertTrue(match("\\\\", "\\"))

    def test_64(self):
        self.assertFalse(match("colou\\?r", "color"))

    def test_65(self):
        self.assertFalse(match("colou\\?r", "colour"))


if __name__ == '__main__':
    unittest.main()
