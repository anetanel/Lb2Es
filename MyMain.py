import sys

import dateutil.parser
from lxml import etree

tree = etree.parse(sys.argv[1])
root = tree.getroot()

newRoot = etree.Element('gameList')

for game in root.iter('Game'):
    newGame = etree.SubElement(newRoot, 'game')

    newGamePath = etree.SubElement(newGame, 'path')
    newGamePath.text = './' + game.find('ApplicationPath').text.rsplit('\\')[-1]

    newGameName = etree.SubElement(newGame, 'name')
    newGameName.text = game.find('Title').text

    newGameDesc = etree.SubElement(newGame, 'desc')
    newGameDesc.text = game.find('Notes').text

    newGameDeveloper = etree.SubElement(newGame, 'developer')
    newGameDeveloper.text = game.find('Developer').text

    newGamePublisher = etree.SubElement(newGame, 'publisher')
    newGamePublisher.text = game.find('Publisher').text

    newGameGenre = etree.SubElement(newGame, 'genre')
    newGameGenre.text = game.find('Genre').text

    newGameReleaseDate = etree.SubElement(newGame, 'releasedate')
    newGameReleaseDate.text = dateutil.parser.parse(game.find('ReleaseDate').text).strftime('%Y%m%dT000000')

    newGameRating = etree.SubElement(newGame, 'rating')
    newGameRating.text = str(float(game.find('CommunityStarRating').text) / 10)

    newGamePlayers = etree.SubElement(newGame, 'players')
    newGamePlayers.text = '1' if 'Single' in game.find('PlayMode').text else '2'

outfile = open(sys.argv[2], 'w')
outfile.write(etree.tostring(newRoot, method='xml', pretty_print=True).decode())
outfile.close()
