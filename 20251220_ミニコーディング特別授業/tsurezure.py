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