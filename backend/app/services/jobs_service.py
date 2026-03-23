import pandas as pd
import numpy as np
from rapidfuzz import fuzz
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import current_app
from ..utils.text_utils import normalize_text, parse_skill_list

class JobsService:
    _df = None
    _vectorizer = None
    _matrix = None
    _col_skills_exists = False

    @staticmethod
    def load_jobs():
        if JobsService._df is None:
            path = current_app.config["JOBS_DATA_PATH"]
            df = pd.read_csv(path)

            def pick(cands):
                for c in cands:
                    if c in df.columns:
                        return c
                return None

            col_company = pick(["company", "Company", "company_name"])
            col_title = pick(["title", "job_title", "Title"])
            col_skills = pick(["skills", "Skills", "skill_list", "required_skills"])
            col_desc = pick(["description", "job_description", "Description"])

            if not (col_company and col_title):
                raise ValueError("jobs_and_skills.csv must have company and title columns.")

            JobsService._col_skills_exists = bool(col_skills)

            df["_company"] = df[col_company].astype(str).fillna("")
            df["_title"] = df[col_title].astype(str).fillna("")
            df["_skills"] = df[col_skills].astype(str).fillna("") if col_skills else ""
            df["_desc"] = df[col_desc].astype(str).fillna("") if col_desc else ""
            df["_role_text"] = (df["_title"] + " " + df["_skills"] + " " + df["_desc"]).fillna("")

            JobsService._df = df

            JobsService._vectorizer = TfidfVectorizer(stop_words="english", max_features=30000)
            JobsService._matrix = JobsService._vectorizer.fit_transform(df["_role_text"].astype(str))
        return JobsService._df

    @staticmethod
    def role_skills_from_row(row) -> list[str]:
        if not JobsService._col_skills_exists:
            return []
        return parse_skill_list(row.get("_skills", ""))

    @staticmethod
    def find_company_role(company: str, role: str, top_k=10):
        df = JobsService.load_jobs()
        company_n = normalize_text(company)
        role_n = normalize_text(role)
        scored = []
        for idx, r in df.iterrows():
            c = normalize_text(r["_company"])
            t = normalize_text(r["_title"])
            c_score = fuzz.partial_ratio(company_n, c) if company_n else 0
            t_score = fuzz.partial_ratio(role_n, t) if role_n else 0
            total = 0.55 * t_score + 0.45 * c_score
            scored.append((total, idx))
        scored.sort(reverse=True, key=lambda x: x[0])
        return [i for _, i in scored[:top_k]]

    @staticmethod
    def find_by_role(role: str, top_k=80):
        df = JobsService.load_jobs()
        role_n = normalize_text(role)
        scored = []
        for idx, r in df.iterrows():
            t = normalize_text(r["_title"])
            scored.append((fuzz.partial_ratio(role_n, t), idx))
        scored.sort(reverse=True, key=lambda x: x[0])
        return [i for _, i in scored[:top_k]]

    @staticmethod
    def recommend_by_resume(resume_text: str, top_k=60):
        df = JobsService.load_jobs()
        q = JobsService._vectorizer.transform([resume_text or ""])
        sims = cosine_similarity(q, JobsService._matrix)[0]
        top_idx = np.argsort(-sims)[:top_k]
        return top_idx.tolist(), sims[top_idx].tolist()
