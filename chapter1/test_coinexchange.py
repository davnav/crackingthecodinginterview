from coinexchange import minDenominationsDP
def test_coin():
    coins = [1,5,6,9]
    # assert minDenominationsDP(coins,10) == 2
    assert minDenominationsDP(coins,30) == 4 
    # assert minDenominationsDP(coins,27) == 4

def test_coin_edge_case():
    coins = [1,5,6,9]
    assert minDenominationsDP(coins,9) == 1  

def test_coin_zero_case():
    coins = [1,5,6,9]
    assert minDenominationsDP(coins,0) == 0  

if __name__ == "__main__":
    test_coin()
    test_coin_edge_case()
    test_coin_zero_case()
    print("everything is passed")