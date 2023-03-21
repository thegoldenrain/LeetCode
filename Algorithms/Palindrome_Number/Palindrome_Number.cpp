class Solution {
public:
    bool isPalindrome(int x) {
        string s = to_string(x);     
        int i = 0;
        int last = s.length() - 1;

        while(i < (s.length() / 2))
        {
            if (s[i] == s[last - i]){   
                i++;
                continue;
            }
            else
                return 0;
        }

        return 1;
    }
};
