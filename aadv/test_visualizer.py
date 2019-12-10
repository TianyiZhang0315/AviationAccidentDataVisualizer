# coding: utf-8
'''Test Files for visualizer.
 This file contains 7 tests.'''
from unittest import mock
import visualizer as vis

INFO_FOR_S = "Test display only. Not for real use."
DATE_TEST_BAD = ['1398221', '125201', '199843102', '202a1011', '254sa#$41', 'ew122012']
DATE_TEST_GOOD = ['20191204', '19940201']
LST_SINGLE = ['a', 'b', 'c', 'd']
BAD_SINGLE = ['e', 'aa', '2']
GOOD_SINGLE = ['a', 'b', 'd']

'''Test files are written below.'''
def test_date_input():
    """Check date_input function."""
    for ele in DATE_TEST_BAD:
        with mock.patch('builtins.input', return_value=ele):
            vis.date_input(INFO_FOR_S)
            assert mock_stdout.getvalue() == 'Date entered is not valid (check length).\n' \
            or mock_stdout.getvalue() == 'Date contains unacceptable char.\n'
    for ele in DATE_TEST_GOOD:
        with mock.patch('builtins.input', return_value=ele):
            assert vis.date_input(INFO_FOR_S) == ele

def test_user_query_input():
    """Check user_query_input function."""
    for ele in BAD_SINGLE:
        with mock.patch('builtins.input', return_value=ele):
            vis.user_query_input(INFO_FOR_S, LST_SINGLE)
            assert mock_stdout.getvalue() == 'Input token not found. Please retry.\n'
    for ele in GOOD_SINGLE:
        with mock.patch('builtins.input', return_value=ele):
            assert vis.user_query_input(INFO_FOR_S, LST_SINGLE) == ele
   