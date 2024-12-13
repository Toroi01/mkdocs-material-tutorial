class Greeter:
    """
    A class to generate greeting messages.
    """

    def __init__(self, name: str):
        """
        Initialize the Greeter class with a name.

        Parameters
        ----------
        name : str
            The name of the person to greet.
        """
        self.name = name

    def greet(self) -> str:
        """
        Generate a greeting message.

        Returns
        -------
        str
            A greeting message including the name.
        """
        return f"Hello, {self.name}!"
