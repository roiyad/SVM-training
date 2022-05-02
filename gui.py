__author__ = 'wolfenfeld'
from tkinter import *
from tkinter import ttk
from svm_handler import SVMHandler
from mail import sendemail
import threading


def create_thread(function, name):
    threading.Thread(target=function, name=name).start()


def run_gui():
    root = Tk()
    root.title("SVM GUI")
    # Here you need to set the frame, grid, row and column configurations of the root.
    root.geometry('240x100')
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=3)
    svm_handler = SVMHandler()
    mainframe = LabelFrame(root, padx=80, pady=80)
    mainframe.pack(padx=90, pady=90)
    actions_signals = [False, False]
    def update_label(message, row, column):
        label = Label(mainframe, text=message)
        label.grid(row=row, column=column, pady=50)
        root.after(5000, lambda: label.destroy())
    # Here you need to start the training of the svm. Remember, the other actions (testing/sending mail) must be
    # responsive to users actions (i.e. hitting their button)- How can this be achieved?

    def activate_train():
        if actions_signals[0]:
            update_label("the model has already trained the data", 5, 1)
            return
        print(threading.current_thread().name + " is running")
        svm_handler.train()
        update_label("The train has finished", 3, 0)
        actions_signals[0] = True
        return

    # Here you need to start the testing with the svm. Remember, the other actions (training/sending mail) must be
    # responsive to users actions (i.e. hitting their button)- How can this be achieved?
    def activate_test():
        print(threading.current_thread().name + " is running")
        if not actions_signals[0]:
            update_label("The system has not been trained yet", 3, 1)
            return
        else:
            svm_handler.test()
            update_label("The test has finished", 3, 2)
            actions_signals[1] = True
            return

    # Here you need to send an email with the svm testing result. Remember, the other actions (training/testing)
    # must be responsive to users actions (i.e. hitting their button)- How can this be achieved?
    def send_mail():
        if not actions_signals[1]:
            print("get life")
            update_label("The model has not been trained yet", 2, 3)
            return
        else:
            print(svm_handler.get_result())
            return
    train_button = Button(mainframe, text="Train", command=lambda: create_thread(activate_train, "training"))
    train_button.grid(row=0, column=0, padx=5, pady=5)
    test_button = Button(mainframe, text="Test", \
                         command=lambda: create_thread(activate_test, "testing"))
    test_button.grid(row=0, column=1, padx=5, pady=5)
    send_button = Button(mainframe, text="Send results", \
                         command=lambda: create_thread(send_mail, "sending mail"))
    send_button.grid(row=0, column=2, padx=5, pady=5)


    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    run_gui()
