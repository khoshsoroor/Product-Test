Feature:Test offices C,R,U,D


  Scenario: Successfully add offices
    When add specify offices with city slug tehran office
      | slug    | title  | address                       | zip_code   | location | phone_number  | is_enabled |
      | valiasr | ولیعصر | خ کمیرزای شیرازی خ ناهید پ ۵۷ | +431873377 | 20,23    | +982112345678 | true       |
    Then create offices code must be 201
    And  office detail with slug valiasr in city tehran must be
      | slug    | title  | address                       | zip_code   | location | phone_number  | is_enabled |
      | valiasr | ولیعصر | خ کمیرزای شیرازی خ ناهید پ ۵۷ | +431873377 | 20,23    | +982112345678 | true       |


  Scenario: Return list of offices inside a city
    When Getting the list of offices in city tehran
    Then Result code offices must be 200


  Scenario: return an office detail with a city
    When Get detail of office valiasr in city tehran
    Then detail code offices must be 200


  Scenario: Successfully edit an office information
    When edit office row in city tehran with slug valiasr
      | slug    | title   | address                   | zip_code   | location | phone_number  | is_enabled |
      | valiasr | ولی عصر | خ کمیرزای شیرازی خ ناهید پ ۵۷ | +431873377 | 20,23    | +982112345678 | true       |
    Then return code for edit office must be 204
    And office detail with slug valiasr in city tehran must be
      | slug    | title           | address                   | zip_code   | location | phone_number  | is_enabled |
      | valiasr | ولی عصر  | خ کمیرزای شیرازی خ ناهید پ ۵۷ | +431873377 | 20,23   | +982112345678 | true       |


  Scenario: Successfully Delete an office from a city
    When Delete office row in city tehran and office valiasr
    Then Successfully deleted code offices must be 204
