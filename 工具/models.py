# 文件相似度的demo
# 导入difflib库
import difflib

# 打开并读取两个文本文件
with open('article_a.txt', 'r', encoding='utf-8') as f:
    a = f.read()
with open('article_b.txt', 'r', encoding='utf-8') as f:
    b = f.read()

# 创建一个SequenceMatcher对象
sm = difflib.SequenceMatcher(None, a, b)

# 计算并打印两篇文章的相似度
similarity = sm.ratio()
print(f'相似度：{similarity:.2f}')

# 创建一个Differ对象
d = difflib.Differ()

# 比较并生成差异报告
diff = d.compare(a.splitlines(), b.splitlines())

# 打印差异报告
print('差异报告：')
for line in diff:
  print(line)