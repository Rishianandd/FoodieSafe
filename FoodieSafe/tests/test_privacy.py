import unittest
from privacy_core import build_minimal_disclosure, assess_dish, validate_preferences

class PrivacyTests(unittest.TestCase):
    def test_no_consent_no_disclosure(self):
        self.assertIsNone(build_minimal_disclosure(['Peanuts'], 'Vegan', False))
    def test_minimal_disclosure(self):
        self.assertEqual(build_minimal_disclosure(['Peanuts'], 'Vegan', True), {'allergens':['Peanuts'], 'dietary_preference':'Vegan'})
    def test_reject_unrecognized_allergens(self):
        with self.assertRaises(ValueError):
            validate_preferences(['unexpected'], 'Vegan')
    def test_allergen_warning(self):
        dish = {'allergens': {'Peanuts'}, 'diet':['Vegan']}
        self.assertEqual(assess_dish(dish, ['Peanuts'], 'Vegan'), (['Peanuts'], False))
    def test_diet_mismatch(self):
        dish = {'allergens': set(), 'diet':['Vegetarian']}
        self.assertEqual(assess_dish(dish, [], 'Vegan'), ([], True))

if __name__ == '__main__':
    unittest.main()
