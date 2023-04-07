from Director import Director
from ConcreteBuilder1 import ConcreteBuilder1


list_regions = [1, 2, 3, 4, 5]
list_builders = []

if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()
    print("Number of points", builder.product.computePointsScheme(8))

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    print("Number of points", builder.product.computePointsScheme(8))

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    print("Number of points", builder.product.computePointsScheme(8))
    builder.product.list_parts()