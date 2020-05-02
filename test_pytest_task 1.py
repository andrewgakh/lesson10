'''
import pytest
from play_card import Cards

class TestCards_pytest:

    def  setup(self):
        self.card_game = Cards()
        #self.card_game = Cards()
        self.card_game.mix_koloda()
        self.card_game.give_cards()
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

    # Тестируем ф-цию mix_koloda()
    def test_mix_koloda(self):
        #self.card_game.mix_koloda()
        assert self.card_game.koloda_play != [['6','B', 6], ['6', 'C', 6], ['6', 'T', 6], ['6', 'P', 6],
                       ['7', 'B', 7], ['7', 'C', 7], ['7', 'T', 7], ['7', 'P', 7],
                       ['8', 'B', 8], ['8', 'C', 8], ['8', 'T', 8], ['8', 'P', 8],
                       ['9', 'B', 9], ['9', 'C', 9], ['7', 'T', 9], ['9', 'P', 9],
                       ['10', 'B', 10], ['10', 'C', 10], ['10', 'T', 10], ['10', 'P', 10],
                       ['J', 'B', 11], ['J', 'C', 11], ['J', 'T', 11], ['J', 'P', 11],
                       ['Q', 'B', 12], ['Q', 'C', 12], ['Q', 'T', 12], ['Q', 'P', 12],
                       ['K', 'B', 13], ['K', 'C', 13], ['K', 'T', 13], ['K', 'P', 13],
                       ['A', 'B', 14], ['A', 'C', 14], ['A', 'T', 14], ['A', 'P', 14]]

    # Тестируем ф-цию give_cards()
    def test_give_cards(self):
        #self.card_game.give_cards()
        assert len(self.card_game.cards_player1) == 6
        assert len(self.card_game.cards_player2) == 6

    # Тестируем ф-цию hod_plr_1()
    def test_hod_plr_1(self):
        self.card_game.hod_plr_1()
        assert self.card_game.pole_plr_1 !=''
        assert self.card_game.pole_plr_2 == []

    # # Тестируем ф-цию otbil_plr_2
    # def test_otbil_plr_2(self):
    #     self.card_game.kozyr = ['Q', 'P', 12]
    #     self.card_game.cards_player2 = [['Q', 'B', 12], ['9', 'P', 9], ['J', 'B', 11], ['6', 'B', 6], ['7', 'P', 7], ['K', 'B', 13]]
    #     self.card_game.cards_player1 = [['8', 'B', 8], ['10', 'B', 10], ['K', 'T', 13], ['A', 'P', 14], ['6', 'T', 6]]
    #     self.card_game.pole_plr_1 = ['9', 'C', 9]
    #     assert self.card_game.win_plr_2 == 0
    #     assert self.card_game.min_koz == [['7', 'P', 7]]
'''