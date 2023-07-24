### Unit testing with Pytest 

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
```