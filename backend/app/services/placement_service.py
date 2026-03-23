import os
import joblib
import pandas as pd
import numpy as np
from flask import current_app

class PlacementService:
    _model = None

    @staticmethod
    def load_model():
        if PlacementService._model is None:
            path = current_app.config["PLACEMENT_MODEL_PATH"]
            if not os.path.exists(path):
                PlacementService._model = None
            else:
                PlacementService._model = joblib.load(path)
        return PlacementService._model

    @staticmethod
    def predict_probability(profile: dict) -> float:
        model = PlacementService.load_model()
        if model is None:
            vals = [float(profile.get(k, 0) or 0) for k in ["ssc_p", "hsc_p", "degree_p", "etest_p", "mba_p"]]
            return float(np.clip(sum(vals) / max(1, len(vals)), 0, 100))

        cols = model.named_steps["preprocess"].feature_names_in_
        row = {}
        for c in cols:
            row[c] = profile.get(c, profile.get(c.lower(), None))
            if row[c] is None:
                row[c] = "No" if c.lower() == "workex" else 0

        X = pd.DataFrame([row])
        proba = model.predict_proba(X)[0][1] * 100
        return float(np.clip(proba, 0, 100))
