import pytest
from play_card import Cards

class TestCards_pytest:

    def  setup(self):
        self.card_game = Cards()
        self.card_game.koloda_play =[['8', 'C', 8], ['Q', 'C', 12], ['7', 'P', 7], ['A', 'P', 14], ['9', 'P', 9],
                                      ['10', 'C', 10], ['A', 'C', 14], ['10', 'B', 10], ['6', 'C', 6], ['9', 'C', 9], ['Q', 'T', 12],
                                      ['Q', 'B', 12], ['10', 'P', 10], ['K', 'C', 13], ['6', 'T', 6], ['6', 'P', 6], ['J', 'P', 11],
                                      ['10', 'T', 10], ['A', 'B', 14], ['7', 'T', 7], ['7', 'C', 7], ['K', 'T', 13], ['9', 'B', 9], ['6', 'B', 6]]
        self.card_game.kozyr = ['Q', 'P', 12]
        self.card_game.cards_player2 = [['Q', 'B', 12], ['9', 'P', 9], ['J', 'B', 11], ['6', 'B', 6], ['7', 'P', 7], ['K', 'B', 13]]
        self.card_game.cards_player1 = [['8', 'B', 8], ['10', 'B', 10], ['K', 'T', 13], ['A', 'P', 14], ['6', 'T', 6]]
        self.card_game.pole_plr_1 = ['9', 'C', 9]

        print('Start test!')

    def teardown(self):
        #self.dice_game.current_throw = 0
        print('Test completed!')

    # # Тестируем ф-цию otbil_plr_2
    def test_otbil_plr_2(self):
        self.card_game.win_plr_2 = 0
        self.card_game.win_plr_1 = 0
        self.card_game.otbil_plr_2()
        print(self.card_game.pole_plr_2)
        assert self.card_game.win_plr_2 == 1
        assert self.card_game.pole_plr_2 == ['7', 'P', 7]