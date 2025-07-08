import os
import pandas as pd

raw_directory = "documents/raw_data"
cleaned_directory = "documents/cleaned_data"

for filename in os.listdir(raw_directory):
    if filename.endswith('.csv'):
        input_filepath = os.path.join(raw_directory, filename)
        output_filepath = os.path.join(cleaned_directory, filename)

        if filename == "cleaned_data_India.csv" or filename == "cleaned_data_Iran.csv" or filename == "cleaned_data_USA.csv":
            df = pd.read_csv(input_filepath, encoding="utf-8")
            df = df.iloc[:,1:]
            df = df.drop(columns=["main_category","rating","reviews","zipcode","Weighted_Score","Weighted_Average"])
            df.to_csv(output_filepath, index=False, encoding="utf-8")

        elif filename == "destinations.csv":
            df = pd.read_csv(input_filepath, encoding="utf-8")
            df = df.drop_duplicates()
            df.to_csv(output_filepath, index=False, encoding="utf-8")

        elif filename == "IrelandTourismAttraction.csv":
            df = pd.read_csv(input_filepath, encoding="utf-8")
            df = df.drop_duplicates()
            df = df.drop(columns=["Telephone"])
            df.to_csv(output_filepath, index=False, encoding="utf-8")
        
        elif filename == "Tourist_Destinations.csv":
            df = pd.read_csv(input_filepath, encoding="utf-8")
            df = df.drop_duplicates()
            df = df.drop(columns=["Avg Rating"])
            df.to_csv(output_filepath, index=False, encoding="utf-8")
        
        elif filename == "travel_QA_v2.csv":
            df = pd.read_csv(input_filepath, encoding="utf-8")
            df = df.drop_duplicates()
            df.to_csv(output_filepath, index=False, encoding="utf-8")
        
        elif filename == "TravelPlannerTest.csv" or filename == "TravelPlannerTrain.csv" or filename == "TravelPlannerValidation.csv":
            print(f"888")
        
        elif filename == "Worldwide Travel Cities Dataset (Ratings and Climate).csv":
            print(f"9")
        
    else:
        print(f"Dovrò ancora implementare la funzione per elaborare {filename}")