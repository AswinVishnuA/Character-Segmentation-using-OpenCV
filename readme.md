# Image Segmentation Project

## Project Overview

This project focuses on image segmentation using the OpenCV library in Python. Image segmentation is the process of partitioning an image into meaningful segments or regions to simplify the representation and make it easier to analyze. In this specific implementation, the goal is to segment text lines, words, and letters from a given input image.

## Project Structure

The project is structured into a Python script and follows a modular approach for image processing. The main script (`segmentation.py`) includes functions for clearing paths, creating contours, and segmenting images into lines, words, and letters.

## Requirements

- Python 3.x
- OpenCV library (`cv2`)

## How to Run

1. Place the input image in the "Input" folder.
2. Run the script `image_segmentation.py`.
3. Enter the name of the input image when prompted.
4. The output will be saved in the "Output" folder, with subfolders for lines, words, and letters.

## Code Explanation

- `clearPath(path)`: Clears files from the specified path.
- `segment(result, cntrs, saveToPath, name)`: Writes segmented images to the output path and draws rectangles around the segments.
- `makeContours(temp, kernalSize)`: Creates contours for a given image using a specified kernel size.
- `main(path)`: The main function that reads the input image, performs segmentation, and saves the results.

## Input and Output Paths

- **Input Path**: `Input/in1.png` (default)
- **Output Paths**:
  - Lines: `Output/Lines/`
  - Words: `Output/Words/`
  - Letters: `Output/Letters/`

## Running the Script

1. Clone the repository.
2. Create a virtualenv and install dependencies from requirement.txt 
3. Run the script: `python segmentation.py`

## Viewing Results

- Uncomment the relevant code in the `main` function to display the intermediate results, such as line segmentation.

## Note

- Ensure that the input image file exists in the "Input" folder before running the script.

## Author

- [Aswin Vishnu A]

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and use the code according to your needs. If you encounter any issues or have suggestions for improvements, please create an issue or pull request.

**Happy coding!**