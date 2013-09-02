from board import *
from trie import *

def loadWords(filepath):
  trie = Trie(isRoot=True, cacheOn=True)
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

def loadWordLengthPoints(filepath):
  word_length_points = {}
  for raw_line in open(filepath, 'r'):
    line = raw_line.strip(' ').strip('\n')
    raw_length, raw_points = line.split(',')
    length = int(raw_length)
    points = int(raw_points)
    word_length_points[length] = points
  return word_length_points

if __name__ == '__main__':
  print '\nLoading dictionary of words...'
  trie = loadWords('./dictionary.txt')
  print 'Dictionary loaded!'

  print '\nLoading points for letters...'
  letter_points = loadLetterPoints('./letter_points.txt')
  print 'Letter points loaded!'

  print '\nLoading points for word lengths...'
  word_length_points = loadWordLengthPoints('./word_length_points.txt')
  print 'Word length points loaded!'

  while True:
    # prompt user for letters on board
    raw = raw_input("\nPlease enter the SWF board as follows: " \
      + "xxxx;xxxx;xxxx;xxxx\n")
    lines = raw.strip(' ').split(';')
    letters = [[letter.upper() for letter in line] for line in lines]

    # prompt user for bonuses on board
    raw = raw_input("\nPlease enter word/letter bonuses as follows: " \
      + "x,x,x,x;x,x,x,x;x,x,x,x;x,x,x,x.\n" \
      + "Accepted values for x are (without quotes): '2L', '3L', '2W', '3W', ''.\n")
    lines = raw.strip(' ').split(';')
    bonuses = [[bonus.strip(' ').upper() for bonus in line.split(',')] for line in lines]

    # letters = [['T','H','G','E'],
    #            ['R','H','N','S'],
    #            ['S','I','A','E'],
    #            ['P','L','X','R']]

    # bonuses = [['','3W','','3L'],
    #            ['3L','','',''],
    #            ['3L','','',''],
    #            ['','','','']]

    board = Board(trie, letter_points, word_length_points, letters, bonuses)
    board.solve()
    board.printSummary()
