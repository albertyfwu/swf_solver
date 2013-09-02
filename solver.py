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

  # prompt user for letters on board
  # raw = raw_input("Please enter the SWF board as follows: " \
  #   + "xxxx xxxx xxxx xxxx\n")
  # lines = raw.strip(' ').split(' ')
  # letters = [[letter.upper() for letter in line] for line in lines]

  letters = [['C', 'O', 'Q', 'Z'],
             ['N', 'S', 'I', 'D'],
             ['T', 'A', 'O', 'N'],
             ['G', 'N', 'I', 'T']]

  board = Board(trie, letter_points, letters)
  board.solve()
  board.sortResults()
  board.dispResults()
