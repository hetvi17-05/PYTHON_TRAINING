#dictionary as a parameter
def student(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} = {v}")
student(name="hetvi", subject="python")