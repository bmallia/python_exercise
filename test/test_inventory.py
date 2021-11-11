import pytest

from source.inventory import updateInventory

def test_update_inventory_sequence_1_length():
   curr_inv = [[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]] 
   new_inv = [[2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"], [7, "Toothpaste"]]
   result_arr = updateInventory(curr_inv, new_inv) 
   assert len(result_arr) == 6

def test_update_inventory_sequence_2():
   curr_inv = [[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]]
   new_inv = [[2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"], [7, "Toothpaste"]]
   result_arr = updateInventory(curr_inv, new_inv)
   assert result_arr == [[88, "Bowling Ball"], [2, "Dirty Sock"], [3, "Hair Pin"], [3, "Half-Eaten Apple"], [5, "Microphone"], [7, "Toothpaste"]]

def test_update_inventory_sequence_3():
   curr_inv = [[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]]
   new_inv =  []
   result_arr = updateInventory(curr_inv, new_inv)
   assert result_arr == [[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]]

def test_update_inventory_sequence_4():
   curr_inv = []
   new_inv = [[2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"], [7, "Toothpaste"]]
   result_arr = updateInventory(curr_inv, new_inv)
   assert result_arr == [[67, "Bowling Ball"], [2, "Hair Pin"], [3, "Half-Eaten Apple"], [7, "Toothpaste"]]

def test_update_inventory_sequence_5():
   curr_inv = [[0, "Bowling Ball"], [0, "Dirty Sock"], [0, "Hair Pin"], [0, "Microphone"]]
   new_inv = [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]
   result_arr = updateInventory(curr_inv, new_inv)
   assert result_arr == [[1, "Bowling Ball"], [0, "Dirty Sock"], [1, "Hair Pin"], [1, "Half-Eaten Apple"], [0, "Microphone"], [1, "Toothpaste"]]