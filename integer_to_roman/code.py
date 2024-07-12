class Solution:
    def InttoRoman(s: int) -> int:
        res = ""
        length = len(str(s))
        match length:
            case 1:
                match int(str(s)[:1]):
                    case 1:
                        res += "I"
                    case 2:
                        res += "II"
                    case 3:
                        res += "III"
                    case 4:
                        res += "IV"
                    case 5:
                        res += "V"
                    case 6:
                        res += "VI"
                    case 7:
                        res += "VII"
                    case 8:
                        res += "VIII"
                    case 9:
                        res += "IX"
            case 2:
                match int(str(s)[:1]):
                    case 1:
                        res += "X"
                    case 2:
                        res += "XX"
                    case 3:
                        res += "XXX"
                    case 4:
                        res += "XL"
                    case 5:
                        res += "L"
                    case 6:
                        res += "LX"
                    case 7:
                        res += "LXX"
                    case 8:
                        res += "LXXX"
                    case 9:
                        res += "XC"
                match int(str(s)[1:2]):
                    case 1:
                        res += "I"
                    case 2:
                        res += "II"
                    case 3:
                        res += "III"
                    case 4:
                        res += "IV"
                    case 5:
                        res += "V"
                    case 6:
                        res += "VI"
                    case 7:
                        res += "VII"
                    case 8:
                        res += "VIII"
                    case 9:
                        res += "IX"
            case 3:
                match int(str(s)[:1]):
                    case 1:
                        res += "C"
                    case 2:
                        res += "CC"
                    case 3:
                        res += "CCC"
                    case 4:
                        res += "CD"
                    case 5:
                        res += "D"
                    case 6:
                        res += "DC"
                    case 7:
                        res += "DCC"
                    case 8:
                        res += "DCCC"
                    case 9:
                        res += "CM"
                match int(str(s)[1:2]):
                    case 1:
                        res += "X"
                    case 2:
                        res += "XX"
                    case 3:
                        res += "XXX"
                    case 4:
                        res += "XL"
                    case 5:
                        res += "L"
                    case 6:
                        res += "LX"
                    case 7:
                        res += "LXX"
                    case 8:
                        res += "LXXX"
                    case 9:
                        res += "XC"
                match int(str(s)[2:3]):
                    case 1:
                        res += "I"
                    case 2:
                        res += "II"
                    case 3:
                        res += "III"
                    case 4:
                        res += "IV"
                    case 5:
                        res += "V"
                    case 6:
                        res += "VI"
                    case 7:
                        res += "VII"
                    case 8:
                        res += "VIII"
                    case 9:
                        res += "IX"
            case 4:
                match int(str(s)[:1]):
                    case 1:
                        res += "M"
                    case 2:
                        res += "MM"
                    case 3:
                        res += "MMM"
                match int(str(s)[1:2]):
                    case 1:
                        res += "C"
                    case 2:
                        res += "CC"
                    case 3:
                        res += "CCC"
                    case 4:
                        res += "CD"
                    case 5:
                        res += "D"
                    case 6:
                        res += "DC"
                    case 7:
                        res += "DCC"
                    case 8:
                        res += "DCCC"
                    case 9:
                        res += "CM"
                match int(str(s)[2:3]):
                    case 1:
                        res += "X"
                    case 2:
                        res += "XX"
                    case 3:
                        res += "XXX"
                    case 4:
                        res += "XL"
                    case 5:
                        res += "L"
                    case 6:
                        res += "LX"
                    case 7:
                        res += "LXX"
                    case 8:
                        res += "LXXX"
                    case 9:
                        res += "XC"
                match int(str(s)[3:4]):
                    case 1:
                        res += "I"
                    case 2:
                        res += "II"
                    case 3:
                        res += "III"
                    case 4:
                        res += "IV"
                    case 5:
                        res += "V"
                    case 6:
                        res += "VI"
                    case 7:
                        res += "VII"
                    case 8:
                        res += "VIII"
                    case 9:
                        res += "IX"
        return res
    
class main():
    print(Solution.InttoRoman(780))