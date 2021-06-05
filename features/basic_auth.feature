@basic-auth
Feature: The-internet basic-auth

  Scenario: Positive auth
    Given User launch the-internet home page with injected http_auth
      | username | password |
      | admin    | admin    |
    When User choose Basic Auth
    Then Positive test message Congratulations! You must have the proper credentials. occurred