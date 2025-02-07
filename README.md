# Signature Verification System

## Project Overview

This Signature Verification System is designed to verify whether two signatures are from the same person or forged. It uses OpenCV for image processing and feature extraction to compare the query signature against a reference signature. The system employs the Scale-Invariant Feature Transform (SIFT) method to extract distinctive features from the signatures and compares them using the FLANN-based matcher.

### Features
- Upload two signature images (query and reference).
- Set a match threshold to adjust the sensitivity of the match (between 5 and 20).
- Displays the number of good matches and the verification result (Genuine or Forged Signature).
- The system is built using Flask for the web interface, with Bootstrap for styling.

## Technologies Used
- **Flask**: A lightweight web framework to build the application.
- **OpenCV**: For image processing and feature extraction.
- **NumPy**: For handling image data.
- **Bootstrap**: For the frontend design.
- **Python**: Programming language for the backend logic.

## Installation

### Prerequisites

Make sure you have Python 3.x installed on your system. You will also need to install the required Python packages, which are listed in the `requirements.txt` file.

### Steps to Install

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/bhanuvi17/Signature-Verification-System.git
   cd Signature-Verification-System

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
