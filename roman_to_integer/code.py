class Solution:
    def romanToInt(s: str) -> int:
        res = 0
        array_of_s = list(s)
        save_x = 0
        save_c = 0
        save_i = 0
        for i in array_of_s:
            match i:
                case "I":
                    save_i = 1
                    res = res+1
                case "V":
                    if save_i == 1 :
                        res = res+3
                    else : 
                        res = res+6
                    save_i = 0
                case "X":
                    if save_i == 1 :
                        res = res+8
                    else : 
                        save_x = 1
                    save_i = 0
                case "L":
                    if save_x == 1 :
                        res = res+40
                    else : 
                        res = res+60
                    save_x = 0
                case "C":
                    save_c = 0
                    if save_x == 1 :
                        res = res+90
                    else : 
                        save_c = 1
                    save_x = 0
                case "D":
                    if save_c == 1 :
                        res = res+400
                    else : 
                        res = res+600
                    save_c = 0
                case "M":
                    if save_c == 1 :
                        res = res+900
                    else : 
                        res = res+1100
                    save_c = 0
        return res
    
class main():
    print(Solution.romanToInt("III"))