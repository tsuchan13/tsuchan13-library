#ランレングス圧縮
def runLengthEncode(S: str):
    grouped = groupby(S) # type: ignore # from collections import groupby
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

#ランレングス圧縮復号
def runLengthDecode(L):
    res = ""
    for c, n in L:
        res += c * int(n)
    return res