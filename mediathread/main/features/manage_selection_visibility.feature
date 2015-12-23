Feature: Manage Selection Visibility

    Scenario: manage_selection_visibility.feature 1. Verify default selection visibility is yes
        Given Using selenium
        Given I am test_instructor in Sample Course
        Given the selection visibility is set to "Yes"

        When I open the manage menu
        Then there is a "Settings" link
        When I click the "Settings" link
        Then I am at the Manage Course Settings page
     
        Then The selection visibility is "Yes"
        
        Then Finished using Selenium
        
    Scenario: manage_selection_visibility.feature 2. Change selection visibility to no
        Given Using selenium
        Given I am test_instructor in Sample Course
        Given the selection visibility is set to "No"
        
        When I open the manage menu
        Then there is a "Settings" link
        When I click the "Settings" link
        Then I am at the Manage Course Settings page
     
        Then The selection visibility is "No"
        
        Then Finished using Selenium        
    
  
