import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile", 
                    layout=[[sg.Text("SELAMAT DATANG DI KELAS",
                                    font=("Aerial",18,"italic","bold","underline"))],
                            
                            [sg.Text("NPM       : 2210010667")],
                            [sg.Text("NAMA      : Muhammad Albar")],
                            [sg.Text("KELAS     : 5M REGULAR BANJARMASIN")]
                            
                            
                            ], size=(400,200),
                            font=("Times",15))
window()
window.close()