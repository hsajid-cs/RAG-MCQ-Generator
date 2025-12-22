from sympy import sympify, Eq
import re
from typing import Optional


def _latex_to_plain(tex: Optional[str]) -> str:
    """Very small heuristic LaTeX -> plain math stripper for simple expressions."""
    if not tex:
        return ""
    s = str(tex)
    # remove display math delimiters and common wrappers
    s = s.replace("$$", "").replace("\\,", " ").strip()
    s = re.sub(r"\\begin\{.*?\}|\\end\{.*?\}", "", s)
    s = re.sub(r"\\left|\\right", "", s)
    # remove simple commands like \frac{a}{b} -> (a)/(b) (very naive)
    s = re.sub(r"\\frac\{([^}]*)\}\{([^}]*)\}", r"(\1)/(\2)", s)
    # remove other backslash commands
    s = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\[a-zA-Z]+", "", s)
    # normalize whitespace
    s = re.sub(r"\s+", " ", s).strip()
    return s


def verify_math_solution(solution_latex: Optional[str]) -> bool:
    """
    Heuristic verifier for STEM solutions.

    - If solution contains an equality "lhs = rhs", try sympy Eq(sympify(lhs), sympify(rhs)).
    - Returns True if sympy reports equality, False otherwise.

    Note: This is intentionally conservative — it will return False on parse errors.
    """
    if not solution_latex:
        return False
    try:
        txt = _latex_to_plain(solution_latex)
        if "=" in txt:
            lhs, rhs = txt.split("=", 1)
            # sympify may raise; wrap in try
            L = sympify(lhs.strip())
            R = sympify(rhs.strip())
            return bool(Eq(L, R))
        # if there is no equality we conservatively return False (or you can try numeric checks)
    except Exception:
        return False
    return False