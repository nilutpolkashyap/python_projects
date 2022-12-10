import pytest
from lib.greeting import greeting

class Test_Greeting:

    def test_greet(self):
        greet = greeting('Nilutpol')
        assert greet == 'Hello Nilutpol'