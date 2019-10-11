from kivy.lang import Builder
import csv

# This is my hacky way to handle loading all of the kv files for now

Builder.load_file('kv_files/common.kv')
Builder.load_file('kv_files/screens/main_menu.kv')
Builder.load_file('kv_files/screens/selection.kv')
Builder.load_file('kv_files/screen_manager.kv')

# This is to load in any global lookup values

# Display Text Lookup table
tld = None
with open('data/ui_name_keys.csv', mode='r') as infile:
    reader = csv.reader(infile)
    tld = {rows[0]: rows[1] for rows in reader}
