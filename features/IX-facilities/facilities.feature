Feature:Test facilities C,R,U,D


  Scenario: Successfully add facilities
    When add specify facilities
      | slug       | title   | icon                                    |
      | facilities | امکانات | http://api.ostadkar.pro/icons/12345.svg |
      | feedback | پشتیبانی | http://api.ostadkar.pro/icons/12345.svg |
      | trip | حمل رایگان | http://api.ostadkar.pro/icons/12345.svg |
    Then return code facilities must be 201
    And  facilities detail with slug facilities must be
      | slug       | title   | icon                                    |
      | facilities | امکانات | http://api.ostadkar.pro/icons/12345.svg |


  Scenario: Check Unique in slug facilities
    When Add facility with same slug
      | slug | title    | icon |
      | free | کارشناسی |      |
      | free | کارشناسی |      |
    Then facilities unique code must be 409

  Scenario: Return list of facilities
    When Getting the list of facilities
    Then Result code facilities must be 200


  Scenario: show details of facilities
    When the list of facilities by slug facilities
    Then detail code of facilities must be 200


  Scenario: Successfully update a facility information
    When update facility row with slug free
      | slug | title           | icon                                    |
      | free | کارشناسی رایگان | http://api.ostadkar.pro/icons/12345.svg |
    Then return code for update facilities should be 204
    And facility row with slug free must be
      | slug | title           | icon                                    |
      | free | کارشناسی رایگان | http://api.ostadkar.pro/icons/12345.svg |


  Scenario: Successfully Delete row facilities
    When Delete facilities row with slug facilities
    Then code in delete method facilities must be 204



