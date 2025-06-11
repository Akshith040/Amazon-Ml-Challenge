# constants.py

entity_unit_map = {
    "width": {"centimetre", "foot", "millimetre", "metre", "inch", "yard"},
    "depth": {"centimetre", "foot", "millimetre", "metre", "inch", "yard"},
    "height": {"centimetre", "foot", "millimetre", "metre", "inch", "yard"},
    "item_weight": {"milligram", "kilogram", "microgram", "gram", "ounce", "ton", "pound"},
    "maximum_weight_recommendation": {"milligram", "kilogram", "microgram", "gram", "ounce", "ton", "pound"},
    "voltage": {"millivolt", "kilovolt", "volt"},
    "wattage": {"kilowatt", "watt"},
    "item_volume": {
        "cubic foot", "microlitre", "cup", "fluid ounce", "centilitre", "imperial gallon",
        "pint", "decilitre", "litre", "millilitre", "quart", "cubic inch", "gallon"
    }
}

# Default units for each entity type (you may want to adjust these)
DEFAULT_UNITS = {
    "width": "centimetre",
    "depth": "centimetre",
    "height": "centimetre",
    "item_weight": "gram",
    "maximum_weight_recommendation": "kilogram",
    "voltage": "volt",
    "wattage": "watt",
    "item_volume": "millilitre"
}