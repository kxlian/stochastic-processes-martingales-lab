from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Preformatted
from reportlab.lib.enums import TA_CENTER

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "paper" / "stochastic_processes_note.pdf"

def add_para(story, text, style):
    if text.strip():
        story.append(Paragraph(text.strip(), style))
        story.append(Spacer(1, 0.18 * cm))


def build_pdf():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="TitleCenter", parent=styles["Title"], alignment=TA_CENTER, fontSize=22, leading=27, spaceAfter=12))
    styles.add(ParagraphStyle(name="Subtitle", parent=styles["Normal"], alignment=TA_CENTER, fontSize=11, leading=15, spaceAfter=18))
    styles.add(ParagraphStyle(name="Section", parent=styles["Heading1"], fontSize=15, leading=19, spaceBefore=10, spaceAfter=8))
    styles.add(ParagraphStyle(name="Body", parent=styles["BodyText"], fontSize=9.8, leading=13.5, spaceAfter=5))
    styles.add(ParagraphStyle(name="CodeBlock", parent=styles["Code"], fontSize=8.5, leading=11, leftIndent=12, spaceBefore=4, spaceAfter=8))

    doc = SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    story = []
    story.append(Paragraph("Stochastic Processes & Martingales", styles["TitleCenter"]))
    story.append(Paragraph("A compact mathematical research note on random walks, filtrations, martingales, stopping times, quadratic variation, and Brownian motion.", styles["Subtitle"]))

    sections = [
        ("1. Random Walks and Information", [
            "Let (X_i) be independent random variables with P(X_i = 1) = P(X_i = -1) = 1/2. The symmetric random walk is S_0 = 0 and S_n = X_1 + ... + X_n.",
            "The natural filtration F_n = sigma(X_1, ..., X_n) represents exactly the information revealed by the first n increments. This distinction between the path and available information is the starting point for dynamic probability.",
        ], ["S_0 = 0\nS_n = X_1 + ... + X_n\nF_n = sigma(X_1, ..., X_n)"]),
        ("2. Martingales", [
            "A process (M_n) is a martingale with respect to (F_n) if it is adapted, integrable, and E[M_n | F_m] = M_m for m <= n.",
            "For the symmetric random walk, future increments are independent of current information and have mean zero. Therefore E[S_n | F_m] = S_m, so the random walk is a martingale.",
            "A useful second example is the exponential martingale M_n(theta) = exp(theta S_n) / (cosh(theta))^n. The denominator removes the expected exponential growth.",
        ], ["E[S_n | F_m] = E[S_m + X_{m+1} + ... + X_n | F_m] = S_m"]),
        ("3. Stopping Times", [
            "A random time tau is a stopping time if the event {tau <= n} is known at time n for every n. A first hitting time is a stopping time; the time of the future maximum is generally not.",
            "This is the mathematical version of avoiding look-ahead bias: a valid rule must be measurable with respect to the information available when the decision is made.",
        ], ["tau = inf{n >= 0 : |S_n| >= a}"]),
        ("4. Optional Stopping", [
            "If (M_n) is a martingale and tau is a bounded stopping time, then E[M_tau] = E[M_0]. For a symmetric random walk starting at zero, this gives E[S_tau] = 0.",
            "The message is precise: under suitable conditions, stopping a fair game does not create positive expectation. The conditions are essential; without boundedness or integrability, the conclusion can fail.",
        ], []),
        ("5. Brownian Motion", [
            "Brownian motion W_t starts at zero, has independent increments, satisfies W_t - W_s ~ Normal(0, t-s), and has continuous sample paths.",
            "It is the canonical continuous-time limit object for accumulated independent shocks.",
        ], []),
        ("6. Quadratic Variation", [
            "For a partition 0 = t_0 < ... < t_n = T, quadratic variation is the sum of squared increments. For Brownian motion, this converges to T.",
            "This is mathematically striking: Brownian paths are continuous but not smooth. Their squared increments do not vanish; they accumulate into elapsed time.",
        ], ["sum_k (W_{t_{k+1}} - W_{t_k})^2 -> T"]),
        ("7. From Random Walks to Brownian Motion", [
            "Define W_n(t) = S_floor(nt) / sqrt(n). At t = 1, the central limit theorem gives convergence toward a standard normal variable.",
            "Donsker's invariance principle extends this endpoint convergence to process-level convergence: the scaled and interpolated random walk converges in distribution toward Brownian motion.",
        ], ["W_n(t) = S_floor(nt) / sqrt(n),  0 <= t <= 1"]),
        ("8. Why This Matters", [
            "This note is not an investment memo. Filtrations explain information sets. Martingales explain conditional fairness. Stopping times explain legitimate timing rules. Quadratic variation explains pathwise roughness. Scaling limits explain how discrete stochastic systems can converge to continuous models.",
            "The correct reading is: this is the mathematical foundation underneath systematic research.",
        ], []),
    ]

    for idx, (title, paras, blocks) in enumerate(sections):
        if idx in {4, 7}:
            story.append(PageBreak())
        story.append(Paragraph(title, styles["Section"]))
        for p in paras:
            add_para(story, p, styles["Body"])
        for block in blocks:
            story.append(Preformatted(block, styles["CodeBlock"]))
            story.append(Spacer(1, 0.1 * cm))

    doc.build(story)

if __name__ == "__main__":
    build_pdf()
