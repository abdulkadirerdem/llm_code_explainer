from core.input_loader import load_dummy_input
from core.function_selector import select_key_functions
from core.summarizer import summarize_function

if __name__ == "__main__":

    data = load_dummy_input()
    top_fns = select_key_functions(data["functions"], top_n=2)

    for fn in top_fns:
        explanation = summarize_function(fn)
        print(f"\n🔍 {fn['name']} Açıklaması:\n{explanation}")
