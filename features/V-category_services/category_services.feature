Feature:Test category_services C,R,U,D


  Scenario: Successfully assign a service to a category
    When assign service ashpazi to category nezafat
    Then return code for category services must be 204


  Scenario: Return list of Services are assigned to a Category
    When Get the list of services for category nezafat
    Then category service code must be 200


  Scenario: Un-Assign a Service from a City
    When Delete service ashpazi from category nezafat
    Then Successfully return code for category services must be 204


  Scenario: add data entry for service to a category
    When add below services to category nezafat
      | service_slug |
      | tamirat     |
      | programing   |
      | ghalishoe    |
    Then result code in data entry first category services must be 204

