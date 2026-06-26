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
            "Sila muat turun dan teliti instrumen sebelum memberikan maklum balas."
        )

    st.caption(
        "STS = Sangat Tidak Setuju | "
        "TS = Tidak Setuju | "
        "N = Neutral | "
        "S = Setuju | "
        "SS = Sangat Setuju"
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
        "Kekuatan Instrumen",
        key=f"{kod}_kekuatan"
    )

    cadangan = st.text_area(
        "Cadangan Penambahbaikan",
        key=f"{kod}_cadangan"
    )

    tambah = st.text_area(
        "Item yang perlu ditambah / digugurkan",
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
Penambahbaikan Instrumen Penilaian Pembelajaran
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

st.info("""

**Tujuan**

Memohon maklum balas daripada semua ahli akademik bagi tujuan 
semakan dan penambahbaikan instrumen Penilaian Pembelajaran yang 
digunakan untuk menilai kualiti penyampaian Pengajaran dan Pembelajaran (PdP), 
Projek Tahun Akhir, Latihan Mengajar dan Latihan Industri. 
        
Maklum balas yang diterima akan membantu memastikan instrumen yang digunakan sentiasa relevan, 
jelas, berkesan serta selaras dengan keperluan semasa dan Objektif Kualiti Universiti.


""")

agree = st.checkbox(
    "Saya telah membaca maklumat di atas dan bersetuju memberikan maklum balas."
)

if not agree:
    st.stop()
# ==========================================================
# MAKLUMAT AHLI AKADEMIK
# ==========================================================

st.divider()

st.subheader("👤 Maklumat Ahli Akademik")

st.write("Sila lengkapkan maklumat berikut sebelum memberikan maklum balas.")

col1, col2 = st.columns(2)

with col1:

    nama = st.text_input(
        "Nama *"
    )

    no_pekerja = st.text_input(
        "No. Pekerja *"
    )

with col2:

    email = st.text_input(
        "Emel Rasmi *"
    )

    fakulti = st.selectbox(
        "Fakulti *",
        [
            "-- Sila Pilih Fakulti --",
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

    tajuk="📘 Instrumen PdP",

    deskripsi="Menilai Kualiti Pengajaran dan Pembelajaran",

    pdf_file="instrumen/Instrumen_PdP.pdf",

    pdf_name="Instrumen_PdP.pdf",

    kod="PDP",

    soalan=SOALAN["pdp"]

)

# ------------------------------
# Latihan Mengajar
# ------------------------------

lm_jawapan, lm_kekuatan, lm_cadangan, lm_item = papar_instrumen(

    tajuk="👨‍🏫 Instrumen Latihan Mengajar",

    deskripsi="Menilai Kualiti Penyeliaan Latihan Mengajar",

    pdf_file="instrumen/Instrumen_LM.pdf",

    pdf_name="Instrumen_LM.pdf",

    kod="LM",

    soalan=SOALAN["lm"]

)

# ------------------------------
# Latihan Industri
# ------------------------------

li_jawapan, li_kekuatan, li_cadangan, li_item = papar_instrumen(

    tajuk="🏭 Instrumen Latihan Industri",

    deskripsi="Menilai Kualiti Penyeliaan Latihan Industri",

    pdf_file="instrumen/Instrumen_LI.pdf",

    pdf_name="Instrumen_LI.pdf",

    kod="LI",

    soalan=SOALAN["li"]

)

# ------------------------------
# Projek Tahun Akhir
# ------------------------------

fyp_jawapan, fyp_kekuatan, fyp_cadangan, fyp_item = papar_instrumen(

    tajuk="🎓 Instrumen Projek Tahun Akhir",

    deskripsi="Menilai Kualiti Penyeliaan Projek Tahun Akhir",

    pdf_file="instrumen/Instrumen_FYP.pdf",

    pdf_name="Instrumen_FYP.pdf",

    kod="FYP",

    soalan=SOALAN["fyp"]

)

# ==========================================================
# HANTAR
# ==========================================================

submit = st.button(
    "✅ HANTAR SEMUA MAKLUM BALAS",
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