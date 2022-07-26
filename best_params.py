params = {
    'lr': {
        'params': {'C': 1.0, 'random_state': 57},
        'score': 0.829
    },
    'svc': {
        'params': {'C': 1000.0, 'gamma': 0.001, 'random_state': 57},
        'score': 0.830
    },
    'lsvc': {
        'params': {'C': 1.0, 'random_state': 57},
        'score': 0.827
    },
    'gnb': {
        'params': {'var_smoothing': 1e-06},
        'score': 0.757
    },
    'mnb': {
        'params': {'alpha': 0.0},
        'score': 0.781
    },
    'knn': {
        'params': {'n_neighbors': 4},
        'score': 0.791
    },
    'dt': {
        'params': {'criterion': 'gini', 'max_depth': 3, 'min_samples_leaf': 0.1, 'random_state': 57},
        'score': 0.775
    },
    'rf': {
        'params': {'criterion': 'gini', 'max_depth': 3, 'min_samples_leaf': 0.1, 'n_estimators': 250, 'random_state': 57},
        'score': 0.787
    },
    'ada': {
        'params': {'n_estimators': 100, 'random_state': 57},
        'score': 0.817
    },
    'gb': {
        'params': {'min_samples_leaf': 0.1, 'n_estimators': 250, 'random_state': 57},
        'score': 0.836
    },
    'sgd': {
        'params': {'alpha': 0.001, 'penalty': 'elasticnet', 'random_state': 57},
        'score': 0.824
    },
    'xgb': {
        'params': {'eta': 0.6, 'gamma': 1.0, 'lambda': 10.0, 'seed': 57},
        'score': 0.839
    }
}