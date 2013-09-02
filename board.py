class Board:
  def __init__(self, trie, letter_points, letters, bonuses):
    """Initializes a SWF board instance containing a trie of dictionary words,
    a dictionary containing default letter tile scores, an array of array
    of letter tiles on the board, and an array of array of bonus tiles.
    Bonuses can take on the values '2L', '2W', '3L', '3W'."""
    self.trie = trie
    self.letter_points = letter_points
    self.letters = self._adjustLetters(letters)
    self.bonuses = bonuses
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
    (i, j, word/prefix, current word/prefix score, tile chain)"""
    letter = self.letters[i][j]
    stack = [(i, j, letter, self.letter_points[letter], [(i, j)])] # initialize with the first tile

    while len(stack) != 0:
      curr_i, curr_j, curr_s, curr_p, curr_c = stack.pop() # current i, j, prefix, points, chain

      if self.trie.containsWord(curr_s):
        self._updateResultsDict(resultsDict, curr_s, curr_p)

      for ii in range(curr_i - 1, curr_i + 2):
        for jj in range(curr_j - 1, curr_j + 2):
          if (ii, jj) != (curr_i, curr_j) and ii >= 0 and ii < 4 and jj >= 0 and jj < 4 \
          and (ii, jj) not in curr_c:
            new_letter = self.letters[ii][jj]
            new_s = curr_s + new_letter

            points_delta = self.letter_points[new_letter]
            bonus_tile = self.bonuses[ii][jj]
            if bonus_tile == '2L':
              points_delta *= 2
            elif bonus_tile == '3L':
              points_delta *= 3
            new_p = curr_p + points_delta

            if self.trie.containsPrefix(new_s):
              stack.append((ii, jj, new_s, new_p, curr_c + [(ii, jj)]))

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
