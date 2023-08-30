Feature: Testing api.myweb.com

  Scenario: API admin users can get a list of users
    Given I am logged as admin
    When I request API GET api/v1/users
    Then I get HTTP 200 status code
    And I get JSON in response body
    And the HTTP response body contains a page with 4 users
    And 1 of them is Administrator
