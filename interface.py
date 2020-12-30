import PySimpleGUI as sg


class PyWindow:

    window = None

    def __init__(self):
        sg.theme('Dark Red')
        self.create_window()

    def options_tab(self):
        return [[sg.Frame('Coordinates', [
            [sg.Text(key='-COORDINATE1-', font='Courier 10', size=(10, 1)),
             sg.Text(key='-COORDINATE2-', font='Courier 10', size=(10, 1)),
             sg.Text(key='-COORDINATEX-', font='Courier 10', size=(10, 1)),
             sg.Text(key='-COORDINATEY-', font='Courier 10', size=(10, 1)),
             sg.Button('Select Coordinates', key='-CHECKFORCOORDINATES-'),
             sg.Button('Save', key='-SAVECOORDINATES-')],
        ])], [sg.Frame('Photograph', [
            [sg.Image(key='-CAPTCHA-')]])],
            [sg.Frame('Decoded', [
                [sg.Text(key='-DECODEDCAPTCHA-', font='Courier 10', size=(50, 3))]])], ]

    def create_tabs(self):

        tab1_layout = self.options_tab()

        tab_1 = sg.Tab('Draw', tab1_layout, font='Courier 15', key='-TAB1-')

        tab_group_layout = [[tab_1]]

        return tab_group_layout

    def create_window_layout(self):

        tab_group_layout = self.create_tabs()

        return [[sg.TabGroup(tab_group_layout,
                             enable_events=True,
                             key='-TABGROUP-')]]

    def create_window(self):

        layout = self.create_window_layout()

        self.window = sg.Window('Python OCR', layout,
                                no_titlebar=False, finalize=True)
