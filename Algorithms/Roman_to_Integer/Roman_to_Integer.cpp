class Solution {
public:
    int romanToInt(string s) {
        int num = 0;
        char prev = ' ';
            
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] == 'I'){
                num += 1;
                prev = s[i];
            }
            else if (s[i] == 'V' && prev == 'I'){ 
                num += 3;
                prev = s[i];
            }
            else if (s[i] == 'V'){
                num += 5;
                prev = s[i];
            }
            else if (s[i] == 'X' && prev == 'I'){
                num += 8;
                prev = s[i];
            }
            else if (s[i] == 'X'){
                num += 10;
                prev = s[i];
            }
            else if (s[i] == 'L' && prev == 'X'){
                num += 30;
                prev = s[i];
            }
            else if (s[i] == 'L'){
                num += 50;
                prev = s[i];
            }
            else if (s[i] == 'C' && prev == 'X'){
                num += 80;
                prev = s[i];
            }
            else if (s[i] == 'C'){
                num += 100;
                prev = s[i];
            }
            else if (s[i] == 'D' && prev == 'C'){
                num += 300;
                prev = s[i];
            }
            else if (s[i] == 'D'){
                num += 500;
                prev = s[i];
            }
            else if (s[i] == 'M' && prev == 'C'){
                num += 800;
                prev = s[i];
            }
            else if (s[i] == 'M'){
                num += 1000;
                prev = s[i];
            }
        }
        
        return num;
    }
};
