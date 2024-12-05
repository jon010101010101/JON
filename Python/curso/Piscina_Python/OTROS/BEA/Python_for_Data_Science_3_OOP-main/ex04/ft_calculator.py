class calculator:
    """Do calculations between two vectors"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate dot product and print result"""
        print(f"Dot product is : {sum([x * y for x, y in zip(V1, V2)])}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Calculate vector subtraction and print result"""
        print(f"Add Vector is : {[float(x + y) for x, y in zip(V1, V2)]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Calculate vector addition and print result"""
        print(f"Sous Vector is : {[float(x - y) for x, y in zip(V1, V2)]}")
