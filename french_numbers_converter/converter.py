class FrenchNumberConverter:
    def __init__(self):
        self.base_numbers = [
            "zéro", "un", "deux", "trois", "quatre",
            "cinq", "six", "sept", "huit", "neuf",
            "dix", "onze", "douze", "treize", "quatorze",
            "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"
        ]
        self.tens = {
            20: "vingt", 30: "trente", 40: "quarante",
            50: "cinquante", 60: "soixante",
            70: "soixante-dix", 80: "quatre-vingt", 90: "quatre-vingt-dix"
        }

    def convert_to_french(self, number: int) -> str:
        if number < 1000000:
            return self._convert_thousands(number)
        millions_part = number // 1000000
        remainder = number % 1000000
        prefix = "un-million" if millions_part == 1 else self._convert_thousands(millions_part, False) + "-millions"
        if remainder == 0:
            return prefix
        return prefix + "-" + self._convert_thousands(remainder, False)

    def _convert_base_numbers(self, number) -> str:
        return self.base_numbers[number]

    def _convert_tens(self, number: int, is_final_part: bool = True) -> str:
        if number < 20:
            return self._convert_base_numbers(number)
        tens_part = (number // 10) * 10
        unit_part = number % 10
        if tens_part == 80 and unit_part == 0:
            return "quatre-vingts" if is_final_part else "quatre-vingt"
        if unit_part == 0:
            return self.tens[tens_part]
        if tens_part == 20 and unit_part == 1:
            return "vingt-et-un"
        if tens_part == 70 or tens_part == 90:
            return self._convert_tens(tens_part - 10, False) + "-" + self._convert_base_numbers(10 + unit_part)
        return self.tens[tens_part] + "-" + self._convert_base_numbers(unit_part)

    def _convert_hundreds(self, number: int, is_final_part: bool = True) -> str:
        if number < 100:
            return self._convert_tens(number, is_final_part)
        hundreds_part = number // 100
        remainder = number % 100
        prefix = "cent" if hundreds_part == 1 else self._convert_base_numbers(hundreds_part) + "-cent"
        if remainder == 0:
            return prefix + ("s" if hundreds_part > 1 and is_final_part else "")
        return prefix + "-" + self._convert_tens(remainder, False)

    def _convert_thousands(self, number: int, is_final_part: bool = True) -> str:
        if number < 1000:
            return self._convert_hundreds(number, is_final_part)
        thousands_part = number // 1000
        remainder = number % 1000
        prefix = "mille" if thousands_part == 1 else self._convert_hundreds(thousands_part, False) + "-mille"
        if remainder == 0:
            return prefix
        return prefix + "-" + self._convert_hundreds(remainder, False)