from ..utils.text_utils import normalize_text

CURATED_SKILLS = [
    "python","java","javascript","typescript","react","node","flask","django","fastapi",
    "sql","mysql","postgresql","mongodb","redis","docker","kubernetes","aws","azure","gcp",
    "git","linux","pandas","numpy","scikit-learn","machine learning","deep learning",
    "data analysis","power bi","tableau","excel","dsa","system design","rest api","graphql",
    "html","css","tailwind","nextjs","express"
]

EVIDENCE_WORDS = [
    "project","internship","built","developed","deployed","impact","achieved",
    "optimized","reduced","increased"
]

class ResumeService:
    @staticmethod
    def extract_resume_skills(resume_text: str):
        t = normalize_text(resume_text)
        found = set()
        for kw in CURATED_SKILLS:
            if normalize_text(kw) in t:
                found.add(kw)
        return sorted(found)

    @staticmethod
    def compute_fit(resume_text: str, role_skills: list[str]):
        resume_sk = set([normalize_text(x) for x in ResumeService.extract_resume_skills(resume_text)])
        role_sk = set([normalize_text(x) for x in (role_skills or []) if x])

        if not role_sk:
            return 50, [], []

        matched = sorted([s for s in role_sk if s in resume_sk])
        missing = sorted([s for s in role_sk if s not in resume_sk])

        raw = (len(matched) / max(1, len(role_sk))) * 100
        fit = int(round(min(100, 15 + raw * 0.85)))
        return fit, matched[:25], missing[:25]

    @staticmethod
    def ats_score(resume_text: str, target_skills: list[str] | None):
        if target_skills:
            fit, matched, missing = ResumeService.compute_fit(resume_text, target_skills)
            t = normalize_text(resume_text)
            bonus = sum(1 for w in EVIDENCE_WORDS if w in t) * 2
            return int(min(100, fit + bonus)), matched, missing

        skills = ResumeService.extract_resume_skills(resume_text)
        return int(min(100, 25 + len(skills) * 6)), skills[:20], []
