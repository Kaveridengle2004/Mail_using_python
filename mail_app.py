import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    try:
        # Email details
        sender_email = "your_email"
        sender_password = "your_password"
        recipient_email = recipient_entry.get()
        subject = subject_entry.get()
        body = body_text.get("1.0", tk.END)

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        # Sending the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()

        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Setting up the main window
root = tk.Tk()
root.title("Mail Application")

# Creating UI components
tk.Label(root, text="Recipient Email:").grid(row=0, column=0, padx=10, pady=10)
recipient_entry = tk.Entry(root, width=50)
recipient_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Subject:").grid(row=1, column=0, padx=10, pady=10)
subject_entry = tk.Entry(root, width=50)
subject_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Body:").grid(row=2, column=0, padx=10, pady=10)
body_text = tk.Text(root, height=10, width=50)
body_text.grid(row=2, column=1, padx=10, pady=10)

send_button = tk.Button(root, text="Send Email", command=send_email)
send_button.grid(row=3, column=0, columnspan=2, pady=10)

# Running the application
root.mainloop()
