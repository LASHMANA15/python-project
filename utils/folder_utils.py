import os

# Fixed path for all folder operations
BASE_PATH = r"C:\Users\LAKSHMAN M\OneDrive\Desktop"

def create_desktop_folder(folder_name):
    path = os.path.join(BASE_PATH, folder_name)
    os.makedirs(path, exist_ok=True)
    hide_folder(path)

def hide_folder(path):
    os.system(f'attrib +h "{path}"')

def unhide_folder(path):
    os.system(f'attrib -h "{path}"')

def lock_desktop_folder(folder_name):
    path = os.path.join(BASE_PATH, folder_name)
    hide_folder(path)

def unlock_desktop_folder(folder_name):
    path = os.path.join(BASE_PATH, folder_name)
    unhide_folder(path)
