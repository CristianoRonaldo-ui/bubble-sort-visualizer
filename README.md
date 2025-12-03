# Bubble Sort Interactive Visualizer


Problem Breakdown & Computational Thinking
Problem Definition

This app helps users understand how the Bubble Sort algorithm works by:

Taking a list of numbers as input.

Allowing the user to choose ascending or descending order.

Optionally showing each comparison and swap step-by-step.

Decomposition

The problem is broken down into smaller parts:

Parse the user input (comma-separated string → list of numbers).

Implement the Bubble Sort algorithm.

Add an option for ascending or descending order.

Collect and display step-by-step logs of each pass.

Build a simple UI for input and output using Gradio.

Pattern Recognition

The algorithm repeatedly:

Compares adjacent elements.

Swaps them if they are in the wrong order.

Each pass "bubbles" the largest (or smallest) element to its correct position.

The process repeats until no more swaps are needed.

Abstraction

The user only sees:

A text box for entering numbers.

Buttons/options to control the sort.

The final sorted list.

(Optionally) a human-readable log of each step.

Internal implementation details (loops, indices) are hidden behind a simple interface.

Algorithm Design

Input → Processing → Output

Input:

String of comma-separated numbers (e.g., "3, 1, 4, 1, 5").

Sort order: Ascending or Descending.

Option: show step-by-step log (True/False).

Processing:

Parse the string into a list of floats.

Run Bubble Sort with:

Nested loops over the list.

Conditional comparisons based on order.

Early stopping when no swaps occur in a pass.

Record steps (comparisons, swaps, list state) if step-by-step is enabled.

Output:

Sorted list as a comma-separated string.

Step-by-step description of the algorithm’s behavior (if enabled).

Steps to Run
1. Run locally

Clone the repository:

git clone https://github.com/YOUR_GITHUB_USERNAME/bubble-sort-visualizer.git
cd bubble-sort-visualizer


Install dependencies:

pip install -r requirements.txt


Run the app:

python app.py


Open the URL shown in your terminal.

2. Hugging Face Link

Your deployed app:

https://huggingface.co/spaces/solitudee4907/bubble-sort-visualizer

Author & Acknowledgment

Author: Vũ Bảo (CISC-121 Student)

Course: CISC-121
