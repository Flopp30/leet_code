# You have a chat log of n messages. You are given two string arrays messages
# and senders where messages[i] is a message sent by senders[i].
#
# A message is list of words that are separated by a single space with no leading or trailing spaces.
# The word count of a sender is the total number of words sent by the sender.
# Note that a sender may send more than one message.
#
# Return the sender with the largest word count. If there is more than one sender
# with the largest word count, return the one with the lexicographically largest name.

class Solution:
    def largestWordCount(self, messages: list[str], senders: list[str]) -> str:
        glossary = {}
        for i, sender in enumerate(senders):
            if sender not in glossary:
                glossary[sender] = ''
            glossary[sender] += messages[i] + ' '
        for key, value in glossary.items():
            glossary[key] = len(list(value.split(' '))) - 1
        glossary = dict(sorted(glossary.items(), key=lambda x: x[0]))
        max_len_name, temp_val = glossary.popitem()
        for key, value in glossary.items():
            if value > temp_val:
                temp_val = value
                max_len_name = key
            if len(max_len_name) < len(key) and value == temp_val:
                max_len_name = key
        return max_len_name

a = Solution()
messages = ["Hello userTwooo", "Hi userThree", "Wonderful day Alice", "Nice day userThree"]
senders = ["Alice", "userTwo", "userThree", "Alice"]
print(a.largestWordCount(messages, senders))
