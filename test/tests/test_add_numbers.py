from functools import partial
from pytest import fixture
from pytest_bdd import (
    scenario as bdd_scenario,
    given,
    when,
    then,
)

scenario = partial(bdd_scenario, "features/add_numbers.feature")


@scenario("As a user I want to sum 2 numbers")
def test_add():
    """ Add """


@fixture
def result():
    return {}


@given("A number")
def number():
    return 2


@given("Another number")
def another_number():
    return 4


@when("I make the sum")
def when_sum(result, number, another_number):
    from .add import add
    result['result'] = add(number, another_number)


@then("The sum matches")
def sum_matches(result, number, another_number):
    assert result['result'] == (number + another_number)
