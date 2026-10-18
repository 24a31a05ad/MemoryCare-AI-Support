import html

import streamlit as st

from agent import support_agent
from memory import recall, remember
from llm import generate_response
from vision import analyze_screenshot


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="MemoryCare AI Support",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background: #f7f4fa;
    }

    .main {
        padding-top: 1rem;
    }

    /* HEADER */

    .main-header {
        background: linear-gradient(
            135deg,
            #6c3fa4 0%,
            #8b5fc7 50%,
            #a87bd8 100%
        );
        padding: 28px 32px;
        border-radius: 20px;
        margin-bottom: 22px;
        color: white;
        box-shadow: 0 8px 25px rgba(90, 50, 130, 0.15);
    }

    .main-header h1 {
        margin: 0;
        font-size: 32px;
        font-weight: 700;
    }

    .main-header p {
        margin-top: 8px;
        margin-bottom: 0;
        font-size: 15px;
        opacity: 0.92;
    }

    /* CARDS */

    .card {
        background: white;
        padding: 20px;
        border-radius: 18px;
        border: 1px solid #e8e1ef;
        box-shadow: 0 4px 15px rgba(70, 40, 100, 0.06);
        margin-bottom: 16px;
    }

    .card-title {
        font-size: 19px;
        font-weight: 700;
        color: #3c2750;
        margin-bottom: 14px;
    }

    .section-title {
        font-size: 22px;
        font-weight: 700;
        color: #39244d;
        margin-top: 12px;
        margin-bottom: 14px;
    }

    /* CUSTOMER */

    .customer-name {
        font-size: 22px;
        font-weight: 700;
        color: #382246;
    }

    .customer-role {
        font-size: 13px;
        color: #777;
        margin-bottom: 14px;
    }

    .info-row {
        padding: 9px 0;
        border-bottom: 1px solid #eeeaf2;
        font-size: 14px;
    }

    .info-label {
        color: #777;
        font-weight: 600;
    }

    .info-value {
        color: #29202f;
    }

    /* STATUS */

    .status-box {
        background: #edf9f1;
        color: #19713b;
        border-radius: 10px;
        padding: 10px 12px;
        font-weight: 600;
        font-size: 13px;
        margin-top: 12px;
    }

    /* METRICS */

    .metric-card {
        background: #faf8fc;
        border: 1px solid #e9e2ef;
        border-radius: 13px;
        padding: 13px;
        text-align: center;
    }

    .metric-number {
        font-size: 22px;
        font-weight: 700;
        color: #6c3fa4;
    }

    .metric-label {
        font-size: 12px;
        color: #777;
        margin-top: 3px;
    }

    /* MEMORY */

    .memory-card {
        background-color: white;
        color: #222222;
        padding: 16px;
        border-radius: 14px;
        border: 1px solid #e7e2ef;
        margin-bottom: 10px;
        box-shadow: 0 2px 8px rgba(50, 30, 70, 0.04);
    }

    .memory-card strong {
        color: #5c348c;
    }

    /* AI RESPONSE */

    .ai-response {
        background: #f6f0fb;
        border-left: 4px solid #7d4db3;
        padding: 17px;
        border-radius: 12px;
        color: #2d2335 !important;
        line-height: 1.65;
        margin-top: 12px;
    }

    /* DIAGNOSIS */

    .diagnosis-box {
        background: #fff8ec;
        border: 1px solid #f0d9aa;
        border-radius: 14px;
        padding: 17px;
        color: #4a3820;
        margin-top: 12px;
    }

    [data-testid="stExpander"] details summary {
        background-color: #fff5fa !important;
        border: 1px solid #f2c6dc !important;
        border-radius: 10px !important;
        color: #492c58 !important;
    }

    [data-testid="stExpander"] details summary p,
    [data-testid="stExpander"] details summary span,
    [data-testid="stExpander"] details summary svg {
        color: #492c58 !important;
        fill: #492c58 !important;
    }

    [data-testid="stExpander"] details > div {
        background-color: #fffafd !important;
        color: #33263d !important;
    }

    /* BUTTONS */

    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
        border: 1px solid #d8c9e5;
    }

    .stButton > button:hover {
        border-color: #7d4db3;
        color: #6c3fa4;
    }

    /* FOOTER */

    .footer {
        text-align: center;
        color: #888;
        font-size: 12px;
        padding: 25px 0 10px 0;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.html(
    """
    <div class="main-header">
        <h1>🧠 MemoryCare AI Support</h1>
        <p>
            Personalized customer support powered by persistent memory,
            multimodal diagnosis and intelligent learning.
        </p>
    </div>
    """
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 👤 Customer 360")

    st.html(
        """
        <div class="card">

            <div class="customer-name">
                Bhavani
            </div>

            <div class="customer-role">
                Customer ID: MC-1024
            </div>

            <div class="info-row">
                <span class="info-label">Preferred Language</span><br>
                <span class="info-value">Telugu (తెలుగు)</span>
            </div>

            <div class="info-row">
                <span class="info-label">Product</span><br>
                <span class="info-value">
                    MemoryCare Mobile App
                </span>
            </div>

            <div class="info-row">
                <span class="info-label">Communication</span><br>
                <span class="info-value">
                    Clear & Simple
                </span>
            </div>

            <div class="info-row">
                <span class="info-label">Customer Since</span><br>
                <span class="info-value">
                    2026
                </span>
            </div>

            <div class="status-box">
                ● Support Status: Active
            </div>

        </div>
        """
    )

    st.markdown("### 📊 Support Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.html(
            """
            <div class="metric-card">
                <div class="metric-number">5</div>
                <div class="metric-label">Tickets</div>
            </div>
            """
        )

    with col2:
        st.html(
            """
            <div class="metric-card">
                <div class="metric-number">4</div>
                <div class="metric-label">Resolved</div>
            </div>
            """
        )

    st.markdown("")

    st.html(
        """
        <div class="card">

            <div class="card-title">
                🧠 Memory Features
            </div>

            <p style="font-size:13px;color:#666;line-height:1.8;">
                ✓ Persistent customer history<br>
                ✓ Previous solution recall<br>
                ✓ Language preference memory<br>
                ✓ Screenshot diagnosis<br>
                ✓ Product-aware support<br>
                ✓ Learning from feedback
            </p>

        </div>
        """
    )


# ============================================================
# MAIN THREE COLUMNS
# ============================================================

left_col, middle_col, right_col = st.columns(
    [1.15, 1.7, 1.25],
    gap="large"
)


# ============================================================
# LEFT COLUMN — AI SUPPORT
# ============================================================

with left_col:

    st.markdown(
        '<div class="section-title">💬 AI Support</div>',
        unsafe_allow_html=True
    )

    st.html(
        """
        <div class="card">

            <div class="card-title">
                Ask MemoryCare
            </div>

            <p style="font-size:13px;color:#777;line-height:1.6;">
                Ask a support question. The agent recalls relevant
                customer history before responding.
            </p>

        </div>
        """
    )

    user_message = st.text_area(
        "Customer message",
        placeholder=(
            "Example: My payment is failing again. "
            "What should I try?"
        ),
        height=130,
        key="support_message"
    )

    if st.button(
        "🤖 Get AI Support",
        use_container_width=True,
        key="support_button"
    ):

        if not user_message.strip():

            st.warning(
                "Please enter a customer message."
            )

        else:

            with st.spinner(
                "Checking customer memory..."
            ):

                try:

                    answer = support_agent(
                        user_message.strip()
                    )

                    safe_answer = (
                        answer
                        .replace("&", "&amp;")
                        .replace("<", "&lt;")
                        .replace(">", "&gt;")
                        .replace("\n", "<br>")
                    )

                    st.html(
                        f"""
                        <div class="ai-response">

                            <strong>
                                🧠 MemoryCare
                            </strong>

                            <br><br>

                            {safe_answer}

                        </div>
                        """
                    )

                except Exception as e:

                    st.error(
                        f"Support agent error: {str(e)}"
                    )


# ============================================================
# MIDDLE COLUMN — HINDSIGHT MEMORY
# ============================================================

with middle_col:

    st.markdown(
        '<div class="section-title">🧠 Hindsight Memory</div>',
        unsafe_allow_html=True
    )

    st.html(
        """
        <div class="card">

            <div class="card-title">
                Customer Memory Inspector
            </div>

            <p style="font-size:13px;color:#777;line-height:1.6;">
                Retrieve information remembered from previous
                customer interactions.
            </p>

        </div>
        """
    )

    st.html(
        """
        <div style="
            display: grid;
            justify-items: start;
            gap: 4px;
            background: #f6f0fb;
            border: 1px solid #e8e1ef;
            border-radius: 12px;
            padding: 12px;
            margin-bottom: 16px;
            color: #4a315f;
            font-size: 12px;
            font-weight: 700;
        ">
            <span>RECALL</span>
            <span aria-hidden="true">↓</span>
            <span>PERSONALIZED RESPONSE</span>
            <span aria-hidden="true">↓</span>
            <span>RESOLVE</span>
            <span aria-hidden="true">↓</span>
            <span>RETAIN</span>
            <span aria-hidden="true">↓</span>
            <span>FUTURE RECALL</span>
        </div>
        """
    )

    memory_query = st.text_input(
        "Search customer memory",
        placeholder=(
            "Example: What happened during my previous "
            "payment issue?"
        ),
        key="memory_query"
    )

    if st.button(
        "🔎 Recall Customer Memory",
        use_container_width=True,
        key="recall_button"
    ):

        if not memory_query.strip():

            st.warning(
                "Enter a memory query first."
            )

        else:

            with st.spinner(
                "Recalling relevant memories..."
            ):

                try:

                    memories = recall(
                        memory_query.strip()
                    )

                    if not memories:

                        st.info(
                            "No relevant memories found."
                        )

                    else:

                        st.success(
                            f"Found {len(memories)} relevant "
                            "memory item(s)."
                        )

                        for memory in memories:

                            memory_text = getattr(
                                memory,
                                "text",
                                str(memory)
                            )

                            safe_memory = (
                                memory_text
                                .replace("&", "&amp;")
                                .replace("<", "&lt;")
                                .replace(">", "&gt;")
                                .replace("\n", "<br>")
                            )

                            st.html(
                                f"""
                                <div class="memory-card" style="
                                    background-color: #ffffff;
                                    color: #29202f !important;
                                    border: 1px solid #e7e2ef;
                                    border-radius: 14px;
                                    padding: 16px;
                                    margin-bottom: 10px;
                                ">

                                    <strong style="color: #5c348c !important;">
                                        🧠 Remembered
                                    </strong>

                                    <br><br>

                                    {safe_memory}

                                </div>
                                """
                            )

                except Exception as e:

                    st.error(
                        f"Memory error: {str(e)}"
                    )


# ============================================================
# RIGHT COLUMN — QUICK DEMO
# ============================================================

with right_col:

    st.markdown(
        '<div class="section-title">⚡ Quick Demo</div>',
        unsafe_allow_html=True
    )

    st.html(
        """
        <div class="card">

            <div class="card-title">
                Try these examples
            </div>

            <p style="font-size:13px;color:#666;line-height:1.6;">
                These examples demonstrate how persistent memory
                changes the support experience.
            </p>

        </div>
        """
    )

    if st.button(
        "💳 Previous Payment Issue",
        use_container_width=True,
        key="demo_payment"
    ):

        st.session_state[
            "support_message"
        ] = (
            "My payment is failing again. "
            "Can you check what happened last time "
            "and tell me what I should try first?"
        )

        st.rerun()

    if st.button(
        "🌐 Language Preference",
        use_container_width=True,
        key="demo_language"
    ):

        st.session_state[
            "memory_query"
        ] = (
            "What language does Bhavani prefer "
            "for customer support?"
        )

        st.rerun()

    if st.button(
        "🧾 Previous Solution",
        use_container_width=True,
        key="demo_solution"
    ):

        st.session_state[
            "memory_query"
        ] = (
            "What solution worked for Bhavani's "
            "previous payment problem?"
        )

        st.rerun()


# ============================================================
# SCREENSHOT DIAGNOSIS
# ============================================================

st.markdown("---")

st.markdown(
    '<div class="section-title">📸 Screenshot Evidence</div>',
    unsafe_allow_html=True
)

st.html(
    """
    <div class="card">

        <div class="card-title">
            Multimodal Customer Support
        </div>

        <p style="font-size:14px;color:#666;">
            Upload a payment or application error screenshot.
            MemoryCare will:
        </p>

        <p style="font-size:14px;color:#555;line-height:1.8;">

            <b>1.</b>
            Understand the screenshot using Vision AI
            <br>

            <b>2.</b>
            Recall the customer's previous support history
            <br>

            <b>3.</b>
            Connect the new problem with previous solutions
            <br>

            <b>4.</b>
            Generate a personalized recommendation

        </p>

    </div>
    """
)

st.html(
    """
    <div style="
        display: grid;
        justify-items: center;
        gap: 3px;
        background-color: #f6f0fb;
        border: 1px solid #e8e1ef;
        border-radius: 12px;
        padding: 10px 14px;
        margin-bottom: 14px;
        color: #4a315f !important;
        font-size: 12px;
        font-weight: 700;
        text-align: center;
    ">
        <span>📸 CUSTOMER SCREENSHOT</span>
        <span aria-hidden="true">↓</span>
        <span>🔍 VISION DIAGNOSIS</span>
        <span aria-hidden="true">↓</span>
        <span>🧠 HINDSIGHT RECALL</span>
        <span aria-hidden="true">↓</span>
        <span>💬 PERSONALIZED SUPPORT</span>
    </div>
    """
)


uploaded_file = st.file_uploader(
    "Upload error screenshot",
    type=[
        "png",
        "jpg",
        "jpeg",
        "webp"
    ],
    key="screenshot_uploader"
)


if uploaded_file is not None:

    image_bytes = uploaded_file.getvalue()

    col_img, col_result = st.columns(
        [1, 1],
        gap="large"
    )

    # --------------------------------------------------------
    # IMAGE
    # --------------------------------------------------------

    with col_img:

        st.markdown(
            "### 📸 Uploaded Screenshot"
        )

        st.image(
            image_bytes,
            caption="Visual evidence provided by the customer",
            use_container_width=True
        )

    # --------------------------------------------------------
    # ANALYSIS
    # --------------------------------------------------------

    with col_result:

        st.markdown(
            "### 🔍 Vision Diagnosis"
        )

        if st.button(
            "🔍 Analyze Screenshot",
            use_container_width=True,
            key="analyze_button"
        ):

            # ------------------------------------------------
            # STEP 1 — VISION
            # ------------------------------------------------

            with st.spinner(
                "Analyzing screenshot with Vision AI..."
            ):

                try:

                    diagnosis = analyze_screenshot(
                        image_bytes=image_bytes,
                        mime_type=uploaded_file.type
                    )

                    st.session_state[
                        "last_diagnosis"
                    ] = diagnosis

                except Exception as e:

                    st.error(
                        f"Vision analysis error: {str(e)}"
                    )

                    st.stop()

            # ------------------------------------------------
            # SHOW VISION RESULT
            # ------------------------------------------------

            diagnosis_labels = {
                "error": "Error",
                "error code": "Error Code",
                "product": "Product",
                "amount": "Amount",
                "category": "Category",
                "important details": "Important Details",
            }
            diagnosis_values = {}
            unparsed_diagnosis_lines = []
            current_diagnosis_field = None

            for diagnosis_line in diagnosis.splitlines():
                diagnosis_label, separator, diagnosis_value = diagnosis_line.partition(":")
                normalized_label = diagnosis_label.strip().lower()

                if separator and normalized_label in diagnosis_labels:
                    current_diagnosis_field = diagnosis_labels[normalized_label]
                    diagnosis_values[current_diagnosis_field] = diagnosis_value.strip()
                elif current_diagnosis_field and diagnosis_line.strip():
                    diagnosis_values[current_diagnosis_field] = (
                        diagnosis_values[current_diagnosis_field]
                        + "\n"
                        + diagnosis_line.strip()
                    ).strip()
                elif diagnosis_line.strip():
                    current_diagnosis_field = None
                    unparsed_diagnosis_lines.append(diagnosis_line.strip())

            diagnosis_order = (
                "Error",
                "Error Code",
                "Product",
                "Amount",
                "Category",
                "Important Details",
            )
            diagnosis_rows = "".join(
                f"""
                <div style="
                    display: grid;
                    grid-template-columns: minmax(115px, 0.32fr) 1fr;
                    gap: 8px;
                    padding: 9px 0;
                    border-bottom: 1px solid #eadfc9;
                ">
                    <span style="color: #684c29 !important; font-weight: 700;">
                        {html.escape(label)}
                    </span>
                    <span style="color: #382b1d !important;">
                        {html.escape(diagnosis_values[label]).replace(chr(10), "<br>")}
                    </span>
                </div>
                """
                for label in diagnosis_order
                if diagnosis_values.get(label)
            )

            if unparsed_diagnosis_lines:
                diagnosis_rows += f"""
                <div style="padding: 9px 0; color: #382b1d !important;">
                    <span style="color: #684c29 !important; font-weight: 700;">
                        Additional Details
                    </span><br>
                    {html.escape("\n".join(unparsed_diagnosis_lines)).replace(chr(10), "<br>")}
                </div>
                """

            if not diagnosis_rows:
                diagnosis_rows = (
                    '<div style="color:#382b1d !important;">'
                    + html.escape(diagnosis).replace("\n", "<br>")
                    + "</div>"
                )

            st.html(
                f"""
                <div style="
                    background-color: #fff8ec;
                    border: 1px solid #f0d9aa;
                    border-radius: 14px;
                    padding: 17px;
                    margin-top: 12px;
                    color: #382b1d !important;
                ">
                    <div style="
                        color: #684c29 !important;
                        font-size: 16px;
                        font-weight: 700;
                        margin-bottom: 8px;
                    ">🔍 Vision Diagnosis</div>
                    {diagnosis_rows}
                </div>
                """
            )

            # ------------------------------------------------
            # STEP 2 — HINDSIGHT RECALL
            # ------------------------------------------------

            with st.spinner(
                "Checking previous customer history..."
            ):

                try:

                    memories = recall(
                        diagnosis
                    )

                    memory_texts = [
                        str(getattr(memory, "text", memory))
                        for memory in memories
                    ]
                    memory_text_combined = "\n".join(memory_texts)
                    memory_text_lower = memory_text_combined.lower()
                    successful_cache_memory = any(
                        "browser cache" in memory_text.lower()
                        and any(
                            marker in memory_text.lower()
                            for marker in (
                                "successful",
                                "successfully",
                                "worked",
                                "resolved",
                            )
                        )
                        for memory_text in memory_texts
                    )

                except Exception as e:

                    st.error(
                        f"Memory recall error: {str(e)}"
                    )

                    st.stop()

            # ------------------------------------------------
            # STEP 3 — PERSONALIZED RESPONSE
            # ------------------------------------------------

            with st.spinner(
                "Generating personalized support..."
            ):

                try:

                    personalized_answer = (
                        generate_response(
                            user_message=diagnosis,
                            memories=memories
                        )
                    )

                except Exception as e:

                    st.error(
                        f"AI response error: {str(e)}"
                    )

                    st.stop()

            # ------------------------------------------------
            # SAVE SESSION DATA
            # ------------------------------------------------

            st.session_state[
                "last_support_answer"
            ] = personalized_answer

            st.session_state[
                "last_uploaded_filename"
            ] = uploaded_file.name

            st.session_state[
                "last_memories"
            ] = memories

            st.session_state[
                "case_saved"
            ] = False

            # ------------------------------------------------
            # SHOW RECOMMENDATION
            # ------------------------------------------------

            st.html(
                """
                <div style="
                    color: #8b245c !important;
                    font-size: 20px;
                    font-weight: 700;
                    margin: 18px 0 10px 0;
                ">
                    💬 MemoryCare Recommendation
                </div>
                """
            )

            safe_answer = (
                personalized_answer
                .replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace("\n", "<br>")
            )

            st.html(
                f"""
                <div class="ai-response" style="
                    background-color: #f6f0fb;
                    border-left: 4px solid #7d4db3;
                    border-radius: 12px;
                    padding: 17px;
                    color: #2d2335 !important;
                    line-height: 1.75;
                    margin-top: 12px;
                    white-space: normal;
                ">

                    {safe_answer}

                </div>
                """
            )

            # ------------------------------------------------
            # SHOW MEMORY CONTEXT
            # ------------------------------------------------

            if memories:

                with st.expander(
                    "🧠 View recalled customer context"
                ):

                    for memory in memories:

                        memory_text = str(
                            getattr(memory, "text", memory)
                        )
                        safe_memory_text = html.escape(memory_text).replace(
                            "\n",
                            "<br>"
                        )
                        st.html(
                            f"""
                            <div style="
                                background-color: #ffffff;
                                border: 1px solid #e7e2ef;
                                border-radius: 10px;
                                padding: 12px;
                                margin: 8px 0;
                                color: #29202f !important;
                                line-height: 1.6;
                            ">{safe_memory_text}</div>
                            """
                        )

            # ------------------------------------------------
            # SHOW THE MEMORY IMPACT
            # ------------------------------------------------

            st.markdown("### 🧠 What Hindsight Changes")

            without_memory_col, with_memory_col = st.columns(2)

            with without_memory_col:

                st.html("""
                <div style="
                    background-color: #f5f4f6;
                    border: 1px solid #e8e1ef;
                    border-radius: 14px;
                    padding: 16px;
                    min-height: 150px;
                    color: #33263d !important;
                ">
                    <div style="
                        color: #5d5064 !important;
                        font-size: 12px;
                        font-weight: 700;
                        margin-bottom: 10px;
                    ">WITHOUT HINDSIGHT</div>
                    <div style="color: #33263d !important; font-size: 15px; line-height: 1.6;">
                        “Payment failed. Please try again or contact support.”
                    </div>
                    <div style="
                        color: #5d5064 !important;
                        font-size: 12px;
                        margin-top: 12px;
                    ">Generic support response</div>
                </div>
                """)

            with with_memory_col:

                if memories:
                    impact_lines = []
                    if "4032" in memory_text_combined:
                        impact_lines.append(
                            "Previous Error 4032 was found."
                        )

                    if successful_cache_memory:
                        impact_lines.append(
                            "Previous successful solution: clearing the browser cache."
                        )

                    if not impact_lines:
                        recalled_excerpt = memory_text_combined.strip()[:320]
                        impact_lines.append(
                            "Recalled customer context: "
                            + recalled_excerpt
                        )

                    memory_impact_html = "<br><br>".join(
                        html.escape(line).replace("\n", "<br>")
                        for line in impact_lines
                    )
                else:
                    memory_impact_html = (
                        "No relevant previous customer experience "
                        "was returned for this issue."
                    )

                st.html(
                    f"""
                    <div style="
                        background-color: #fff5fa;
                        border: 1px solid #f2c6dc;
                        border-radius: 14px;
                        padding: 16px;
                        min-height: 150px;
                        color: #33263d !important;
                    ">
                        <div style="
                            color: #8b245c !important;
                            font-size: 12px;
                            font-weight: 700;
                            margin-bottom: 10px;
                        ">WITH HINDSIGHT</div>
                        <div style="color: #33263d !important; font-size: 15px; line-height: 1.6;">
                            {memory_impact_html}
                        </div>
                        <div style="
                            color: #5d5064 !important;
                            font-size: 12px;
                            margin-top: 12px;
                        ">Personalized support based on memory</div>
                    </div>
                    """
                )

            st.markdown("#### 🧠 HINDSIGHT MEMORY")

            if memories:
                memory_claims = [
                    "✓ Recall completed",
                    "✓ Previous customer experience found",
                    "✓ Relevant support context retrieved",
                ]
                if "4032" in memory_text_combined:
                    memory_claims.append(
                        "✓ Previous Error 4032 found"
                    )
                if successful_cache_memory:
                    memory_claims.append(
                        "✓ Previous successful solution found"
                    )
                if any(
                    ("telugu" in memory_text.lower() or "తెలుగు" in memory_text)
                    and any(
                        marker in memory_text.lower()
                        for marker in ("language", "prefer")
                    )
                    for memory_text in memory_texts
                ):
                    memory_claims.append(
                        "✓ Preferred language found"
                    )

                memory_claims_html = "<br>".join(
                    html.escape(memory_claim)
                    for memory_claim in memory_claims
                )
                st.html(
                    f"""
                    <div style="
                        background-color: #f1faf4;
                        border: 1px solid #c8e4d0;
                        border-radius: 12px;
                        padding: 12px 14px;
                        color: #24452f !important;
                        line-height: 1.8;
                        margin: 8px 0;
                    ">
                        {memory_claims_html}
                    </div>
                    """
                )
                st.html(
                    """
                    <div style="
                        color: #4a315f !important;
                        font-size: 14px;
                        font-weight: 700;
                        margin: 10px 0;
                    ">Memory → Personalized Support</div>
                    """
                )
            else:
                st.html(
                    """
                    <div style="
                        background-color: #f5f4f6;
                        border: 1px solid #ded9e2;
                        border-radius: 12px;
                        padding: 12px 14px;
                        color: #403647 !important;
                    ">
                        Recall completed — no relevant previous experience found.
                    </div>
                    """
                )


# ============================================================
# SAVE RESOLVED CASE
# ============================================================

if (
    st.session_state.get("last_diagnosis")
    and st.session_state.get("last_support_answer")
):

    last_diagnosis = st.session_state.get("last_diagnosis", "")
    last_support_answer = st.session_state.get("last_support_answer", "")

    st.markdown("---")

    st.html("""
    <div style="
            color: #7a174f !important;
      font-size: 22px;
      font-weight: 700;
      margin-top: 10px;
      margin-bottom: 8px;
    ">
      💾 Learn From This Support Case
    </div>
    """)

    st.html("""
<div style="
    color: #555555 !important;
    font-size: 14px;
    margin-bottom: 12px;
">
    If the issue was resolved, save the case outcome
    so MemoryCare can use it in future conversations.
</div>
""")

    col1, col2 = st.columns(2)

    # --------------------------------------------------------
    # RESOLVED
    # --------------------------------------------------------

    with col1:

        if st.button(
            "✅ Save Resolved Case to Memory",
            use_container_width=True,
            key="save_case_button"
        ):

            case_memory = f"""
Customer: Bhavani

Resolved support case:

Screenshot diagnosis:
{last_diagnosis}

Support recommendation:
{last_support_answer}

Outcome:
The customer resolved the issue successfully.

Learning:
Remember this support case and consider the previous
successful solution when a similar issue occurs again.
"""

            with st.spinner(
                "Saving support learning to Hindsight..."
            ):

                try:

                    remember(
                        case_memory
                    )

                    st.success(
                        "Resolved case saved to customer memory."
                    )

                    st.session_state[
                        "case_saved"
                    ] = True

                except Exception as e:

                    st.error(
                        f"Could not save case: {str(e)}"
                    )

    # --------------------------------------------------------
    # NOT RESOLVED
    # --------------------------------------------------------

    with col2:

        if st.button(
            "❌ Issue Not Resolved",
            use_container_width=True,
            key="unresolved_button"
        ):

            st.warning(
                "This case can be escalated to a human support "
                "agent with the diagnosis and previous troubleshooting context."
            )

    if st.session_state.get("case_saved"):

        retained_memories = st.session_state.get("last_memories", []) or []
        retained_solution_confirmed = any(
            "browser cache" in str(getattr(memory, "text", memory)).lower()
            and any(
                marker in str(getattr(memory, "text", memory)).lower()
                for marker in ("successful", "successfully", "worked", "resolved")
            )
            for memory in retained_memories
        )
        retained_issue = (
            "Error 4032"
            if "4032" in last_diagnosis
            else last_diagnosis.strip()
        )
        retained_issue_html = html.escape(retained_issue).replace("\n", "<br>")

        retained_solution_row = ""
        if retained_solution_confirmed:
            retained_solution_row = """
                <div style="margin-top: 8px; color: #253d2d !important;">
                    <b style="color: #253d2d !important;">Solution:</b>
                    Browser cache cleared
                </div>
            """

        st.html(
            f"""
            <div style="
                background-color: #f1faf4;
                border: 1px solid #b9dfc5;
                border-radius: 12px;
                padding: 16px;
                margin-top: 14px;
                color: #253d2d !important;
                font-size: 14px;
                line-height: 1.65;
            ">
                <div style="
                    color: #19713b !important;
                    font-weight: 700;
                    margin-bottom: 8px;
                ">✓ RETAIN COMPLETE</div>
                <div style="color: #253d2d !important;">New support experience stored in Hindsight.</div>
                <div style="margin-top: 8px; color: #253d2d !important;">
                    <b style="color: #253d2d !important;">Issue:</b> {retained_issue_html}
                </div>
                {retained_solution_row}
                <div style="margin-top: 8px; color: #253d2d !important;">
                    <b style="color: #253d2d !important;">Outcome:</b> Resolved
                </div>
                <div style="margin-top: 10px; color: #253d2d !important;">
                    This experience can now be recalled in future support conversations.
                </div>
            </div>
            """
        )


# ============================================================
# HUMAN ESCALATION
# ============================================================

if (
    st.session_state.get("last_diagnosis")
    and st.session_state.get("last_support_answer")
):

    last_diagnosis = st.session_state.get("last_diagnosis", "")
    last_support_answer = st.session_state.get("last_support_answer", "")

    safe_handoff_diagnosis = (
        last_diagnosis
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\n", "<br>")
    )

    safe_handoff_answer = (
        last_support_answer
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\n", "<br>")
    )

    with st.expander("🚨 Human Escalation Preview"):

        st.html("""
        <div style="
            background: linear-gradient(135deg, #fff5fa, #fffafd);
            border: 1px solid #f2c6dc;
            border-radius: 14px;
            padding: 18px;
            margin-bottom: 15px;
            color: #333333 !important;
        ">
            <div style="
                color: #8b245c !important;
                font-size: 21px;
                font-weight: 700;
                margin-bottom: 14px;
            ">
                👤 Support Agent Handoff
            </div>

            <div style="
                color: #333333 !important;
                font-size: 15px;
                line-height: 1.8;
            ">
                <b>Customer:</b> Bhavani<br>
                <b>Product:</b> MemoryCare Mobile App
            </div>
        </div>
        """)

        st.html("""
        <div style="
            color: #8b245c !important;
            font-size: 18px;
            font-weight: 700;
            margin-top: 12px;
            margin-bottom: 8px;
        ">
            🔎 Issue Detected
        </div>
        """)

        st.html(
            f"""
            <div style="
                background: #fffafd;
                border: 1px solid #f2c6dc;
                border-radius: 12px;
                padding: 16px;
                color: #333333 !important;
                font-size: 15px;
                line-height: 1.7;
                margin-bottom: 15px;
            ">
                {safe_handoff_diagnosis}
            </div>
            """
        )

        st.html("""
        <div style="
            color: #8b245c !important;
            font-size: 18px;
            font-weight: 700;
            margin-top: 18px;
            margin-bottom: 8px;
        ">
            🤖 Previous AI Recommendation
        </div>
        """)

        st.html(
            f"""
            <div style="
                background: #fffafd;
                border: 1px solid #f2c6dc;
                border-radius: 12px;
                padding: 16px;
                color: #333333 !important;
                font-size: 15px;
                line-height: 1.7;
                margin-bottom: 15px;
            ">
                {safe_handoff_answer}
            </div>
            """
        )

        st.html(
            """
            <div style="
                background-color: #f6f0fb;
                border: 1px solid #e3d6ee;
                border-radius: 10px;
                padding: 12px 14px;
                color: #392b43 !important;
                line-height: 1.6;
                margin-bottom: 8px;
            ">
                A human agent receives the issue together with the customer's
                previous context, reducing repeated questioning.
            </div>
            """
        )