class Board:
  def __init__(self, trie, letter_points, letters):
    """Initializes a SWF board instance containing a trie of dictionary words,
    a dictionary containing default letter tile scores, and an array of array
    of letter tiles on the board."""
    self.trie = trie
    self.letter_points = letter_points
    self.letters = self._adjustLetters(letters)
    self.results = None

  def _adjustLetters(self, letters):
    """Make sure Q tiles are actually represented as QU tiles."""
    for i in xrange(len(letters)):
      for j in xrange(len(letters[i])):
        if letters[i][j] == 'Q':
          letters[i][j] = 'QU'
    return letters

  def solve(self):
    """Starting at each of the 16 tiles on the board, execute a DFS,
    checking for existence of the prefix in `self.trie`. If the word can be
    found, add it to an ongoing set of found words along with its score."""
    print 'Solving...'
    resultsDict = {}
    
    # execute BFS and other algorithms
    for i in xrange(4):
      for j in xrange(4):
        print 'Solving...%d/16 completed' % (4*i+j+1)
        self._solveOneTile(i, j, resultsDict)

    self.results = resultsDict.items() # store results as a list of tuples

  def _solveOneTile(self, i, j, resultsDict):
    """Starting at the given tile, execute a DFS to find words. The elements
    in the DFS stack are tuples of the following form:
    (i, j, word/prefix, current word/prefix score)"""
    letter = self.letters[i][j]
    stack = [(i, j, letter, self.letter_points[letter])] # initialize with the first tile

    # make sure we don't repeat words

    while len(stack) != 0:
      curr_i, curr_j, curr_s, curr_p = stack.pop() # current i, j, prefix, points

      if self.trie.containsWord(curr_s):
        self._updateResultsDict(resultsDict, curr_s, curr_p)

      for ii in range(curr_i - 1, curr_i + 2):
        for jj in range(curr_j - 1, curr_j + 2):
          if (ii, jj) != (curr_i, curr_j) and ii >= 0 and ii < 4 and jj >= 0 and jj < 4:
            new_letter = self.letters[ii][jj]
            new_s = curr_s + new_letter
            new_p = curr_p + self.letter_points[new_letter]
            if self.trie.containsPrefix(new_s):
              stack.append((ii, jj, new_s, new_p))

  def _updateResultsDict(self, resultsDict, word, points):
    if word not in resultsDict:
      resultsDict[word] = points
    elif points > resultsDict[word]:
      resultsDict[word] = points

  def sortResults(self):
    """self.results are in form [(word1, score1), (word2, score2), ...]"""
    self.results.sort(key=lambda (word, score) : score, reverse=True)

  def getResults(self):
    return self.results

  def dispResults(self):
    # for result in self.results:
    #   print result
    print self.results
