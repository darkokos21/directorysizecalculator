# Directory Size Calculator

A simple Python automation project that calculates the total size of files in a directory, packaged in a Docker container, and integrated with GitHub Actions for CI/CD.

## Features

- Python script to compute directory size in bytes.
- Dockerized for easy deployment.
- Automated testing and Docker image building via GitHub Actions.
- Unit tests with pytest for reliability.

## Prerequisites

- Python 3.9+
- Docker Desktop
- Git

## Project Structure

```
├── dir_size.py          # Main Python script
├── test_dir_size.py     # Unit tests
├── Dockerfile           # Docker configuration
├── files/               # Sample files for testing
└── .github/workflows/ci.yml  # GitHub Actions pipeline
```

## Setup and Testing

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/darkokos21/directorysizecalculator.git
   cd directorysizecalculator
   ```

2. **Run Tests Locally**:

   ```bash
   pip install pytest
   pytest test_dir_size.py
   ```

3. **Build and Run Docker**:

   - Create a `files` folder with sample files (e.g., `file1.txt`, `file2.txt`).

   - Build the image:

     ```bash
     docker build -t dir-size-calculator .
     ```

   - Run the container:

     ```bash
     docker run -v $(pwd)/files:/app/files dir-size-calculator
     ```

## CI/CD with GitHub Actions

- The pipeline (`.github/workflows/ci.yml`) runs on push/pull requests to `main`.
- It tests the Python script with pytest and builds the Docker image.

## Usage

- Place files in the `files` directory.
- Run the Docker container to calculate the total size of files in bytes.

## Contributing

Feel free to open issues or submit pull requests for improvements.