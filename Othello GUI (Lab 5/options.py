#Kevin Luu 48783106 Lab Section 3
import tkinter
class GameOptions:
    def __init__(self):
        self._dialog_window = tkinter.Tk()
        self._ok_clicked = False
        self._num_rows = 0
        self._num_columns = 0
        self._move_first = None
        self._top_left = None
        self._game_type = None


        num_rows = tkinter.Label(master = self._dialog_window, text = 'Rows?')

        num_rows.grid( row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

        self._num_rows_entry = tkinter.Entry( master = self._dialog_window, width = 20)

        self._num_rows_entry.grid( row = 1, column = 1, padx = 10, pady = 1, sticky = tkinter.W + tkinter.E)

        num_columns = tkinter.Label(master = self._dialog_window, text = 'Columns?')

        num_columns.grid( row = 2, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

        self._num_columns_entry = tkinter.Entry(master = self._dialog_window, width = 20)

        self._num_columns_entry.grid(row = 2, column = 1, padx = 10, pady = 1, sticky = tkinter.W + tkinter.E)

        move_first = tkinter.Label(master = self._dialog_window, text = 'Black or White to move first?')

        move_first.grid( row = 3, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

        self._move_first_entry = tkinter.Entry(master = self._dialog_window, width = 20)

        self._move_first_entry.grid(row = 3, column = 1, padx = 10, pady = 1, sticky = tkinter.W + tkinter.E)
        
        top_left = tkinter.Label(master = self._dialog_window, text = 'Color of top left corner, black or white?')

        top_left.grid( row = 4, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

        self._top_left_entry = tkinter.Entry(master = self._dialog_window, width = 20)

        self._top_left_entry.grid(row = 4, column = 1, padx = 10, pady = 1, sticky = tkinter.W + tkinter.E)
        
        game_type = tkinter.Label(master = self._dialog_window, text = 'Game type? Most or Least to win?')

        game_type.grid( row = 5, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

        self._game_type_entry = tkinter.Entry(master = self._dialog_window, width = 20)

        self._game_type_entry.grid(row = 5, column = 1, padx = 10, pady = 1, sticky = tkinter.W + tkinter.E)

        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(row = 6, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(master = button_frame, text = 'Press to Start', command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)

       
        self._dialog_window.rowconfigure(3, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)


    def _on_ok_button(self) -> None:
        self._ok_clicked = True
        self._num_rows = self._num_rows_entry.get()
        self._num_columns = self._num_columns_entry.get()
        self._move_first = self._move_first_entry.get()
        self._top_left = self._top_left_entry.get()
        self._game_type = self._game_type_entry.get()

        self._dialog_window.destroy()




    def show(self) -> None:
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()


    def was_ok_clicked(self) -> bool:
        return self._ok_clicked


    def return_rows(self) -> int:
        if int(self._num_rows) % 2 == 0 and int(self._num_rows) > 0 and int(self._num_rows) < 17:
            return int(self._num_rows)


    def return_columns(self) -> int:
        if int(self._num_columns) % 2 == 0 and int(self._num_columns) > 0 and int(self._num_columns) < 17:
            return int(self._num_columns)
        
    def return_topLeft(self) ->str:
        if self._top_left == "white" or self._top_left == "black":
            return self._top_left


    def return_firstMove(self) -> str:
        if self._move_first.lower() == "black" or self._move_first.lower() == "white":
            return self._move_first

    
    def return_gameType(self) -> str:
        if self._game_type.lower() == "most" or self._game_type.lower() == "least":
            return self._game_type



        
    def start(self) -> None:
        self._dialog_window.mainloop()





            
if __name__ == '__main__':
    pass

    

    
    
