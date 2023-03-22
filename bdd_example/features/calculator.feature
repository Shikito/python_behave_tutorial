Feature: Calculator
    I'm a user of calculator.
    I want to add / sub some numbers.
    I want to get correct result by using calculator.

    Scenario: Add two numbers
        Given I have a calculator
        When I input "2" and "3" and press add
        Then I should get "5" as the result

