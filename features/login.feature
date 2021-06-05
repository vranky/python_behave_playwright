Feature: Sign in feature

  Scenario: Positive Sign In into LTP
    Given User launch home page
    When User fill in credentials
      | user_name               | password  |
      | jeff.harper@test.com | Password |
    And User click on Sign in button
    Then User is signed in with welcome message Welcome back, Jeff
    And User click on userProfile button
    And User click on Log out button

  Scenario Outline: Negative Sign In into LTP
    Given User launch home page
    When User fill in credentials
      | user_name   | password   |
      | <user_name> | <password> |
    And User click on Sign in button
    Then User sign in failed with Invalid username or password.
    Examples:
      | user_name               | password  |
      | m.vranka@haha.com | Password |
      | m.wefas@hehe.com  | Password |