
# Define states for the ConversationHandler

class States():
    CHOOSE_QUESTION = 0
    CHOOSE_CATEGORY = 1
    CHOOSE_COUNTRIES = 2

question_keyboard = {
    "keyboard" : [
        ["Bevölkerung"],
        ["Beginn"],
        ["Kuchen"]
    ],
    "resize_keyboard" : True
}
contries_keyboard = {
    "keyboard" : [
        ["🇫🇷", "🇮🇹", "🇬🇧", "🇦🇹", "🇩🇪"],
        ["🇪🇸","🇬🇷","🇨🇭", "🇮🇳","🇹🇷"],
        ["🇨🇲", "🇮🇷", "🇺🇸", "🇨🇳", "🏳️‍🌈"],
        ["Zurück", "Andere", "Bestätigen"]
    ],
    "resize_keyboard" : True
}

category_keyboard = {
    "keyboard" : [
        ["Tote", "Infizierte"],
        ["Geheilte", "Aktive"],
        ["Zurück"]
    ],
    "resize_keyboard" : True
}

remove_keyboard = {
    "remove_keyboard" : True
}

jh_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"

first_jh_daily_entry = "2020-01-22.csv"

welcome_message = """Willkommen! Ich bin der CoronaBot.

Ich liefere dir Grafiken, auf denen du den Verlauf der Coronapandemie in verschiednen Ländern vergleichen kannst. Ich zeige dir Informationen über die Corona Toten, Geheilten, Erkrankten und über die aktuell Erkrankten.

Ich kann dir folgende Grafiken anzeigen:

- *Bevölkerung:* Der Verlauf der Krankheit in Relation zu seiner Bevölkerung (pro 100.000 Einwohner).
- *Beginn:* Der Verlauf der Krankheit pro Tag seit dem Ausbruch (100. Fall)
- *Kuchen:* Das Verhältnis der an Corona Gestorbenen zu allen Gestorbenen seit Beginn der Pandemie.

_Anmerkung: Für diese Statistik mache ich die Annahmen, dass Corona Tote auch nur an Corona gestorben sind, und, dass seit Beginn der Pandemie genau so viele Menschen gestorben sind, wie im Durchschnitt in den vergangenen Jahren_.

Klick dich gerne durch meine Menüs! 🙂"""

def format_country(emoji):
    country = ""

    if emoji == "🇦🇨":
        country = "Ascension Island"

    if emoji == "🏳️‍🌈":
        country = "World"

    if emoji == "🇦🇩":
        country = "Andorra"

    if emoji == "🇦🇪":
        country = "United Arab Emirates"

    if emoji == "🇦🇫":
        country = "Afghanistan"

    if emoji == "🇦🇬":
        country = "Antigua & Barbuda"

    if emoji == "🇦🇮":
        country = "Anguilla"

    if emoji == "🇦🇱":
        country = "Albania"

    if emoji == "🇦🇲":
        country = "Armenia"

    if emoji == "🇦🇴":
        country = "Angola"

    if emoji == "🇦🇶":
        country = "Antarctica"

    if emoji == "🇦🇷":
        country = "Argentina"

    if emoji == "🇦🇸":
        country = "American Samoa"

    if emoji == "🇦🇹":
        country = "Austria"

    if emoji == "🇦🇺":
        country = "Australia"

    if emoji == "🇦🇼":
        country = "Aruba"

    if emoji == "🇦🇽":
        country = "Åland Islands"

    if emoji == "🇦🇿":
        country = "Azerbaijan"

    if emoji == "🇧🇦":
        country = "Bosnia & Herzegovina"

    if emoji == "🇧🇧":
        country = "Barbados"

    if emoji == "🇧🇩":
        country = "Bangladesh"

    if emoji == "🇧🇪":
        country = "Belgium"

    if emoji == "🇧🇫":
        country = "Burkina Faso"

    if emoji == "🇧🇬":
        country = "Bulgaria"

    if emoji == "🇧🇭":
        country = "Bahrain"

    if emoji == "🇧🇮":
        country = "Burundi"

    if emoji == "🇧🇯":
        country = "Benin"

    if emoji == "🇧🇱":
        country = "St. Barthélemy"

    if emoji == "🇧🇲":
        country = "Bermuda"

    if emoji == "🇧🇳":
        country = "Brunei"

    if emoji == "🇧🇴":
        country = "Bolivia"

    if emoji == "🇧🇶":
        country = "Caribbean Netherlands"

    if emoji == "🇧🇷":
        country = "Brazil"

    if emoji == "🇧🇸":
        country = "Bahamas"

    if emoji == "🇧🇹":
        country = "Bhutan"

    if emoji == "🇧🇻":
        country = "Bouvet Island"

    if emoji == "🇧🇼":
        country = "Botswana"

    if emoji == "🇧🇾":
        country = "Belarus"

    if emoji == "🇧🇿":
        country = "Belize"

    if emoji == "🇨🇦":
        country = "Canada"

    if emoji == "🇨🇨":
        country = "Cocos (Keeling) Islands"

    if emoji == "🇨🇩":
        country = "Congo - Kinshasa"

    if emoji == "🇨🇫":
        country = "Central African Republic"

    if emoji == "🇨🇬":
        country = "Congo - Brazzaville"

    if emoji == "🇨🇭":
        country = "Switzerland"

    if emoji == "🇨🇮":
        country = "Côte d’Ivoire"

    if emoji == "🇨🇰":
        country = "Cook Islands"

    if emoji == "🇨🇱":
        country = "Chile"

    if emoji == "🇨🇲":
        country = "Cameroon"

    if emoji == "🇨🇳":
        country = "China"

    if emoji == "🇨🇴":
        country = "Colombia"

    if emoji == "🇨🇵":
        country = "Clipperton Island"

    if emoji == "🇨🇷":
        country = "Costa Rica"

    if emoji == "🇨🇺":
        country = "Cuba"

    if emoji == "🇨🇻":
        country = "Cape Verde"

    if emoji == "🇨🇼":
        country = "Curaçao"

    if emoji == "🇨🇽":
        country = "Christmas Island"

    if emoji == "🇨🇾":
        country = "Cyprus"

    if emoji == "🇨🇿":
        country = "Czechia"

    if emoji == "🇩🇪":
        country = "Germany"

    if emoji == "🇩🇬":
        country = "Diego Garcia"

    if emoji == "🇩🇯":
        country = "Djibouti"

    if emoji == "🇩🇰":
        country = "Denmark"

    if emoji == "🇩🇲":
        country = "Dominica"

    if emoji == "🇩🇴":
        country = "Dominican Republic"

    if emoji == "🇩🇿":
        country = "Algeria"

    if emoji == "🇪🇦":
        country = "Ceuta & Melilla"

    if emoji == "🇪🇨":
        country = "Ecuador"

    if emoji == "🇪🇪":
        country = "Estonia"

    if emoji == "🇪🇬":
        country = "Egypt"

    if emoji == "🇪🇭":
        country = "Western Sahara"

    if emoji == "🇪🇷":
        country = "Eritrea"

    if emoji == "🇪🇸":
        country = "Spain"

    if emoji == "🇪🇹":
        country = "Ethiopia"

    if emoji == "🇫🇮":
        country = "Finland"

    if emoji == "🇫🇯":
        country = "Fiji"

    if emoji == "🇫🇰":
        country = "Falkland Islands"

    if emoji == "🇫🇲":
        country = "Micronesia"

    if emoji == "🇫🇴":
        country = "Faroe Islands"

    if emoji == "🇫🇷":
        country = "France"

    if emoji == "🇬🇦":
        country = "Gabon"

    if emoji == "🇬🇧":
        country = "United Kingdom"

    if emoji == "🇬🇩":
        country = "Grenada"

    if emoji == "🇬🇪":
        country = "Georgia"

    if emoji == "🇬🇫":
        country = "French Guiana"

    if emoji == "🇬🇬":
        country = "Guernsey"

    if emoji == "🇬🇭":
        country = "Ghana"

    if emoji == "🇬🇮":
        country = "Gibraltar"

    if emoji == "🇬🇱":
        country = "Greenland"

    if emoji == "🇬🇲":
        country = "Gambia"

    if emoji == "🇬🇳":
        country = "Guinea"

    if emoji == "🇬🇵":
        country = "Guadeloupe"

    if emoji == "🇬🇶":
        country = "Equatorial Guinea"

    if emoji == "🇬🇷":
        country = "Greece"

    if emoji == "🇬🇸":
        country = "South Georgia & South Sandwich Islands"

    if emoji == "🇬🇹":
        country = "Guatemala"

    if emoji == "🇬🇺":
        country = "Guam"

    if emoji == "🇬🇼":
        country = "Guinea-Bissau"

    if emoji == "🇬🇾":
        country = "Guyana"

    if emoji == "🇭🇰":
        country = "Hong Kong SAR China"

    if emoji == "🇭🇲":
        country = "Heard & McDonald Islands"

    if emoji == "🇭🇳":
        country = "Honduras"

    if emoji == "🇭🇷":
        country = "Croatia"

    if emoji == "🇭🇹":
        country = "Haiti"

    if emoji == "🇭🇺":
        country = "Hungary"

    if emoji == "🇮🇨":
        country = "Canary Islands"

    if emoji == "🇮🇩":
        country = "Indonesia"

    if emoji == "🇮🇪":
        country = "Ireland"

    if emoji == "🇮🇱":
        country = "Israel"

    if emoji == "🇮🇲":
        country = "Isle of Man"

    if emoji == "🇮🇳":
        country = "India"

    if emoji == "🇮🇴":
        country = "British Indian Ocean Territory"

    if emoji == "🇮🇶":
        country = "Iraq"

    if emoji == "🇮🇷":
        country = "Iran"

    if emoji == "🇮🇸":
        country = "Iceland"

    if emoji == "🇮🇹":
        country = "Italy"

    if emoji == "🇯🇪":
        country = "Jersey"

    if emoji == "🇯🇲":
        country = "Jamaica"

    if emoji == "🇯🇴":
        country = "Jordan"

    if emoji == "🇯🇵":
        country = "Japan"

    if emoji == "🇰🇪":
        country = "Kenya"

    if emoji == "🇰🇬":
        country = "Kyrgyzstan"

    if emoji == "🇰🇭":
        country = "Cambodia"

    if emoji == "🇰🇮":
        country = "Kiribati"

    if emoji == "🇰🇲":
        country = "Comoros"

    if emoji == "🇰🇳":
        country = "St. Kitts & Nevis"

    if emoji == "🇰🇵":
        country = "North Korea"

    if emoji == "🇰🇷":
        country = "South Korea"

    if emoji == "🇰🇼":
        country = "Kuwait"

    if emoji == "🇰🇾":
        country = "Cayman Islands"

    if emoji == "🇰🇿":
        country = "Kazakhstan"

    if emoji == "🇱🇦":
        country = "Laos"

    if emoji == "🇱🇧":
        country = "Lebanon"

    if emoji == "🇱🇨":
        country = "St. Lucia"

    if emoji == "🇱🇮":
        country = "Liechtenstein"

    if emoji == "🇱🇰":
        country = "Sri Lanka"

    if emoji == "🇱🇷":
        country = "Liberia"

    if emoji == "🇱🇸":
        country = "Lesotho"

    if emoji == "🇱🇹":
        country = "Lithuania"

    if emoji == "🇱🇺":
        country = "Luxembourg"

    if emoji == "🇱🇻":
        country = "Latvia"

    if emoji == "🇱🇾":
        country = "Libya"

    if emoji == "🇲🇦":
        country = "Morocco"

    if emoji == "🇲🇨":
        country = "Monaco"

    if emoji == "🇲🇩":
        country = "Moldova"

    if emoji == "🇲🇪":
        country = "Montenegro"

    if emoji == "🇲🇫":
        country = "St. Martin"

    if emoji == "🇲🇬":
        country = "Madagascar"

    if emoji == "🇲🇭":
        country = "Marshall Islands"

    if emoji == "🇲🇰":
        country = "North Macedonia"

    if emoji == "🇲🇱":
        country = "Mali"

    if emoji == "🇲🇲":
        country = "Myanmar (Burma)"

    if emoji == "🇲🇳":
        country = "Mongolia"

    if emoji == "🇲🇴":
        country = "Macao Sar China"

    if emoji == "🇲🇵":
        country = "Northern Mariana Islands"

    if emoji == "🇲🇶":
        country = "Martinique"

    if emoji == "🇲🇷":
        country = "Mauritania"

    if emoji == "🇲🇸":
        country = "Montserrat"

    if emoji == "🇲🇹":
        country = "Malta"

    if emoji == "🇲🇺":
        country = "Mauritius"

    if emoji == "🇲🇻":
        country = "Maldives"

    if emoji == "🇲🇼":
        country = "Malawi"

    if emoji == "🇲🇽":
        country = "Mexico"

    if emoji == "🇲🇾":
        country = "Malaysia"

    if emoji == "🇲🇿":
        country = "Mozambique"

    if emoji == "🇳🇦":
        country = "Namibia"

    if emoji == "🇳🇨":
        country = "New Caledonia"

    if emoji == "🇳🇪":
        country = "Niger"

    if emoji == "🇳🇫":
        country = "Norfolk Island"

    if emoji == "🇳🇬":
        country = "Nigeria"

    if emoji == "🇳🇮":
        country = "Nicaragua"

    if emoji == "🇳🇱":
        country = "Netherlands"

    if emoji == "🇳🇴":
        country = "Norway"

    if emoji == "🇳🇵":
        country = "Nepal"

    if emoji == "🇳🇷":
        country = "Nauru"

    if emoji == "🇳🇺":
        country = "Niue"

    if emoji == "🇳🇿":
        country = "New Zealand"

    if emoji == "🇴🇲":
        country = "Oman"

    if emoji == "🇵🇦":
        country = "Panama"

    if emoji == "🇵🇪":
        country = "Peru"

    if emoji == "🇵🇫":
        country = "French Polynesia"

    if emoji == "🇵🇬":
        country = "Papua New Guinea"

    if emoji == "🇵🇭":
        country = "Philippines"

    if emoji == "🇵🇰":
        country = "Pakistan"

    if emoji == "🇵🇱":
        country = "Poland"

    if emoji == "🇵🇲":
        country = "St. Pierre & Miquelon"

    if emoji == "🇵🇳":
        country = "Pitcairn Islands"

    if emoji == "🇵🇷":
        country = "Puerto Rico"

    if emoji == "🇵🇸":
        country = "Palestinian Territories"

    if emoji == "🇵🇹":
        country = "Portugal"

    if emoji == "🇵🇼":
        country = "Palau"

    if emoji == "🇵🇾":
        country = "Paraguay"

    if emoji == "🇶🇦":
        country = "Qatar"

    if emoji == "🇷🇪":
        country = "Réunion"

    if emoji == "🇷🇴":
        country = "Romania"

    if emoji == "🇷🇸":
        country = "Serbia"

    if emoji == "🇷🇺":
        country = "Russia"

    if emoji == "🇷🇼":
        country = "Rwanda"

    if emoji == "🇸🇦":
        country = "Saudi Arabia"

    if emoji == "🇸🇧":
        country = "Solomon Islands"

    if emoji == "🇸🇨":
        country = "Seychelles"

    if emoji == "🇸🇩":
        country = "Sudan"

    if emoji == "🇸🇪":
        country = "Sweden"

    if emoji == "🇸🇬":
        country = "Singapore"

    if emoji == "🇸🇭":
        country = "St. Helena"

    if emoji == "🇸🇮":
        country = "Slovenia"

    if emoji == "🇸🇯":
        country = "Svalbard & Jan Mayen"

    if emoji == "🇸🇰":
        country = "Slovakia"

    if emoji == "🇸🇱":
        country = "Sierra Leone"

    if emoji == "🇸🇲":
        country = "San Marino"

    if emoji == "🇸🇳":
        country = "Senegal"

    if emoji == "🇸🇴":
        country = "Somalia"

    if emoji == "🇸🇷":
        country = "Suriname"

    if emoji == "🇸🇸":
        country = "South Sudan"

    if emoji == "🇸🇹":
        country = "São Tomé & Príncipe"

    if emoji == "🇸🇻":
        country = "El Salvador"

    if emoji == "🇸🇽":
        country = "Sint Maarten"

    if emoji == "🇸🇾":
        country = "Syria"

    if emoji == "🇸🇿":
        country = "Eswatini"

    if emoji == "🇹🇦":
        country = "Tristan Da Cunha"

    if emoji == "🇹🇨":
        country = "Turks & Caicos Islands"

    if emoji == "🇹🇩":
        country = "Chad"

    if emoji == "🇹🇫":
        country = "French Southern Territories"

    if emoji == "🇹🇬":
        country = "Togo"

    if emoji == "🇹🇭":
        country = "Thailand"

    if emoji == "🇹🇯":
        country = "Tajikistan"

    if emoji == "🇹🇰":
        country = "Tokelau"

    if emoji == "🇹🇱":
        country = "Timor-Leste"

    if emoji == "🇹🇲":
        country = "Turkmenistan"

    if emoji == "🇹🇳":
        country = "Tunisia"

    if emoji == "🇹🇴":
        country = "Tonga"

    if emoji == "🇹🇷":
        country = "Turkey"

    if emoji == "🇹🇹":
        country = "Trinidad & Tobago"

    if emoji == "🇹🇻":
        country = "Tuvalu"

    if emoji == "🇹🇼":
        country = "Taiwan"

    if emoji == "🇹🇿":
        country = "Tanzania"

    if emoji == "🇺🇦":
        country = "Ukraine"

    if emoji == "🇺🇬":
        country = "Uganda"

    if emoji == "🇺🇲":
        country = "U.S. Outlying Islands"

    if emoji == "🇺🇳":
        country = "United Nations"

    if emoji == "🇺🇸":
        country = "United States"

    if emoji == "🇺🇾":
        country = "Uruguay"

    if emoji == "🇺🇿":
        country = "Uzbekistan"

    if emoji == "🇻🇦":
        country = "Vatican City"

    if emoji == "🇻🇨":
        country = "St. Vincent & Grenadines"

    if emoji == "🇻🇪":
        country = "Venezuela"

    if emoji == "🇻🇬":
        country = "British Virgin Islands"

    if emoji == "🇻🇮":
        country = "U.S. Virgin Islands"

    if emoji == "🇻🇳":
        country = "Vietnam"

    if emoji == "🇻🇺":
        country = "Vanuatu"

    if emoji == "🇼🇫":
        country = "Wallis & Futuna"

    if emoji == "🇼🇸":
        country = "Samoa"

    if emoji == "🇽🇰":
        country = "Kosovo"

    if emoji == "🇾🇪":
        country = "Yemen"

    if emoji == "🇾🇹":
        country = "Mayotte"

    if emoji == "🇿🇦":
        country = "South Africa"

    if emoji == "🇿🇲":
        country = "Zambia"

    if emoji == "🇿🇼":
        country = "Zimbabwe"

    return country
