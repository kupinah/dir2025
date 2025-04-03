import os

def get_latest_file(directory):
    # Get a list of all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    if not files:
        print("No files found in the directory.")
        return None
    
    # Get the full path of each file
    full_paths = [os.path.join(directory, f) for f in files]
    
    # Sort the files by their last modified time (descending order)
    latest_file = max(full_paths, key=os.path.getmtime)
    
    return latest_file

if __name__ == "__main__":
    # Set the path to the directory containing your photos
    photos_directory = "C:/Users/student/Pictures/Camera Roll"
    
    latest_file = str(get_latest_file(photos_directory)).replace("\\", "/")
    
    if latest_file:
        print(f"The latest file is: {latest_file}")
    else:
        print("No files found.")
