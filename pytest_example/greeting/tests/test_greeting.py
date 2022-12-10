import pytest
from lib.greeting import greeting

class Test_Greeting:

    def test_greet(self):
        greet = greeting('Nilutpol')
        assert greet == 'Hello Nilutpol'

    def test_greet2(self):
        greet = greeting('You')
        assert greet == 'Hello You'