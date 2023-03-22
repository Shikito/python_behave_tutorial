from behave import given, when, then
from calculator import Calculator

@given('I have a calculator')
def step_given_have_calculator(context):
    context.calculator = Calculator()

@when('I input "{num1:d}" and "{num2:d}" and press add')
def step_when_input_numbers_and_press_add(context, num1: int, num2: int):
    context.result = context.calculator.add(num1, num2)

@then('I should get "{expected_result:d}" as the result')
def step_then_get_result(context, expected_result: int):
    assert context.result == int(expected_result), \
        f"Expected {expected_result}, but got {context.result}"
