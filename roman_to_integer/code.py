class Solution:
    def romanToInt(self, s: str) -> int:
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
                        res = res+5
                    save_i = 0
                case "X":
                    if save_i == 1 :
                        res = res+8
                    else : 
                        save_x = 1
                        res = res+10
                    save_i = 0
                case "L":
                    if save_x == 1 :
                        res = res+30
                    else : 
                        res = res+50
                    save_x = 0
                case "C":
                    if save_x == 1 :
                        res = res+80
                    else : 
                        save_c = 1
                        res = res+100
                    save_x = 0
                case "D":
                    if save_c == 1 :
                        res = res+300
                    else : 
                        res = res+500
                    save_c = 0
                case "M":
                    if save_c == 1 :
                        res = res+800
                    else : 
                        res = res+1000
                    save_c = 0
        return res
    
class main():
    print(Solution.romanToInt("LVIII"))