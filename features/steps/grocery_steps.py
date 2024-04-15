from behave import *

from grocery_list import GroceryList


@given('I have an empty shopping list')
def step_impl(context):
    context.grocery_list = GroceryList()


@when('I add "{item_list}" to the list')
def step_impl(context, item_list):
    items = item_list.split(" and ")
    context.grocery_list.add_item(items)


@then('the list should contain "{item_list}"')
def step_impl(context, item_list):
    expected_items = item_list.split(" and ")
    for item in expected_items:
        assert item in context.grocery_list.items


@given('I have a shopping list with items "{initial_items}"')
def step_impl(context, initial_items):
    context.grocery_list = GroceryList()
    context.grocery_list.add_item(initial_items.split(" and "))


@when('I remove "{item}" from the list')
def step_impl(context, item):
    context.grocery_list.remove_item(item)


@when('I check off "{item}" as purchased')
def step_impl(context, item):
    context.grocery_list.check_off_item(item)


@then('"{item}" should be marked as purchased')
def step_impl(context, item):
    assert item not in context.grocery_list.items


@then('"{other_item}" should still be on the list')
def step_impl(context, other_item):
    assert other_item in context.grocery_list.items
