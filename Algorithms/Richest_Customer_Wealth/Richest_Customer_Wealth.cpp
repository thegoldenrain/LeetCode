class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int wealthiest = 0;
        
        for(int i = 0; i < accounts.size(); i++)
        {
            int wealth = 0;
            
            for(int x = 0; x < accounts[i].size(); x++)
                wealth += accounts[i][x];
            
            if(wealth > wealthiest)
                wealthiest = wealth;
            
        }
        
        return wealthiest;
    }
};
