import os
import shutil
import time

def getfile_or_foldertime(path):

	ctime = os.stat(path).st_ctime

	return ctime


def main():

	deleted_folders_count = 0
	deleted_files_count = 0

	path = input("Enter the path to the directory that you want to delete.")

	days = 30

	seconds = time.time() - (days * 24 * 60 * 60)

	if os.path.exists(path):

		for root_folder, folders, files in os.walk(path):

			# comparing the days
			if seconds >= getfile_or_foldertime(root_folder):

				remove_folder(root_folder)
				deleted_folders_count += 1

				break

			else:

				for folder in folders:

					folder_path = os.path.join(root_folder, folder)

					if seconds >= getfile_or_foldertime(folder_path):

						remove_folder(folder_path)
						deleted_folders_count += 1

				for file in files:

					file_path = os.path.join(root_folder, file)

					if seconds >= getfile_or_foldertime(file_path):

						remove_file(file_path)
						deleted_files_count += 1

		else:

			# Deletes the path instead of what is in the path
			if seconds >= getfile_or_foldertime(path):


				remove_file(path)
				deleted_files_count +=1

	else:

		print(path,"is not found")
		deleted_files_count += 1

	print("Total folders deleted: ",deleted_files_count)
	print("Total files deleted: ",deleted_files_count)

#Remove Folder
def remove_folder(path):

	if not shutil.rmtree(path):

		print(path,"is removed successfully")

	else:
		print("Unable to delete",path)

#Remove Folder
def remove_file(path):

	if not os.remove(path):

		print(path,"is removed successfully")

	else:
		print("Unable to delete ",path)