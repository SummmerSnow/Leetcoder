/
***
题目描述：
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

For example, given s ="aab",
Return
  [
    ["aa","b"],
    ["a","a","b"]
  ]

***
/





// solution:
class Solution {
public:
    
    bool palindrome(string s)
    {
        // s.rbegin 和 s.rend() 表示反转字符串的两个指针
        return s == string(s.rbegin(), s.rend());
    }
    
    void dfs(string s, vector<string> current, vector<vector<string>> &result)
    {
        if(s == "")
        {
            result.push_back(current);
            return;
        }
        for(int i = 1; i <= s.size(); i++)
        {
            string temp = s.substr(0, i);
            if (palindrome(temp))
            {
                current.push_back(temp);
                dfs(s.substr(i, s.size()-i), current, result);
                current.pop_back();
            }
        }
    }
public:
    vector<vector<string>> partition(string s) {
        vector<string> current;
        vector<vector<string>> result;
        dfs(s, current, result);
        
        return result;
    }
};
