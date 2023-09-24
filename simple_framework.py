
# Importing required libraries
from tkinter import Tk, Label, Button, Entry, StringVar, Listbox, MULTIPLE
import csv
import json
import requests

# Default aspects and their URLs
default_aspect_url_mapping = {
    'Correctness': 'https://github.com/user/repo/blob/main/correctness.py',
    'Efficiency': 'https://github.com/user/repo/blob/main/efficiency.py'
}

# Function to save aspects to a JSON file
def save_aspects_to_file():
    with open('aspects.json', 'w') as f:
        json.dump(aspect_url_mapping, f)

# Function to load aspects from a JSON file
def load_aspects_from_file():
    try:
        with open('aspects.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return default_aspect_url_mapping

# Initialize aspect_url_mapping from the file or use default
aspect_url_mapping = load_aspects_from_file()

# Function to fetch code from GitHub using URL (Placeholder)
def fetch_code_from_github(aspect):
    raw_url = aspect_url_mapping.get(aspect, None)
    if raw_url:
        response = requests.get(raw_url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Error fetching the code: {response.status_code}"
    else:
        return f"No URL mapping found for aspect: {aspect}" '''
def main_function(problem, solution):
    return f"Assessment for {problem} and {solution} completed for aspect {aspect}."
'''

# Modify and execute the fetched code
# def parameterize_and_execute_code(fetched_code, problem, solution):
#     exec_locals = {}
#     exec(fetched_code, {}, exec_locals)
    
#     main_function = exec_locals['main_function']
#     result = main_function(problem=problem, solution=solution)
    
#     return result



def parameterize_and_execute_code(fetched_code, problem, solution):
    # Remove any example usage from the fetched code.
    # This is to avoid running the function without the required parameters.
    fetched_code = fetched_code.split("# Example usage:")[0]
    
    # Append a new function call at the end of the fetched code.
    # This will call the get_grade function with problem and solution as arguments.
    modified_code = fetched_code + f'\nresult = get_grade("{problem}", "{solution}")'
    
    exec_locals = {'problem': problem, 'solution': solution, 'result': None}
    exec(modified_code, {}, exec_locals)
    
    return exec_locals['result']

# Function to generate CSV
def generate_csv(result):
    lines = result.split('. ')
    rows = []
    for line in lines:
        if not line:
            continue
        aspect_str, score_str = line.split(' is ')
        aspect = aspect_str.split(' ')[-1]
        score = int(score_str)
        rows.append([aspect, score])

    with open('assessment_feedback.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Aspect', 'Score'])
        csvwriter.writerows(rows)

# Create a class for the GUI
class AssessmentApp:
    def __init__(self, master):
        self.master = master
        master.title("AI Solution Assessment")
        
        self.label_problem = Label(master, text="Enter your Python Problem:")
        self.label_problem.pack()
        self.entry_problem = Entry(master)
        self.entry_problem.pack()
        
        self.label_solution = Label(master, text="Enter your Python Solution:")
        self.label_solution.pack()
        self.entry_solution = Entry(master)
        self.entry_solution.pack()
        
        self.label_aspect = Label(master, text="Choose Assessment Aspects:")
        self.label_aspect.pack()
        self.listbox_aspect = Listbox(master, selectmode=MULTIPLE)
        for aspect in aspect_url_mapping.keys():
            self.listbox_aspect.insert('end', aspect)
        self.listbox_aspect.pack()
        
        self.label_new_aspect = Label(master, text="Add New Aspect:")
        self.label_new_aspect.pack()
        self.entry_new_aspect = Entry(master)
        self.entry_new_aspect.pack()
        
        self.label_new_url = Label(master, text="Aspect URL:")
        self.label_new_url.pack()
        self.entry_new_url = Entry(master)
        self.entry_new_url.pack()
        
        self.add_aspect_button = Button(master, text="Add Aspect", command=self.add_aspect)
        self.add_aspect_button.pack()

        self.submit_button = Button(master, text="Submit", command=self.submit)
        self.submit_button.pack()
        
        self.label_result = Label(master, text="")
        self.label_result.pack()

    def add_aspect(self):
        new_aspect = self.entry_new_aspect.get()
        new_url = self.entry_new_url.get()
        aspect_url_mapping[new_aspect] = new_url
        self.listbox_aspect.insert('end', new_aspect)
        save_aspects_to_file()

    def submit(self):
        problem = self.entry_problem.get()
        solution = self.entry_solution.get()
        selected_aspects = [self.listbox_aspect.get(i) for i in self.listbox_aspect.curselection()]
        
        results = []
        for aspect in selected_aspects:
            fetched_code = fetch_code_from_github(aspect)
            result = parameterize_and_execute_code(fetched_code, problem, solution)
            results.append(result)
        
        final_result = '. '.join(results)
        self.label_result.config(text=final_result)

        # testing only
        # final_result = "The grade for Efficiency is 90"
        # self.label_result.config(text=final_result)
        generate_csv(final_result)

# Initialize and run the Tkinter application
root = Tk()
app = AssessmentApp(root)
root.mainloop()
