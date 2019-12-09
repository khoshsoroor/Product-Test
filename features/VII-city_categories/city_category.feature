Feature:Test city_category R


  Scenario: Return category from city
    When Get list of categories for city karaj
    Then return code city categories must be 200


  Scenario: not found any category from city
    When Get categories for a city tehran
    Then result code for category city must be 404