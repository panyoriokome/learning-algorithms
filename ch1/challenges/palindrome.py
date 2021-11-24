def is_palindrome1(w):
  """Create slice with negative step and confirm equality with w."""
  return w[::-1] == w

def is_palindrome2(w):
  """Strip outermost characters if same, return false when mismatch."""
  while len(w) > 1:
    if w[0] != w[-1]:     # if mismatch, return False
      return False
    w = w[1:-1]           # strip characters on either end; repeat

  return True             # must have been palindrome

print(is_palindrome1('A man, a plan, a canal. Panama!'))


test1 = 'madam'
test2 = 'A man, a plan, a canal. Panama!'

def is_palindrome3(w):
    """空白や記号にも対応したバージョン
    """
    import re
    code_regex = re.compile('[!"#$%&\'\\\\()*+,-./:;<=>?@[\\]^_`{|}~「」〔〕“”〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥％]')
    # 小文字に変換
    w = w.lower()
    # 空白を削除
    w = w.replace(' ', '')
    # 記号を削除
    w = code_regex.sub('', w)

    result =  ''.join(reversed(w))
    if result == w:
        result = True
    else:
        result = False

    return result

print(is_palindrome3(test1))
print(is_palindrome3(test2))