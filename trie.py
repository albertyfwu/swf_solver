class Trie:
  def __init__(self):
    self.children = {}
    self.isWord = False

  def importWords(self, filepath):
    """Given a filepath to a file of words separated by newlines,
    adds all the words to the trie.""" 
    for raw_word in open(filepath, 'r'):
      word = raw_word.strip(' ').strip('\n').upper()
      self.add(word)

  def add(self, s):
    """Add the string `s` in this subtree."""
    head, tail = s[0], s[1:]
    if head not in self.children:
      self.children[head] = Trie()
    next_node = self.children[head]
    if not tail: # no further recursion
      next_node.isWord = True
    else:
      self.children[head].add(tail)

  def containsWord(self, s):
    """Returns true if the string `s` is contained
    in the trie."""
    if not s:
      return self.isWord
    head, tail = s[0], s[1:]
    if head not in self.children:
      return False
    next_node = self.children[head]
    return next_node.containsWord(tail)

  def containsPrefix(self, s):
    """Check whether the given string `s` is a prefix of
    some member string."""
    if not s:
      return True
    head, tail = s[0], s[1:]
    if head not in self.children:
      return False
    next_node = self.children[head]
    return next_node.containsPrefix(tail)
