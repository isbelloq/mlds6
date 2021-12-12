from mlds6.models.model import load_model_pipeline
from mlds6.environment.base import get_data_paths
from mlds6.database.io import load_table
from mlds6.preprocessing.cleaning import preprocess_pipe
from mlds6.models.feature_extraction import select_features
import re
import argparse
from os import path

def main():
    data_path = get_data_paths()
    data_path.models
    
    
    parser = argparse.ArgumentParser(description='Training model from a path')
    parser.add_argument('--path', help="path where the model get the data", dest='path')
    parser.add_argument('--model', help="model name", dest='model_name')
    args = parser.parse_args() 
    
       
    if args.path: 
        
        model_name = 'model.joblib' if not args.model_name else args.model_name
        src_path = path.dirname(args.path)
        file = re.search(r'(\w+)\.(\w+)',path.basename(args.path))  
        file_name = file.group(1)
        extension = file.group(2)
        train_data = load_table(src_path, file_name, extension)
        train_data = preprocess_pipe(train_data)
        print(model_name)
        X, y = select_features(train_data)
        model = load_model_pipeline(data_path.models, model_name)
        model.fit(X,y)
        


if __name__ == '__main__':

    main()
   