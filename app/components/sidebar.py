
import streamlit as st


def render_sidebar(active_page="Dashboard"):
    st.markdown(
        """
        <style>
        /* =========================================
           SIDEBAR: FULL HEIGHT, MINIMAL TOP GAP
        ========================================= */
        section[data-testid="stSidebar"] {
            width: 255px !important;
            min-width: 255px !important;
            background: linear-gradient(
                180deg,
                #091b32 0%,
                #0b2342 55%,
                #07182c 100%
            ) !important;
            border-right: 1px solid #29435f !important;
        }

        section[data-testid="stSidebar"] > div:first-child {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }

        section[data-testid="stSidebar"] [data-testid="stSidebarHeader"] {
            height: 0 !important;
            min-height: 0 !important;
            padding: 0 !important;
            margin: 0 !important;
            overflow: hidden !important;
        }

        section[data-testid="stSidebar"] [data-testid="stSidebarContent"] {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }

        section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
            color: #dce9f7 !important;
        }

        section[data-testid="stSidebar"] [data-testid="stCaptionContainer"],
        section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p {
            color: #b8cce1 !important;
            font-size: 12px !important;
            line-height: 1.55 !important;
        }

        /* Hide duplicate default navigation */
        [data-testid="stSidebarNav"] {
            display: none !important;
        }

        /* =========================================
           BRAND
        ========================================= */
        .sidebar-brand {
            display: flex;
            align-items: center;
            gap: 11px;
            padding: 8px 3px 16px;
            margin: 0 0 10px;
            border-bottom: 1px solid #29435f;
        }

        .sidebar-logo {
            width: 43px;
            height: 43px;
            flex-shrink: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 12px;
            background: linear-gradient(135deg, #17659a, #1689c1);
            border: 1px solid #3c83b2;
            font-size: 22px;
        }

        .sidebar-brand-name {
            color: #ffffff;
            font-size: 16px;
            font-weight: 800;
            letter-spacing: -0.3px;
        }

        .sidebar-brand-subtitle {
            color: #b8cee4;
            font-size: 9px;
            font-weight: 700;
            letter-spacing: 1px;
            margin-top: 4px;
        }

        /* =========================================
           SECTION LABELS
        ========================================= */
        .sidebar-section {
            color: #91b5d5 !important;
            font-size: 10px;
            font-weight: 800;
            letter-spacing: 1.3px;
            margin: 12px 0 5px;
            padding-left: 8px;
        }

        /* =========================================
           NAVIGATION LINKS
        ========================================= */
        section[data-testid="stSidebar"] [data-testid="stPageLink"] {
            margin: 2px 0 !important;
        }

        section[data-testid="stSidebar"] [data-testid="stPageLink"] a {
            display: flex !important;
            align-items: center !important;
            min-height: 40px !important;
            box-sizing: border-box !important;
            padding: 9px 10px !important;
            border-radius: 8px !important;
            border: 1px solid transparent !important;
            color: #e1ecf8 !important;
            background: transparent !important;
            font-size: 12px !important;
            font-weight: 600 !important;
            text-decoration: none !important;
            transition: background 0.2s ease;
        }

        section[data-testid="stSidebar"] [data-testid="stPageLink"] a:hover {
            background: #153957 !important;
            border-color: #315778 !important;
            color: #ffffff !important;
        }

        section[data-testid="stSidebar"] [data-testid="stPageLink"] a[aria-current="page"] {
            background: linear-gradient(
                100deg,
                #174b77,
                #14517e
            ) !important;
            border-color: #3477a5 !important;
            color: #ffffff !important;
        }

        /* =========================================
           INFORMATION PANELS
        ========================================= */
        section[data-testid="stSidebar"] [data-testid="stExpander"] {
            background: #102b48 !important;
            border: 1px solid #294663 !important;
            border-radius: 8px !important;
            margin: 4px 0 !important;
        }

        section[data-testid="stSidebar"] [data-testid="stExpander"] summary,
        section[data-testid="stSidebar"] [data-testid="stExpander"] summary p {
            color: #e5effa !important;
            font-size: 12px !important;
        }

        section[data-testid="stSidebar"] [data-testid="stExpander"] p {
            color: #c6d9eb !important;
            font-size: 12px !important;
            line-height: 1.6 !important;
        }

        /* =========================================
           FOOTER
        ========================================= */
        .sidebar-footer {
            margin-top: 12px;
            padding: 12px 4px 6px;
            border-top: 1px solid #29435f;
            color: #b8cce1;
            font-size: 10px;
            line-height: 1.8;
            text-align: center;
        }

        .sidebar-footer strong {
            color: #e3effb;
            font-size: 10px;
        }

        /* =========================================
           MAIN CONTENT TOP SPACING
        ========================================= */
        [data-testid="stMainBlockContainer"] {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }

        [data-testid="stAppViewBlockContainer"] {
            padding-top: 0 !important;
        }

        .block-container {
            padding-top: 0.5rem !important;
        }

        @media (max-width: 700px) {
            .block-container {
                padding: 0.5rem 1rem 2rem !important;
            }
        }


/* HELP & GUIDELINES - FORCE READABLE WHITE TEXT */
section[data-testid="stSidebar"] [data-testid="stExpander"] {
    background: #102b48 !important;
    border: 1px solid #315675 !important;
    border-radius: 10px !important;
}

section[data-testid="stSidebar"] [data-testid="stExpander"] summary,
section[data-testid="stSidebar"] [data-testid="stExpander"] summary * {
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
}

section[data-testid="stSidebar"] [data-testid="stExpander"] [data-testid="stMarkdownContainer"],
section[data-testid="stSidebar"] [data-testid="stExpander"] [data-testid="stMarkdownContainer"] *,
section[data-testid="stSidebar"] [data-testid="stExpander"] p,
section[data-testid="stSidebar"] [data-testid="stExpander"] strong {
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    opacity: 1 !important;
}

section[data-testid="stSidebar"] [data-testid="stExpander"] [data-testid="stExpanderDetails"] {
    background: #102b48 !important;
}

section[data-testid="stSidebar"] [data-testid="stExpander"] [style*="background: #173e65"] {
    background: #173e65 !important;
    color: #ffffff !important;
}

        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.sidebar:
        # BRAND
        st.markdown(
            """
            <div class="sidebar-brand">
                <div class="sidebar-logo">📚</div>
                <div>
                    <div class="sidebar-brand-name">PlagiarismAI</div>
                    <div class="sidebar-brand-subtitle">
                        ACADEMIC INTEGRITY
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # MAIN MENU
        st.markdown(
            '<div class="sidebar-section">MAIN MENU</div>',
            unsafe_allow_html=True,
        )

        st.page_link(
            "app.py",
            label="🏠  Dashboard",
            help="Return to the homepage",
        )

        st.page_link(
            "pages/1_Detect_Plagiarism.py",
            label="🔎  Detect Plagiarism",
            help="Upload and compare documents",
        )

        st.page_link(
            "pages/1_Detect_Plagiarism.py",
            label="📄  Document Comparison",
            help="Open document comparison",
        )

        # ANALYSIS
        st.markdown(
            '<div class="sidebar-section">ANALYSIS</div>',
            unsafe_allow_html=True,
        )

        st.page_link(
            "pages/1_Detect_Plagiarism.py",
            label="📊  Analysis Results",
            help="Open the comparison workspace",
        )

        st.page_link(
            "pages/1_Detect_Plagiarism.py",
            label="🕘  Recent Analyses",
            help="Open the analysis workspace",
        )

        # INFORMATION
        st.markdown(
            '<div class="sidebar-section">INFORMATION</div>',
            unsafe_allow_html=True,
        )

        
    
        with st.expander("ℹ️  About Project", expanded=False):
            st.write("AI-Based Plagiarism Detection System")
            st.write(
                "Compares academic documents using text "
                "preprocessing, TF-IDF and cosine similarity."
            )
            st.write("Supports TXT, PDF and DOCX documents.")

    


        with st.expander("❔  Help & Guidelines", expanded=False):
            st.html("""
            <style>
                .help-guide,
                .help-guide p,
                .help-guide strong {
                    color: #ffffff !important;
                    -webkit-text-fill-color: #ffffff !important;
                    opacity: 1 !important;
                }

                .help-guide {
                    font-size: 13px;
                    line-height: 1.8;
                }

                .help-notice {
                    background: #173e65;
                    border: 1px solid #35658c;
                    border-radius: 10px;
                    padding: 12px;
                    margin-top: 12px;
                    color: #ffffff !important;
                    -webkit-text-fill-color: #ffffff !important;
                    font-size: 12px;
                    line-height: 1.7;
                }
            </style>

            <div class="help-guide">
                <p>1. Open Detect Plagiarism.</p>
                <p>2. Upload two TXT, PDF or DOCX documents.</p>
                <p>3. Click Analyze Documents.</p>
                <p>4. Review the score and matching passages.</p>
            </div>

            <div class="help-notice">
                <strong>Important</strong>
                <p>Similarity is not proof of plagiarism.
                Human review is essential.</p>
            </div>
            """)

        # FOOTER
        st.markdown(
            """
            <div class="sidebar-footer">
                <strong>AI PLAGIARISM DETECTION</strong><br>
                Academic Project Prototype<br>
                Python · Streamlit · Machine Learning
            </div>
            """,
            unsafe_allow_html=True,
        )
