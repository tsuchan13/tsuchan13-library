# このライブラリについて
このライブラリは<a href="https://atcoder.jp/users/tsuchan13">tsuchan13</a>(緑コーダー)がAtcoderで使っているライブラリです。
# ライブラリの内容
このライブラリには`main.py`と2つのフォルダーで構成されています。
## <a href='https://github.com/tsuchan13/tsuchan13-library/blob/main/main.py'>main.py</a>
main.pyは全てのプログラム共通のテンプレートです。
入力関連の関数やライブラリのimport等が書いてあります。
バンバンしてるAAは個人的なお気に入り。
昔は┌(^o^┐)┐こいつがいた。
## <a href='https://github.com/tsuchan13/tsuchan13-library/tree/main/Library'>Library</a>
Libraryフォルダーには何かを判定するプログラムやデータ構造などがあります。
### <a href='https://github.com/tsuchan13/tsuchan13-library/blob/main/Library/is_prime.py'>is_prime.py</a>
名前の通り素数を判定するプログラムです。
計算量は`O(√N)`です。
### <a href='https://github.com/tsuchan13/tsuchan13-library/blob/main/Library/runlength.py'>runlength.py</a>
ランレングス圧縮(名前覚えられない)を実行・復号するプログラムです。
計算量は`O(N)`です。
### <a href='https://github.com/tsuchan13/tsuchan13-library/blob/main/Library/zaatsu.py'>zaatsu.py</a>
座標圧縮をするプログラムです。
計算量は`O(N)`です。
### <a href='https://github.com/tsuchan13/tsuchan13-library/blob/main/Library/UnionFind.py'>UnionFind.py</a>
UnionFindのライブラリです。
いまだに逆アッカーマン関数のことをよくわかっていませんが、
計算量は`α(n)`らしいです。
### <a href='https://github.com/tsuchan13/tsuchan13-library/blob/main/Library/comb.py'>comb.py</a>
逆元を利用してnCr mod p をすることができます。
計算量は分かりません(確かO(log n))が速いのでOKです。
### <a href='https://github.com/tsuchan13/tsuchan13-library/blob/main/Library/group.py'>group.py</a>
n個の要素を持つlistが与えられた時に幾つかのlistに分割してくれるやつです。
計算量はO(B(n))です。(だいたいn<=12くらいまでなら間に合うはず。)
ChatGPTに作らせました。
### <a href='https://github.com/tsuchan13/tsuchan13-library/blob/main/Library/is_sqrt.py'>is_sqrt.py</a>
平方数かどうか判定するライブラリです。
計算量はO(log n)です。
内部で二分探索しているようです。
### <a href='https://github.com/tsuchan13/tsuchan13-library/blob/main/Library/soinsubunkai.py'>soinsubunkai.py</a>
素因数分解してくれるライブラリです。
素因数分解の英語ってなんなんだろう。
計算量は`O(√N)`です。
たまに使うけどACはできない
### <a href='https://github.com/tsuchan13/tsuchan13-library/blob/main/Library/treap.py'>treap.py</a>
二分探索木です。ChatGPTとなんやかんや言いながら作りました。(group.pyと違って丸投げはしなかった。えらい。)
大体の操作がO(log n)で高速な代わりに作成するのに貴重な祝日を失った。
main.pyにも入ってる。
重複ありと重複なしを切り替えられる上にコードが短い。


