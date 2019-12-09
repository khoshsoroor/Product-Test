Feature:Test service facility


  Scenario: assign specified facility to a service
    When specify facility for service tamirat with slug free
    Then return facility code must be 204


  Scenario: Getting list of facilities assigned to a service
    When Get list of facilities by service slug tamirat
    Then return code in facility service must be 200


  Scenario: Delete facility from a service
    When Delete facility free with service slug tamirat
    Then result code for facility service deleted must be 204