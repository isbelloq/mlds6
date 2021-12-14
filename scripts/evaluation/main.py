from argparse import ArgumentParser
import argparse


from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


from mlds6.datamodels.training import ModelType
from mlds6.models.feature_extraction import get_train_data
from mlds6.evaluation.gridEvaluation import (train_search_model,
                                             save_model_report, 
                                             save_evaluation_model,
                                             get_hiperparams)


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
                      model_type)
    
    y_pred = grid_model.predict(X_test)
    print("Accuracy: ", accuracy_score(y_test, y_pred))
    
    save_evaluation_model(grid_model, model_type)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate a grid search model")
    parser.add_argument('--model', type=str, help="model type selection")
    main(parser)