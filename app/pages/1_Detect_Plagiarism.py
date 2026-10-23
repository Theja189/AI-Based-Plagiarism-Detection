
import re
import sys
import tempfile
from pathlib import Path

import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.predict import predict_pair
from src.semantic_similarity import semantic_similarity

# =========================================================
# 1. PROJECT PATHS AND IMPORTS
# =========================================================
PROJECT_ROOT = Path(__file__).resolve().parents[2]
APP_DIR = PROJECT_ROOT / "app"

for folder in (PROJECT_ROOT, APP_DIR):
    folder_string = str(folder)
    if folder_string not in sys.path:
        sys.path.insert(0, folder_string)

from components.sidebar import render_sidebar
from src.document_parser import extract_text
from src.preprocessing import normalize_text


# =========================================================
# 2. PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Detect Plagiarism | PlagiarismAI",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded",
)

render_sidebar("Detect Plagiarism")


# =========================================================
# 3. PROFESSIONAL CSS
# =========================================================
st.markdown(
    """
    <style>
    /* ---------- Page background and spacing ---------- */

    .stApp {
        background: linear-gradient(
            135deg,
            #f8fbff 0%,
            #eef5fc 100%
        );
    }

    [data-testid="stMainBlockContainer"],
    .block-container {
        max-width: 1450px !important;
        width: 100% !important;
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
    }

    /* Hide Streamlit's top navigation/header only.
       Keep the application sidebar visible. */

    [data-testid="stHeader"] {
        display: none !important;
    }

    [data-testid="stToolbar"] {
        display: none !important;
    }

    /* ---------- Main page heading ---------- */

    .page-heading {
        margin: 0 0 22px 0;
    }

    .page-heading h1 {
        color: #102b4e !important;
        font-size: 2.3rem;
        font-weight: 800;
        line-height: 1.25;
        margin: 0 0 10px 0;
    }

    .page-heading p {
        color: #58708e !important;
        font-size: 1rem;
        line-height: 1.7;
        margin: 0;
    }

    /* ---------- Navy-blue gradient banner ---------- */

    .detect-banner {
        background: linear-gradient(
            110deg,
            #071d38 0%,
            #10476f 55%,
            #1475a8 100%
        );
        border: 1px solid #2587b8;
        border-radius: 16px;
        padding: 28px;
        margin: 22px 0 28px 0;
        box-shadow: 0 10px 28px rgba(16, 54, 91, 0.10);
    }

    .detect-banner h2 {
        color: #ffffff !important;
        font-size: 1.65rem;
        font-weight: 800;
        line-height: 1.4;
        margin: 0 0 12px 0;
    }

    .detect-banner p {
        color: #f1f7ff !important;
        font-size: 1rem;
        line-height: 1.7;
        margin: 0;
    }

    /* ---------- Headings and standard text ---------- */

    .block-container h1,
    .block-container h2,
    .block-container h3,
    .block-container h4 {
        color: #172b46;
    }

    [data-testid="stMarkdownContainer"] p {
        color: #263d58;
    }

    /* ---------- Radio input ---------- */

    [data-testid="stRadio"] {
        margin-bottom: 24px !important;
    }

    [data-testid="stRadio"] label,
    [data-testid="stRadio"] p,
    [data-testid="stRadio"] span {
        color: #24364b !important;
    }

/* =========================================
   PREMIUM LIGHT FILE UPLOADER
========================================= */

/* Outer uploader container */
[data-testid="stFileUploader"] {
    background: #eef4fa !important;
    border: 1px solid #dce8f5 !important;
    border-radius: 12px !important;
    padding: 12px !important;
}

/* Dropzone */
[data-testid="stFileUploaderDropzone"] {
    background: #f8fbff !important;
    background-color: #f8fbff !important;
    border: 1px dashed #b7cce2 !important;
    border-radius: 9px !important;
}

/* Dropzone text */
[data-testid="stFileUploaderDropzone"] p,
[data-testid="stFileUploaderDropzone"] span,
[data-testid="stFileUploaderDropzone"] small,
[data-testid="stFileUploaderDropzone"] label {
    color: #172b46 !important;
    -webkit-text-fill-color: #172b46 !important;
}

/* Upload button */
[data-testid="stFileUploader"] button {
    background: #ffffff !important;
    background-color: #ffffff !important;
    color: #172b46 !important;
    -webkit-text-fill-color: #172b46 !important;
    border: 1px solid #d5e0ee !important;
    border-radius: 8px !important;
}

[data-testid="stFileUploader"] button:hover {
    background: #e6f2ff !important;
    background-color: #e6f2ff !important;
    border-color: #2586c9 !important;
}

/* Uploaded file item — white background */
[data-testid="stFileUploaderFile"] {
    background: #ffffff !important;
    background-color: #ffffff !important;
    color: #172b46 !important;
    border: 1px solid #d5e2f0 !important;
    border-radius: 8px !important;
    box-shadow: none !important;
}

/* Filename and file details */
[data-testid="stFileUploaderFile"] p,
[data-testid="stFileUploaderFile"] span,
[data-testid="stFileUploaderFile"] small,
[data-testid="stFileUploaderFile"] div {
    color: #172b46 !important;
    -webkit-text-fill-color: #172b46 !important;
}

/* File remove button */
[data-testid="stFileUploaderFile"] button {
    background: #ffffff !important;
    background-color: #ffffff !important;
    color: #17365d !important;
    border: 1px solid #d6e5f5 !important;
}

/* Upload instructions */
[data-testid="stFileUploader"] small,
[data-testid="stFileUploader"] label {
    color: #405875 !important;
    -webkit-text-fill-color: #405875 !important;
}
    /* ---------- Text areas and text inputs ---------- */

    [data-testid="stTextArea"] textarea,
    [data-testid="stTextInput"] input {
        background: #ffffff !important;
        color: #172b46 !important;
        -webkit-text-fill-color: #172b46 !important;
        border: 1px solid #d5e2f0 !important;
        border-radius: 10px !important;
    }

    [data-testid="stTextArea"] textarea::placeholder,
    [data-testid="stTextInput"] input::placeholder {
        color: #788ba2 !important;
        -webkit-text-fill-color: #788ba2 !important;
    }

    /* ---------- Buttons ---------- */

    .stButton > button[kind="primary"] {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        background: linear-gradient(
            105deg,
            #10365b,
            #087eb6
        ) !important;
        border: 1px solid #2489c4 !important;
        border-radius: 10px !important;
        min-height: 49px !important;
        font-weight: 700 !important;
        box-shadow: 0 5px 14px rgba(8, 80, 130, 0.12);
    }

    .stButton > button[kind="primary"]:hover {
        background: linear-gradient(
            105deg,
            #0b2948,
            #066b9d
        ) !important;
        border-color: #49a8df !important;
    }

    /* ---------- Premium download button ---------- */
[data-testid="stDownloadButton"] button {
    background: linear-gradient(105deg, #10365b, #087eb6) !important;
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    border: 1px solid #2489c4 !important;
    border-radius: 10px !important;
    min-height: 48px !important;
    font-weight: 700 !important;
    box-shadow: 0 5px 14px rgba(8, 80, 130, 0.15) !important;
}

[data-testid="stDownloadButton"] button:hover {
    background: linear-gradient(105deg, #0b2948, #066b9d) !important;
    border-color: #49a8df !important;
}

    /* ---------- Analysis metrics ---------- */

    [data-testid="stMetric"] {
        background: #ffffff !important;
        border: 1px solid #dce8f5 !important;
        border-radius: 12px !important;
        padding: 17px !important;
    }

    [data-testid="stMetricLabel"],
    [data-testid="stMetricLabel"] * {
        color: #405875 !important;
    }

    [data-testid="stMetricValue"],
    [data-testid="stMetricValue"] * {
        color: #172b46 !important;
    }

    /* ---------- Similarity result card ---------- */

    .result-card {
        padding: 25px;
        border-radius: 16px;
        border: 1px solid #cfe2f6;
        background: #ffffff;
        margin: 18px 0;
    }

    .result-card h3 {
        color: #315f98 !important;
        margin-top: 0;
    }

    .result-score {
        color: #1269ad !important;
        font-size: 2.7rem;
        font-weight: 800;
        line-height: 1.3;
        margin: 12px 0;
    }

    .score-track {
        width: 100%;
        height: 12px;
        background: #dce8f5;
        border-radius: 20px;
        overflow: hidden;
    }

    .score-fill {
        height: 100%;
        border-radius: 20px;
        background: linear-gradient(
            90deg,
            #2586ff,
            #35c5ef
        );
    }

    .result-note {
        color: #58708e !important;
        margin-top: 12px;
        line-height: 1.7;
    }

    /* ---------- Matching passages ---------- */

    .match-card {
        padding: 15px;
        margin: 12px 0 8px 0;
        border: 1px solid #dce8f5;
        border-radius: 12px;
        background: #ffffff;
    }

    .match-label {
        color: #176db3 !important;
        font-weight: 700;
        line-height: 1.6;
    }

    /* ---------- Mobile layout ---------- */

    @media (max-width: 700px) {
        [data-testid="stMainBlockContainer"],
        .block-container {
            padding: 1.3rem 1rem 2rem !important;
        }

        .page-heading h1 {
            font-size: 1.8rem;
        }

        .detect-banner {
            padding: 20px;
        }

        .detect-banner h2 {
            font-size: 1.35rem;
        }

        .result-card {
            padding: 18px;
        }

        .result-score {
            font-size: 2.2rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# 4. DOCUMENT PROCESSING FUNCTIONS
# =========================================================
def read_uploaded_document(uploaded_file):
    """Extract readable text from TXT, PDF or DOCX."""

    if uploaded_file is None:
        return ""

    extension = Path(uploaded_file.name).suffix.lower()

    if extension not in {".txt", ".pdf", ".docx"}:
        raise ValueError(
            "Unsupported file type. Upload a TXT, PDF or DOCX file."
        )

    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(
            suffix=extension,
            delete=False,
        ) as temp_file:
            temp_file.write(uploaded_file.getvalue())
            temp_path = Path(temp_file.name)

        extracted_text = extract_text(str(temp_path))
        return normalize_text(extracted_text or "").strip()

    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)


def clean_for_analysis(text):
    """Normalize document text before comparing."""
    return normalize_text(text or "").strip()


# =========================================================
# 5. TF-IDF COSINE SIMILARITY
# =========================================================
def get_similarity(text_a, text_b):
    """Calculate lexical similarity between two documents."""

    vectorizer = TfidfVectorizer(
        lowercase=True,
        strip_accents="unicode",
        ngram_range=(1, 2),
        sublinear_tf=True,
    )

    matrix = vectorizer.fit_transform([text_a, text_b])

    score = cosine_similarity(
        matrix[0:1],
        matrix[1:2],
    )[0][0]

    return float(score)


# =========================================================
# 6. MATCHING SENTENCE DETECTION
# =========================================================
def split_sentences(text):
    """Split text into sentence-like passages."""

    parts = re.split(r"(?<=[.!?])\s+|\n+", text)

    return [
        part.strip()
        for part in parts
        if len(part.strip()) > 15
    ]


def find_matching_sentences(text_a, text_b, limit=10):
    """Return sentence pairs with lexical similarity >= 25%."""

    sentences_a = split_sentences(text_a)
    sentences_b = split_sentences(text_b)

    if not sentences_a or not sentences_b:
        return []

    all_sentences = sentences_a + sentences_b

    try:
        vectorizer = TfidfVectorizer(
            lowercase=True,
            strip_accents="unicode",
            ngram_range=(1, 2),
        )

        matrix = vectorizer.fit_transform(all_sentences)

    except ValueError:
        return []

    vectors_a = matrix[:len(sentences_a)]
    vectors_b = matrix[len(sentences_a):]

    scores = cosine_similarity(vectors_a, vectors_b)
    matches = []

    for i, sentence_a in enumerate(sentences_a):
        for j, sentence_b in enumerate(sentences_b):
            score = float(scores[i, j])

            if score >= 0.25:
                matches.append(
                    {
                        "sentence_a": sentence_a,
                        "sentence_b": sentence_b,
                        "score": score,
                    }
                )

    matches.sort(
        key=lambda item: item["score"],
        reverse=True,
    )

    unique_matches = []
    seen = set()

    for match in matches:
        key = (
            match["sentence_a"],
            match["sentence_b"],
        )

        if key in seen:
            continue

        seen.add(key)
        unique_matches.append(match)

        if len(unique_matches) >= limit:
            break

    return unique_matches


# =========================================================
# 7. PAGE HEADING
# =========================================================
st.markdown(
    """
    <div class="page-heading">
        <h1>📘 Detect Plagiarism</h1>
        <p>
            Upload two academic documents or paste text
            to compare their content.
        </p>
    </div>

    <div class="detect-banner">
        <h2>Academic Document Comparison</h2>
        <p>
            Compare documents using TF-IDF and cosine similarity.
            Review matching passages and interpret results carefully.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# 8. INPUT METHOD
# =========================================================
input_method = st.radio(
    "Choose how to compare documents",
    ["Upload Documents", "Paste Text"],
    horizontal=True,
)

text_a = ""
text_b = ""

name_a = "Original document"
name_b = "Compared document"

file_a = None
file_b = None


# =========================================================
# 9. UPLOAD DOCUMENTS
# =========================================================
if input_method == "Upload Documents":

    st.markdown("### Upload your documents")

    col_a, col_b = st.columns(2, gap="large")

    with col_a:
        st.markdown("#### 📄 Original Document")
        st.caption("Upload the original/reference document")

        file_a = st.file_uploader(
            "Choose original document",
            type=["txt", "pdf", "docx"],
            key="original_upload",
            label_visibility="collapsed",
        )

        if file_a is not None:
            name_a = file_a.name
            st.success(f"Selected: {file_a.name}")

    with col_b:
        st.markdown("#### 📝 Compared Document")
        st.caption("Upload the document you want to compare")

        file_b = st.file_uploader(
            "Choose compared document",
            type=["txt", "pdf", "docx"],
            key="compared_upload",
            label_visibility="collapsed",
        )

        if file_b is not None:
            name_b = file_b.name
            st.success(f"Selected: {file_b.name}")


# =========================================================
# 10. PASTE TEXT
# =========================================================
else:

    st.markdown("### Enter the document text")

    col_a, col_b = st.columns(2, gap="large")

    with col_a:
        name_a = st.text_input(
            "Original document name",
            value="Original document",
        )

        text_a = st.text_area(
            "Original text",
            height=260,
            placeholder="Paste the original academic text here...",
        )

    with col_b:
        name_b = st.text_input(
            "Compared document name",
            value="Compared document",
        )

        text_b = st.text_area(
            "Text to compare",
            height=260,
            placeholder="Paste the second academic text here...",
        )


# =========================================================
# 11. ANALYZE DOCUMENTS
# =========================================================
st.write("")

if st.button(
    "🔍 Analyze Documents",
    type="primary",
    use_container_width=True,
):

    try:
        if input_method == "Upload Documents":

            if file_a is None or file_b is None:
                st.error(
                    "Please upload both documents before analyzing."
                )
                st.stop()

            with st.spinner("Extracting document text..."):
                text_a = read_uploaded_document(file_a)
                text_b = read_uploaded_document(file_b)

        text_a = clean_for_analysis(text_a)
        text_b = clean_for_analysis(text_b)

        if not text_a or not text_b:
            st.error(
                "No readable text was found. Check the documents "
                "or paste the text manually."
            )
            st.stop()

        if text_a == text_b:
            st.warning(
                "Both documents contain identical text. "
                "Review the comparison result carefully."
            )

        with st.spinner("Calculating text similarity and ML prediction..."):
            similarity = get_similarity(text_a, text_b)

            matches = find_matching_sentences(
                text_a,
                text_b,
            )

            ml_result = predict_pair(text_a, text_b)

        percentage = round(similarity * 100, 2)

        semantic_score = semantic_similarity(text_a, text_b)

        st.session_state["plagiarism_result"] = {
            "similarity": percentage,
            "ml_prediction": ml_result["prediction"],
            "ml_label": ml_result["label"],
            "ml_probability": ml_result["model_positive_probability"],
            "ml_warning": ml_result["warning"],
            "semantic_similarity": semantic_score,
            "matches": matches,
            "name_a": name_a,
            "name_b": name_b,
            "length_a": len(text_a.split()),
            "length_b": len(text_b.split()),
            "text_a": text_a,
            "text_b": text_b,
        }

    except Exception as exc:
        st.error(
            f"Could not analyze the documents: {exc}"
        )


# =========================================================
# 12. DISPLAY ANALYSIS RESULTS
# =========================================================
result = st.session_state.get("plagiarism_result")

if result:

    st.divider()
    st.markdown("## 📊 Analysis Results")

    score = result["similarity"]

    metric1, metric2, metric3 = st.columns(3)

    with metric1:
        st.metric(
            "Text Similarity",
            f'{score:.2f}%',
        )

    with metric2:
        st.metric(
            "Original Word Count",
            result["length_a"],
        )

    with metric3:
        st.metric(
            "Compared Word Count",
            result["length_b"],
        )

    st.markdown("### TF-IDF Cosine Similarity")

    st.markdown(
    f"""
    <div style="
        font-size:42px;
        font-weight:800;
        color:#1269ad;
        margin:8px 0 12px 0;
    ">{score:.2f}%</div>
    """,
    unsafe_allow_html=True,
)

    st.progress(min(max(float(score) / 100, 0.0), 1.0))

    st.markdown("### 🤖 Experimental ML Prediction")

    ml_col1, ml_col2 = st.columns(2)

    with ml_col1:
        st.metric(
            "Model Positive Probability",
            f"{result['ml_probability'] * 100:.2f}%",
        )

    with ml_col2:
        st.write(
            "Prediction:",
            result["ml_label"],
        )

    st.warning(result["ml_warning"])

    st.markdown("### 🧠 Semantic Similarity")

    semantic_score = result["semantic_similarity"]

    st.metric(
        "Meaning Similarity",
        f"{semantic_score:.2f}%"
    )

    st.progress(
        min(max(float(semantic_score) / 100, 0.0), 1.0)
    )

    st.caption(
        "Semantic similarity estimates similarity in meaning. "
        "It is not proof of plagiarism."
    )

    st.caption(
    "Similarity between the two supplied documents. "
    "This score is not proof of plagiarism."
)

    # ---------- Documents compared ----------

    st.markdown("### 📄 Documents Compared")

    doc_col_a, doc_col_b = st.columns(2)

    with doc_col_a:
        st.info(f"**Original:** {result['name_a']}")

    with doc_col_b:
        st.info(f"**Compared:** {result['name_b']}")

    # ---------- Matching passages ----------

    st.markdown("### 🔎 Potentially Matching Passages")

    if result["matches"]:

        for index, match in enumerate(
            result["matches"],
            start=1,
        ):

            st.markdown(
                f"""
                <div class="match-card">
                    <div class="match-label">
                        Match {index} · Sentence similarity:
                        {match['score'] * 100:.1f}%
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            left, right = st.columns(2, gap="medium")

            with left:
                st.markdown("**Original passage**")
                st.write(match["sentence_a"])

            with right:
                st.markdown("**Compared passage**")
                st.write(match["sentence_b"])

    else:
        st.info(
            "No sentence pairs met the current matching threshold. "
            "This does not prove that the documents are plagiarism-free."
        )

    # =====================================================
    # 13. DOWNLOAD ANALYSIS REPORT
    # =====================================================
    
    report_lines = [
        "AI-BASED PLAGIARISM DETECTION SYSTEM",
        "=" * 45,
        "",
        "1. DOCUMENT DETAILS",
        "-" * 30,
        f"Original document: {result['name_a']}",
        f"Compared document: {result['name_b']}",
        f"Original word count: {result['length_a']}",
        f"Compared word count: {result['length_b']}",
        "",
        "2. SIMILARITY RESULTS",
        "-" * 30,
        f"TF-IDF cosine similarity: {score:.2f}%",
        (
            "Semantic similarity: "
            f"{result['semantic_similarity']:.2f}%"
        ),
        "",
        "3. EXPERIMENTAL ML PREDICTION",
        "-" * 30,
        f"Prediction label: {result['ml_label']}",
        (
            "Model positive probability: "
            f"{result['ml_probability'] * 100:.2f}%"
        ),
        f"Model prediction value: {result['ml_prediction']}",
        "",
        "4. MATCHING PASSAGES",
        "-" * 30,
        f"Number of matching sentence pairs: {len(result['matches'])}",
    ]

    if result["matches"]:
        for index, match in enumerate(result["matches"], start=1):
            report_lines.extend([
                "",
                f"Match {index}",
                f"Sentence similarity: {match['score'] * 100:.1f}%",
                f"Original passage: {match['sentence_a']}",
                f"Compared passage: {match['sentence_b']}",
            ])
    else:
        report_lines.append(
            "No sentence pairs met the current matching threshold."
        )

    report_lines.extend([
        "",
        "5. INTERPRETATION AND LIMITATIONS",
        "-" * 30,
        "Similarity scores indicate textual or semantic resemblance.",
        "Similarity scores are not proof of plagiarism.",
        "Semantic similarity estimates similarity in meaning.",
        (
            "The ML model is experimental and was trained on "
            "10 synthetic examples."
        ),
        (
            "Its prediction and probability are not reliable "
            "evidence of plagiarism."
        ),
        "Only the two supplied documents were compared.",
        "The system does not search the entire internet or all academic databases.",
        "Human review is required to interpret the findings.",
        "",
        "End of report.",
    ])

    report_content = "\n".join(report_lines)



    st.download_button(
        "⬇️ Download Analysis Report",
        data=report_content,
        file_name="plagiarism_analysis_report.txt",
        mime="text/plain",
        use_container_width=True,
    )

