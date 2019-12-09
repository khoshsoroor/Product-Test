Feature:Test Categories C,R,U,D


  Scenario: Successful create specified categories
    When Create specify category information:
      | slug           | title      | is_enabled | parent_slug | tags          | index | icon                             | logo                             | image                             | description       |
      | nezafat        | نظافت      | true       |             | عید,بهار      | 1     | http://cdn.pstadkar.pro/icon.svg | http://cdn.pstadkar.pro/logo.png | http://cdn.pstadkar.pro/image.png | توضیحات دسته بندی |
      | nezafat_manzel | نظافت منزل | true       | nezafat     | متن           | 2     | http://cdn.pstadkar.pro/icon.svg |                                  | http://cdn.pstadkar.pro/image.png | توضیحات           |
      | lessons        | آموزشی     | true       |             | مدرسه , تفریح | 0     |                                  |                                  | http://cdn.pstadkar.pro/image.png | برای دسته بندی    |
      | building       | ساختمانی   | true       |             |               | 1     |                                  |                                  |                                   | توضیح             |
    Then create category code must be 201
    And  category detail with slug nezafat_manzel must be
      | slug           | title      | is_enabled | parent_slug | tags | index | icon                             | logo | image                             | description |
      | nezafat_manzel | نظافت منزل | true       | nezafat     | متن  | 2     | http://cdn.pstadkar.pro/icon.svg |      | http://cdn.pstadkar.pro/image.png | توضیحات     |


  Scenario: Getting category list
    When Getting the list of categories
    Then categories code must be 200


  Scenario: show category details from specific slug
    When Getting the list of category by slug building
    Then detail of category code must be 200


  Scenario: Unsuccessful Register categories with empty data
    When add category with invalid data
      | slug | title | is_enabled | parent_slug | tags | index | description |
      |      | test  | true       |             | بهار | 1     | توضیحات     |
    Then category code with invalid data must be 400


  Scenario: Successfully modified the categories
    When for update modify category row with slug nezafat
      | slug    | title  | is_enabled | parent_slug | tags | index | icon                             | logo                             | image                             |
      | nezafat | نظافتت | true       |             | عید  | 1     | http://cdn.pstadkar.pro/icon.svg | http://cdn.pstadkar.pro/logo.png | http://cdn.pstadkar.pro/image.png |
    Then Modify code for categories must be 204
    And  check row in category with slug nezafat must be
      | slug    | title  | is_enabled | parent_slug | tags     | index | icon                             | logo                             | image                             |
      | nezafat | نظافتت | true       |             | عید,بهار | 1     | http://cdn.pstadkar.pro/icon.svg | http://cdn.pstadkar.pro/logo.png | http://cdn.pstadkar.pro/image.png |


  Scenario: Successfully Delete row in categories
    When Delete category row with slug building
    Then Successfully deleted code for category must be 204


  Scenario: Check Unique in slug field category
    When Adding category with same slug categories
      | slug     | title    | is_enabled | parent_slug | tags     | index |
      | computer | کامپیوتر | true       |             | عید,بهار | 1     |
      | computer | کامپیوتر | true       |             | عید,بهار | 1     |
    Then categories unique code should be 409


  Scenario: check odata filter for tags in categories
    When check category tags that has متن
    Then return code status for tags must be 200
    And row in categories for tags must be
      | slug           | title      | is_enabled | parent_slug | tags | index | icon                             | logo | image                             | description |
      | nezafat_manzel | نظافت منزل | true       | nezafat     | متن  | 2     | http://cdn.pstadkar.pro/icon.svg |      | http://cdn.pstadkar.pro/image.png | توضیحات     |


  Scenario: check odata filter for indexes in categories
    When list categories that index is equal 1
    Then result status code for index must be 200


  Scenario: check odata filter for not equal in categories
    When categories list that index is not equal 0
    Then status code for not equal must be 200


  Scenario: check odata filter for greater than and less than in categories
    When categories list that index is grater equal than 2 and is less equal than 4
    Then check code for and equal must be 200


  Scenario: check odata filter for g or g not in categories
    When categories list that index is grater equal than 2 or is less equal than 4
    Then check code for or filter must be 200


  Scenario: check odata orderby index categories
    When categories list orderby index
    Then check code for orderby categories must be 200


  Scenario: check odata top count for categories
    When categories list top 3 and orderby title
    Then check code top count categories must be 200


  Scenario: check odata top count for categories
    When categories list top 3 and orderby title
    Then check code top count categories must be 200


  Scenario: check odata skip for categories
    When categories list skip 2
    Then check code for list of categories by skip must be 200


  Scenario: check odata expand for categories
    When categories list expand parent_id
    Then check code for expand categories must be 200


  Scenario: check odata select for categories
    When categories list for select title
    Then check code selected categories must be 200

   #TODO Deployment other odata