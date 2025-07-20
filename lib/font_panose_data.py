__all__ = ["PANOSE",
           "LATIN_TEXT",
           "LATIN_TEXT_MONOSPACE",
           "LATIN_HAND_WRITTEN",
           "LATIN_HAND_WRITTEN_MONOSPACE",
           "FAMILY_KIND_ANY",
           "LATIN_TEXT_MONOSPACE"]

FAMILY_KIND__ANY = 0
FAMILY_KIND__NO_FIT = 1
FAMILY_KIND__LATIN_TEXT = 2
FAMILY_KIND__LATIN_HANDWRITTEN = 3
FAMILY_KIND__LATIN_DECORATIVE = 4
FAMILY_KIND__LATIN_SYMBOL = 5

FIELD__LATIN_TEXT__FAMILY_KIND = 0
FIELD__LATIN_TEXT__SERIF_STYLE = 1
FIELD__LATIN_TEXT__WEIGHT = 2
FIELD__LATIN_TEXT__PROPORTION = 3
FIELD__LATIN_TEXT__CONTRAST = 4
FIELD__LATIN_TEXT__STROKE_VARIATION = 5
FIELD__LATIN_TEXT__ARM_STYLE = 6
FIELD__LATIN_TEXT__LETTERFORM = 7
FIELD__LATIN_TEXT__MIDLINE = 8
FIELD__LATIN_TEXT__X_HEIGHT = 9
FIELD__LATIN_HANDWRITTEN__FAMILY_KIND = 0
FIELD__LATIN_HANDWRITTEN__TOOL_KIND = 1
FIELD__LATIN_HANDWRITTEN__WEIGHT = 2
FIELD__LATIN_HANDWRITTEN__SPACING = 3
FIELD__LATIN_HANDWRITTEN__ASPECT_RATIO = 4
FIELD__LATIN_HANDWRITTEN__CONTRAST = 5
FIELD__LATIN_HANDWRITTEN__TOPOLOGY = 6
FIELD__LATIN_HANDWRITTEN__FORM = 7
FIELD__LATIN_HANDWRITTEN__FINIALS = 8
FIELD__LATIN_HANDWRITTEN__X_ASCENT = 9
FIELD__LATIN_DECORATIVE__FAMILY_KIND = 0
FIELD__LATIN_DECORATIVE__CLASS = 1
FIELD__LATIN_DECORATIVE__WEIGHT = 2
FIELD__LATIN_DECORATIVE__ASPECT = 3
FIELD__LATIN_DECORATIVE__CONTRAST = 4
FIELD__LATIN_DECORATIVE__SERIF_VARIANT = 5
FIELD__LATIN_DECORATIVE__TREATMENT = 6
FIELD__LATIN_DECORATIVE__LINING = 7
FIELD__LATIN_DECORATIVE__TOPOLOGY = 8
FIELD__LATIN_DECORATIVE__RANGE_OF_CHARACTERS = 9
FIELD__LATIN_SYMBOL__FAMILY_KIND = 0
FIELD__LATIN_SYMBOL__KIND = 1
FIELD__LATIN_SYMBOL__WEIGHT = 2
FIELD__LATIN_SYMBOL__SPACING = 3
FIELD__LATIN_SYMBOL__ASPECT_RATIO_AND_CONTRAST = 4
FIELD__LATIN_SYMBOL__ASPECT_RATIO_OF_CHARACTER_94 = 5
FIELD__LATIN_SYMBOL__ASPECT_RATIO_OF_CHARACTER_119 = 6
FIELD__LATIN_SYMBOL__ASPECT_RATIO_OF_CHARACTER_157 = 7
FIELD__LATIN_SYMBOL__ASPECT_RATIO_OF_CHARACTER_163 = 8
FIELD__LATIN_SYMBOL__ASPECT_RATIO_OF_CHARACTER_211 = 9

PANOSE = [
    {
        "name": "Any",
    },
    {
        "name": "No Fit",
    },
    {
        "name": "Latin Text",
        "sub_digits_data": [
            {
                "name": "Family Kind (= 2 for Latin Text)",
            },
            {
                "name": "Serif Style",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "Cove", },
                    { "name": "Obtuse Cove", },
                    { "name": "Square Cove", },
                    { "name": "Obtuse Square Cove", },
                    { "name": "Square", },
                    { "name": "Thin", },
                    { "name": "Oval", },
                    { "name": "Exaggerated", },
                    { "name": "Triangle", },
                    { "name": "Normal Sans", },
                    { "name": "Obtuse Sans", },
                    { "name": "Perpendicular Sans", },
                ],
            },
            {
                "name": "Weight",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "Very Light", },
                    { "name": "Light", },
                    { "name": "Thin", },
                    { "name": "Book", },
                    { "name": "Medium", },
                    { "name": "Demi", },
                    { "name": "Bold", },
                    { "name": "Heavy", },
                    { "name": "Black", },
                    { "name": "Extra Black", },
                ],
            },
            {
                "name": "Proportion",
                "values": [
                    { "name": "Any", },
                    { "name": "No fit", },
                    { "name": "Old Style", },
                    { "name": "Modern", },
                    { "name": "Even Width", },
                    { "name": "Extended", },
                    { "name": "Condensed", },
                    { "name": "Very Extended", },
                    { "name": "Very Condensed", },
                    { "name": "Monospaced", },
                ],
            },
            {
                "name": "Contrast",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "None", },
                    { "name": "Very Low", },
                    { "name": "Low", },
                    { "name": "Medium Low", },
                    { "name": "Medium", },
                    { "name": "Medium High", },
                    { "name": "High", },
                    { "name": "Very High", },
                ],
            },
            {
                "name": "Stroke Variation",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "No Variation", },
                    { "name": "Gradual/Diagonal", },
                    { "name": "Gradual/Transitional", },
                    { "name": "Gradual/Vertical", },
                    { "name": "Gradual/Horizontal", },
                    { "name": "Rapid/Vertical", },
                    { "name": "Rapid/Horizontal", },
                    { "name": "Instant/Vertical", },
                    { "name": "Instant/Horizontal", },
                ],
            },
            {
                "name": "Arm Style",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "Straight Arms/Horizontal", },
                    { "name": "Straight Arms/Wedge", },
                    { "name": "Straight Arms/Vertical", },
                    { "name": "Straight Arms/Single Serif", },
                    { "name": "Straight Arms/Double Serif", },
                    { "name": "Non-Straight/Horizontal", },
                    { "name": "Non-Straight/Wedge", },
                    { "name": "Non-Straight/Vertical", },
                    { "name": "Non-Straight/Single Serif", },
                    { "name": "Non-Straight/Double Serif", },
                ],
            },
            {
                "name": "Letterform",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "Normal/Contact", },
                    { "name": "Normal/Weighted", },
                    { "name": "Normal/Boxed", },
                    { "name": "Normal/Flattened", },
                    { "name": "Normal/Rounded", },
                    { "name": "Normal/Off Center", },
                    { "name": "Normal/Square", },
                    { "name": "Oblique/Contact", },
                    { "name": "Oblique/Weighted", },
                    { "name": "Oblique/Boxed", },
                    { "name": "Oblique/Flattened", },
                    { "name": "Oblique/Rounded", },
                    { "name": "Oblique/Off Center", },
                    { "name": "Oblique/Square", },
                ],
            },
            {
                "name": "Midline",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "Standard/Trimmed", },
                    { "name": "Standard/Pointed", },
                    { "name": "Standard/Serifed", },
                    { "name": "High/Trimmed", },
                    { "name": "High/Pointed", },
                    { "name": "High/Serifed", },
                    { "name": "Constant/Trimmed", },
                    { "name": "Constant/Pointed", },
                    { "name": "Constant/Serifed", },
                    { "name": "Low/Trimmed", },
                    { "name": "Low/Pointed", },
                    { "name": "Low/Serifed", },
                ],
            },
            {
                "name": "X-height",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "Constant/Small", },
                    { "name": "Constant/Standard", },
                    { "name": "Constant/Large", },
                    { "name": "Ducking/Small", },
                    { "name": "Ducking/Standard", },
                    { "name": "Ducking/Large", },
                ],
            },
        ],
    },
    {
        "name": "Latin Handwritten",
        "sub_digits_data": [
            {
                "name": "Family Kind (= 3 for Latin Hand Written)",
            },
            {
                "name": "Tool Kind",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "Flat Nib", },
                    { "name": "Pressure Point", },
                    { "name": "Engraved", },
                    { "name": "Ball (Round Cap)", },
                    { "name": "Brush", },
                    { "name": "Rough", },
                    { "name": "Felt Pen/Brush Tip", },
                    { "name": "Wild Brush - Drips a lot", },
                ],
            },
            {
                "name": "Weight",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "Very Light", },
                    { "name": "Light", },
                    { "name": "Thin", },
                    { "name": "Book", },
                    { "name": "Medium", },
                    { "name": "Demi", },
                    { "name": "Bold", },
                    { "name": "Heavy", },
                    { "name": "Black", },
                    { "name": "Extra Black (Nord)", },
                ],
            },
            {
                "name": "Spacing",
                "values": [
                    { "name": "Any", },
                    { "name": "No fit", },
                    { "name": "Proportional Spaced", },
                    { "name": "Monospaced", },
                ],
            },
            {
                "name": "Aspect Ratio",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "Very Condensed", },
                    { "name": "Condensed", },
                    { "name": "Normal", },
                    { "name": "Expanded", },
                    { "name": "Very Expanded", },
                ],
            },
            {
                "name": "Contrast",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "None", },
                    { "name": "Very Low", },
                    { "name": "Low", },
                    { "name": "Medium Low", },
                    { "name": "Medium", },
                    { "name": "Medium High", },
                    { "name": "High", },
                    { "name": "Very High", },
                ],
            },
            {
                "name": "Topology",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "Roman Disconnected", },
                    { "name": "Roman Trailing", },
                    { "name": "Roman Connected", },
                    { "name": "Cursive Disconnected", },
                    { "name": "Cursive Trailing", },
                    { "name": "Cursive Connected", },
                    { "name": "Blackletter Disconnected", },
                    { "name": "Blackletter Trailing", },
                    { "name": "Blackletter Connected", },
                ],
            },
            {
                "name": "Form",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "Upright / No Wrapping", },
                    { "name": "Upright / Some Wrapping", },
                    { "name": "Upright / More Wrapping", },
                    { "name": "Upright / Extreme Wrapping", },
                    { "name": "Oblique / No Wrapping", },
                    { "name": "Oblique / Some Wrapping", },
                    { "name": "Oblique / More Wrapping", },
                    { "name": "Oblique / Extreme Wrapping", },
                    { "name": "Exaggerated / No Wrapping", },
                    { "name": "Exaggerated / Some Wrapping", },
                    { "name": "Exaggerated / More Wrapping", },
                    { "name": "Exaggerated / Extreme Wrapping", },
                ],
            },
            {
                "name": "Finials",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "None / No loops", },
                    { "name": "None / Closed loops", },
                    { "name": "None / Open loops", },
                    { "name": "Sharp / No loops", },
                    { "name": "Sharp / Closed loops", },
                    { "name": "Sharp / Open loops", },
                    { "name": "Tapered / No loops", },
                    { "name": "Tapered / Closed loops", },
                    { "name": "Tapered / Open loops", },
                ],
            },
            {
                "name": "X-ascent",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "Very Low", },
                    { "name": "Low", },
                    { "name": "Medium", },
                    { "name": "High", },
                    { "name": "Very High", },
                ],
            },
        ],
    },
    {
        "name": "Latin Decorative",
        "sub_digits_data": [
            {
                "name": "Family Kind (= 4 for Latin Decorative)",
            },
            {
                "name": "Class",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "Derivative", },
                    { "name": "Non-standard Topology", },
                    { "name": "Non-standard Elements", },
                    { "name": " Non-standard Aspect", },
                    { "name": "Initials", },
                    { "name": "Cartoon", },
                    { "name": "Picture Stems", },
                    { "name": "Ornamented", },
                    { "name": "Text and Background", },
                    { "name": "Collage", },
                    { "name": "Montage", },
                ],
            },
            {
                "name": "Weight",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "Very Light", },
                    { "name": "Light", },
                    { "name": "Thin", },
                    { "name": "Book", },
                    { "name": "Medium", },
                    { "name": "Demi", },
                    { "name": "Bold", },
                    { "name": "Heavy", },
                    { "name": "Black", },
                    { "name": "Extra Black", },
                ],
            },
            {
                "name": "Aspect",
                "values": [
                    { "name": "Any", },
                    { "name": "No fit", },
                    { "name": "Super Condensed", },
                    { "name": "Very Condensed", },
                    { "name": "Condensed", },
                    { "name": "Normal", },
                    { "name": "Extended", },
                    { "name": "Very Extended", },
                    { "name": "Super Extended", },
                    { "name": "Monospaced", },
                ],
            },
            {
                "name": "Contrast",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "None", },
                    { "name": "Very Low", },
                    { "name": "Low", },
                    { "name": "Medium Low", },
                    { "name": "Medium", },
                    { "name": "Medium High", },
                    { "name": "High", },
                    { "name": "Very High", },
                    { "name": "Horizontal Low", },
                    { "name": "Horizontal Medium", },
                    { "name": "Horizontal High", },
                    { "name": "Broken", },
                ],
            },
            {
                "name": "Serif Variant",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "Cove", },
                    { "name": "Obtuse Cove", },
                    { "name": "Square Cove", },
                    { "name": "Obtuse Square Cove", },
                    { "name": "Square", },
                    { "name": "Thin", },
                    { "name": "Oval", },
                    { "name": "Exaggerated", },
                    { "name": "Triangle", },
                    { "name": "Normal Sans", },
                    { "name": "Obtuse Sans", },
                    { "name": "Perpendicular Sans", },
                    { "name": "Flared", },
                    { "name": "Rounded", },
                    { "name": "Script", },
                ],
            },
            {
                "name": "Treatment",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "None - Standard Solid Fill", },
                    { "name": "White / No Fill", },
                    { "name": "Patterned Fill", },
                    { "name": "Complex Fill", },
                    { "name": "Shaped Fill", },
                    { "name": "Drawn / Distressed", },
                ],
            },
            {
                "name": "Lining",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "None", },
                    { "name": "Inline", },
                    { "name": "Outline", },
                    { "name": "Engraved (Multiple Lines)", },
                    { "name": "Shadow", },
                    { "name": "Relief", },
                    { "name": "Backdrop", },
                ],
            },
            {
                "name": "Topology",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "Standard", },
                    { "name": "Square", },
                    { "name": "Multiple Segment", },
                    { "name": "Deco (E,M,S) Waco midlines", },
                    { "name": "Uneven Weighting", },
                    { "name": "Diverse Arms", },
                    { "name": "Diverse Forms", },
                    { "name": "Lombardic Forms", },
                    { "name": "Upper Case in Lower Case", },
                    { "name": "Implied Topology", },
                    { "name": "Horseshoe E and A", },
                    { "name": "Cursive", },
                    { "name": "Blackletter", },
                    { "name": "Swash Variance", },
                ],
            },
            {
                "name": "Range of Characters",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "Extended Collection", },
                    { "name": "Litterals", },
                    { "name": "No Lower Case", },
                    { "name": "Small Caps", },
                ],
            },
        ],
    },
    {
        "name": "Latin Symbol",
        "sub_digits_data": [
            {
                "name": "Family Kind (= 5 for Latin Symbol)",
            },
            {
                "name": "Kind",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "Montages", },
                    { "name": "Pictures", },
                    { "name": "Shapes", },
                    { "name": "Scientific", },
                    { "name": "Music", },
                    { "name": "Expert", },
                    { "name": "Patterns", },
                    { "name": "Boarders", },
                    { "name": "Icons", },
                    { "name": "Logos", },
                    { "name": "Industry specific", },
                ],
            },
            {
                "name": "Weight",
                "values": [
                    None,
                    { "name": "No Fit", },
                ],
            },
            {
                "name": "Spacing",
                "values": [
                    { "name": "Any", },
                    { "name": "No fit", },
                    { "name": "Proportional Spaced", },
                    { "name": "Monospaced", },
                ],
            },
            {
                "name": "Aspect Ratio & Contrast",
                "values": [
                    None,
                    { "name": "No Fit", },
                ],
            },
            {
                "name": "Aspect Ratio of Character 94",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "No Width", },
                    { "name": "Exceptionally Wide", },
                    { "name": "Super Wide", },
                    { "name": "Very Wide", },
                    { "name": "Wide", },
                    { "name": "Normal", },
                    { "name": "Narrow", },
                    { "name": "Very Narrow", },
                ],
            },
            {
                "name": "Aspect Ratio of Character 119",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "No Width", },
                    { "name": "Exceptionally Wide", },
                    { "name": "Super Wide", },
                    { "name": "Very Wide", },
                    { "name": "Wide", },
                    { "name": "Normal", },
                    { "name": "Narrow", },
                    { "name": "Very Narrow", },
                ],
            },
            {
                "name": "Aspect Ratio of Character 157",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "No Width", },
                    { "name": "Exceptionally Wide", },
                    { "name": "Super Wide", },
                    { "name": "Very Wide", },
                    { "name": "Wide", },
                    { "name": "Normal", },
                    { "name": "Narrow", },
                    { "name": "Very Narrow", },
                ],
            },
            {
                "name": "Aspect Ratio of Character 163",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "No Width", },
                    { "name": "Exceptionally Wide", },
                    { "name": "Super Wide", },
                    { "name": "Very Wide", },
                    { "name": "Wide", },
                    { "name": "Normal", },
                    { "name": "Narrow", },
                    { "name": "Very Narrow", },
                ],
            },
            {
                "name": "Aspect Ratio of Character 211",
                "values": [
                    { "name": "Any", },
                    { "name": "No Fit", },
                    { "name": "No Width", },
                    { "name": "Exceptionally Wide", },
                    { "name": "Super Wide", },
                    { "name": "Very Wide", },
                    { "name": "Wide", },
                    { "name": "Normal", },
                    { "name": "Narrow", },
                    { "name": "Very Narrow", },
                ],
            },
        ],
    },
]
