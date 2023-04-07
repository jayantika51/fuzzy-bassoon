from tkinter import*
root = Tk()
root.geometry("400x250")

list_a = ["Naruto","sasuke","Tori","Gaara"]
student_name = {"Name":"Saakura", "Age":"12"}

try:
    print(list_a[4])
    print(student_name["Ino"])
    
except IndexError : 
    messagebox.showinfo("Error","This index does not exist")
        
except KeyError : 
    messagebox.showinfo("Error","This key does not exist")
        
root.mainloop()