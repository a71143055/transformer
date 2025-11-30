def summarize_requirements(idea, goals, constraints):
    summary = [
        f"아이디어: {idea[:80]}",
        f"목표: {goals[:80]}",
        f"제약: {constraints[:80]}",
        "권장: 로깅/테스트/설정 분리"
    ]
    return "\n".join(summary)