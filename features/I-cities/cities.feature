Feature:Test City C,R,U,D

  Scenario: city list is empty
    When Get the list of all city and specify city tehran
    Then not found code for city must be 404


  Scenario: successful add cities
    When Adding cities with data
      | slug   | title | is_enabled |
      | ahvaz  | اهواز | true       |
      | yazd   | یزد   | true       |
      | tehran | تهران | true       |
      | karaj  | کرج   | true       |
    Then Status code must be 201
    And Cities row with slug ahvaz must be
      | slug  | title | is_enabled |
      | ahvaz | اهواز | true       |


  Scenario: Successfully modified the city
    When modify city row with slug tehran
      | slug   | title | is_enabled |
      | tehran | طهران | true       |
    Then Modified code must be 204
    And Modified cities row with slug tehran must be
      | slug   | title | is_enabled |
      | tehran | طهران | true       |


  Scenario: Unsuccessful add cities
    When Add cities with empty data
      | slug | title | is_enabled |
      |      | test  | true       |
    Then Failure code must be 400


  Scenario: Getting all City lists
    When Getting the list of cities
    Then Result code city must be 200
    And List must not be empty


  Scenario: Successfully Delete row in cities
    When Delete city row with slug ahvaz
    Then Successfully disabled code must be 204


  Scenario: Check Unique in slug field city
    When Add cities with same slug city
      | slug   | title | is_enabled |
      | shiraz | شیراز | true       |
      | shiraz | شیراز | true       |
    Then after code should be 409


  Scenario: Delete wrong row in cities
    When Delete city row with wrong slug دد
    Then wrong slug for disable code must be 404


  Scenario: check odata filter for tags in categories
    When check category tags that has متن
    Then return code status for tags must be 200
    And row in categories for tags must be
      | slug           | title      | is_enabled | parent_slug | tags | index | icon                             | logo | image                             | description |
      | nezafat_manzel | نظافت منزل | true       | nezafat     | متن  | 2     | http://cdn.pstadkar.pro/icon.svg |      | http://cdn.pstadkar.pro/image.png | توضیحات     |


#  Scenario: check odata filter for indexes in cities
#    When list cities that index is equal 1
#    Then result status code for index must be 200


#  Scenario: check odata filter for not equal in categories
#    When categories list that index is not equal 0
#    Then status code for not equal must be 200
#
#
#  Scenario: check odata filter for greater than and less than in categories
#    When categories list that index is grater equal than 2 and is less equal than 4
#    Then check code for and equal must be 200
#
#
#  Scenario: check odata filter for g or g not in categories
#    When categories list that index is grater equal than 2 or is less equal than 4
#    Then check code for or filter must be 200
#
#
#  Scenario: check odata orderby index categories
#    When categories list orderby index
#    Then check code for orderby categories must be 200
#
#
#  Scenario: check odata top count for categories
#    When categories list top 3 and orderby title
#    Then check code top count categories must be 200
#
#
#  Scenario: check odata top count for categories
#    When categories list top 3 and orderby title
#    Then check code top count categories must be 200
#
#
#  Scenario: check odata skip for categories
#    When categories list skip 2
#    Then check code for list of categories by skip must be 200
#
#
#  Scenario: check odata expand for categories
#    When categories list expand parent_id
#    Then check code for expand categories must be 200
#
#
#  Scenario: check odata select for categories
#    When categories list for select title
#    Then check code selected categories must be 200
#
#   #TODO Deployment other odata