from sklearn.metrics import accuracy_score, classification_report, roc_auc_score


def evaluate_model(model, X_test, y_test):

    predictions = model.predict(X_test)
    # accuracy
    acc = accuracy_score(y_test, predictions)

    # classification report
    report = classification_report(y_test, predictions)

    # ROC-AUC 
    try:
        proba = model.predict_proba(X_test)[:, 1]
        roc_auc = roc_auc_score(y_test, proba)
    except:
        roc_auc = None

    return {
        "accuracy": acc,
        "roc_auc": roc_auc,
        "report": report
    }