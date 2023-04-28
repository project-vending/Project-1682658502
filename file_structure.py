
import os

# Create the main project directory
main_dir = "Real-time Data Visualization Dashboard"
os.mkdir(main_dir)

# Create subdirectories for data processing and visualization
data_dir = os.path.join(main_dir, "data_processing")
os.mkdir(data_dir)

visual_dir = os.path.join(main_dir, "visualization")
os.mkdir(visual_dir)

# Create empty files for data processing
data_file1 = os.path.join(data_dir, "data_processing_1.csv")
open(data_file1, "w").close()

data_file2 = os.path.join(data_dir, "data_processing_2.csv")
open(data_file2, "w").close()

# Create empty files for visualization
visual_file1 = os.path.join(visual_dir, "visualization_1.png")
open(visual_file1, "w").close()

visual_file2 = os.path.join(visual_dir, "visualization_2.png")
open(visual_file2, "w").close()
