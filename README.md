# AI Solution Assessment Program

## Table of Contents

1. [Introduction](#introduction)
2. [Instructions to Run](#instructions-to-run)
3. [How It Works](#how-it-works)
4. [Workflow](#workflow)
5. [Example Output](#example-output)
6. [Extendibility](#extendibility)

## Introduction

This program provides a graphical user interface (GUI) for users to input Python problems and their AI solutions for automated assessment. The assessment aspects can be chosen from a dropdown menu, and the results are displayed on the GUI.

## Instructions to Run

1. Clone the repository or download the source code.
2. Make sure you have Python 3.x installed on your machine.
3. Install the required package `requests`:
   ```
   pip install requests
   ```
4. Run the main Python file to start the application.
   ```
   python main.py
   ```

## How It Works

1. The user is presented with a GUI where they can input the Python problem and the corresponding AI solution.
2. A dropdown menu allows the user to choose the aspect(s) for assessment—like Correctness, Efficiency, or All aspects.
3. On submission, the program fetches the corresponding assessment code from specified GitHub repositories based on the selected aspects.
4. The fetched code is then executed dynamically to assess the user's solution, and the results are displayed back on the GUI.

## Workflow

1. User inputs the Python problem and solution in the GUI.
2. User selects the assessment aspect(s) from the dropdown.
3. Click the "Submit" button.
4. Program fetches the assessment code from GitHub repositories.
5. Fetched code is executed with the user's input as parameters.
6. Assessment result is displayed on the GUI.

## Example Output

If the user selects the "Efficiency" aspect, the output might look something like this:

```
The grade for efficiency is 90.
```

## Extendibility

Adding a new assessment aspect involves the following steps:

1. Upload the assessment code for the new aspect to a GitHub repository.
2. Update the `url_map` dictionary in the `fetch_code_from_github()` function to include the URL of the new GitHub repository.
3. Add the new aspect to the `aspect_options` list to make it available in the dropdown menu.

By following these steps, the program can easily be extended to support new assessment aspects. (An updated to the code will allow user to input the name of new aspect as well as the new url and will automatically add it to the program)
