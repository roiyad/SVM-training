__author__ = 'wolfenfeld'

import threading
from tkinter import *

import mail
from svm_handler import SVMHandler


def run_gui():
    root = Tk()
    root.title("SVM GUI")
    # Here you need to set the frame, grid, row and column configurations of the root.
    root.geometry('600x300')
    root.resizable(False, False)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=3)
    svm_handler = SVMHandler()
    mainframe = LabelFrame(root, text="SVM GUI Roi Yad Shalom", padx=70, pady=70)
    mainframe.pack(padx=40, pady=40, expand="No")
    actions_signals = [False, False]
    train_button = Button(mainframe, text="Train")
    test_button = Button(mainframe, text="Test", state=DISABLED)
    send_button = Button(mainframe, text="Send results", state=DISABLED)
    # Here you need to start the training of the svm. Remember, the other actions (testing/sending mail) must be
    # responsive to users actions (i.e. hitting their button)- How can this be achieved?

    def activate_train():
        if actions_signals[0]:
            update_label("Model is trained, test it now ", 3, 1)
            return
        disable_buttons([train_button, test_button, send_button])
        print(threading.current_thread().name + " is running")
        label = Label(mainframe, text="Training...")
        label.grid(row=2, column=1, pady=10)
        svm_handler.train()
        label.destroy()
        update_label("The train has finished", 2, 1)
        actions_signals[0] = True
        train_button.config(state=ACTIVE)
        test_button.config(state=ACTIVE)
        return

    # Here you need to start the testing with the svm. Remember, the other actions (training/sending mail) must be
    # responsive to users actions (i.e. hitting their button)- How can this be achieved?
    def activate_test():
        print(threading.current_thread().name + " is running")
        if actions_signals[1]:
            update_label("Test finished, send the result now", 3, 1)
            test_button.config(state=ACTIVE)
            return
        else:
            disable_buttons([train_button, test_button, send_button])
            label = Label(mainframe, text="Testing...")
            label.grid(row=2, column=2, pady=10)
            svm_handler.test()
            update_label("The test has finished", 2, 1)
            actions_signals[1] = True
            enable_buttons([train_button, test_button, send_button])
            label.destroy()
            return

    # Here you need to send an email with the svm testing result. Remember, the other actions (training/testing)
    # must be responsive to users actions (i.e. hitting their button)- How can this be achieved?
    def send_mail():
        disable_buttons([train_button, test_button, send_button])
        send_button.config(state=DISABLED)
        update_label("Sending mail", 2, 1)
        message = "The error percentage of the model is " + str(svm_handler.error_pct)
        enable_buttons([train_button, test_button, send_button])
        mail.sendemail(message)
        return

    def update_label(message, row, column):
        label = Label(mainframe, text=message)
        label.grid(row=row, column=column, pady=10)
        root.after(5000, lambda: label.destroy())

    def disable_buttons(button_array):
        for button in button_array:
            button.config(state=DISABLED)

    def enable_buttons(button_array):
        for button in button_array:
            button.config(state=ACTIVE)

    train_button.config(command=lambda: create_thread(activate_train, "training"))
    train_button.grid(row=0, column=0, padx=5, pady=5)
    test_button.config(command=lambda: create_thread(activate_test, "testing"))
    test_button.grid(row=0, column=1, padx=5, pady=5)
    send_button.config(command=lambda: create_thread(send_mail, "sending mail"))
    send_button.grid(row=0, column=2, padx=5, pady=5)

    root.mainloop()


def create_thread(function, name):
    threading.Thread(target=function, name=name).start()


if __name__ == "__main__":
    run_gui()
