import pytest
from play_card import Cards

class TestCards_pytest:

    def  setup(self):
        self.card_game = Cards()
        print('Start test!')

    def teardown(self):
        #self.dice_game.current_throw = 0
        print('Test completed!')

    def test_init(self):
        assert self.card_game.koloda == [['6','B', 6], ['6', 'C', 6], ['6', 'T', 6], ['6', 'P', 6],
                       ['7', 'B', 7], ['7', 'C', 7], ['7', 'T', 7], ['7', 'P', 7],
                       ['8', 'B', 8], ['8', 'C', 8], ['8', 'T', 8], ['8', 'P', 8],
                       ['9', 'B', 9], ['9', 'C', 9], ['7', 'T', 9], ['9', 'P', 9],
                       ['10', 'B', 10], ['10', 'C', 10], ['10', 'T', 10], ['10', 'P', 10],
                       ['J', 'B', 11], ['J', 'C', 11], ['J', 'T', 11], ['J', 'P', 11],
                       ['Q', 'B', 12], ['Q', 'C', 12], ['Q', 'T', 12], ['Q', 'P', 12],
                       ['K', 'B', 13], ['K', 'C', 13], ['K', 'T', 13], ['K', 'P', 13],
                       ['A', 'B', 14], ['A', 'C', 14], ['A', 'T', 14], ['A', 'P', 14]]
        assert self.card_game.koloda_play != []
    