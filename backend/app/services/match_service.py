from .placement_service import PlacementService
from .resume_service import ResumeService
from .jobs_service import JobsService

class MatchService:
    @staticmethod
    def match(profile: dict, resume_text: str, company: str = "", role: str = "") -> dict:
        placement_prob = PlacementService.predict_probability(profile)
        company = (company or "").strip()
        role = (role or "").strip()

        mode = "B"
        if company and role:
            mode = "A"
        elif (not company) and role:
            mode = "C"

        if mode == "A":
            ids = JobsService.find_company_role(company, role, top_k=10)
            df = JobsService.load_jobs()
            best_row = df.loc[ids].iloc[0]
            skills = JobsService.role_skills_from_row(best_row)

            fit, matched, missing = ResumeService.compute_fit(resume_text, skills)
            ats, _, _ = ResumeService.ats_score(resume_text, skills)

            suggestions = []
            if missing:
                suggestions.append(f"Add/learn these skills: {', '.join(missing[:8])}.")
            suggestions += [
                "Add 2 quantified projects (impact metrics).",
                "Mirror role keywords in Skills + Projects (ATS).",
                "Add internship outcomes with numbers.",
            ]

            return {
                "mode": "A",
                "placement_probability": round(placement_prob, 2),
                "target": {"company": company, "role": role},
                "role_fit_score": fit,
                "resume_ats_score": ats,
                "matched_skills": matched[:15],
                "missing_skills": missing[:15],
                "suggestions": suggestions
            }

        if mode == "C":
            ids = JobsService.find_by_role(role, top_k=80)
            df = JobsService.load_jobs()
            subset = df.loc[ids]

            results = []
            for _, r in subset.iterrows():
                skills = JobsService.role_skills_from_row(r)
                role_fit, _, _ = ResumeService.compute_fit(resume_text, skills)
                ats, _, _ = ResumeService.ats_score(resume_text, skills)
                fit_score = int(round(0.55 * role_fit + 0.25 * ats + 0.20 * placement_prob))
                results.append({
                    "company": r["_company"],
                    "role": r["_title"],
                    "fit_score": fit_score,
                    "role_fit": role_fit,
                    "ats": ats
                })

            seen, uniq = set(), []
            for x in sorted(results, key=lambda z: z["fit_score"], reverse=True):
                key = (x["company"].lower(), x["role"].lower())
                if key in seen:
                    continue
                seen.add(key)
                uniq.append(x)
                if len(uniq) >= 25:
                    break

            return {
                "mode": "C",
                "placement_probability": round(placement_prob, 2),
                "target": {"role": role},
                "matches": uniq
            }

        # mode B
        top_ids, sims = JobsService.recommend_by_resume(resume_text, top_k=60)
        df = JobsService.load_jobs()
        subset = df.loc[top_ids].copy()
        subset["_sim"] = sims

        results = []
        for _, r in subset.iterrows():
            skills = JobsService.role_skills_from_row(r)
            role_fit, _, _ = ResumeService.compute_fit(resume_text, skills)
            ats, _, _ = ResumeService.ats_score(resume_text, skills)
            fit_score = int(round(0.45 * (r["_sim"] * 100) + 0.30 * role_fit + 0.10 * ats + 0.15 * placement_prob))
            results.append({
                "company": r["_company"],
                "role": r["_title"],
                "fit_score": fit_score,
                "role_fit": role_fit,
                "ats": ats
            })

        seen, uniq = set(), []
        for x in sorted(results, key=lambda z: z["fit_score"], reverse=True):
            key = (x["company"].lower(), x["role"].lower())
            if key in seen:
                continue
            seen.add(key)
            uniq.append(x)
            if len(uniq) >= 25:
                break

        return {
            "mode": "B",
            "placement_probability": round(placement_prob, 2),
            "matches": uniq,
            "note": "No company/role provided → showing best role matches from dataset."
        }
