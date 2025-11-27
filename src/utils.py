import os 

def load_examples(path):
    """Load few-shot examples from a text file"""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Examples file not found: {path}")
    
    with open(path, "r") as f:
        return f.read()
    

def build_few_shot_prompt(task, examples):
    """Attach examples above the task"""
    return f"{examples}\n\nTask:\n{task}"
