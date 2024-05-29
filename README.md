# Coin-Detection

Training and using a machine learning model locally to accurately identify and count coins in a given image. This project includes data preprocessing, model training, and evaluation to ensure precise coin detection and counting.

## Demo

I. Example Input Image

![Input Image](https://user-images.githubusercontent.com/37275728/200141206-688cf1be-a38f-4205-b44d-977cc153b020.png)

II. Example Output Image

![Output Image](https://user-images.githubusercontent.com/37275728/200141208-d525c6ab-54b6-4df9-b697-677ed7564d52.png)

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
   
   ```bash
   git clone https://github.com/djeada/kaggle-house-prices.git
   ```

2. **Install virtualenv (if it's not already installed)**:

   ```bash
   pip install virtualenv
   ```

3. **Set up the virtual environment and install dependencies**:

   ```bash
   cd kaggle-house-prices
   virtualenv env
   source env/bin/activate
   pip install -r requirements.txt
   ```
   
4. **Run the project**:

   ```bash
   cd src
   python -m src.main
   ```

## Usage

To display the help message and learn about the available options, run the following command:

```bash
python -m src.main -h
```

The output should look like this:

```
usage: main.py [-h] [--path PATH] [--output_dir OUTPUT_DIR] [--r_min R_MIN]
               [--r_max R_MAX] [--interactive INTERACTIVE] [--verbose VERBOSE]
               [--image_output IMAGE_OUTPUT] [--csv_output CSV_OUTPUT]

options:
  -h, --help            show this help message and exit
  --path PATH           Path to the image
  --output_dir OUTPUT_DIR
                        Path to the output directory
  --r_min R_MIN         Minimum radius of the coins
  --r_max R_MAX         Maximum radius of the coins
  --interactive INTERACTIVE
                        Interactive mode
  --verbose VERBOSE     Verbose mode
  --image_output IMAGE_OUTPUT
                        Should the images be displayed
  --csv_output CSV_OUTPUT
                        Should the csv with coin coordinates be saved
```

### Example Command

If your image is located at '/home/user/images/image.png', and you want to specify coin radii between 20 and 30 pixels, display the images, and save the results to a CSV file, use the following command:

```bash
python -m src.main --path /home/user/images/image.png --r_min 20 --r_max 30 --image_output True --csv_output True
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
