Feature: Shipment Quote Calculation

  Scenario: Verify user can calculate the shipment quote from Malaysia to India
    Given the user navigates to the rate calculator page
    When the user enters "35600" as the postcode
    And the user enters "India" as the "To" country and leaves the postcode empty
    And the user enters "1" as the "Weight" and presses Calculate
    Then the user can see multiple quotes and shipments options available