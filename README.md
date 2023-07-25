### Unit testing with Pytest 
https://docs.python.org/3/library/unittest.mock.html 


Preparation:
```bash
$ virtualenv venv
$ source venv/bin/activate
$ pip install pytest
``` 

Run
```bash
$ pytest
$ pytest -v
$ pytest -v -s
$ pytest ./test_shopping_cart.py::test_can_add_item_to_cart

$ pytest ./test_shopping_cart.py::test_can_get_total_price -s
```