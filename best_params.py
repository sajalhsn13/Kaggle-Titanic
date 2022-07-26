params = {
    'lr': {
        'params': {'C': 100.0, 'random_state': 57},
        'score': 0.802
    },
    'svc': {
        'params': {'C': 100.0, 'gamma': 0.001, 'random_state': 57},
        'score': 0.744
    },
    'lsvc': {
        'params': {'C': 1.0, 'random_state': 57},
        'score': 0.769
    },
    'gnb': {
        'params': {'var_smoothing': 1e-06},
        'score': 0.788
    },
    'mnb': {
        'params': {'alpha': 0.0},
        'score': 0.786
    },
    'dt': {
        'params': {'criterion': 'gini', 'max_depth': 3, 'min_samples_leaf': 0.1, 'random_state': 57},
        'score': 0.775
    },
    'rf': {
        'params': {'criterion': 'entropy', 'max_depth': 3, 'min_samples_leaf': 0.1, 'n_estimators': 50, 'random_state': 57},
        'score': 0.792
    },
    'ada': {
        'params': {'n_estimators': 50, 'random_state': 57},
        'score': 0.808
    },
    'gb': {
        'params': {'min_samples_leaf': 0.1, 'n_estimators': 50, 'random_state': 57},
        'score': 0.823
    },
    'sgb': {
        'params': {'alpha': 0.01, 'penalty': 'l1', 'random_state': 57},
        'score': 0.780
    },
    'xgb': {
        'params': {'eta': 0.1, 'gamma': 1.0, 'lambda': 10.0, 'seed': 57},
        'score': 0.826
    }
}