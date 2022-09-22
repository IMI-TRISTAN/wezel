import pytest

from PyQt5 import QtCore

import wezel.widgets.user_input

#pytest fixtures are functions attached to the tests 
#which run before the test function is executed.
@pytest.fixture
def app(qtbot):
    test_hello_app = PyTestQtExample.MyApp()
    qtbot.addWidget(test_hello_app)

    return test_hello_app


def test_label(app):
    assert app.text_label.text() == "Hello World!"


def test_label_after_click(app, qtbot):
    qtbot.mouseClick(app.button, QtCore.Qt.LeftButton)
    assert app.text_label.text() == "Goodbye World!"
