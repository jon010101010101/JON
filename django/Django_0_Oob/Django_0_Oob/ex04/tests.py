#!/usr/bin/env python3
# coding: utf-8

import traceback
from elem import Elem, Text


def test_text():
    """
    Test the functionality of the Text class.
    This includes checking:
    - Default behavior.
    - Behavior with arguments.
    - Pattern replacements (e.g., newlines replaced with <br />).
    - Escaping of special characters (<, >, ").
    """
    # Check if Text is an instance of str
    assert isinstance(Text(), str)
    # Default behavior: Text with no arguments should be empty
    assert str(Text()) == ''
    # Behavior with an empty argument
    assert str(Text('')) == ''
    # Behavior with a non-empty argument
    assert str(Text('foo')) == 'foo'
    # Pattern replacement: newline to <br />
    assert str(Text('\n')) == '\n<br />\n'
    # Pattern replacement: multiple newlines
    assert str(Text('foo\nbar')) == 'foo\n<br />\nbar'
    # Escaping special characters: <
    assert str(Text('<')) == '&lt;'
    # Escaping special characters: >
    assert str(Text('>')) == '&gt;'
    # Escaping special characters: "
    assert str(Text('"')) == '&quot;'
    print('Text behaviour : OK.')  # Indicate that the test passed


def test_elem_basics():
    """
    Test the basic functionality of the Elem class.
    This includes:
    - Default behavior.
    - Handling of arguments in different orders.
    - Handling of content (single elements and lists).
    """
    # Default behavior: Elem with no arguments should be an empty <div>
    assert str(Elem()) == '<div></div>'
    # Arguments order: tag, attr, content, tag_type
    assert str(Elem('div', {}, None, 'double')) == '<div></div>'
    # Argument names: tag, attr, content, tag_type
    assert str(Elem(tag='body', attr={}, content=Elem(),
                    tag_type='double')) == '<body>\n  <div></div>\n</body>'
    # With elem as content: nesting elements
    assert str(Elem(content=Elem())) == '<div>\n  <div></div>\n</div>'
    # With list as content: multiple elements
    assert str(Elem(content=[Text('foo'), Text('bar'), Elem()])) == '<div>\n  foo\n  bar\n \
 <div></div>\n</div>'
    print('Basic Elem behaviour : OK.')  # Indicate that the test passed


def test_empty_texts():
    """
    Test how Elem handles empty texts.
    This includes:
    - Empty text as content.
    - Lists containing empty texts.
    """
    # Empty text as content
    assert str(Elem(content=Text(''))) == '<div></div>'
    # List of empty texts as content
    assert str(Elem(content=[Text(''), Text('')])) == '<div></div>'
    # Mixed content with empty and non-empty texts
    assert str(Elem(content=[Text('foo'), Text(''), Elem()])) == '<div>\n  foo\
\n  <div></div>\n</div>'
    print('Elem with empty texts : OK.')  # Indicate that the test passed


def test_errors():
    """
    Test error handling in the Elem class.
    
    This includes:
    - Ensuring that invalid content raises ValidationError.
      (e.g., integers or invalid types as content).
    
      Valid cases are also tested for comparison.
    
      The add_content() method is tested for similar scenarios.
    
      Invalid lists and empty strings are also tested.
    
    """
    # Type error if the content isn't made of Text or Elem.
    try:
        # Attempt to create an Elem with invalid content (integer)
        Elem(content=1)
    except Exception as e:
        # Verify that the correct exception is raised
        assert type(e) == Elem.ValidationError
    # The right way: content should be Text or Elem
    assert str(Elem(content=Text(1))) == '<div>\n  1\n</div>'

    # Type error if the elements of the list aren't Text or Elem instances.
    try:
        # Attempt to create an Elem with a list containing invalid content
        Elem(content=['foo', Elem(), 1])
    except Exception as e:
        # Verify that the correct exception is raised
        assert type(e) == Elem.ValidationError
    # The right way: all elements should be Text or Elem
    assert (str(Elem(content=[Text('foo'), Elem(), Text(1)]))
            == '<div>\n  foo\n  <div></div>\n  1\n</div>')

    # Same with add_method()
    try:
        # Create an empty Elem
        elem = Elem()
        # Attempt to add invalid content (integer)
        elem.add_content(1)
        # If no exception is raised, this is incorrect behavior
        raise(Exception("incorrect behaviour."))
    except Exception as e:
        # Verify that the correct exception is raised
        assert isinstance(e, Elem.ValidationError)
    
    # Or with lists:
    try:
        # Create an empty Elem
        elem = Elem()
        # Attempt to add a list with invalid content
        elem.add_content([1,])
        # If no exception is raised, this is incorrect behavior
        raise(Exception('incorrect behaviour'))
    except Exception as e:
        # Verify that the correct exception is raised
        assert isinstance(e, Elem.ValidationError)

    # str can't be used:
    try:
        # Create an empty Elem
        elem = Elem()
        # Attempt to add a list with empty string
        elem.add_content(['',])
        # If no exception is raised, this is incorrect behavior
        raise(Exception("incorrect behaviour."))
    except Exception as e:
        # Verify that the correct exception is raised
        assert isinstance(e, Elem.ValidationError)
    
    try:
        # Attempt to create an Elem with empty string as content
        elem = Elem(content='')
        # If no exception is raised, this is incorrect behavior
        raise(Exception("incorrect behaviour."))
    except Exception as e:
        # Verify that the correct exception is raised
        assert isinstance(e, Elem.ValidationError)
    print('Error cases : OK.')  # Indicate that the test passed


def test_embedding():
    """
    Test embedding of Elem elements.
    
    This includes nesting multiple levels of Elem instances.
    """
    # Verify nesting of multiple levels
    assert (str(Elem(content=Elem(content=Elem(content=Elem()))))
            == """<div>
  <div>
    <div>
      <div></div>
    </div>
  </div>
</div>""")
    print('Element embedding : OK.')  # Indicate that the test passed


def test():
    """
    Run all tests.
    
    This function calls each test function in sequence.
    """
    test_text()
    test_elem_basics()
    test_embedding()
    test_empty_texts()
    test_errors()
    
if __name__ == '__main__':
    try:
        # Run the main test function
        test()
        print('Tests succeeded!')  # Indicate that all tests passed
    except AssertionError as e:
        # If an assertion error occurs, print the traceback and error message
        traceback.print_exc()
        print(e)
        print('Tests failed!')  # Indicate that tests failed

