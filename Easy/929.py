from typing import List, Set


class Solution:
    
    def numUniqueEmails(self, emails: List[str]) -> int:
        domain_names = []
        for i in range(len(emails)):
            domain_names.append(emails[i].split('@', 1)[1])
            emails[i] = emails[i].split('@', 1)[0]
            emails[i] = emails[i].split('+', 1)[0]

        print(domain_names)
        print(emails)
        result_set = set()
        for i, email in enumerate(emails):
            unique_email = email.replace('.', '') + '@' + domain_names[i]
            result_set.add(unique_email)

        return len(result_set)

        
test = Solution()
print(test.numUniqueEmails(["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]))