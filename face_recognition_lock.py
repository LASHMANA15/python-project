import cv2
import face_recognition
import os
import shutil
import utils.logger as logger
import utils.folder_utils as folder_utils
import utils.face_utils as face_utils

def verify_user():
    return face_utils.scan_face()

def create_folder(name):
    user = verify_user()
    if user:
        folder_utils.create_desktop_folder(name)
        logger.log_action(user[0], user[1], user[2], f"Created folder {name}")

def lock_folder(name):
    user = verify_user()
    if user:
        folder_utils.lock_desktop_folder(name)
        logger.log_action(user[0], user[1], user[2], f"Locked folder {name}")

def unlock_folder(name):
    user = verify_user()
    if user:
        folder_utils.unlock_desktop_folder(name)
        logger.log_action(user[0], user[1], user[2], f"Unlocked folder {name}")