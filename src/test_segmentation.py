import unittest
import cv2
import os
import shutil
import numpy as np
from segmentation import main

class TestImageProcessing(unittest.TestCase):
    def setUp(self):
        self.paths = {
            "images": "test_input/test_image.png",
            "lines": "test_output/test_lines/",
            "words": "test_output/test_words/",
            "letter": "test_output/test_letters/"
        }
        # Create test folders
        for path in self.paths.values():
            os.makedirs(path, exist_ok=True)

    def tearDown(self):
        # Remove test folders and their contents
        for path in self.paths.values():
            shutil.rmtree(path, ignore_errors=True)

    def test_main_function(self):
        # Create a dummy test image
        dummy_image = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.imwrite(self.paths["images"], dummy_image)

        # Test the main function
        main(self.paths)

        # Assert that the output folders are not empty
        self.assertTrue(os.listdir(self.paths["lines"]))
        self.assertTrue(os.listdir(self.paths["words"]))
        self.assertTrue(os.listdir(self.paths["letter"]))

if __name__ == "__main__":
    unittest.main()
