Feature: Sliding Panels in the Asset View
    
    Scenario Outline: 1. Full Collection at various resolutions
        Given Using selenium
        Given I am test_instructor in Sample Course
        Given my browser resolution is <width> x <height>
    
        # Full Collection
        When I click the "View Full Collection" link
        Then I am at the Collection page
        
        # View an individual asset
        When I click the "MAAP Award Reception" link
        Then there is a minimized Collection panel
        And there is an open Asset panel
        
        # Verify the asset is really there
        When The item header is "MAAP Award Reception"
        Then There is an "Item" link
        Then There is a "Source" link
        Then There is a "References" link
        
        Then Finished using Selenium
        
      Examples:
        | width | height |
        | 900   | 500    |
        | 1024  | 768    |
        | 1280  | 800    |
        | 1440  | 900    |
        
    Scenario Outline: 2. Individual Item View
        Given Using selenium
        Given I am test_instructor in Sample Course
        Given my browser resolution is <width> x <height>
    
        # View an individual asset
        When I access the url "/asset/2/"
        Then I am at the Collection page
        Then there is a minimized Collection panel
        And there is an open Asset panel
        
        # Verify the asset is really there
        When The item header is "MAAP Award Reception"
        Then There is an "Item" link
        Then There is a "Source" link
        Then There is a "References" link
        
        Then Finished using Selenium
        
      Examples:
        | width | height |
        | 900   | 500    |
        | 1024  | 768    |
        | 1280  | 800    |
        | 1440  | 900    |
