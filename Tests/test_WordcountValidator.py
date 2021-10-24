from unittest import TestCase

import WordCountValidation


class Test(TestCase):
    def test_wordCount(self):
        test_string = "Ich bin ein lieber netter kleiner äußerst verzückender Teststring."
        result = 9
        self.assertEqual(WordCountValidation.count_words_in_string(test_string), result)

    def test_wordCount2(self):
        test_string = "Eins"
        result = 1
        self.assertEqual(WordCountValidation.count_words_in_string(test_string), result)

    def test_wordCount_over_sentence_boundaries(self):
        test_string = "Ich bin ein Satz. Ich bin ein zweiter Satz."
        result = 9
        self.assertEqual(WordCountValidation.count_words_in_string(test_string), result)
