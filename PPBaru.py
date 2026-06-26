import streamlit as st

from database import save_feedback
from datetime import datetime

from soalan import SOALAN


# ==========================================================
# i-MAKLUM
# VERSION 2
# Single Page
# Developer : Dr. Nur Hamiza Adenan
# ==========================================================

st.set_page_config(
    page_title="i-MAKLUM",
    page_icon="🏛️",
    layout="wide"
)

# ==========================================================
# CSS
# ==========================================================

st.markdown("""
<style>

.main{
    padding-top:20px;
}

.title{
    text-align:center;
    color:#003366;
    font-size:40px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    font-size:22px;
    font-weight:600;
}

.ppa{
    text-align:center;
    color:#666666;
    font-size:17px;
}

.footer{
    text-align:center;
    color:gray;
    font-size:13px;
}

.section{
    background:#fafafa;
    padding:18px;
    border-radius:12px;
    border:1px solid #dddddd;
    margin-bottom:25px;
}
.english{
    display:block;
    width:100%;
    text-align:center;
    color:#6c757d;
    font-size:14px;
    font-style:italic;
    font-weight:400;
    line-height:1.5;
    margin-top:6px;
    margin-bottom:18px;
}
.english-left{
    color:#6c757d;
    font-size:13px;
    font-style:italic;
    margin-top:-8px;
    margin-bottom:10px;
}
</style>
""", unsafe_allow_html=True)
# ==========================================================
# FUNCTION PAPAR INSTRUMEN
# ==========================================================

def papar_instrumen(
    tajuk,
    deskripsi,
    pdf_file,
    pdf_name,
    kod,
    soalan
):

    st.subheader(tajuk)

    st.caption(deskripsi)

    col1, col2 = st.columns([1,4])

    with col1:

        with open(pdf_file, "rb") as pdf:

            st.download_button(
                "📄 Muat Turun",
                data=pdf,
                file_name=pdf_name,
                mime="application/pdf",
                key=f"download_{kod}",
                use_container_width=True
            )

    with col2:

        st.info(
            "Sila muat turun dan teliti instrumen sebelum memberikan maklum balas. | Please download and review the instrument before providing feedback."
        )

    st.caption(
        "STS = Sangat Tidak Setuju/Very Disagree |"
        "TS = Tidak Setuju/Disagree |"
        "N = Neutral/Neutral |"
        "S = Setuju/Agree |"
        "SS = Sangat Setuju/Very Agree"
    )

    pilihan = [
        "STS",
        "TS",
        "N",
        "S",
        "SS"
    ]

    jawapan = {}

    for item in soalan:

        jawapan[item[0]] = st.radio(

            item[1],

            pilihan,

            horizontal=True,

            key=item[0]

        )

    kekuatan = st.text_area(
        "Kekuatan Instrumen | Strengths of the Instrument",
        key=f"{kod}_kekuatan"
    )

    cadangan = st.text_area(
        "Cadangan Penambahbaikan | Suggestions for Improvement",
        key=f"{kod}_cadangan"
    )

    tambah = st.text_area(
        "Item yang perlu ditambah / digugurkan | Items to be added / removed",
        key=f"{kod}_item"
    )

    st.divider()

    return jawapan, kekuatan, cadangan, tambah
# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    """
<div class='title'>
MAKLUM BALAS AHLI AKADEMIK
</div>
""",
    unsafe_allow_html=True
)

st.markdown(
    """
<div class='subtitle'>
Platform Maklum Balas Ahli Akademik<br>
bagi Penambahbaikan Instrumen Penilaian Pembelajaran
</div>

<div class='english'>
Academic Staff Feedback Platform<br>
for the Enhancement of Learning Assessment Instruments
</div>
""",
    unsafe_allow_html=True
)

st.markdown(
    """
<div class='ppa'>
Pusat Pembangunan Akademik (PPA)<br>
Universiti Pendidikan Sultan Idris
</div>
""",
    unsafe_allow_html=True
)

st.divider()

# ==========================================================
# TUJUAN
# ==========================================================

st.subheader("📢 Tujuan")

st.markdown("""
<div class='english-left'>
Purpose
</div>
""", unsafe_allow_html=True)

st.info("""

**Tujuan**

Memohon maklum balas daripada semua ahli akademik bagi tujuan 
semakan dan penambahbaikan instrumen Penilaian Pembelajaran yang 
digunakan untuk menilai kualiti penyampaian Pengajaran dan Pembelajaran (PdP), 
Projek Tahun Akhir, Latihan Mengajar dan Latihan Industri. 
        
Maklum balas yang diterima akan membantu memastikan instrumen yang digunakan sentiasa relevan, 
jelas, berkesan serta selaras dengan keperluan semasa dan Objektif Kualiti Universiti.

**Purpose**

This survey aims to obtain feedback from academic staff for the 
review and enhancement of the Learning Evaluation instrument used 
to assess the quality of teaching and learning (T&L) delivery, 
Final Year Projects, Teaching Practicum, and Industrial Training.

The feedback received will support the continuous improvement of the 
instrument to ensure that it remains relevant, clear, effective, 
and aligned with current needs as well as the University's Quality Objectives.


""")

agree = st.checkbox(
    "Saya telah membaca maklumat di atas dan bersetuju memberikan maklum balas.| I have read the above information and agree to provide feedback."
)

if not agree:
    st.stop()
# ==========================================================
# MAKLUMAT AHLI AKADEMIK
# ==========================================================

st.divider()

st.subheader("📋 Maklumat Ahli Akademik")

st.markdown("""
<div class='english-left'>
Academic Staff Information
</div>
""", unsafe_allow_html=True)

st.write("Sila lengkapkan maklumat berikut sebelum memberikan maklum balas.")

col1, col2 = st.columns(2)

with col1:

    nama = st.text_input(
        "Nama | Name *"
    )

    no_pekerja = st.text_input(
        "No. Pekerja | Employee Number *"
    )

with col2:

    email = st.text_input(
        "Emel Rasmi | Official Email *"
    )

    fakulti = st.selectbox(
        "Fakulti | Faculty *",
        [
            "-- Sila Pilih Fakulti | Please Select Faculty --",
            "FBK",
            "FKMT",
            "FMSP",
            "FPM",
            "FPE",
            "FSM",
            "FSK",
            "FSSK",
            "FSKIK",
            "FTV"
        ]
    )

st.divider()

# ==========================================================
# SEMUA INSTRUMEN
# ==========================================================

# ------------------------------
# PdP
# ------------------------------

pdp_jawapan, pdp_kekuatan, pdp_cadangan, pdp_item = papar_instrumen(

    tajuk="📘 Instrumen Pengajaran dan Pembelajaran (PdP) | Teaching and Learning (T&L) Evaluation Instrument",

    deskripsi="Menilai Kualiti Pengajaran dan Pembelajaran | Assessing the Quality of Teaching and Learning",

    pdf_file="instrumen/Instrumen_PdP.pdf",

    pdf_name="Instrumen_PdP.pdf",

    kod="PDP",

    soalan=SOALAN["pdp"]

)

# ------------------------------
# Latihan Mengajar
# ------------------------------

lm_jawapan, lm_kekuatan, lm_cadangan, lm_item = papar_instrumen(

    tajuk="👨‍🏫 Instrumen Latihan Mengajar | Teaching Practice Evaluation Instrument",

    deskripsi="Menilai Kualiti Penyeliaan Latihan Mengajar | Assessing the Quality of Teaching Practice",

    pdf_file="instrumen/Instrumen_LM.pdf",

    pdf_name="Instrumen_LM.pdf",

    kod="LM",

    soalan=SOALAN["lm"]

)

# ------------------------------
# Latihan Industri
# ------------------------------

li_jawapan, li_kekuatan, li_cadangan, li_item = papar_instrumen(

    tajuk="🏭 Instrumen Latihan Industri | Industrial Training Evaluation Instrument",

    deskripsi="Menilai Kualiti Penyeliaan Latihan Industri | Assessing the Quality of Industrial Training",

    pdf_file="instrumen/Instrumen_LI.pdf",

    pdf_name="Instrumen_LI.pdf",

    kod="LI",

    soalan=SOALAN["li"]

)

# ------------------------------
# Projek Tahun Akhir
# ------------------------------

fyp_jawapan, fyp_kekuatan, fyp_cadangan, fyp_item = papar_instrumen(

    tajuk="🎓 Instrumen Projek Tahun Akhir | Final Year Project Evaluation Instrument",

    deskripsi="Menilai Kualiti Penyeliaan Projek Tahun Akhir | Assessing the Quality of Final Year Project",

    pdf_file="instrumen/Instrumen_FYP.pdf",

    pdf_name="Instrumen_FYP.pdf",

    kod="FYP",

    soalan=SOALAN["fyp"]

)

# ==========================================================
# HANTAR
# ==========================================================

submit = st.button(
    "✅ HANTAR SEMUA MAKLUM BALAS | SUBMIT ALL FEEDBACK",
    type="primary",
    use_container_width=True
)

if submit:

    from datetime import datetime

    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
 # ==========================================================
# VALIDASI MAKLUMAT AHLI AKADEMIK
 # ==========================================================

    ralat = []

    if nama.strip() == "":
        ralat.append("• Nama")

    if no_pekerja.strip() == "":
        ralat.append("• No. Pekerja")

    if email.strip() == "":
        ralat.append("• Emel Rasmi")

    if fakulti == "-- Sila Pilih Fakulti --":
        ralat.append("• Fakulti")

    if len(ralat) > 0:

        st.warning(
            "⚠️ Sila lengkapkan maklumat berikut:\n\n"
            + "\n".join(ralat)
        )

        st.stop()

    skor = {
        "STS": 1,
        "TS": 2,
        "N": 3,
        "S": 4,
        "SS": 5
    }

    # ==========================================================
    # DATA PDP
    # ==========================================================

    data_pdp = {

        "sheet": "PdP",

        "values": [

            timestamp,

            nama,

            no_pekerja,

            email,

            fakulti,

            "PdP",

            skor[pdp_jawapan["PDPA1"]],
            skor[pdp_jawapan["PDPA2"]],
            skor[pdp_jawapan["PDPA3"]],
            skor[pdp_jawapan["PDPA4"]],
            skor[pdp_jawapan["PDPA5"]],

            pdp_kekuatan,

            pdp_cadangan,

            pdp_item

        ]

    }

    # ==========================================================
    # DATA LM
    # ==========================================================

    data_lm = {

        "sheet": "LM",

        "values":[

            timestamp,

            nama,

            no_pekerja,

            email,

            fakulti,

            "LM",

            skor[lm_jawapan["LMA1"]],
            skor[lm_jawapan["LMA2"]],
            skor[lm_jawapan["LMA3"]],
            skor[lm_jawapan["LMA4"]],
            skor[lm_jawapan["LMA5"]],

            lm_kekuatan,

            lm_cadangan,

            lm_item

        ]

    }
        # ==========================================================
    # DATA LI
    # ==========================================================

    data_li = {

        "sheet": "LI",

        "values":[

            timestamp,

            nama,

            no_pekerja,

            email,

            fakulti,

            "LI",

            skor[li_jawapan["LIA1"]],
            skor[li_jawapan["LIA2"]],
            skor[li_jawapan["LIA3"]],
            skor[li_jawapan["LIA4"]],
            skor[li_jawapan["LIA5"]],

            li_kekuatan,

            li_cadangan,

            li_item

        ]

    }

    # ==========================================================
    # DATA FYP
    # ==========================================================

    data_fyp = {

        "sheet": "FYP",

        "values":[

            timestamp,

            nama,

            no_pekerja,

            email,

            fakulti,

            "FYP",

            skor[fyp_jawapan["FYPA1"]],
            skor[fyp_jawapan["FYPA2"]],
            skor[fyp_jawapan["FYPA3"]],
            skor[fyp_jawapan["FYPA4"]],
            skor[fyp_jawapan["FYPA5"]],

            fyp_kekuatan,

            fyp_cadangan,

            fyp_item

        ]

    }
    # ==========================================================
    # HANTAR KE GOOGLE SHEETS
    # ==========================================================

    berjaya_pdp = save_feedback(data_pdp)

    berjaya_lm = save_feedback(data_lm)

    berjaya_li = save_feedback(data_li)

    berjaya_fyp = save_feedback(data_fyp)

    # ==========================================================
    # SEMAK STATUS PENGHANTARAN
    # ==========================================================

    if (
        berjaya_pdp
        and berjaya_lm
        and berjaya_li
        and berjaya_fyp
    ):

        st.balloons()

        st.success("""
🎉 Terima kasih!

Maklum balas anda telah berjaya dihantar.

Pusat Pembangunan Akademik (PPA)
menghargai kerjasama anda.
""")

    else:

        st.error("""
❌ Sebahagian data gagal dihantar.

Sila cuba sekali lagi atau hubungi Pentadbir Sistem.
""")