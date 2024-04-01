class Experiment:
    def _init_(self, name, computation_speed_preference, memory_preference):
        self.name = name
        self.computation_speed_preference = computation_speed_preference
        self.memory_preference = memory_preference
        self.resource = None

    def utility(self, resource):
        if self.resource is None:
            self.resource = {
                'memory': min(self.memory_preference, resource['memory']),
                'computation_speed': min(self.computation_speed_preference, resource['computation_speed'])
            }

        return self.resource['computation_speed'] + self.resource['memory']

class ResourceAllocator:
    def _init_(self, experiments, available_resource):
        self.experiments = experiments
        self.available_resource = available_resource

    def allocate_resources(self):
        allocated_resources = {}

        for experiment in self.experiments:
            print(f"Resources before allocation: {self.available_resource['memory']} "
                  f"{self.available_resource['computation_speed']}")
            allocated_resource = self.allocate_experiment_resource(experiment)
            self.available_resource['memory'] -= allocated_resource['memory']
            self.available_resource['computation_speed'] -= allocated_resource['computation_speed']
            allocated_resources[experiment] = allocated_resource
            print(f"Resources allocated to {experiment.name}: "
                  f"{allocated_resource['memory']} {allocated_resource['computation_speed']}")

        return allocated_resources

    def allocate_experiment_resource(self, experiment):
        return {
            'memory': min(experiment.memory_preference, self.available_resource['memory']),
            'computation_speed': min(experiment.computation_speed_preference, self.available_resource['computation_speed'])
        }


experiment1 = Experiment("Experiment 1", 15, 20)
experiment2 = Experiment("Experiment 2", 24, 10)
experiment3 = Experiment("Experiment 3", 5, 15)

available_resource = {'memory': 30, 'computation_speed': 40}

resource_allocator = ResourceAllocator([experiment1, experiment2, experiment3], available_resource)
allocated_resources = resource_allocator.allocate_resources()

total_utility = 0

for experiment, allocated_resource in allocated_resources.items():
    print(f"Experiment: {experiment.name} allocated resources: "
          f"{allocated_resource['memory']} {allocated_resource['computation_speed']}")
    total_utility += experiment.utility(allocated_resource)

print(f"Total utility: {total_utility}")
