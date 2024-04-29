class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        array_of_s = list(s)
        for i in array_of_s:
            match i:
                case "I":
                    save = 1
                case "V":
                    if save == 1 :
                        res = res+4
                    else res = res+6
                case "X":
                    if save == 1 :
                        res = res+9
                    else res = res+11
                case "L":
                    res = res+50
                case "C":
                    res = res+100
                case "D":
                    res = res+500
                case "M":
                    res = res+1000