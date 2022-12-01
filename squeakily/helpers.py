# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_helpers.ipynb.

# %% auto 0
__all__ = ['english_flagged_words', 'flagged_words', 'KENLM_MODEL_REPO', 'get_words', 'FastTextLanguageDetector', 'SentencePiece',
           'KenlmModel']

# %% ../nbs/03_helpers.ipynb 2
import os
import re
import squeakily
import unicodedata
import urllib.request

from huggingface_hub import cached_download, hf_hub_url
from requests.exceptions import HTTPError
from typing import Dict

# %% ../nbs/03_helpers.ipynb 6
def get_words(
    text: str, # the text to extract words from
) -> list:
    """custom regex to extract all the words in a string"""
    return re.findall(r'\w+', text.lower())

# %% ../nbs/03_helpers.ipynb 7
# Built from native speakers, with inspiration from
# https://github.com/zacanger/profane-words
# and
# https://github.com/thisandagain/washyourmouthoutwithsoap/blob/develop/data/build.json
# and
# https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words


english_flagged_words = [
    "anal",
    # "bareback", # not sure about this one
    "bbw",
    "bdsm",
    "blowjob",
    "blowjobs",
    "brazzers",
    "bukkake",
    "camgirl",
    "camwhore",
    "cocksucking",
    # "cougar", # not sure about this one
    "creampie",
    "cuckold",
    "cum",
    "cumming",
    "cums",
    "cumshot",
    "cumshots",
    "cumslut",
    "cunnilingus",
    "deepthroat",
    "deepthroating",
    "dildo",
    "dildos",
    "dogging",
    "doggystyle",
    # "dominatrix", # not sure about this one
    "erotic",
    "fellatio",
    "femdom",
    "fingering",
    "fisting",
    "footjob",
    "gangbang",
    "handjob",
    "hentai",
    "horney",
    "horniest",
    "horny",
    "jism",
    "jizz",
    "lolli",
    "lolling",
    "masterbating",
    "masturbate",
    "masturbating",
    "masturbation",
    "milf",
    "orgies",
    "orgy",
    "pegging",
    "porn",
    "pornhub",
    "porno",
    "pornos",
    "pornstar",
    "pornstars",
    "redtube",
    "rimming",
    "slutty",
    # "squirting", # not sure about this one
    "strapon",
    "threesome",
    "vibrator",
    "xhamster",
    "xnxx",
    "xvideos",
    "xxx",
    "youporn",
]


flagged_words = {
    "ar": english_flagged_words
    + [
        "إباحي",
        "احتلام",
        "است",
        "استمناء",
        "اغتصاب",
        "أورغازم",
        "إيروتيك",
        "أير",
        "بز",
        "بزاز",
        "بظر",
        "بورن",
        "بيضان",
        "مص",
        "ثدي",
        "جماع",
        "جنس",
        "حلمة",
        "خلاعة",
        "خنثي",
        "خول",
        "دعارة",
        "زب",
        "سحاق",
        "سحاقية",
        "سكس",
        "سيكس",
        "شاذ",
        "شبق",
        "شرج",
        "شرموطة",
        "شهواني",
        "شهوة",
        "طيز",
        "عادة السرية",
        "عاهرة",
        "عرص",
        "فاسقة",
        "فرج",
        "قحبة",
        "قضيب",
        "كس",
        "لحس",
        "لعق",
        "لواط",
        "لوطي",
        "مؤخرة",
        "متناك",
        "متناكة",
        "مومس",
        "مثير",
        "مص",
        "مضاجعة",
        "مفلقسة",
        "مني",
        "مهتاج",
        "نشوة",
        "نكاح",
        "نيك",
    ],
    "bn": english_flagged_words
    + [
        "আঙ্গুলি করা",
        "আচোদা",
        "খানকি",
        "খানকি মাগি",
        "গান্ড মারানো",
        "গুদ মারানি",
        "চুচুক",
        "চোদ",
        "চোদনা",
        "চোদা",
        "চোদা বোন",
        "চোদাচুদি",
        "জারজ",
        "নাঙ্গ",
        "নেংটা",
        "পর্ণহাব",
        "পর্ন",
        "পর্নস্টার",
        "পর্নোগ্রাফি",
        "পোঁদ",
        "পোঁদ মারানি",
        "পোদ মারানি",
        "বাঁড়া",
        "বানচোদ",
        "বেশ্যা",
        "বেশ্যার ছেলে",
        "বোকাচোদা",
        "ভগ",
        "মা চোদা",
        "মাগী",
        "মাদারচোদ",
        "মুখে নিবি",
        "মোরগ",
        "রেন্ডি",
        "শিশ্ন",
        "স্তন",
        "স্তনবৃন্ত",
        "হস্তমৈথুন",
    ],
    "ca": english_flagged_words
    + [
        "cagarro",
        "cagarros",
        "cipote",
        "cipotes",
        "collons",
        "colló",
        "consolador",
        "consoladors",
        "cony",
        "conys",
        "corre's",
        "corre't",
        "corregut",
        "cunillingus",
        "córrer-se",
        "escorreguda",
        "escorregudes",
        "escorregut",
        "escrot",
        "escrots",
        "escórre's",
        "escórre't",
        "escórrer-se",
        "mamada",
        "mamadera",
        "mamaderes",
        "mamades",
        "masturba",
        "masturbacions",
        "masturbació",
        "masturbant",
        "masturbar",
        "masturbar-se",
        "masturbat",
        "masturbats",
        "masturbes",
        "orgasme",
        "orgasmes",
        "ou",
        "ous",
        "palla",
        "palles",
        "pornografia",
        "semen",
        "semens",
        "verga",
        "vergues",
        "xxx",
    ],
    "en": english_flagged_words,
    "es": english_flagged_words
    + [
        "chupar el coño",
        "chupar la concha",
        "chupar la polla",
        "chupar la verga",
        "comer el coño",
        "comer la concha",
        "comer la polla",
        "comer la verga",
        "coprofagía",
        "correrse",
        "cunillingus",
        "fagging",
        "felación",
        "felching",
        "follada",
        "follador de culo",
        "folladores",
        "fudge packer",
        "hacer una paja",
        "hacerse una paja",
        "hore",
        "kock",
        "macizorra",
        "madre folladora",
        "mamada",
        "perro follador",
        "pisser",
        "pornografía",
        "sado",
        "sadomasoquismo",
        "sadomasoquista",
        "sexo anal",
        "skank",
        "smegma",
        "x clasificado",
    ],
    "eu": english_flagged_words + [],
    "fr": english_flagged_words
    + [
        "baiseurs",
        "baiseur",
        "baiseuse",
        "baiseuses",
        "branlette",
        "branlettes",
        "branleuse",
        "branleuses",
        "cunillingus",
        "cunilingus",
        "enculée",
        "enculées",
        "enculation",
        "enculations",
        "enculement",
        "enculements",
        "fellation",
        "fellations",
        "porno",
        "pornos",
        "pornographie",
        "pornographique",
        "pornographiques",
        "salope",
        "salopes",
        "suceuse",
        "suceuses",
        "xxx",
    ],
    "hi": english_flagged_words
    + [
        "अंडकोश की थैली",
        "एक्स रेटेड",
        "ओगाज़्म",
        "कामोद्दीपक चित्र",
        "कालीन का चूरा",
        "कून",
        "कॉक",
        "गेंद का थैला",
        "चाकलेट का रंग",
        "चूची",
        "चूतड़",
        "झटका बंद",
        "ठगना पैकर",
        "डिल्डो",
        "नितंब",
        "पिछाड़ी",
        "पीड़न कामुक",
        "पॉर्न",
        "फटना",
        "फूहड़",
        "बट",
        "बहुत मदहोश",
        "बेल अंत",
        "भगवान-शापित",
        "भगशेफ",
        "माँ कमीने",
        "मुखमैथुन",
        "मुर्गा चूसने वाला",
        "रक्तरंजित",
        "लेबिया",
        "वहशी",
        "वहशीता",
        "वैंग",
        "शिश्नमल",
        "संभोग सुख",
        "सह शॉट",
        "सींग का बना हुआ",
        "होर",
        "घपा घप",
        "चुदाई",
        "चुदक्कड़",
    ],
    "id": english_flagged_words
    + [
        "bokep",
        "coli",
        "colmek",
        "grepe",
        "horni",
        "janda",
        "jembut",
        "jilat memek",
        "jilmek",
        "kontol",
        "masturbasi",
        "memek",
        "ngentot",
        "ngewe",
        "peju",
        "pepek",
        "pornografi",
        "sange",
        "sepong",
        "tusbol",
    ],
    "pt": english_flagged_words
    + [
        "balalao",
        "bate uma",
        "beijo grego",
        "boceta",
        "boquete",
        "buceta",
        "caralho",
        "chochota",
        "coito",
        "cona",
        "consolo",
        "corno",
        "cu",
        "dar a bunda",
        "dar o rabo",
        "dildo",
        "dildos",
        "esporrar",
        "estrovenga",
        "felação",
        "filho da puta",
        "filhos da puta",
        "gozada",
        "jeba",
        "perereca",
        "pica",
        "piru",
        "porno",
        "pornografia",
        "pornô",
        "porra",
        "prostituta",
        "pube",
        "punheta",
        "punheteiro",
        "putaria",
        "queca",
        "sexo",
        "siririca",
        "tesão",
        "trepada",
        "verga",
        "vibrador",
        "xana",
        "xochota",
        "xoxota",
    ],
    "ur": english_flagged_words
    + [
        "انگلی کرنا",
        "ایکس ریٹیڈ",
        "بلو جاب",
        "بٹ",
        "جھٹکا بند",
        "دلڈو",
        "رنڈی",
        "سلٹ",
        "سکلیرا",
        "سیڈسٹ",
        "سیکس بم",
        "شہوانی",
        "شہوت انگیز",
        "فحش نگاری",
        "لن",
        "لنڈ",
        "لنڈ چوسنے والا",
        "لوڑہ",
        "ماں کمینے",
        "مشت زنی",
        "ممے",
        "مٹھ",
        "مٹھی",
        "ویشیا",
        "پورن",
        "پھدی",
        "پیگنگ",
        "چدائ",
        "چدک",
        "چوت",
        "چودنا",
        "چوچی",
        "کسبی",
        "کسنگ",
        "گانڈ",
        "گدا",
        "ہینڈ جاب",
    ],
    "vi": english_flagged_words
    + [
        "cặc",
        "lồn",
        "địt",
        "buồi",
        "đụ",
        "nứng",
        "phò",
        "bú lol",
        "bú lon",
        "bú cac",
        "bú cak",
        "bú cax",
        "bú buoi",
        "bú mút",
        "húp lol",
        "húp lon",
        "húp sò",
        "nung lol",
        "nung lon",
        "nug lon",
        "nung cac",
        "nung buoi",
        "thèm dit",
        "thèm lon",
        "thèm lol",
        "thèm buoi",
        "thèm dit",
        "thèm chich",
        "thèm chịch",
        "thèm cax",
        "thèm cak",
        "móc lol",
        "móc lon",
        "buscu",
        "lol non",
        "bướm non",
        "vú to",
        "vú bự",
        "lon to",
        "phim sex",
        "phim xex",
        "phim xxx",
    ],
    "zh": english_flagged_words
    + [
        "三级片",
        "乳交",
        "卖B",
        "卖比",
        "卖淫",
        "口交",
        "姣西",
        "打炮",
        "打飞机",
        "抽插",
        "招妓",
        "插你",
        "插死你",
        "淫水",
        "肉壁",
        "肉棍子",
        "肉缝",
        "肏",
        "肛交",
    ],
}

# %% ../nbs/03_helpers.ipynb 9
class FastTextLanguageDetector:
    def __init__(self, model_path: str = "/tmp/lid.176.bin"):
        import fasttext
        self.model_path = model_path
        self.model = fasttext.load_model(model_path)

    def get_language(self, text):
        prediction = self.model.predict(text, k=1) # returns top 2 matching languages
        lang, prob = prediction[0][0].replace("__label__", ""), prediction[1][0]
        return lang, prob

    @classmethod
    def from_pretrained(
        cls,
        *,
        url: str = "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin",
        output_dir: str = squeakily.__path__[0],
    ):
        path = os.path.join(output_dir, "lid.176.bin")
        if not os.path.exists(path):
            # download pretrained model with standard lib (From: https://stackoverflow.com/questions/22676/how-to-download-a-file-over-http)
            response = urllib.request.urlretrieve(url, )
            if response:
                return cls(model_path=os.path.join(output_dir, "lid.176.bin"))
            else:
                raise Exception("Failed to download model")
        else:
            return cls(model_path=path)
    
    def __reduce__(self):
        return (self.__class__, (self.model_path,))
    
    def __eq__(self, other):
        return self.model_path == other.model_path


# %% ../nbs/03_helpers.ipynb 13
class SentencePiece:
    def __init__(
        self,
        model: str,
    ):
        import sentencepiece
        super().__init__()
        self.sp = sentencepiece.SentencePieceProcessor()
        self.sp.load(str(model))

    def do(self, text: dict) -> dict:
        tokenized = self.sp.encode_as_pieces(text)
        return " ".join(tokenized)

# %% ../nbs/03_helpers.ipynb 14
KENLM_MODEL_REPO = "edugp/kenlm"

class KenlmModel:
    digit_re: re.Pattern = re.compile(r"\d")
    unicode_punct: Dict[str, str] = {
        "，": ",",
        "。": ".",
        "、": ",",
        "„": '"',
        "”": '"',
        "“": '"',
        "«": '"',
        "»": '"',
        "１": '"',
        "」": '"',
        "「": '"',
        "《": '"',
        "》": '"',
        "´": "'",
        "∶": ":",
        "：": ":",
        "？": "?",
        "！": "!",
        "（": "(",
        "）": ")",
        "；": ";",
        "–": "-",
        "—": " - ",
        "．": ". ",
        "～": "~",
        "’": "'",
        "…": "...",
        "━": "-",
        "〈": "<",
        "〉": ">",
        "【": "[",
        "】": "]",
        "％": "%",
        "►": "-",
    }
    unicode_punct_re = re.compile(f"[{''.join(unicode_punct.keys())}]")
    non_printing_chars_re = re.compile(
        f"[{''.join(map(chr, list(range(0,32)) + list(range(127,160))))}]"
    )
    kenlm_model_dir = None
    sentence_piece_model_dir = None

    def __init__(
        self,
        model_dataset: str,
        language: str,
        lower_case: bool = False,
        remove_accents: bool = False,
        normalize_numbers: bool = True,
        punctuation: int = 1,
    ):
        import kenlm

        self.download_kenlm_model(model_dataset, language)
        try:
            self.model = kenlm.Model(self.kenlm_model_dir)
            self.tokenizer = SentencePiece(self.sentence_piece_model_dir)
        except OSError:
            os.remove(self.kenlm_model_dir)
            if os.path.exists(self.sentence_piece_model_dir):
                os.remove(self.sentence_piece_model_dir)
            raise OSError(
                "File was corrupt and should have been removed. Please, retry."
            )
        self.accent = remove_accents
        self.case = lower_case
        self.numbers = normalize_numbers
        self.punct = punctuation

    @classmethod
    def from_pretrained(
        cls,
        *,
        model_dataset: str,
        language: str,
        lower_case: bool,
        remove_accents: bool,
        normalize_numbers: bool,
        punctuation: int,
    ):
        return cls(
            model_dataset,
            language,
            lower_case,
            remove_accents,
            normalize_numbers,
            punctuation,
        )

    def pp(self, log_score, length):
        return 10.0 ** (-log_score / length)

    def get_perplexity(self, doc: str, normalize_cc_net: bool = True):
        if normalize_cc_net:
            doc = self.normalize(
                doc,
                accent=self.accent,
                case=self.case,
                numbers=self.numbers,
                punct=self.punct,
            )
        # Tokenize (after normalizing): See https://github.com/facebookresearch/cc_net/blob/bda555bd1cf1ee2e0b925363e62a61cd46c8b60d/cc_net/mine.py#L352 for full pipeline
        doc = self.tokenizer.do(doc)
        doc_log_score, doc_length = 0, 0
        for line in doc.split("\n"):
            log_score = self.model.score(line)
            length = len(line.split()) + 1
            doc_log_score += log_score
            doc_length += length
        return round(self.pp(doc_log_score, doc_length), 1)

    def normalize(
        self,
        line: str,
        accent: bool = True,
        case: bool = True,
        numbers: bool = True,
        punct: int = 1,
    ) -> str:
        line = line.strip()
        if not line:
            return line
        if case:
            line = line.lower()
        if accent:
            line = self.strip_accents(line)
        if numbers:
            line = self.digit_re.sub("0", line)
        if punct == 1:
            line = self.replace_unicode_punct(line)
        elif punct == 2:
            line = self.remove_unicode_punct(line)
        line = self.remove_non_printing_char(line)
        return line

    def strip_accents(self, line: str) -> str:
        """Strips accents from a piece of text."""
        nfd = unicodedata.normalize("NFD", line)
        output = [c for c in nfd if unicodedata.category(c) != "Mn"]
        if len(output) == line:
            return line
        return "".join(output)

    def replace_unicode_punct(self, text: str) -> str:
        return "".join(self.unicode_punct.get(c, c) for c in text)

    def remove_unicode_punct(self, text: str) -> str:
        """More aggressive version of replace_unicode_punct but also faster."""
        return self.unicode_punct_re.sub("", text)

    def remove_non_printing_char(self, text: str) -> str:
        return self.non_printing_chars_re.sub("", text)

    def download_kenlm_model(self, model_dataset: str, language: str):
        try:
            kenlm_model_url = hf_hub_url(
                KENLM_MODEL_REPO, filename=f"{model_dataset}/{language}.arpa.trie.bin"
            )
            self.kenlm_model_dir = cached_download(kenlm_model_url)
        except HTTPError:
            kenlm_model_url = hf_hub_url(
                KENLM_MODEL_REPO, filename=f"{model_dataset}/{language}.arpa.bin"
            )
            self.kenlm_model_dir = cached_download(kenlm_model_url)
        sentence_piece_model_url = hf_hub_url(
            KENLM_MODEL_REPO, filename=f"{model_dataset}/{language}.sp.model"
        )
        self.sentence_piece_model_dir = cached_download(sentence_piece_model_url)
