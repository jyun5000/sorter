from sorter import sorter

def test_sorter_standard():
    assert sorter(10, 10, 10, 5) == "STANDARD"
    assert sorter(50, 50, 50, 10) == "STANDARD"

def test_sorter_rejected():
    assert sorter(250, 250, 250, 250) == "REJECTED"
    assert sorter(150, 150, 150, 20) == "REJECTED" 

def test_sorter_special():
    assert sorter(150, 10, 10, 5) == "SPECIAL" 
    assert sorter(10, 10, 10, 20) == "SPECIAL"



