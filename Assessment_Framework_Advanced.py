
# Importing required libraries
from tkinter import Tk, Label, Button, Entry, StringVar, OptionMenu
import csv
import json

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
    url = aspect_url_mapping.get(aspect, None)
    if url:
        # Here, you would normally download code from the URL
        return '''
def main_function(problem, solution):
    return f"Assessment for {problem} and {solution} completed for aspect {aspect}."
'''

# Modify and execute the fetched code
def parameterize_and_execute_code(fetched_code, problem, solution):
    exec_locals = {}
    exec(fetched_code, {}, exec_locals)
    
    main_function = exec_locals['main_function']
    result = main_function(problem=problem, solution=solution)
    
    return result

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
        
        self.label_aspect = Label(master, text="Choose Assessment Aspect:")
        self.label_aspect.pack()
        self.aspect_options = list(aspect_url_mapping.keys())
        self.selected_aspect = StringVar(master)
        self.selected_aspect.set(self.aspect_options[0])
        self.dropdown_aspect = OptionMenu(master, self.selected_aspect, *self.aspect_options)
        self.dropdown_aspect.pack()
        
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
        self.aspect_options.append(new_aspect)
        self.dropdown_aspect['menu'].add_command(label=new_aspect, command=lambda value=new_aspect: self.selected_aspect.set(value))
        save_aspects_to_file()

    def submit(self):
        # problem = self.entry_problem.get()
        # solution = self.entry_solution.get()
        # selected_aspect = self.selected_aspect.get()
        
        # fetched_code = fetch_code_from_github(selected_aspect)
        # result = parameterize_and_execute_code(fetched_code, problem, solution)

        #test only
        result = "the grade for efficiency is 90"
        self.label_result.config(text=result)
        generate_csv(result)

# Initialize and run the Tkinter application
root = Tk()
app = AssessmentApp(root)
root.mainloop()
