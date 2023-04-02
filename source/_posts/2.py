#要统计的句子
sentence="I like python? no! I hate python? no! I love python!"
# 把! 和? 去掉 ,只统计单词
sentence=sentence.replace('?', '').replace('!', '')
# 按照空格把单词一个个划分
all_word=sentence.split(' ')
# 利用set去重, 
single_word=set(all_word)
# 对于set里面的每一个单词
for word in single_word:
    # 利用列表的函数,统计列表里面有几个
    print(word,all_word.count(word))