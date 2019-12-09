Feature:Test zones C,R,U,D


  Scenario: Successful add zones
    When adding zones for karaj with info
      | slug    | title  | is_enabled |
      | andishe | اندیشه | true       |
      | marlik  | مارلیک | true       |
      | fardis  | فردیس  | true       |
    Then check code for zones must be 201
    And  show zone detail with city_slug karaj and slug andishe must be
      | slug    | title  | is_enabled |
      | andishe | اندیشه | true       |


  Scenario: Getting zones list
    When Getting the list of zones from karaj
    Then zones get code must be 200


  Scenario: show zones details from specific slug
    When Getting the list of zones by zone_slug andishe and city karaj
    Then detail of zones code must be 200


  Scenario: Unsuccessful Register zones with empty data
    When add zone with invalid data for city yazd
      | title | is_enabled |
      |       | true       |
    Then status code for zone with invalid data must be 400


  Scenario: Successfully modified the zones
    When modify zones row with city karaj and slug andishe
      |slug| title          | is_enabled |
      |andisheh| اندییییشه | true       |
    Then Modify code for zones must be 204
    And Modified zone row with city karaj and zone slug andisheh must be
      |slug| title          | is_enabled |
      |andisheh| اندییییشه | true       |


  Scenario: Successfully Delete row in zone
    When Delete zone row in karaj with slug andisheh
    Then Successfully deleted code for zone must be 204


  Scenario: Check Unique in slug field zones
    When Add zone with same city yazd
      | slug  | title | is_enabled |
      | kavir | کویر  | true       |
      | kavir | کوه   | true       |
    Then zone unique code should be 409


  Scenario: add new zone for data entry
    When add zones for city tehran with
      | slug     | title    | is_enabled |
      | valiasr  | ولیعصر   | true       |
      | pasdaran | پاسداران | true       |
      | zafar    | ظفر      | true       |
    Then return code for added zone must be 201