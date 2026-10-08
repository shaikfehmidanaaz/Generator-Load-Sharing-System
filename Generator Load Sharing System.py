class Generator:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.load = 0

    def assign_load(self, load):
        if load <= self.capacity:
            self.load = load
        else:
            self.load = self.capacity

    def load_percentage(self):
        if self.capacity == 0:
            return 0
        return (self.load / self.capacity) * 100


class GeneratorLoadSharingSystem:

    def __init__(self):
        self.generators = []

    def add_generator(self, generator):
        self.generators.append(generator)

    def share_load(self, total_load):
        remaining_load = total_load

        # First, remove previous load
        for generator in self.generators:
            generator.load = 0

        # Distribute load according to generator capacity
        total_capacity = sum(
            generator.capacity for generator in self.generators
        )

        if total_load > total_capacity:
            print("WARNING: Total load is greater than available generation.")
            print("Not all load can be supplied.\n")

        for generator in self.generators:
            if remaining_load <= 0:
                break

            share = (generator.capacity / total_capacity) * total_load

            # Do not exceed generator capacity
            assigned = min(share, generator.capacity)

            generator.assign_load(assigned)
            remaining_load -= assigned

        # Distribute any small remaining load
        for generator in self.generators:
            if remaining_load <= 0:
                break

            available = generator.capacity - generator.load
            additional = min(available, remaining_load)

            generator.load += additional
            remaining_load -= additional

    def display_status(self, total_load):
        print("----- Generator Load Sharing System -----")
        print(f"Total Load: {total_load:.2f} kW\n")

        total_supplied = 0

        for generator in self.generators:
            print(f"{generator.name}")
            print(f"  Capacity      : {generator.capacity:.2f} kW")
            print(f"  Load Assigned : {generator.load:.2f} kW")
            print(f"  Load Percentage: {generator.load_percentage():.2f}%")
            print()

            total_supplied += generator.load

        print(f"Total Power Supplied: {total_supplied:.2f} kW")

        if total_supplied >= total_load:
            print("Status: LOAD FULLY SUPPLIED")
        else:
            print("Status: LOAD NOT FULLY SUPPLIED")


# Create generators
generator1 = Generator("Generator 1", 500)
generator2 = Generator("Generator 2", 300)
generator3 = Generator("Generator 3", 200)

# Create load sharing system
system = GeneratorLoadSharingSystem()

system.add_generator(generator1)
system.add_generator(generator2)
system.add_generator(generator3)

# Total load
total_load = 800

# Share load between generators
system.share_load(total_load)

# Display result
system.display_status(total_load)
