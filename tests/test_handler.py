import pytest
from handler import hello
from expects import expect, be, equal, isinstance


class TestHandler:
    def test_event_failsWithNumberAsEvent(self):
        response = hello(1, 2)
        expect(response.get('statusCode')).to(equal(200))
        expect(isinstance(response.get('body'))).to(be(str))
