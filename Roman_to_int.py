class Solution(object):
    def romanToInt(self, roman_list: list[int]) -> int:
        converted_list = self.convert_roman_list(roman_list)
        for i in range(len(roman_list)-1):
            converted_list[i] = self.negate_roman(roman_list[i], roman_list[i+1])
        return sum(converted_list)


    def roman_char_to_int(self, s: str) -> int:
        # roman_table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        # return roman_table[s]
        return {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}[s]

    def convert_roman_list(self, roman_list: list[str]) -> list[int]:
        return list(map(self.roman_char_to_int, roman_list))

    def negate_roman(self, numeral_a: str, numeral_b: str) -> int:
        # elif (s[0] == "X" and s[1] == "L" ) or (s[0] == "X" and s[1] == "C"):
        if numeral_a == "I" and numeral_b in "VX":
            return -self.roman_char_to_int(numeral_a)
        elif numeral_a == "X" and numeral_b in "LC":
            return -self.roman_char_to_int(numeral_a)
        elif numeral_a == "C" and numeral_b in "DM":
            return -self.roman_char_to_int(numeral_a)
        return self.roman_char_to_int(numeral_a)


def test():
    users_input = str(input("Your roman: ")).upper()
    user_split = list(users_input)

    print(user_split)
    # Test roman_char_to_int
    #print(Solution().roman_char_to_int(user_split[0]))
    print(Solution().convert_roman_list(user_split))

    # Test calculations
    print(Solution().solution(user_split))

    # String -> Integer
    # String -> List[char] -> List[int] -> Integer

def main():
    pass

main()





# USER INPUTS S --> AND RETURNS THE VALUE