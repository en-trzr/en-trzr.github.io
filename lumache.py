
# lumache.py
"""
Lumache - A Simple Python Script

This script provides functions for basic operations on numbers, strings, and lists.
It is intended to serve as an example for Read the Docs documentation.

Usage:
    from lumache import add_numbers, reverse_string, sort_list
"""

def add_numbers(a, b):
    """
    Adds two numbers together.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    
    Returns:
        int or float: The sum of a and b.
    """
    return a + b

def reverse_string(s):
    """
    Reverses a given string.
    
    Args:
        s (str): The string to be reversed.
    
    Returns:
        str: The reversed string.
    """
    return s[::-1]

def sort_list(lst):
    """
    Sorts a list of numbers in ascending order.
    
    Args:
        lst (list): A list of numbers.
    
    Returns:
        list: A sorted list.
    """
    return sorted(lst)
