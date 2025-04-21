from core.input_loader import load_dummy_input
from core.function_selector import select_key_functions
from core.summarizer import summarize_function
from core.formatter import format_as_json, format_as_markdown
import os


def run_pipeline(
    input_path: str = "examples/dummy_input.json", output_dir: str = "outputs"
):
    print("🚀 Loading input...")
    data = load_dummy_input(input_path)
    file_name = data["file"]
    functions = data["functions"]

    print("🔍 Selecting key functions...")
    selected = select_key_functions(functions, top_n=3)

    summarized = []
    for fn in selected:
        print(f"🧠 Summarizing `{fn['name']}`...")
        explanation = summarize_function(fn)
        summarized.append(
            {"name": fn["name"], "code": fn["code"], "explanation": explanation}
        )

    print("📦 Formatting outputs...")
    os.makedirs(output_dir, exist_ok=True)

    # JSON Output
    with open(os.path.join(output_dir, "run_output.json"), "w", encoding="utf-8") as f:
        f.write(format_as_json(file_name, summarized))

    # Markdown Output
    with open(os.path.join(output_dir, "doc_output.md"), "w", encoding="utf-8") as f:
        f.write(format_as_markdown(file_name, summarized))

    print("✅ All done! Outputs saved in:", output_dir)


if __name__ == "__main__":
    run_pipeline()
