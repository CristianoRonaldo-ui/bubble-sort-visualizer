import gradio as gr

def parse_input_numbers(input_str: str):
    """
    Parse a comma-separated string of numbers into a Python list of floats.
    Accepts spaces, e.g. '3, 1, 4.5'.
    """
    if not input_str or input_str.strip() == "":
        raise ValueError("Input is empty. Please enter at least one number.")

    parts = input_str.split(",")
    numbers = []
    for p in parts:
        p = p.strip()
        if p == "":
            continue
        try:
            num = float(p)
        except ValueError:
            raise ValueError(f"'{p}' is not a valid number.")
        numbers.append(num)

    if len(numbers) == 0:
        raise ValueError("No valid numbers found. Please check your input.")

    return numbers


def bubble_sort(numbers, order="Ascending", show_steps=True):
    """
    Bubble Sort implementation with optional step-by-step logging.
    Args:
        numbers (list[float]): list of numbers to sort
        order (str): "Ascending" or "Descending"
        show_steps (bool): whether to record each step
    Returns:
        sorted_numbers (list[float]), steps_log (list[str])
    """
    arr = numbers.copy()
    n = len(arr)
    steps_log = []

    ascending = (order == "Ascending")

    if show_steps:
        steps_log.append(f"Initial list: {arr}")

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if ascending:
                condition = arr[j] > arr[j + 1]
            else:
                condition = arr[j] < arr[j + 1]

            if condition:
                
                if show_steps:
                    steps_log.append(
                        f"Pass {i+1}, compare index {j} and {j+1}: "
                        f"swap {arr[j]} and {arr[j+1]}"
                    )
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            else:
                if show_steps:
                    steps_log.append(
                        f"Pass {i+1}, compare index {j} and {j+1}: no swap"
                    )

        if show_steps:
            steps_log.append(f"After pass {i+1}: {arr}")

        
        if not swapped:
            if show_steps:
                steps_log.append(
                    f"No swap in pass {i+1}, the list is already sorted. Stopping early."
                )
            break

    if show_steps:
        steps_log.append(f"Final sorted list: {arr}")

    return arr, steps_log


def run_bubble_sort(input_numbers: str, order: str, show_steps: bool):
    """
    Wrapper function for Gradio interface.
    Takes raw string input, parses it, runs Bubble Sort, and formats output.
    """
    try:
        numbers = parse_input_numbers(input_numbers)
    except ValueError as e:
        
        return "", f"Error: {str(e)}\nExample input: 3, 1, 4, 1, 5"

    sorted_list, steps_log = bubble_sort(numbers, order=order, show_steps=show_steps)

    
    sorted_str = ", ".join(str(x) for x in sorted_list)

    if show_steps:
        steps_text = "\n".join(steps_log)
    else:
        steps_text = (
            "Step-by-step log is hidden.\n"
            "Check the 'Show step-by-step' box and run again to see the details."
        )

    return sorted_str, steps_text


with gr.Blocks() as demo:
    gr.Markdown(
        """
    # Bubble Sort Interactive Visualizer
    Enter a list of numbers separated by commas, choose the sort order,
    and see how the Bubble Sort algorithm works step by step.
    **Example:** `3, 1, 4, 1, 5`
    """
    )

    with gr.Row():
        input_numbers = gr.Textbox(
            label="List of numbers (comma-separated)",
            placeholder="e.g. 3, 1, 4, 1, 5",
        )

    order = gr.Radio(
        ["Ascending", "Descending"],
        value="Ascending",
        label="Sort order",
    )

    show_steps = gr.Checkbox(
        label="Show step-by-step",
        value=True,
    )

    run_button = gr.Button("Run Bubble Sort")

    with gr.Row():
        sorted_output = gr.Textbox(
            label="Sorted Result",
            interactive=False,
        )

    steps_output = gr.Textbox(
        label="Step-by-step log",
        lines=15,
        interactive=False,
    )

    run_button.click(
        fn=run_bubble_sort,
        inputs=[input_numbers, order, show_steps],
        outputs=[sorted_output, steps_output],
    )

if __name__ == "__main__":
    demo.launch()
