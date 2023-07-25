from shopping_cart import ShoppingCart
import pytest 


@pytest.fixture
def cart():
    return ShoppingCart(5)

def test_can_add_item_to_cart(cart):
    cart.add('apple')
    assert cart.size() == 1 

def test_when_item_added_then_cart_contains_item(cart):
    cart.add('apple')
    assert 'apple' in cart.get_items()

def test_when_add_more_than_max_items_should_fail(cart):
    with pytest.raises(OverflowError):
        for _ in range(6):
            cart.add('apple')


def test_can_get_total_price(cart):
    cart.add('apple')
    cart.add('orange')

    price_map = {
        'apple': 1.0,
        'orange':2.0
    }
    
    assert cart.get_total_price(price_map) == 3