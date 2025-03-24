class Coffee:
    """Represents a coffee object with a standardized description."""
    
    def __str__(self) -> str:
        """Provides the coffee's quality assessment."""
        return "This is the worst coffee you ever tasted."


class Intern:
    """Represents an intern with basic workplace capabilities."""
    
    def __init__(self, name: str = "My name? I'm nobody, an intern, I have no name.") -> None:
        """
        Initialize intern instance.
        
        Args:
            name: Optional name for the intern (default placeholder text)
        """
        self.Name = name

    def __str__(self) -> str:
        """Return the intern's name representation."""
        return self.Name

    def work(self) -> None:
        """Simulate work attempt that always fails."""
        raise Exception("I'm just an intern, I can't do that...")

    def make_coffee(self) -> Coffee:
        """Create and return a Coffee instance."""
        return Coffee()


if __name__ == "__main__":
    # Basic functionality test
    nameless = Intern()
    mark = Intern("Mark")
    
    print(nameless)
    print(mark)
    
    try:
        print(mark.make_coffee())
    except Exception as e:
        print(f"Coffee error: {e}")
    
    try:
        nameless.work()
    except Exception as e:
        print(f"Work error: {e}")

