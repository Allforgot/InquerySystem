from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox

import pandas as pd

from data_handling import sort_data, search_data, join_data
import const
# from file_handling import import_data

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_frame_st_container = self.__tk_label_frame_st_container(self)
        self.tk_frame_st_in_cter_1 = self.__tk_frame_st_in_cter_1( self.tk_label_frame_st_container) 
        self.tk_select_box_st_in_cter1_key = self.__tk_select_box_st_in_cter1_key( self.tk_frame_st_in_cter_1) 
        self.tk_select_box_st_in_cter1_ord = self.__tk_select_box_st_in_cter1_ord( self.tk_frame_st_in_cter_1) 
        self.tk_label_st_in_tag_key = self.__tk_label_st_in_tag_key( self.tk_label_frame_st_container) 
        self.tk_label_st_in_tag_ord = self.__tk_label_st_in_tag_ord( self.tk_label_frame_st_container)
        self.tk_frame_st_in_cter_2 = self.__tk_frame_st_in_cter_2( self.tk_label_frame_st_container) 
        self.tk_select_box_st_in_cter2_key = self.__tk_select_box_st_in_cter2_key( self.tk_frame_st_in_cter_2) 
        self.tk_select_box_st_in_cter2_ord = self.__tk_select_box_st_in_cter2_ord( self.tk_frame_st_in_cter_2)
        self.tk_label_frame_flt_cter = self.__tk_label_frame_flt_cter(self)
        self.tk_frame_ft_in_cter1 = self.__tk_frame_ft_in_cter1( self.tk_label_frame_flt_cter) 
        # self.tk_select_box_ft_in_cter1_to = self.__tk_select_box_ft_in_cter1_to( self.tk_frame_ft_in_cter1) 
        # self.tk_select_box_ft_in_cter1_fr = self.__tk_select_box_ft_in_cter1_fr( self.tk_frame_ft_in_cter1) 
        self.tk_label_ft_in_cter1_tag = self.__tk_label_ft_in_cter1_tag( self.tk_frame_ft_in_cter1) 
        self.tk_input_ft_in_cter1_input = self.__tk_input_ft_in_cter1_input( self.tk_frame_ft_in_cter1)
        self.tk_frame_ft_in_cter2 = self.__tk_frame_ft_in_cter2( self.tk_label_frame_flt_cter) 
        self.tk_label_ft_in_cter2_tag_tl = self.__tk_label_ft_in_cter2_tag_tl( self.tk_frame_ft_in_cter2) 
        self.tk_input_ft_in_cter2_fr = self.__tk_input_ft_in_cter2_fr( self.tk_frame_ft_in_cter2) 
        self.tk_label_ft_in_cter2_tag_fr = self.__tk_label_ft_in_cter2_tag_fr( self.tk_frame_ft_in_cter2) 
        self.tk_label_ft_in_cter2_tag_to = self.__tk_label_ft_in_cter2_tag_to( self.tk_frame_ft_in_cter2) 
        self.tk_input_ft_in_cter2_to = self.__tk_input_ft_in_cter2_to( self.tk_frame_ft_in_cter2) 
        self.tk_frame_lqdl9818 = self.__tk_frame_lqdl9818( self.tk_label_frame_flt_cter) 
        self.tk_label_ft_in_cter3_tag_tl = self.__tk_label_ft_in_cter3_tag_tl( self.tk_frame_lqdl9818) 
        self.tk_input_ft_in_cter3_fr = self.__tk_input_ft_in_cter3_fr( self.tk_frame_lqdl9818) 
        self.tk_label_ft_in_cter3_tag_fr = self.__tk_label_ft_in_cter3_tag_fr( self.tk_frame_lqdl9818) 
        self.tk_label_ft_in_cter3_tag_to = self.__tk_label_ft_in_cter3_tag_to( self.tk_frame_lqdl9818) 
        self.tk_input_ft_in_cter3_to = self.__tk_input_ft_in_cter3_to( self.tk_frame_lqdl9818) 
        self.tk_frame_lqdla056 = self.__tk_frame_lqdla056( self.tk_label_frame_flt_cter) 
        self.tk_label_ft_in_cter4_tag_tl = self.__tk_label_ft_in_cter4_tag_tl( self.tk_frame_lqdla056) 
        self.tk_input_ft_in_cter4_fr = self.__tk_input_ft_in_cter4_fr( self.tk_frame_lqdla056) 
        self.tk_label_ft_in_cter4_tag_fr = self.__tk_label_ft_in_cter4_tag_fr( self.tk_frame_lqdla056) 
        self.tk_label_ft_in_cter4_tag_to = self.__tk_label_ft_in_cter4_tag_to( self.tk_frame_lqdla056) 
        self.tk_input_ft_in_cter4_to = self.__tk_input_ft_in_cter4_to( self.tk_frame_lqdla056) 
        self.tk_label_frame_opt_cter = self.__tk_label_frame_opt_cter(self)
        self.tk_button_opt_search = self.__tk_button_opt_search( self.tk_label_frame_opt_cter) 
        self.tk_button_opt_sort = self.__tk_button_opt_sort( self.tk_label_frame_opt_cter) 
        self.tk_frame_result_cter = self.__tk_frame_result_cter(self)
        self.tk_table_result_table = self.__tk_table_result_table( self.tk_frame_result_cter) 
        # self.tk_toplevel_join_data = self.__tk_toplevel_join_data(self)
    def __win(self):
        self.title("InquerySystem")
        # 设置窗口大小、居中
        width = 1200
        height = 800
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.minsize(width=width, height=height)
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def __tk_label_frame_st_container(self,parent):
        frame = LabelFrame(parent,text="Sorting",)
        frame.place(relx=0.03, rely=0.04, relwidth=0.18, relheight=0.21)
        return frame
    def __tk_frame_st_in_cter_1(self,parent):
        frame = Frame(parent,)
        frame.place(relx=0.00, rely=0.28, relwidth=1.00, relheight=0.29)
        return frame
    def __tk_select_box_st_in_cter1_key(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ('Column')
        cb.place(relx=0.02, rely=0.19, relwidth=0.45, relheight=0.63)
        return cb
    def __tk_select_box_st_in_cter1_ord(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ('Ascending', 'Descending')
        cb.place(relx=0.52, rely=0.19, relwidth=0.45, relheight=0.63)
        return cb
    def __tk_label_st_in_tag_key(self,parent):
        label = Label(parent,text="Key",anchor="center", )
        label.place(relx=0.00, rely=0.04, relwidth=0.45, relheight=0.18)
        return label
    def __tk_label_st_in_tag_ord(self,parent):
        label = Label(parent,text="Order",anchor="center", )
        label.place(relx=0.52, rely=0.04, relwidth=0.45, relheight=0.18)
        return label
    def __tk_frame_st_in_cter_2(self,parent):
        frame = Frame(parent,)
        frame.place(relx=0.00, rely=0.60, relwidth=1.00, relheight=0.29)
        return frame
    def __tk_select_box_st_in_cter2_key(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("列表框","Python","Tkinter Helper")
        cb.place(relx=0.02, rely=0.19, relwidth=0.45, relheight=0.63)
        return cb
    def __tk_select_box_st_in_cter2_ord(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ('Ascending', 'Descending')
        cb.place(relx=0.52, rely=0.19, relwidth=0.45, relheight=0.63)
        return cb
    def __tk_label_frame_flt_cter(self,parent):
        frame = LabelFrame(parent,text="Filtering",)
        frame.place(relx=0.24, rely=0.04, relwidth=0.62, relheight=0.21)
        return frame
    def __tk_frame_ft_in_cter1(self,parent):
        frame = Frame(parent,)
        frame.place(relx=0.03, rely=0.06, relwidth=0.21, relheight=0.71)
        return frame
    def __tk_label_ft_in_cter1_tag(self,parent):
        label = Label(parent,text="VehicleType",anchor="center", )
        label.place(relx=0.21, rely=0.06, relwidth=0.59, relheight=0.25)
        return label
    def __tk_input_ft_in_cter1_input(self,parent):
        ipt = Entry(parent, )
        ipt.place(relx=0.03, rely=0.49, relwidth=0.94, relheight=0.25)
        return ipt
    def __tk_frame_ft_in_cter2(self,parent):
        frame = Frame(parent,)
        frame.place(relx=0.27, rely=0.06, relwidth=0.21, relheight=0.71)
        return frame
    def __tk_label_ft_in_cter2_tag_tl(self,parent):
        label = Label(parent,text="TripLength",anchor="center", )
        label.place(relx=0.25, rely=0.06, relwidth=0.50, relheight=0.25)
        return label
    def __tk_input_ft_in_cter2_fr(self,parent):
        ipt = Entry(parent, )
        ipt.place(relx=0.31, rely=0.39, relwidth=0.66, relheight=0.25)
        return ipt
    def __tk_label_ft_in_cter2_tag_fr(self,parent):
        label = Label(parent,text="From",anchor="center", )
        label.place(relx=0.02, rely=0.39, relwidth=0.25, relheight=0.25)
        return label
    def __tk_label_ft_in_cter2_tag_to(self,parent):
        label = Label(parent,text="To",anchor="center", )
        label.place(relx=0.02, rely=0.70, relwidth=0.25, relheight=0.25)
        return label
    def __tk_input_ft_in_cter2_to(self,parent):
        ipt = Entry(parent, )
        ipt.place(relx=0.31, rely=0.70, relwidth=0.66, relheight=0.25)
        return ipt
    def __tk_frame_lqdl9818(self,parent):
        frame = Frame(parent,)
        frame.place(relx=0.52, rely=0.06, relwidth=0.21, relheight=0.71)
        return frame
    def __tk_label_ft_in_cter3_tag_tl(self,parent):
        label = Label(parent,text="DerectionTime_O",anchor="center", )
        label.place(relx=0, rely=0.06, relwidth=1, relheight=0.25)
        return label
    def __tk_input_ft_in_cter3_fr(self,parent):
        ipt = Entry(parent, )
        ipt.place(relx=0.31, rely=0.39, relwidth=0.66, relheight=0.25)
        return ipt
    def __tk_label_ft_in_cter3_tag_fr(self,parent):
        label = Label(parent,text="From",anchor="center", )
        label.place(relx=0.02, rely=0.39, relwidth=0.25, relheight=0.25)
        return label
    def __tk_label_ft_in_cter3_tag_to(self,parent):
        label = Label(parent,text="To",anchor="center", )
        label.place(relx=0.02, rely=0.70, relwidth=0.25, relheight=0.25)
        return label
    def __tk_input_ft_in_cter3_to(self,parent):
        ipt = Entry(parent, )
        ipt.place(relx=0.31, rely=0.70, relwidth=0.66, relheight=0.25)
        return ipt
    def __tk_frame_lqdla056(self,parent):
        frame = Frame(parent,)
        frame.place(relx=0.76, rely=0.06, relwidth=0.21, relheight=0.71)
        return frame
    def __tk_label_ft_in_cter4_tag_tl(self,parent):
        label = Label(parent,text="DerectionTime_D",anchor="center", )
        label.place(relx=0, rely=0.06, relwidth=1, relheight=0.25)
        return label
    def __tk_input_ft_in_cter4_fr(self,parent):
        ipt = Entry(parent, )
        ipt.place(relx=0.31, rely=0.39, relwidth=0.66, relheight=0.25)
        return ipt
    def __tk_label_ft_in_cter4_tag_fr(self,parent):
        label = Label(parent,text="From",anchor="center", )
        label.place(relx=0.02, rely=0.39, relwidth=0.25, relheight=0.25)
        return label
    def __tk_label_ft_in_cter4_tag_to(self,parent):
        label = Label(parent,text="To",anchor="center", )
        label.place(relx=0.02, rely=0.70, relwidth=0.25, relheight=0.25)
        return label
    def __tk_input_ft_in_cter4_to(self,parent):
        ipt = Entry(parent, )
        ipt.place(relx=0.31, rely=0.70, relwidth=0.66, relheight=0.25)
        return ipt
    def __tk_label_frame_opt_cter(self,parent):
        frame = LabelFrame(parent,text="Operation",)
        frame.place(relx=0.89, rely=0.04, relwidth=0.08, relheight=0.21)
        return frame
    def __tk_button_opt_search(self,parent):
        btn = Button(parent, text="Search", takefocus=False,)
        btn.place(relx=0, rely=0.17, relwidth=1, relheight=0.18)
        return btn
    def __tk_button_opt_sort(self,parent):
        btn = Button(parent, text="Sort", takefocus=False,)
        btn.place(relx=0, rely=0.50, relwidth=1, relheight=0.18)
        return btn
    def __tk_frame_result_cter(self,parent):
        frame = Frame(parent,)
        frame.place(relx=0.03, rely=0.30, relwidth=0.94, relheight=0.65)
        return frame
    def __tk_table_result_table(self,parent):
        # 表头字段 表头宽度
        col_w = 136
        columns = {'VehicleType':col_w,'DerectionTime_O':col_w,'GantryID_O':col_w,'DerectionTime_D':col_w,
                   'GantryID_D':col_w,'TripLength':col_w,'TripEnd':col_w,'TripInformation':col_w}
        tk_table = Treeview(parent, show="headings", columns=list(columns),)
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸
        
        tk_table.place(relx=0.00, rely=0.00, relwidth=1.00, relheight=1.00)
        return tk_table


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.config(menu=self.create_menu())
        self.ctl.init(self)
    def create_menu(self):
        menu = Menu(self,tearoff=False)
        menu.add_cascade(label="File",menu=self.menu_lqdbceri(menu))
        return menu
    def menu_lqdbceri(self,parent):
        menu = Menu(parent,tearoff=False)
        menu.add_command(label="Open",command=self.ctl.open_file)
        menu.add_command(label="Export",command=self.ctl.export_data)
        menu.add_command(label="Join Data",command=self.ctl.join_data)
        return menu
    
    def populate_treeview_from_dataframe(self, dataframe, max_rows=30):
        # Clear previous data
        treeview = self.tk_table_result_table
        treeview.delete(*treeview.get_children())

        # Set up new columns
        treeview['columns'] = list(dataframe.columns)
        treeview['show'] = 'headings'

        # Define headings and column width
        for col in dataframe.columns:
            treeview.heading(col, text=col)
            treeview.column(col, width=100)

        # Add data rows, limiting to max_rows if specified
        for index, row in dataframe.iterrows():
            if max_rows is not None and index >= max_rows:
                break
            treeview.insert('', 'end', values=list(row))

    def update_column_key(self, df):
        st_in_cter1_key = self.tk_select_box_st_in_cter1_key
        st_in_cter1_key['values'] = tuple(df.columns)
        st_in_cter2_key = self.tk_select_box_st_in_cter2_key
        st_in_cter2_key['values'] = tuple(df.columns)


    def display_searching_data(self, event):
        print('run display_sorted_data')
        sorted_data = self.ctl.get_searched_data()
        self.populate_treeview_from_dataframe(sorted_data)

    def display_sorted_data(self, event):
        print('run display_sorted_data')
        sorted_data = self.ctl.get_sorted_data()
        self.populate_treeview_from_dataframe(sorted_data)

    def __event_bind(self):
        self.tk_button_opt_sort.bind('<Button-1>', self.display_sorted_data)
        self.tk_button_opt_search.bind('<Button-1>', self.display_searching_data)
    

class GUI_Controller():
    def __init__(self):
        self.file_data = None  # Holds the data read from the file
        self.filtered_data = None

    def init(self, Win):
        self.Win = Win

    def __open_file(self):
        file_path = filedialog.askopenfilename(
            title="Select a file",
            filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
        )
        data = None
        if file_path:
            data = pd.read_csv(file_path)
        return data
    
    def open_file(self):
        try:
            self.file_data = self.__open_file()
            self.filtered_data = None
            self.Win.populate_treeview_from_dataframe(self.file_data)
            self.Win.update_column_key(self.file_data)
            messagebox.showinfo("Success", "File opened successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {e}")

    def join_data(self):
        extra_data = self.__open_file()
        self.file_data = join_data(self.file_data, extra_data)
        messagebox.showinfo("Success", "Data joined successfully.")
        self.Win.populate_treeview_from_dataframe(self.file_data)
        self.Win.update_column_key(self.file_data)

    def export_data(self):
        """ Export data to a file. """
        file_path = filedialog.asksaveasfilename(
            title="Save file as",
            filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
        )

        if file_path:
            try:
                with open(file_path, 'w') as file:
                    self.filtered_data.to_csv(file_path, index=False)
                messagebox.showinfo("Success", "File saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")

    def get_search_sort_func(self, search_flag, data=None):
        params = {}
        params['data'] = self.file_data
        if data is not None:
            params['data'] = data
        select_list = []
        filtering_list = []
        sorting_list = []

        # filtering vehicle type
        ft_in_cter1_key_val = 'VehicleType'
        ft_in_cter1_input_val = self.Win.tk_input_ft_in_cter1_input.get()
        if ft_in_cter1_input_val != '':
            select_cond1 = {}
            select_cond1['col_idx'] = self.file_data.columns.get_loc(ft_in_cter1_key_val)
            select_cond1['data'] = [int(s) for s in str(ft_in_cter1_input_val).split(',')]
            select_list.append(select_cond1)
        params['select'] = select_list

        # filtering TripLength
        ft_in_cter2_key_val = 'TripLength'
        ft_in_cter2_fr_val = self.Win.tk_input_ft_in_cter2_fr.get()
        ft_in_cter2_to_val = self.Win.tk_input_ft_in_cter2_to.get()
        if ft_in_cter2_fr_val != '' and ft_in_cter2_to_val != '':
            filtering_cond2 = {'col_idx': self.file_data.columns.get_loc(ft_in_cter2_key_val), 'from': float(ft_in_cter2_fr_val), 'to': float(ft_in_cter2_to_val)}
            filtering_list.append(filtering_cond2)

        # filtering DerectionTime_O
        ft_in_cter3_key_val = 'DerectionTime_O'
        ft_in_cter3_fr_val = self.Win.tk_input_ft_in_cter3_fr.get()
        ft_in_cter3_to_val = self.Win.tk_input_ft_in_cter3_to.get()
        if ft_in_cter3_fr_val != '' and ft_in_cter3_to_val != '':
            filter_cond = {'col_idx': self.file_data.columns.get_loc(ft_in_cter3_key_val), 'from': ft_in_cter3_fr_val, 'to': ft_in_cter3_to_val}
            filtering_list.append(filter_cond)

        # filtering DerectionTime_O
        ft_in_cter4_key_val = 'DerectionTime_D'
        ft_in_cter4_fr_val = self.Win.tk_input_ft_in_cter4_fr.get()
        ft_in_cter4_to_val = self.Win.tk_input_ft_in_cter4_to.get()
        if ft_in_cter4_fr_val != '' and ft_in_cter4_to_val != '':
            filter_cond = {'col_idx': self.file_data.columns.get_loc(ft_in_cter4_key_val), 'from': ft_in_cter4_fr_val, 'to': ft_in_cter4_to_val}
            filtering_list.append(filter_cond)
        
        params['filtering'] = filtering_list

        # sorting
        st_in_cter1_key_val = self.Win.tk_select_box_st_in_cter1_key.get()
        st_in_cter1_ord_val = self.Win.tk_select_box_st_in_cter1_ord.get()
        if st_in_cter1_key_val != '' and st_in_cter1_ord_val != '':
            sorting_cond = {'key': self.file_data.columns.get_loc(st_in_cter1_key_val), 'order': const.Const[st_in_cter1_ord_val]}
            sorting_list.append(sorting_cond)
        st_in_cter2_key_val = self.Win.tk_select_box_st_in_cter2_key.get()
        st_in_cter2_ord_val = self.Win.tk_select_box_st_in_cter2_ord.get()
        if st_in_cter2_key_val != '' and st_in_cter2_ord_val != '':
            sorting_cond = {'key': self.file_data.columns.get_loc(st_in_cter2_key_val), 'order': const.Const[st_in_cter2_ord_val]}
            sorting_list.append(sorting_cond)
        
        params['sorting'] = sorting_list

        # print(params)
        
        if search_flag:
            sorted_data = search_data(params)
            self.filtered_data = sorted_data
        else:
            sorted_data = sort_data(params)
            self.filtered_data = sorted_data
        return sorted_data
    
    def get_searched_data(self):
        return self.get_search_sort_func(True)
    
    def get_sorted_data(self):
        return self.get_search_sort_func(False, self.filtered_data)

def run_app():
    controller = GUI_Controller()
    win = Win(controller)
    win.mainloop()

if __name__ == "__main__":
    controller = GUI_Controller()
    win = Win(controller)
    win.mainloop()