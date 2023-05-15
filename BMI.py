import tkinter as tk

def cal(weight, heightcm):
    if weight <= 0 or weight >= 400:
        result_label.config(text="Enter valid \nweight")
        return None

    if heightcm <=0 or heightcm>=300:
        result_label.config(text="Enter valid \nheight")
        return None

    height = heightcm/100
    BMI = float((weight)/(height*height))
    return BMI

def check(BMI):
    if BMI is None:
        return
    elif BMI <= 18.5:
        result_label.config(text="Your BMI is: {:.1f}\nYou are \nunder weight, \neat more!".format(BMI))

    elif 18.5 < BMI <= 24.9:
        result_label.config(text="Your BMI is: {:.1f}\nYou are \nHealthy!".format(BMI))

    elif 24.9 < BMI <= 29.9:
        result_label.config(text="Your BMI is: {:.1f}\nYou are \noverweight!".format(BMI))

    elif 29.9 < BMI <= 100:
        result_label.config(text="Your BMI is: {:.1f}\nYou are \nobese, you are \nat a risk!".format(BMI))
    
    else:
        result_label.config(text="Your BMI is: {:.1f}\nYou cannot be a human!".format(BMI))

def main():
    weight = float(weight_entry.get())
    heightcm = float(height_entry.get())

    BMI = cal(weight, heightcm)
    check(BMI)

# Create main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x350")

# Create labels and entries for weight and height
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.pack(side=tk.TOP, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.pack(side=tk.TOP, padx=10, pady=5)
height_label = tk.Label(root, text="Height (cm):")
height_label.pack(side=tk.TOP, padx=10, pady=5)
height_entry = tk.Entry(root)
height_entry.pack(side=tk.TOP, padx=10, pady=5)

# Create button to calculate BMI
calculate_button = tk.Button(root, text="Calculate", command=main)
calculate_button.pack(side=tk.TOP, padx=10, pady=10)

# Create label to display result
result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="white", width=20, height=5)
result_label.pack(side=tk.TOP, padx=10, pady=10)

root.mainloop()
