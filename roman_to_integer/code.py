class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        array_of_s = list(s)
        for i in array_of_s:
            match i:
                case "I":
                    save_i = 1
                case "V":
                    if save_i == 1 :
                        res = res+4
                    else : 
                        res = res+6
                    save_i = 0
                case "X":
                    if save_i == 1 :
                        res = res+9
                    else : 
                        save_x = 1
                    save_i = 0
                case "L":
                    res = res+50
                case "C":
                    save_c = 1
                    res = res+100
                case "D":
                    res = res+500
                case "M":
                    res = res+1000