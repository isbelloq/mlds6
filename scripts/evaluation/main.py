from argparse import ArgumentParser
import argparse


from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


from mlds6.datamodels.training import ModelType
from mlds6.models.feature_extraction import get_train_data
from mlds6.evaluation.gridEvaluation import (train_search_model,
                                             save_model_report, 
                                             save_grid_model,
                                             save_scoring_report,
                                             get_hiperparams)
from mlds6.models.model import save_model

def main(parser: ArgumentParser):
    args = parser.parse_args()
    model_type = ModelType(args.model)
    model = eval(f'{model_type.name}()')
    hiperparams = get_hiperparams(model_type)
    
    print("Evaluating", model_type.name)    
    X_train, X_test, y_train, y_test = get_train_data()
    
    grid_model = train_search_model(X_train, 
                                  y_train, 
                                  model,  
                                  hiperparams)
    
    save_model_report(grid_model, 
                      model_type.name)
    save_scoring_report(X_test, 
                        y_test, 
                        grid_model,
                        model_type.name)
    
   
    
    save_grid_model(grid_model, model_type.name)
    save_model(grid_model.best_estimator_, model_type.name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate a grid search model")
    parser.add_argument('--model', type=str, help="model type selection")
    main(parser)