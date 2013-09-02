class Board:
  def __init__(self, trie, letter_points, letters, bonuses):
    """Initializes a SWF board instance containing a trie of dictionary words,
    a dictionary containing default letter tile scores, an array of array
    of letter tiles on the board, and an array of array of bonus tiles.
    Bonuses can take on the values '2L', '2W', '3L', '3W'."""
    self.trie = trie
    self.letter_points = letter_points
    self.letters = self._adjustLetters(letters)
    self.letter_bonuses = None
    self.word_bonuses = None
    self._construct_bonuses(bonuses)
    self.results = None

  def solve(self):
    """Starting at each of the 16 tiles on the board, execute a DFS,
    checking for existence of the prefix in `self.trie`. If the word can be
    found, add it to an ongoing set of found words along with its score."""
    print '\nSolving',
    resultsDict = {}
    progress = 0 # for progress bar
   
    # initialize stack
    stack = []
    for i in xrange(4):
      for j in xrange(4):
        letter = self.letters[i][j]
        stack.append((i, j, letter, self.letter_points[letter], [(i, j)], 1))

    while len(stack) != 0:
      if len(stack) == 16 - progress: # for progress bar
        print '.',
        progress += 1

      # current i, j, prefix, points, chain, word bonus
      curr_i, curr_j, curr_s, curr_p, curr_c, curr_w = stack.pop()

      if self.trie.containsWord(curr_s):
        self._updateResultsDict(resultsDict, curr_s, curr_p * curr_w)

      for ii in range(curr_i - 1, curr_i + 2):
        for jj in range(curr_j - 1, curr_j + 2):
          if (ii, jj) != (curr_i, curr_j) and ii >= 0 and ii < 4 and jj >= 0 and jj < 4 \
          and (ii, jj) not in curr_c:
            new_letter = self.letters[ii][jj]

            new_s = curr_s + new_letter
            new_p = curr_p + self.letter_points[new_letter] * self.letter_bonuses[ii][jj]
            new_c = curr_c + [(ii, jj)]
            new_w = curr_w * self.word_bonuses[ii][jj]

            if self.trie.containsPrefix(new_s):
              stack.append((ii, jj, new_s, new_p, new_c, new_w))

    # store results as a list of tuples
    self.results = sorted(resultsDict.items(), key=lambda (word, score) : score, reverse=True)
    print 'done!'

  def getResults(self):
    """Returns a list of (word, points) results."""
    return self.results

  def printSummary(self):
    """Prints a summary of results, number of words, max number of points."""
    max_points = sum([points for (word, points) in self.results])
    print 'Possible words and scores:'
    print self.results
    print '%d words' % len(self.results)
    print '%d max points' % max_points

  def _updateResultsDict(self, resultsDict, word, points):
    """Updates word:points mapping with new points value."""
    if word not in resultsDict:
      resultsDict[word] = points
    elif points > resultsDict[word]:
      resultsDict[word] = points

  def _adjustLetters(self, letters):
    """Make sure Q tiles are actually represented as QU tiles."""
    for i in xrange(len(letters)):
      for j in xrange(len(letters[i])):
        if letters[i][j] == 'Q':
          letters[i][j] = 'QU'
    return letters

  def _construct_bonuses(self, bonuses):
    """Given an array of arrays of values '2L', '2W', '3L', '3W',
    update letter_bonuses and word_bonuses."""
    self.letter_bonuses = []
    self.word_bonuses = []

    for i in xrange(4):
      letter_bonus_row = []
      word_bonus_row = []

      for j in xrange(4):
        word_bonus = 1
        letter_bonus = 1
        bonus_tile = bonuses[i][j]
        if bonus_tile == '2L':
          letter_bonus = 2
        elif bonus_tile == '3L':
          letter_bonus = 3
        elif bonus_tile == '2W':
          word_bonus = 2
        elif bonus_tile == '3W':
          word_bonus = 3

        letter_bonus_row.append(letter_bonus)
        word_bonus_row.append(word_bonus)

      self.letter_bonuses.append(letter_bonus_row)
      self.word_bonuses.append(word_bonus_row)
