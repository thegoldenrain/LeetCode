class Solution {
public:
    vector<string> fizzBuzz(int n) 
    {
        vector<string> li;
        
        for(int i = 1; i <= n; i++)
        {
            if ((i % 5 == 0) && (i % 3 == 0))
                li.push_back("FizzBuzz");
            else if (i % 5 == 0)
                li.push_back("Buzz");
            else if (i % 3 == 0)
                li.push_back("Fizz");
            else
                li.push_back(to_string(i));
        }
        
        return li;
    }
};
