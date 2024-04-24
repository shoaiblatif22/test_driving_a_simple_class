from lib.most_often import *

def test_passing_in_a_list():
    new_list = [1, 2, 3]
    mostOften = MostOften(new_list)
    assert mostOften.starting_list == new_list

def test_add_new_item_to_a_list():
    new_list = [1, 2, 3]
    mostOften = MostOften(new_list)
    mostOften.add_new(4)
    assert mostOften.starting_list == [1, 2, 3, 4]

def test_getting_the_most_items_in_a_list():
    new_list = [1, 1, 1, 2, 2, 5, 6, 8]
    mostOften = MostOften(new_list)
    assert mostOften.get_most_often() == 1

def test_no_clear_winner():
    new_list = [1, 1, 2, 2, 3]
    mostOften = MostOften(new_list)
    assert mostOften.get_most_often() == "no clear winner"

def test_no_clear_winner_two():
    new_list = [1, 1, 2, 2, 3, 3]
    mostOften = MostOften(new_list)
    assert mostOften.get_most_often() == "no clear winner"

def test_side_effects():
    list = [1]
    instance = MostOften(list)
    list.append('a') #Code here is being directly
    expected = 1
    actual = instance.get_most_often()
    assert actual == expected

    '''
    
    '''