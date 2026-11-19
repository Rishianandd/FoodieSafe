"""Pure, testable privacy and allergen logic. No network or persistent storage."""
from typing import Iterable

ALLOWED_ALLERGENS = frozenset({'Eggs','Fish','Milk','Peanuts','Sesame','Shellfish','Soy','Tree nuts','Wheat'})
ALLOWED_DIETS = frozenset({'No restriction','Vegetarian','Vegan'})


def validate_preferences(allergens: Iterable[str], diet: str) -> tuple[list[str], str]:
    selected = set(allergens)
    if not selected.issubset(ALLOWED_ALLERGENS):
        raise ValueError('Unknown allergen selection')
    if diet not in ALLOWED_DIETS:
        raise ValueError('Unknown dietary preference')
    return sorted(selected), diet


def build_minimal_disclosure(allergens: Iterable[str], diet: str, consent: bool) -> dict | None:
    """Prepare a minimal on-screen preview only; never sends it anywhere."""
    if not consent:
        return None
    selected, validated_diet = validate_preferences(allergens, diet)
    return {'allergens': selected, 'dietary_preference': validated_diet}


def assess_dish(dish: dict, allergens: Iterable[str], diet: str) -> tuple[list[str], bool]:
    selected, validated_diet = validate_preferences(allergens, diet)
    return sorted(set(selected) & set(dish['allergens'])), validated_diet not in dish['diet']
