"""
LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！
“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,
并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。
LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。
为了方便起见,你可以认为大小王是0。
"""


class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers or len(numbers) == 0:
            return False
        transdict = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
        for i in range(len(numbers)):
            if numbers[i] in transdict.keys():
                numbers[i] = transdict[numbers[i]]

        numbers = sorted(numbers)
        number_0 = 0
        number_gap = 0

        i = 0
        while i < len(numbers) and numbers[i] == 0:
            number_0 += 1
            i += 1

        front = number_0
        behind = front + 1
        while behind < len(numbers):
            if numbers[front] == numbers[behind]:
                return False
            number_gap += numbers[behind] - numbers[front] - 1
            front = behind
            behind += 1
        return False if number_gap > number_0 else True
