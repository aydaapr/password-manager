facefrom tkinter import *
from tkinter import messagebox
import random
#import pyperclip
import json 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():

    
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
  password_symbols=[random.choice(symbols)for char in range(random.randint(2, 4))]
  password_numbers=[random.choice(numbers) for char in range(random.randint(2, 4))]
  password_list=password_letters+password_numbers+password_symbols
  random.shuffle(password_list)


  password = ""
  for char in password_list:
    password += char

  user_pass=password  
  entry_password.insert(0, string=password)
  #pyperclip.copy(password)

  #print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
  

  user_w=str(entry_website.get())
  user_e=str(entry_email.get())
  user_pass=str(entry_password.get())
  new_data={user_w:
            {
              "email":user_e,
              "password":user_pass,
          
            }
  }              

  if len(user_w)==0 or len(user_pass)==0:
    messagebox.showinfo(title="Ooop", message="please make sure you haven't left any fields empty")

  else:
    try:
      #reading old data
      with open("data.json", mode="r") as file: 
        data=json.load(file)
    except FileNotFoundError:
       with open("data.json", mode="w") as file: 
         json.dump(new_data, file, indent=4)
    else:
      #updating old data with new data
      data.update(new_data)
      with open("data.json", mode="w") as file: 
         #saving updated data
         json.dump(data, file, indent=4)


    finally:
      entry_website.delete(0, END)
      entry_password.delete(0, END)
  
  
  


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
  user_w=str(entry_website.get())

  try:
    with open("data.json", mode="r") as file: 
      data=json.load(file)
      try: 
        e_search=data[user_w]["email"]
        p_search=data[user_w]["password"]
        messagebox.showinfo(title=f"{user_w}", message=f"Email:{e_search}\nPassword:{p_search}")
        
      except KeyError:
        messagebox.showinfo(title="error", message=f"No details for {user_w} exists")
  

    
  except FileNotFoundError:
    
   messagebox.showinfo(title="error", message="No Data File Found")
  




# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas=Canvas(width=200, height=200, bg="white", highlightthickness=0)
password_pic=PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_pic)
canvas.grid(row=0, column=1)
#labels
website_label=Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)
email_label=Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)
pass_label=Label(text="Password:", bg="white")
pass_label.grid(row=3, column=0)

#entry
entry_website=Entry(width=33)
entry_website.grid(row=1, column=1)
entry_website.focus()
entry_email=Entry(width=52)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0, string="alipour_ayda98@yahoo.com")
entry_password=Entry(width=33)
entry_password.grid(row=3, column=1)


pass_button=Button(text="Generate Password", bg="white", command=generate_password)
pass_button.grid(row=3, column=2)

add_button=Button(text="Add", width=50, command=save_pass, bg="white")
add_button.grid(row=4, column=1, columnspan=2)

search_button=Button(text="Search", width=14, bg="white", command=find_password)
search_button.grid(row=1, column=2)
window.mainloop()