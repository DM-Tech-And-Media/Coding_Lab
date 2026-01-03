# 徒然草の一部（例）
text = """
つれづれなるままに、日くらし、硯にむかひて、心にうつりゆくよしなしごとを、
そこはかとなく書きつくれば、あやしうこそものぐるほしけれ。
"""

# ① 全体の文字数
length = len(text)

# ② 「心」という語がいくつあるか
count_kokoro = text.count("心")

# ③ 読点で区切って文ごとにリスト化
sentences = text.split("、")

# ④ ミニゲーム：ランダムに一文を表示
import random
quiz = random.choice(sentences)

print("【文字数】", length)
print("【「心」の出現回数】", count_kokoro)
print("【文のリスト】", sentences)
print("【クイズ：この文の次は？】", quiz)


# 正解①：count() を使う方法（最も基本）
text = "つれづれなるままに、心にうつりゆくよしなしごとを"
count = text.count("心")
print(count)

# 正解②：split() と len() を組み合わせる方法
text = "心の中にある心を考える"
parts = text.split("心")
count = len(parts) - 1
print(count)

# 正解③：for 文を使って1文字ずつ調べる方法
text = "心に心を重ねる"
count = 0

for c in text:
    if c == "心":
        count += 1

print(count)

# 正解④（発展）：辞書（dictionary）で数える方法
text = "心に心を映す心"
result = {}

for c in text:
    if c in result:
        result[c] += 1
    else:
        result[c] = 1

print(result["心"])


