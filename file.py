import csv

def read_quartus_csv_skip_comments(file_path, comment_char='#'):
    with open(file_path, mode='r', newline='') as file:
        # Skip comment lines to find the header
        header = None
        while header is None:
            pos = file.tell()
            line = file.readline()
            if not line.startswith(comment_char) and not line.startswith('\n'):
                file.seek(pos)
                header = next(csv.reader([line.strip()]))
        
        file.seek(pos)  # Move back to the position before the header line

        # Now use DictReader with the header
        reader = csv.DictReader(file)

        return list(reader)

def main():
    pinplanner_file = 'pin_planner_export.csv'
    c2 = read_csv_skip_comments(pinplanner_file)
    print(c2)


if __name__ == "__main__":
    main()
