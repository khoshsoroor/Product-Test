Feature:Test Search of services
  title and tags


  Scenario: list of services with short keyword tags
    When Get services with keyword بهار
    Then second return code search must be 200


  Scenario: list of services with short keyword
    When Get list of services with keyword ب
    Then  third search must be 200


  Scenario: search services with title
    When list of services with keyword آشپزی
    Then first code for search must be 200
