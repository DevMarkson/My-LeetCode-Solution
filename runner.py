import importlib
import sys


def run_dsa_code(module_name):
    # Dynamically import the module (your DSA code file)
    module = importlib.import_module(module_name)

    # Read input from file
    with open("DSA/input.txt", "r") as f:
        input_data = eval(f.read().strip())

    # Assuming the DSA function is the first callable in the module
    dsa_function = getattr(module, dir(module)[0])

    # Run the function and capture the result
    result = dsa_function(input_data)

    # Write output to file
    with open("DSA/output.txt", "w") as f:
        f.write(str(result))

    print(f"Result: {result}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python runner.py <module_name>")
    else:
        run_dsa_code(sys.argv[1])
