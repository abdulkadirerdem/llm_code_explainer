if __name__ == "__main__":
    from core.input_loader import load_dummy_input
    from core.function_selector import select_key_functions
    from core.summarizer import summarize_function
    from core.formatter import format_as_markdown, format_as_json
    
    data = load_dummy_input()
    top_fns = select_key_functions(data["functions"], top_n=2)

    summarized = []
    for fn in top_fns:
        explanation = summarize_function(fn)
        summarized.append(
            {"name": fn["name"], "code": fn["code"], "explanation": explanation}
        )

    md = format_as_markdown(data["file"], summarized)
    with open("outputs/doc_output.md", "w") as f:
        f.write(md)

    json_out = format_as_json(data["file"], summarized)
    with open("outputs/run_output.json", "w") as f:
        f.write(json_out)

    print("✅ Output files saved in outputs/")
