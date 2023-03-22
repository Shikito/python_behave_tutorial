Feature: Caluculator
    As a user
    I want to use a calculator to add numbers
    So that I can get the correct result

    Scenario: Add two numbers
        Given I have a calculator
        When I input "2" and "3" and press add
        Then I should get "5" as the result

