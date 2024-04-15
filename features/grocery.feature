Feature: Grocery Shopping List

  @Add_items
  Scenario Outline: Add items to the list
    Given I have an empty shopping list
    When I add "<item_list>" to the list
    Then the list should contain "<item_list>"
    Examples:
      | item_list                           |
      | 7 and 8 and 9                       |
      | apple and mango               |
      | bread and lassi and cake |
      | eggs and milk           |

  @Remove_items
  Scenario Outline: Remove items from the list
    Given I have a shopping list with items "<initial_items>"
    When I remove "<item>" from the list
    Then the list should contain "<expected_items>"
    Examples:
      | initial_items      | item   | expected_items |
      | apples and bananas | apples | bananas        |
      | milk and bread     | milk   | bread          |
      | cheese and eggs    | eggs   | cheese         |

  @checkoff_items
  Scenario Outline: Check off items as purchased
    Given I have a shopping list with items "<initial_items>"
    When I check off "<item>" as purchased
    Then "<item>" should be marked as purchased
    And "<other_item>" should still be on the list
    Examples:
      | initial_items      | item    | other_item |
      | apples and bananas | bananas | apples     |
      | milk and bread     | milk    | bread      |
      | cheese and eggs    | cheese  | eggs       |
