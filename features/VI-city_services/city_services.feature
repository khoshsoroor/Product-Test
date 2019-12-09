Feature:Test city_services


    Scenario: Successfully add the city_services
        When add city services for city karaj and service tamirat
            | gender | is_enabled| start_at| finish_at |
            | MALE   | true      | 11:00:00 | 19:00:00 |
        Then result code for city services must be 204
        And Modified city services with city karaj and service tamirat must be
            | gender | is_enabled| start_at| finish_at |
            | MALE   | true      | 11:00:00 | 19:00:00 |


    Scenario: Getting city_services all list
        When Getting the list of services for city karaj
        Then return city_services code must be 200


    Scenario: show city_services details from specific city
        When Get the list of service tamirat by slug karaj
        Then detail of city_services code must be 200


   Scenario: Successfully Delete row in city_services
       When Delete city_services row with slug karaj and service tamirat
       Then Successfully deleted code for city_services must be 204


   Scenario: data entry for city_services
       When adding data city services for city karaj and service ghalishoe
            | gender | is_enabled| start_at| finish_at |
            |  MALE  | true      | 11:00:00 | 19:00:00 |
       Then code for data city services must be 204










