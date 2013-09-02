from board import *
from trie import *

def loadWords(filepath):
  trie = Trie()
  trie.importWords(filepath)
  return trie

def loadLetterPoints(filepath):
  letter_points = {}
  for raw_line in open(filepath, 'r'):
    line = raw_line.strip(' ').strip('\n')
    letter, raw_points = line.split(',')
    points = int(raw_points)
    letter_points[letter] = points
  return letter_points

if __name__ == '__main__':
  print 'Loading dictionary of words...'
  trie = loadWords('./dictionary.txt')
  print 'Dictionary loaded!\n'

  print 'Loading points for letters...'
  letter_points = loadLetterPoints('./letter_points.txt')
  print 'Letter points loaded!\n'

  # # prompt user for letters on board
  # raw = raw_input("Please enter the SWF board as follows: " \
  #   + "xxxx;xxxx;xxxx;xxxx\n")
  # lines = raw.strip(' ').split(';')
  # letters = [[letter.upper() for letter in line] for line in lines]

  # # prompt user for bonuses on board
  # raw = raw_input("Please enter word/letter bonuses as follows: " \
  #   + "x,x,x,x;x,x,x,x;x,x,x,x;x,x,x,x. Accepted values for x are: " \
  #   + "'2L', '3L', '2W', '3W', ''.")
  # lines = raw.strip(' ').split(';')
  # bonuses = [[bonus for bonus in line.split(',')] for line in lines]

  letters = [['T','H','G','E'],
             ['R','H','N','S'],
             ['S','I','A','E'],
             ['P','L','X','R']]

  bonuses = [['','3W','','3L'],
             ['3L','','',''],
             ['3L','','',''],
             ['','','','']]

  board = Board(trie, letter_points, letters, bonuses)
  board.solve()
  results = board.getResults()

  max_points = sum([points for (word, points) in results])

  print results, "%d words" % len(results), "%d max points" % max_points