# Resource Allocator for Experiments 

## Overview
This Python project is designed to facilitate resource allocation for experiments using dictionaries to represent resources. It enables users to specify experiment preferences regarding computation speed and memory and then efficiently allocate available resources based on these preferences.

## Classes
- Experiment: Represents an experiment with a name, computation speed preference, memory preference, and allocated resources.
- ResourceAllocator: Allocates resources to experiments based on their preferences.

## Usage
1. Import the Experiment and ResourceAllocator classes into your Python script.
2. Create instances of experiments using the Experiment class, specifying computation speed and memory preferences as dictionaries.
3. Define the available resources using a dictionary with 'memory' and 'computation_speed' keys.
4. Create a ResourceAllocator instance with a list of experiments and the available resources.
5. Call the allocate_resources method of the ResourceAllocator instance to allocate resources to experiments.
6. Access the allocated resources for each experiment through the returned dictionary.
