name = "Hello World"


def print_name_box():
    print(name)
    def smaller_box():
        print(name)
        def smallest_box():
            print(name)
        smallest_box()
    smaller_box()

print_name_box()
