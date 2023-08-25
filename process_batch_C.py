import csv
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

INPUT_FILE_NAME = "batchfile_2_kelvin.csv"
OUTPUT_FILE_NAME = "batchfile_3_farenheit.csv"

def convert_k_to_f(temp_k):
    return (temp_k - 273.15) * 9/5 + 32  # Conversion formula: K to F

def process_rows(input_file_name, output_file_name):
    try:
        with open(input_file_name, "r") as input_file, open(output_file_name, "w", newline="") as output_file:
            csv_reader = csv.reader(input_file)
            csv_writer = csv.writer(output_file)
            
            # Write header to the output file
            header = next(csv_reader)
            csv_writer.writerow(header + ["Temperature (F)"])  # Adding a new column
            
            for row in csv_reader:
                temp_k = float(row[4])  # Assuming temperature is in the second column
                temp_f = convert_k_to_f(temp_k)
                csv_writer.writerow(row + [temp_f])
                logging.info(f"Converted {temp_k} K to {temp_f} F")
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        logging.info("===============================================")
        logging.info("Starting batch process C.")
        process_rows(INPUT_FILE_NAME, OUTPUT_FILE_NAME)
        logging.info("Processing complete! Check for the new file.")
        logging.info("===============================================")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
