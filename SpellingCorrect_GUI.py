import sys
from PyQt5.QtWidgets import *
import re, collections
# class Example
def words(text): return re.findall('[a-z]+', text.lower())
#读入big.txt并将所有单词转换成小写的函数。
def train(features):#计算每个单词出现的频率的函数。
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1#最少为出现一次。
    return model
NWORDS = train(words(open('big.txt').read()))#打开并读入big.txt并将所有单词转换成小写。
alphabet = 'abcdefghijklmnopqrstuvwxyz'
#字母表
def edits1(word):#执行计算编辑距离为1.动态规划，时间复杂度为O（M*N）；
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)
def known_edits2(word):#执行计算编辑距离为2.利用编辑距离为1的基础上；
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)
#同时还可能有编辑距离为0次的即本身就拼写正确的。
def known(words): return set(w for w in words if w in NWORDS)
def correct(word):#假设编辑距离1次的概率远大于2次的，0次的远大于1次的。
                  #通过correct函数先选择编辑距离最小的单词
                 # 其对应的概率就会越大，作为候选单词集，
                 # 再选择概率最大的那个单词作为拼写建议。
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=NWORDS.get)

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.left = 30
        self.top = 30
        self.width = 440
        self.height = 280
        self.InitUI()

    def InitUI(self):
        self.btn = QPushButton("输入一个词语", self)
        self.btn.move(50, 20)
        self.btn.clicked.connect(self.ShowDialog)

        self.le = QLineEdit("正确词语在这里显示！",self)
        self.le.move(130, 22)

        self.setWindowTitle("SpellingCorrect app")
        self.show()

    def ShowDialog(self):
        text, ok = QInputDialog.getText(self, "Input one word!", "Enter your word here！:")

        if ok:
            self.le.setText("正确写法："+str(correct(text)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
