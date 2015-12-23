Feature: Homepage

    Scenario: homepage.feature 1. Instructor default view
        Given Using selenium
        Given I am test_instructor in Sample Course

        When I open the manage menu
        Then there is a "Settings" link
        Then there is a "Sources" link
        Then there is a "Migrations" link
        Then there is a "Vocabulary" link

        When I open the reports menu
        Then there is an "Assignment Responses" link
        And there is a "Class Activity" link
        And there is a "Class Member Contributions" link

        And there is a From Your Instructor column
        And there is a Composition column
        And there is a Collection column
        And there is help for the From Your Instructor column
        And there is help for the Composition column
        And there is help for the Collection column

        Then Finished using Selenium

    Scenario: homepage.feature 2. Student view w/o assignment
        Given Using selenium
        Given I am test_student_one in Sample Course
        Then there is no manage menu
        And there is no reports menu

        And there is not a From Your Instructor column
        And there is a Composition column
        And there is a Collection column

        And there is help for the Composition column
        And there is help for the Collection column

        Then Finished using Selenium

    Scenario: homepage.feature 3. Student view w/assignment
        Given Using selenium
        Given there is a sample assignment
        Given I am test_student_one in Sample Course

        And there is not a From Your Instructor column
        Then the composition panel has 1 projects named "Sample Assignment"

        And there is a Composition column
        And there is a Collection column

        And there is help for the Composition column
        And there is help for the Collection column

        When I click the "Sample Assignment" link
        Then I am at the Sample Assignment page
        And there is an open Assignment panel
        And the Assignment title is "Sample Assignment"

        Then Finished using Selenium

    Scenario: homepage.feature 4. Student view w/assignment & response
        Given Using selenium
        Given there is a sample response
        Given I am test_student_one in Sample Course

        Given the home workspace is loaded
        Then There is not a From Your Instructor column
        Then The composition panel has 1 projects named "Sample Assignment"
        Then the composition panel has 1 response named "Sample Assignment Response"

        When I click the "Sample Assignment Response" link
        Then I am at the Sample Assignment Response page
        And there is an open Composition panel
        And the Composition title is "Sample Assignment Response"

        Then Finished using Selenium


    Scenario Outline: homepage.feature 5. User Settings menu
        Given Using selenium
        Given I am <user_name> in Sample Course

        Given the home workspace is loaded
        When I open the user menu
        Then there is a "Log Out" link
        Then There is not a "Switch Course" link
        Then There is not an "Admin" link

        When I click the "Log Out" link
        Then I am at the Login page

        Then Finished using Selenium

    Examples:
        | user_name           |
        | test_instructor     |
        | test_student_one    |
