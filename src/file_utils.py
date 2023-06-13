import os


class FileUtils:
    def find_file(self, directory, filename):
        for (root, dirs, files) in os.walk(directory):
            if filename in files:
                return os.path.join(root, filename)
        return None  # File not found

    def print_files(self, directory):
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                print(file_path)

    def find_src_directory(self, path):
        # Get the current working directory
        current_directory = os.getcwd()

        # Walk up the directory tree until "src" directory is found
        while current_directory != "/":
            # Check if "src" directory exists in the current directory
            src_directory = os.path.join(current_directory, path)
            if os.path.isdir(src_directory):
                return src_directory

            # Move up to the parent directory
            current_directory = os.path.dirname(current_directory)

        # If "src" directory is not found
        return None

    def collect_py_files(self, src_directory):
        py_files = {}
        for root, dirs, files in os.walk(src_directory):
            for file in files:
                if file.endswith(".py"):
                    file_name = os.path.splitext(file)[0]
                    file_path = os.path.join(root, file)
                    py_files[file_name] = file_path
        return py_files
