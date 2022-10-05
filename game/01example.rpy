python early:

    # This maps from example name to the text of a fragment.
    examples = { }

    # The size of the example - large or small.
    example_size = "small"

    # The location of the example - top or bottom.
    example_location = "top"

    # The screen in the last example.
    example_screen = None

    # A transition used with examples
    example_transition = None

    def reset_example():
        """
        Called to reset the example code to the defaults.
        """

        global example_size
        global example_location
        global example_screen

        example_size = "small"
        example_location = "top"
        example_screen = None

