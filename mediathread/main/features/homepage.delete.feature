Feature: Homepage Delete Operations. Project, Item

    Scenario: homepage.delete.feature 1. Student cannot delete assignment
        Given Using selenium
        Given there is a sample assignment
        Given I am test_student_one in Sample Course

        Given the home workspace is loaded
        Then The "Sample Assignment" project has no delete icon

        Then Finished using Selenium

    Scenario: homepage.delete.feature 2. Instructor cannot delete student's response
        Given Using selenium
        Given there is a sample response
        Given I am test_instructor in Sample Course

        Given the home workspace is loaded
        When I select "Student One" as the owner in the Composition column
        Then the owner is "Student One" in the Composition column
        Then the composition panel has 1 response named "Sample Assignment Response"
        Then The "Sample Assignment Response" project has no delete icon

        Then Finished using Selenium

    Scenario: homepage.delete.feature 3. Instructor can delete his own assignment
        Given Using selenium
        Given there is a sample assignment
        Given I am test_instructor in Sample Course

        Given the home workspace is loaded
        Then The "Sample Assignment" project has a delete icon

        When I click the "Sample Assignment" project delete icon
        Then I cancel the action
        Then The "Sample Assignment" project has a delete icon
        Then there is a "Sample Assignment" link

        When I click the "Sample Assignment" project delete icon
        Then I confirm the action

        Then there is not a "Sample Assignment" link

        Then Finished using Selenium

    Scenario: homepage.delete.feature 4. Student can delete his own response
        Given Using selenium
        Given there is a sample response
        Given I am test_student_one in Sample Course

        Given the home workspace is loaded
        Then The "Sample Assignment Response" project has no delete icon

        # Add a title and some text
        When I click the "Sample Assignment Response" link
        Then I am at the Sample Assignment Response page

        # Save
        When I click the Saved button
        Then I set the project visibility to "Draft - only you can view"
        Then I save the changes
        Then there is a "Draft" link

        When I click the "Sample Course" link
        Given the home workspace is loaded

        When I click the "Sample Assignment Response" project delete icon
        Then I cancel the action

        When I click the "Sample Assignment Response" project delete icon
        Then I confirm the action

        Then there is not a "Sample Assignment Response" link
        Then the composition panel has 1 project named "Sample Assignment"

        Then Finished using Selenium
