Feature:Test services C,R,U,D


  Scenario: Successful Register new service
    When Register a service with data:
      | slug       | title       | is_enabled | tags         | summary                 | index | price_guide             | image                      | tips                      | description                    |
      | ashpazi    | آشپزی        | true       | بهار , جایزه | توضیحات توضیحات توضیحات | 0     | هزینه اجرت سی هزارتومان | www.ostadkar.pro/image.png | سرویس در منزل انجام میشود |                                |
      | tamirat    | تعمیرات      | true       |              | از ۱۰۰ هزار تومان       | 1     |                         |                            | سرویس در منزل انجام میشود | هزینه اقلام مصرفی با مشتری است |
      | programing | برنامه نویسی | true       | طرح          |                         | 1     |                         |                            |                           | سرویس در منزل انجام میشود      |
      | car        | خودرو        | true       |              | خلاصه                   | 0     | هزینه اجرت سی هزارتومان | www.ostadkar.pro/image.png | سرویس در منزل انجام میشود | سرویس در منزل انجام میشود      |
    Then Successfully register service code must be 201
    And  service detail with slug ashpazi must be
      | slug    | title | is_enabled | tags         | summary                 | index | price_guide             | image                      | tips                      | description |
      | ashpazi | آشپزی | true       | بهار , جایزه | توضیحات توضیحات توضیحات | 0     | هزینه اجرت سی هزارتومان | www.ostadkar.pro/image.png | سرویس در منزل انجام میشود |             |


  Scenario: Getting Services list
    When Getting the list of services
    Then Result code services must be 200


  Scenario: show Service details from specific slug
    When Getting a services by ashpazi
    Then detail code services must be 200


  Scenario: Unsuccessful Register services with empty data
    When add service with invalid data
      | slug | title | is_enabled | tags         | summary                 | index |
      |      | test  | true       | بهار , جایزه | توضیحات توضیحات توضیحات | 0     |
    Then status code for invalid data service must be 400


  Scenario: Successfully modified the services
    When update service row with slug tamirat
      | slug    | title       | is_enabled | tags | summary           | index | price_guide | image | tips                      | description                    |
      | tamirat | تعمیییرات | true       |      | از ۱۰۰ هزار تومان | 1     |             |       | سرویس در منزل انجام میشود | هزینه اقلام مصرفی با مشتری است |
    Then result code for update must be 204
    And services row with slug tamirat must be
      | slug    | title   | is_enabled | tags | summary           | index | price_guide | image | tips                      | description                    |
      | tamirat | تعمیییرات | true       |      | از ۱۰۰ هزار تومان | 1     |             |       | سرویس در منزل انجام میشود | هزینه اقلام مصرفی با مشتری است |


  Scenario: Successfully Delete row in services
    When Delete service row with slug car
    Then Successfully disabled code for service must be 204


  Scenario: Check Unique in slug field services
    When Add services with same slug services
      | slug      | title    | is_enabled | index | description |
      | ghalishoe | قالیشویی | true       | 0     | توضیح       |
      | ghalishoe | قالیشویی | true       | 0     | توضیح       |
    Then services unique code should be 409

