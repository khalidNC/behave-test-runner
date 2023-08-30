Feature: Testing myweb.com

  Scenario: Frontend admin users can get a list of users
    Given I am logged as admin frontend
    When I am in Users page
    Then 4 users are listed
    And 1 of them is Admin
