from core.function_selector import select_key_functions

if __name__ == "__main__":
    from core.input_loader import load_dummy_input

    data = load_dummy_input()
    top_functions = select_key_functions(data["functions"], top_n=2)

    from pprint import pprint

    pprint(top_functions)
