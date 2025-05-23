import json
import os

def main():
    input_file_path = "my_scraper/output.jl"
    pretty_json_output_path = "output_pretty.json"
    html_output_dir = "scraped_html_outputs"

    print(f"Attempting to read from {input_file_path}")
    print(f"Structured JSON will be written to {pretty_json_output_path}")
    print(f"Extracted HTML pages will be saved in ./{html_output_dir}/\n")

    # Create the HTML output directory if it doesn't exist
    try:
        if not os.path.exists(html_output_dir):
            os.makedirs(html_output_dir)
            print(f"Created directory: ./{html_output_dir}/")
    except OSError as e:
        print(f"Error creating directory {html_output_dir}: {e}")
        return # Exit if we can't create the output directory

    items_processed = 0
    html_files_created = 0
    try:
        with open(input_file_path, 'r') as infile, open(pretty_json_output_path, 'w') as pretty_outfile:
            for i, line in enumerate(infile):
                try:
                    cleaned_line = line.strip()
                    if not cleaned_line:
                        continue
                    
                    data = json.loads(cleaned_line)
                    items_processed += 1

                    # Write to pretty JSON output file
                    if i > 0: # Add a newline separator if not the first item for output_pretty.json
                        pretty_outfile.write("\n") 
                    json.dump(data, pretty_outfile, indent=4, sort_keys=True)

                    # Extract and write HTML content
                    if 'page_content' in data and isinstance(data['page_content'], str):
                        html_content = data['page_content']
                        html_filename = f"scraped_page_{html_files_created + 1}.html"
                        html_filepath = os.path.join(html_output_dir, html_filename)
                        
                        try:
                            with open(html_filepath, 'w', encoding='utf-8') as html_file:
                                html_file.write(html_content)
                            html_files_created += 1
                            # print(f"Successfully created HTML file: {html_filepath}") # Optional: too verbose for many files
                        except IOError as e:
                            print(f"Error writing HTML file {html_filepath}: {e}")
                    else:
                        print(f"Warning: Item {items_processed} does not contain 'page_content' or it's not a string.")

                except json.JSONDecodeError as e:
                    error_message = f"Error decoding JSON from line {i+1} in {input_file_path}: {e}\nProblematic line: {line.strip()}\n"
                    print(error_message)
                    pretty_outfile.write(error_message) 
                except Exception as e:
                    error_message = f"Unexpected error processing line {i+1} in {input_file_path}: {e}\nLine: {line.strip()}\n"
                    print(error_message)
                    pretty_outfile.write(error_message)

            if items_processed > 0:
                print(f"\nSuccessfully processed {items_processed} item(s).")
                print(f"Pretty JSON output saved to: {pretty_json_output_path}")
                if html_files_created > 0:
                    print(f"{html_files_created} HTML file(s) saved in ./{html_output_dir}/")
                else:
                    print("No HTML content found to extract.")
            else:
                print(f"No items found or processed from {input_file_path}")

    except FileNotFoundError:
        print(f"Error: The input file {input_file_path} was not found.")
    except IOError as e:
        print(f"IOError occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()