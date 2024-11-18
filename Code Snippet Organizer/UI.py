from tkinter import *
from SnippetManager import *
from tkinter import messagebox

class SnippetManagerUI:
    def __init__(self) -> None:
        self.root=Tk()
        self.clear()
        self.obj1=SnippetManager_Authentication()
        self.obj2=SnippetManager(self.obj1)
       
        self.root.title('Code Snippet Organizer')
        self.root.iconbitmap('favicon.ico')
        self.root.geometry('400x500')
        
        self.root.configure(background='#EB8317')
        
        self.desktop()
        
        
        
        
        self.root.mainloop()
    def desktop(self):
        self.clear()
        label1=Label(self.root,text='🧑‍💻 Code Snippet Organizer 🧑‍💻',bg='#EB8317',fg='#10375C')
        label1.pack(pady=(30,30))
        label1.configure(font=('verdana',14,'bold'))
        
        btn1=Button(self.root,text='Login',bg='#10375C',fg='white',command=self.user_login_ui)
        btn1.pack(padx=25,pady=(20,10),anchor='w')
        btn1.configure(font=('verdana',13,'bold'))
        
        btn2=Button(self.root,text='SignUp',bg='#10375C',fg='white',command=self.signup_ui)
        btn2.pack(padx=25,pady=(20,10),anchor='w')
        btn2.configure(font=('verdana',13,'bold'))
        
        
        btn3=Button(self.root,text='Reset Password',bg='#10375C',fg='white',command=self.reset_password_ui)
        btn3.pack(padx=25,pady=(20,10),anchor='w')
        btn3.configure(font=('verdana',13,'bold'))

        btn4=Button(self.root,text='Exit',bg='#10375C',fg='white',command=self.exit)
        btn4.pack(padx=25,pady=(20,10),anchor='w')
        btn4.configure(font=('verdana',13,'bold'))
        
        
        label2=Label(self.root,text='Made by 💓',bg='#EB8317',fg='#10375C',font=("verdana",15,'bold'))
        label2.pack(padx=(30,50),anchor='se')
        
           
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
        
    def user_login_ui(self):
        self.clear()
        self.root.configure(background='#EB8317')
        
        label1=Label(self.root,text='🧑‍💻 Code Snippet Organizer 🧑‍💻',bg='#EB8317',fg='#10375C')
        label1.pack(pady=(30,30))
        label1.configure(font=('verdana',14,'bold'))
        
        label2=Label(self.root,text='Login Here 🧑‍💻',bg='#EB8317',fg='#10375C')
        label2.pack(pady=(30,30))
        label2.configure(font=('verdana',14,'bold'))
        
        email=Label(self.root,text="Enter your email",bg="#EB8317",fg="#10375C",font=('verdana',13,'bold'))
        email.pack(pady=(20,10),padx=(45,10),anchor='w')
        self.email_value=Entry(self.root,width=50)
        self.email_value.pack(ipady=4)
        
        password=Label(self.root,text="Enter your password",bg="#EB8317",fg="#10375C",font=('verdana',13,'bold'))
        password.pack(pady=(20,10),padx=(45,10),anchor='w')
        self.password_value=Entry(self.root,width=50,show='*')
        self.password_value.pack(ipady=4)
        
        
        btn=Button(self.root,text='Login',width=8,bg="#10375C",fg="#EB8317",font=('verdana',10,'bold'),command=self.login_process)
        btn.pack(pady=(10,10),padx=(48,10),anchor='w')
        
     
        label2=Label(self.root,text='Made by 💓',bg='#EB8317',fg='#10375C',font=("verdana",15,'bold'))
        label2.pack(padx=(30,50),anchor='se')
        goback=Button(self.root,text="Go Back",bg="#10375C",fg="#EB8317",font=('verdana',10,'bold'),command=self.desktop)    
        goback.pack(pady=(20,10),padx=(45,10),anchor='w')
    
    def signup_ui(self):
        self.clear()
        self.root.geometry('400x800')
        self.root.configure(background='#EB8317')
        
        label1=Label(self.root,text='🧑‍💻 Code Snippet Organizer 🧑‍💻',bg='#EB8317',fg='#10375C')
        label1.pack(pady=(30,30))
        label1.configure(font=('verdana',14,'bold'))
        
        label2=Label(self.root,text='Signup Here 🧑‍💻',bg='#EB8317',fg='#10375C')
        label2.pack(pady=(30,30))
        label2.configure(font=('verdana',14,'bold'))
        
        
        name=Label(self.root,text="Enter your name",bg="#EB8317",fg="#10375C",font=('verdana',13,'bold'))
        name.pack(pady=(20,10),padx=(45,10),anchor='w')
        self.name_value=Entry(self.root,width=50)
        self.name_value.pack(ipady=4)
        
        
        email=Label(self.root,text="Enter your email",bg="#EB8317",fg="#10375C",font=('verdana',13,'bold'))
        email.pack(pady=(20,10),padx=(45,10),anchor='w')
        self.email_value=Entry(self.root,width=50)
        self.email_value.pack(ipady=4)
        
        password=Label(self.root,text="Enter your password",bg="#EB8317",fg="#10375C",font=('verdana',13,'bold'))
        password.pack(pady=(20,10),padx=(45,10),anchor='w')
        self.password_value=Entry(self.root,width=50,show='*')
        self.password_value.pack(ipady=4)
        
        question=Label(self.root,text="Enter your nickname",bg="#EB8317",fg="#10375C",font=('verdana',13,'bold'))
        question.pack(pady=(20,10),padx=(45,10),anchor='w')
        self.question_value=Entry(self.root,width=50)
        self.question_value.pack(ipady=4)
      
        confirm_password=Label(self.root,text="Confirm your password",bg="#EB8317",fg="#10375C",font=('verdana',13,'bold'))
        confirm_password.pack(pady=(20,10),padx=(45,10),anchor='w')
        self.confirm_password_value=Entry(self.root,width=50,show='*')
        self.confirm_password_value.pack(ipady=4)
        
        
        btn=Button(self.root,text='Signup',width=8,bg="#10375C",fg="#EB8317",font=('verdana',10,'bold'),command=self.signup_process)
        btn.pack(pady=(10,10),padx=(48,10),anchor='w')
        
        label2=Label(self.root,text='Made by 💓',bg='#EB8317',fg='#10375C',font=("verdana",15,'bold'))
        label2.pack(padx=(30,50),anchor='se')
        
        goback=Button(self.root,text="Go Back",bg="#10375C",fg="#EB8317",font=('verdana',10,'bold'),command=self.desktop)    
        goback.pack(pady=(20,10),padx=(45,10),anchor='w')
        
        
    def home_ui(self):
        self.clear()
        self.root.geometry('400x1000')
        self.root.configure(background='#EB8317')
        
        label1=Label(self.root,text='🧑‍💻 Code Snippet Organizer 🧑‍💻',bg='#EB8317',fg='#10375C')
        label1.pack(pady=(30,10))
        label1.configure(font=('verdana',14,'bold'))
        
        label2=Label(self.root,text='What do you want ? 🧑‍💻',bg='#EB8317',fg='#10375C')
        label2.pack(pady=(30,10))
        label2.configure(font=('verdana',14,'bold'))
        
        
        create=Button(self.root,text="Create Snippet",bg="#10375C",fg="#EB8317",font=('verdana',13,'bold'),command=self.create_snippet_ui)
        create.pack(pady=(20,10),padx=(45,10),anchor='w')
        
        
        read=Button(self.root,text="Read Snippet",bg="#10375C",fg="#EB8317",font=('verdana',13,'bold'),command=self.read_snippet_ui)
        read.pack(pady=(20,10),padx=(45,10),anchor='w')
       
        update=Button(self.root,text="Update Snippet",bg="#10375C",fg="#EB8317",font=('verdana',13,'bold'),command=self.update_snippet_ui)
        update.pack(pady=(20,10),padx=(45,10),anchor='w')
     
        
        delete=Button(self.root,text="Delete Snippet",bg="#10375C",fg="#EB8317",font=('verdana',13,'bold'),command=self.delete_snippet_ui)  
        delete.pack(pady=(20,10),padx=(45,10),anchor='w')
        
      
        search=Button(self.root,text="Search Snippet",bg="#10375C",fg="#EB8317",font=('verdana',13,'bold'),command=self.search_snippet_ui)  
        search.pack(pady=(20,10),padx=(45,10),anchor='w')
        
        
        
        save=Button(self.root,text="Save Snippet",bg="#10375C",fg="#EB8317",font=('verdana',13,'bold'),command=self.download_snippet_ui)    
        save.pack(pady=(20,10),padx=(45,10),anchor='w')
       
        
        goback=Button(self.root,text="Go Back",bg="#10375C",fg="#EB8317",font=('verdana',10,'bold'),command=self.desktop)    
        goback.pack(pady=(20,10),padx=(45,10),anchor='w')
       
        
        label2=Label(self.root,text='Made by 💓',bg='#EB8317',fg='#10375C',font=("verdana",15,'bold'))
        label2.pack(padx=(30,50),anchor='se')
        
        
        
        
    def create_snippet_ui(self):
        self.clear()
        self.root.geometry('400x700')
        
        lang=Label(self.root,text="Enter the programming language",bg="#EB8317",fg="#10375C",font=('verdana',13,'bold'))
        lang.pack(pady=(20,10),padx=(45,10),anchor='w')
        self.lang_value=Entry(self.root,width=50)
        self.lang_value.pack(ipady=4)
        
        code=Label(self.root,text="Enter the code",bg="#EB8317",fg="#10375C",font=('verdana',13,'bold'))
        code.pack(pady=(20,10),padx=(45,10),anchor='w')
        self.code_value=Entry(self.root,width=50)
        self.code_value.pack(ipady=4)
        
        desc=Label(self.root,text="Enter the description",bg="#EB8317",fg="#10375C",font=('verdana',13,'bold'))
        desc.pack(pady=(20,10),padx=(45,10),anchor='w')
        self.desc_value=Entry(self.root,width=50)
        self.desc_value.pack(ipady=4)
        
        btn=Button(self.root,text='Save',width=8,bg="#10375C",fg="#EB8317",font=('verdana',10,'bold'),command=self.create_snippet_process)
        btn.pack(pady=(10,10),padx=(48,10),anchor='w')
        
        label2=Label(self.root,text='Made by 💓',bg='#EB8317',fg='#10375C',font=("verdana",15,'bold'))
        label2.pack(padx=(30,50),anchor='se')
        
        goback=Button(self.root,text="Go Back",bg="#10375C",fg="#EB8317",font=('verdana',10,'bold'),command=self.home_ui)    
        goback.pack(pady=(20,10),padx=(45,10),anchor='w')
        
    def create_snippet_process(self):
        lang=self.lang_value.get()
        code=self.code_value.get()
        desc=self.desc_value.get()
        self.obj2.create_snippet(lang,code,desc)
        messagebox.showinfo('Success','Snippet saved successfully')
        self.home_ui()
        
        
    def read_snippet_ui(self):
        self.clear()
        self.root.geometry('600x600')
        res=self.obj2.read_snippet()
        if res==0:
            messagebox.showerror('Error','No snippets found')
            self.home_ui()
        else:
                        # Frame for Text widget and Scrollbar
            frame = Frame(self.root)
            frame.pack(fill=BOTH, expand=True)  # Expand to take up available space

            # Text widget
            text_widget = Text(frame, wrap='word', width=40, height=15)
            text_widget.pack(side=LEFT, fill=BOTH, expand=True)

            # Scrollbar
            scrollbar = Scrollbar(frame, orient=VERTICAL, command=text_widget.yview)
            scrollbar.pack(side=RIGHT, fill=Y)

            # Link Scrollbar to Text widget
            text_widget.config(yscrollcommand=scrollbar.set)

            # Insert sample data
            for i in res:
                text_widget.insert(END, f'# Snippet {i["id"]}\n')
                for k, v in i.items():
                    if k == "Code":
                        text_widget.insert(END, f"{k} :\n{v}\n")
                    else:
                        text_widget.insert(END, f"{k} : {v}\n")

            # Button below the Text widget
            btn = Button(
                self.root,
                text='Go Back',
                width=8,
                bg="white",
                fg="#EB8317",
                font=('verdana', 10, 'bold'),
                command=self.home_ui
            )
            btn.pack(pady=(10, 10))  # Add vertical padding to space it properly
         
                                
                    
                      


    
    def update_snippet_ui(self):
        res=self.obj2.read_snippet()
        if res==0:
            messagebox.showerror('Error','No snippets found')
            self.home_ui()
        else:
            self.clear()
            self.root.geometry("600x700")
            label1=Label(self.root,text='🧑‍💻 Code Snippet Organizer 🧑‍💻',bg='#EB8317',fg='#10375C')
            label1.pack(pady=(30,10))
            label1.configure(font=('verdana',14,'bold'))
            
            label2=Label(self.root,text='Here is your stored snippets 🧑‍💻',bg='#EB8317',fg='#10375C')
            label2.pack(pady=(30,10))
            label2.configure(font=('verdana',14,'bold'))
            
            frame = Frame(self.root)
            frame.pack(fill=BOTH, expand=True)  # Expand to take up available space

            # Text widget
            text_widget = Text(frame, wrap='word', width=40, height=15)
            text_widget.pack(side=LEFT, fill=BOTH, expand=True)

            # Scrollbar
            scrollbar = Scrollbar(frame, orient=VERTICAL, command=text_widget.yview)
            scrollbar.pack(side=RIGHT, fill=Y)

            # Link Scrollbar to Text widget
            text_widget.config(yscrollcommand=scrollbar.set)

            # Insert sample data
            for i in res:
                text_widget.insert(END, f'# Snippet {i["id"]}\n')
                for k, v in i.items():
                    if k == "Code":
                        text_widget.insert(END, f"{k} :\n{v}\n")
                    else:
                        text_widget.insert(END, f"{k} : {v}\n")
                
                
            
            # Button below the Text widget
            btn = Button(
                self.root,
                text='Update Snippet',
                width=15,
                bg="white",
                fg="#EB8317",
                font=('verdana', 10, 'bold'),
                command=self.update_snippet_details
            )
            btn.pack(pady=(10, 10))  # Add vertical padding to space it properly
            
            goback=Button(self.root,text="Go Back",bg="#10375C",fg="#EB8317",font=('verdana',10,'bold'),command=self.home_ui)    
            goback.pack(pady=(20,10),padx=(45,10),anchor='w')
            
        
    def update_snippet_details(self):
            self.clear()
            self.root.geometry("600x700")
            label1=Label(self.root,text='🧑‍💻 Code Snippet Organizer 🧑‍💻',bg='#EB8317',fg='#10375C')
            label1.pack(pady=(30,10))
            label1.configure(font=('verdana',14,'bold'))
            
            label2=Label(self.root,text='Update Snippet',bg='#EB8317',fg='#10375C')
            label2.pack(pady=(30,10))
            label2.configure(font=('verdana',14,'bold'))
            
            label3=Label(self.root,text='Enter the snippet id to update',bg='#EB8317',fg='#10375C')
            label3.pack(pady=(20,10),padx=(45,10),anchor='w')
            label3.configure(font=('verdana',13,'bold'))         
            self.id=Entry(self.root,width=50)
            self.id.pack(ipady=4)

            
            lang=Label(self.root,text="Enter the programming language",bg="#EB8317",fg="#10375C",font=('verdana',13,'bold'))
            lang.pack(pady=(20,10),padx=(45,10),anchor='w')
            self.lang_value=Entry(self.root,width=50)
            self.lang_value.pack(ipady=4)
            
            code=Label(self.root,text="Enter the code",bg="#EB8317",fg="#10375C",font=('verdana',13,'bold'))
            code.pack(pady=(20,10),padx=(45,10),anchor='w')
            self.code_value=Entry(self.root,width=50)
            self.code_value.pack(ipady=4)
            
            desc=Label(self.root,text="Enter the description",bg="#EB8317",fg="#10375C",font=('verdana',13,'bold'))
            desc.pack(pady=(20,10),padx=(45,10),anchor='w')
            self.desc_value=Entry(self.root,width=50)
            self.desc_value.pack(ipady=4)
          
            btn=Button(self.root,text='Update',width=8,bg="#10375C",fg="#EB8317",font=('verdana',10,'bold'),command=self.update_snippet_process)
            btn.pack(pady=(10,10),padx=(48,10),anchor='w')


    def update_snippet_process(self):
        id=self.id.get()
        lang=self.lang_value.get()
        code=self.code_value.get()
        desc=self.desc_value.get()
        res=self.obj2.update_snippet(id,lang,code,desc)
        if res==0:
            messagebox.showerror('Error','Snippet not found')
            self.home_ui()
        if res==1:
            messagebox.showinfo('Success','Snippet updated successfully')
            self.home_ui()
            




            
            
        
        
    
    def delete_snippet_ui(self):
            res=self.obj2.read_snippet()
            if res==0:
                messagebox.showerror('Error','No snippets found')
                self.home_ui()
            else:
                self.clear()
                self.root.geometry("600x700")
                label1=Label(self.root,text='🧑‍💻 Code Snippet Organizer 🧑‍💻',bg='#EB8317',fg='#10375C')
                label1.pack(pady=(30,10))
                label1.configure(font=('verdana',14,'bold'))
                
                label2=Label(self.root,text='Here is your stored snippets 🧑‍💻',bg='#EB8317',fg='#10375C')
                label2.pack(pady=(30,10))
                label2.configure(font=('verdana',14,'bold'))
                
                frame = Frame(self.root)
                frame.pack(fill=BOTH, expand=True)  # Expand to take up available space

                # Text widget
                text_widget = Text(frame, wrap='word', width=40, height=15)
                text_widget.pack(side=LEFT, fill=BOTH, expand=True)

                    # Scrollbar
                scrollbar = Scrollbar(frame, orient=VERTICAL, command=text_widget.yview)
                scrollbar.pack(side=RIGHT, fill=Y)

                    # Link Scrollbar to Text widget
                text_widget.config(yscrollcommand=scrollbar.set)

                    # Insert sample data
                for i in res:
                        text_widget.insert(END, f'# Snippet {i["id"]}\n')
                        for k, v in i.items():
                            if k == "Code":
                                 text_widget.insert(END, f"{k} :\n{v}\n")
                            else:
                                 text_widget.insert(END, f"{k} : {v}\n")
                
                
            
            # Button below the Text widget
            btn = Button(
                self.root,
                text='Delete Snippet',
                width=15,
                bg="white",
                fg="#EB8317",
                font=('verdana', 10, 'bold'),
                command=self.delete_snippet_details
                
            )
            btn.pack(pady=(10, 10))  # Add vertical padd
            
            goback=Button(self.root,text="Go Back",bg="#10375C",fg="#EB8317",font=('verdana',10,'bold'),command=self.home_ui)    
            goback.pack(pady=(20,10),padx=(45,10),anchor='w')
            
            
    def delete_snippet_details(self):
            self.clear()
            self.root.geometry("600x700")
            label1=Label(self.root,text='🧑‍💻 Code Snippet Organizer 🧑‍💻',bg='#EB8317',fg='#10375C')
            label1.pack(pady=(30,10))
            label1.configure(font=('verdana',14,'bold'))
            
            label2=Label(self.root,text='Update Snippet',bg='#EB8317',fg='#10375C')
            label2.pack(pady=(30,10))
            label2.configure(font=('verdana',14,'bold'))
            
            label3=Label(self.root,text='Enter the snippet id to update',bg='#EB8317',fg='#10375C')
            label3.pack(pady=(20,10),padx=(45,10),anchor='w')
            label3.configure(font=('verdana',13,'bold'))         
            self.id=Entry(self.root,width=50)
            self.id.pack(ipady=4)
            
            btn=Button(self.root,text='Delete',width=8,bg="#10375C",fg="#EB8317",font=('verdana',10,'bold'),command=self.delete_snippet_process)
            btn.pack(pady=(10,10),padx=(48,10),anchor='w')
            
    def delete_snippet_process(self):
        id=self.id.get()
        res=self.obj2.delete_snippet(id)
        if res==1:
            messagebox.showinfo('Success','Snippet deleted successfully')
            self.home_ui()
        
    def search_snippet_ui(self):
        self.clear()
        self.root.geometry("600x700")
        label1=Label(self.root,text='🧑‍💻 Code Snippet Organizer 🧑‍💻',bg='#EB8317',fg='#10375C')
        label1.pack(pady=(30,10))
        label1.configure(font=('verdana',14,'bold'))
        
        label2=Label(self.root,text='Search Snippet',bg='#EB8317',fg='#10375C')
        label2.pack(pady=(30,10))
        label2.configure(font=('verdana',14,'bold'))
        
        label3=Label(self.root,text='Enter the keyword to search or "exit" to exit ',bg='#EB8317',fg='#10375C')
        label3.pack(pady=(20,10),padx=(45,10),anchor='w')
        label3.configure(font=('verdana',13,'bold'))
        
        self.keyword=Entry(self.root,width=50)
        self.keyword.pack(ipady=4)
        
        btn=Button(self.root,text='Search',width=8,bg="#10375C",fg="#EB8317",font=('verdana',10,'bold'),command=self.search_snippet_process)
        btn.pack(pady=(10,10),padx=(48,10),anchor='w')
        
        goback=Button(self.root,text="Go Back",bg="#10375C",fg="#EB8317",font=('verdana',10,'bold'),command=self.home_ui)    
        goback.pack(pady=(20,10),padx=(45,10),anchor='w')
    def search_snippet_process(self):
        keyword=self.keyword.get()
        res=self.obj2.search_snippet(keyword)
        if res==0:
            self.home_ui()
            self.home_ui()
        elif res==1:
            messagebox.showerror('Error','No snippets found')
            self.home_ui()
        else:
            self.clear()
            self.root.geometry("600x700")
            label1=Label(self.root,text='🧑‍💻 Code Snippet Organizer 🧑‍💻',bg='#EB8317',fg='#10375C')
            label1.pack(pady=(30,10))
            label1.configure(font=('verdana',14,'bold'))
            
            label2=Label(self.root,text='Here is your stored snippets 🧑‍💻',bg='#EB8317',fg='#10375C')
            label2.pack(pady=(30,10))
            label2.configure(font=('verdana',14,'bold'))
            
            frame = Frame(self.root)
            frame.pack(fill=BOTH, expand=True)  # Expand to take up available space

            # Text widget
            text_widget = Text(frame, wrap='word', width=40, height=15)
            text_widget.pack(side=LEFT, fill=BOTH, expand=True)

            # Scrollbar
            scrollbar = Scrollbar(frame, orient=VERTICAL, command=text_widget.yview)
            scrollbar.pack(side=RIGHT, fill=Y)

            # Link Scrollbar to Text widget
            text_widget.config(yscrollcommand=scrollbar.set)

            # Insert sample data
            for i in res:
                text_widget.insert(END, f'# Snippet {i["id"]}\n')
                for k, v in i.items():
                    if k == "Code":
                        text_widget.insert(END, f"{k} :\n{v}\n")
                    else:
                        text_widget.insert(END, f"{k} : {v}\n")
                    
            btn = Button(
                self.root,
                text='Go Back',
                width=8,
                bg="white",
                fg="#EB8317",
                font=('verdana', 10, 'bold'),
                command=self.home_ui
            )
            btn.pack(pady=(10, 10))  # Add vertical padding to space it properly

        
                                
                
                
            
            
            
    def download_snippet_ui(self): 
        res=self.obj2.save_snippet() 
        if res==0:
            messagebox.showerror('Error','No snippets found')
            self.home_ui()
        else:
            messagebox.showinfo('Success','Snippets saved successfully')
            self.home_ui()
        goback=Button(self.root,text="Go Back",bg="#10375C",fg="#EB8317",font=('verdana',10,'bold'),command=self.home_ui)    
        goback.pack(pady=(20,10),padx=(45,10),anchor='w')
        
    
    def login_process(self):
        email=self.email_value.get()
        password=self.password_value.get()
        res=self.obj1.user_login(email,password)
        if res==0:
            messagebox.showerror('Error','Incorrect Email or Password')
            self.user_login_ui()
        
        elif res==1:
            messagebox.showerror('Error',"Not registered yet,Please sign up first")
            self.signup_ui()
        else:
            messagebox.showinfo('Success','Login Successful')
            self.home_ui()                
            
            
    def signup_process(self):
        name=self.name_value.get()
        email=self.email_value.get()
        password=self.password_value.get()
        confirm_password=self.confirm_password_value.get()
        security_question=self.question_value.get()
        res=self.obj1.user_signup(name,email,password,confirm_password,security_question)
        if res==0:
            messagebox.showerror('Error','Incorrect Email or Password')
            self.signup_ui()
        elif res==1:
            messagebox.showinfo('Error','Email already exist')
            self.user_login_ui()
        else:
            messagebox.showerror('Success','Registration Successful')
            self.user_login_ui()
                
                
    def reset_password_ui(self):
        self.clear()
        self.root.geometry('400x700')
        label1=Label(self.root,text='🧑‍💻 Code Snippet Organizer 🧑‍💻',bg='#EB8317',fg='#10375C')
        label1.pack(pady=(30,30))
        label1.configure(font=('verdana',14,'bold'))
        
        label2=Label(self.root,text='Enter the email to reset password',bg='#EB8317',fg='#10375C',font=('verdana',13,'bold'))
        label2.pack(pady=(20,10),padx=(45,10),anchor='w')
        
        self.email=Entry(self.root,width=50)
        self.email.pack(ipady=4)
        
        label3=Label(self.root,text='Enter your nickname',bg='#EB8317',fg='#10375C',font=('verdana',13,'bold'))
        label3.pack(pady=(20,10),padx=(45,10),anchor='w')
                
        self.nickname=Entry(self.root,width=50)
        self.nickname.pack(ipady=4)
        
        label3=Label(self.root,text='Enter your new password',bg='#EB8317',fg='#10375C',font=('verdana',13,'bold'))
        label3.pack(pady=(20,10),padx=(45,10),anchor='w')
                
        self.password=Entry(self.root,width=50)
        self.password.pack(ipady=4)
            
        label5=Label(self.root,text='Confirm your new password',bg='#EB8317',fg='#10375C',font=('verdana',13,'bold'))
        label5.pack(pady=(20,10),padx=(45,10),anchor='w')
                        
        self.confirm_password=Entry(self.root,width=50)
        self.confirm_password.pack(ipady=4)
            
        
        btn=Button(self.root,text='Reset',width=8,bg="#10375C",fg="#EB8317",font=('verdana',10,'bold'),command=self.reset_password_process)
        btn.pack(pady=(10,10),padx=(48,10),anchor='w')
        
        goback=Button(self.root,text="Go Back",bg="#10375C",fg="#EB8317",font=('verdana',10,'bold'),command=self.desktop)    
        goback.pack(pady=(20,10),padx=(45,10),anchor='w')
        
    def reset_password_process(self):
        email=self.email.get()
        nickname=self.nickname.get()
        password=self.password.get()
        confirm_password=self.confirm_password.get()
        res=self.obj1.reset(email,nickname,password,confirm_password)
        if res==0:
            messagebox.showerror('Error','Not registered yet')
            self.desktop()
        elif res==1:
            messagebox.showerror('Error','Incorrect Nickname')
            self.reset_password_ui()
        elif res==2:
            messagebox.showerror('Error','Incorrect Password')
            self.reset_password_ui()
        else:
            messagebox.showinfo('Success','Password Reset Successful')
            self.user_login_ui()
            
    def reseit(self):
        password=self.password.get()
        confirm_password=self.confirm_password.get()
        res=self.obj1.reset_password_process(self.email.get(),self.nickname.get(),password,confirm_password)
        if res==0:
            messagebox.showerror('Error','Incorrect Password')
            self.reset_password_ui()
        else:
            messagebox.showinfo('Success','Password Reset Successful')
            self.user_login_ui()
            
            
    def exit(self):
        self.root.destroy()



SnippetManagerUI()