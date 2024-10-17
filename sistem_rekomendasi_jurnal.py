{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "kCOSPANm6aUB"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "jurnal = pd.read_csv(r\"C:\\Users\\acer\\anaconda3\\envs\\ki\\datajurnal2.csv\",sep=\";\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "B6V7fqKmRWGk",
        "outputId": "04546121-238e-4add-ea02-1aeb7a286ed5"
      },
      "outputs": [
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>journalId</th>\n",
              "      <th>title</th>\n",
              "      <th>abstract</th>\n",
              "      <th>keywords</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>Mesenchymal Transformation: The Rosetta Stone ...</td>\n",
              "      <td>Despite decades of research, glioblastoma (GB...</td>\n",
              "      <td>clinical outcome|glioblastoma (GBM)|mesenchyma...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>DGAT1 protects tumor from lipotoxicity, emergi...</td>\n",
              "      <td>We recently demonstrated that glioblastoma, th...</td>\n",
              "      <td>DGAT1|glioblastoma|lipotoxicity|oxidative stre...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>Anti-PD-1 Immunotherapy in Preclinical GL261 G...</td>\n",
              "      <td>Glioblastomas (GBs) are malignant brain tumou...</td>\n",
              "      <td>TMZ|checkpoint inhibitors|glioblastoma|long-te...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>Recent Updates on the Relationship between Can...</td>\n",
              "      <td>Autoimmune pancreatitis (AIP) is now considere...</td>\n",
              "      <td>IgG4-related disease|autoimmune pancreatitis|c...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>Cancer and cure: A critical analysis</td>\n",
              "      <td>Cancer is one of the most dreaded diseases of ...</td>\n",
              "      <td>cancer|cure.</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   journalId                                              title  \\\n",
              "0          1  Mesenchymal Transformation: The Rosetta Stone ...   \n",
              "1          2  DGAT1 protects tumor from lipotoxicity, emergi...   \n",
              "2          3  Anti-PD-1 Immunotherapy in Preclinical GL261 G...   \n",
              "3          4  Recent Updates on the Relationship between Can...   \n",
              "4          5               Cancer and cure: A critical analysis   \n",
              "\n",
              "                                            abstract  \\\n",
              "0   Despite decades of research, glioblastoma (GB...   \n",
              "1  We recently demonstrated that glioblastoma, th...   \n",
              "2   Glioblastomas (GBs) are malignant brain tumou...   \n",
              "3  Autoimmune pancreatitis (AIP) is now considere...   \n",
              "4  Cancer is one of the most dreaded diseases of ...   \n",
              "\n",
              "                                            keywords  \n",
              "0  clinical outcome|glioblastoma (GBM)|mesenchyma...  \n",
              "1  DGAT1|glioblastoma|lipotoxicity|oxidative stre...  \n",
              "2  TMZ|checkpoint inhibitors|glioblastoma|long-te...  \n",
              "3  IgG4-related disease|autoimmune pancreatitis|c...  \n",
              "4                                       cancer|cure.  "
            ]
          },
          "execution_count": 2,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "jurnal.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Usq6O0FMVw0i",
        "outputId": "ad879b89-7f27-42cd-8ae5-c78a7bd1c3d8"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "[nltk_data] Downloading package punkt to\n",
            "[nltk_data]     C:\\Users\\acer\\AppData\\Roaming\\nltk_data...\n",
            "[nltk_data]   Unzipping tokenizers\\punkt.zip.\n",
            "[nltk_data] Downloading package stopwords to\n",
            "[nltk_data]     C:\\Users\\acer\\AppData\\Roaming\\nltk_data...\n",
            "[nltk_data]   Unzipping corpora\\stopwords.zip.\n",
            "[nltk_data] Downloading package wordnet to\n",
            "[nltk_data]     C:\\Users\\acer\\AppData\\Roaming\\nltk_data...\n",
            "[nltk_data] Downloading package omw-1.4 to\n",
            "[nltk_data]     C:\\Users\\acer\\AppData\\Roaming\\nltk_data...\n"
          ]
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Completed\n"
          ]
        }
      ],
      "source": [
        "import nltk\n",
        "import nltk.tokenize\n",
        "\n",
        "\n",
        "# Tokenizing\n",
        "nltk.download('punkt')\n",
        "# Stopwords removal\n",
        "nltk.download('stopwords')\n",
        "# Lemmatizer\n",
        "nltk.download('wordnet')\n",
        "nltk.download('omw-1.4')\n",
        "\n",
        "print('Completed')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "id": "V3TN6IXGJDAO"
      },
      "outputs": [],
      "source": [
        "import re\n",
        "\n",
        "def clean_title(title):\n",
        "  re.sub(\"[^a-zA-Z0-9 ]\", \"\", title)\n",
        "  return title"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "id": "7uJpEaMLQ2TC"
      },
      "outputs": [],
      "source": [
        "jurnal[\"clean_title\"] = jurnal[\"title\"].apply(clean_title)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "id": "N7ahEOJbRPs8"
      },
      "outputs": [],
      "source": [
        "#jurnal"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "id": "-IX3frvGXaU6"
      },
      "outputs": [],
      "source": [
        "import re\n",
        "\n",
        "def clean_abstract(abstract):\n",
        "  re.sub(\"[a-zA-Z ]\", \"\", abstract)\n",
        "  return abstract"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "id": "2yHQf-BDXpaK"
      },
      "outputs": [],
      "source": [
        "jurnal[\"clean_abstract\"] = jurnal[\"abstract\"].apply(clean_abstract)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1ZEHAJBfXp1G",
        "outputId": "895d3047-3f05-45de-bdbe-e7894f8288a1"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "keywords\n",
              " Biopsy|Blood|Breast cancer|Droplet digital|Liquid biopsy|PCR|PIK3CA|cancer|Plasma.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          12.000000\n",
              " COVID-19|SARS-CoV-2|vitamin D.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               8.000000\n",
              " Derek Parfit focuses on normative theories (and the aims they provide to agents), David McNaughton and Piers Rawling focus on rules and reasons, Skorupski on predicates, and there are other suggestions too. Some writers suspect that we fundamentally talk about one and the same distinction. This work is about practical reasons for action rather than theoretical reasons for belief. Moreover, focus is on whether reasons do or do not essentially refer to particular agents. A challenge that undermines the dichotomy in this sense is posed. After having rejected different attempts to defend the distinction, it is argued that there is a possible defence that sets out from Jonathan Dancy’s recent distinction between enablers and favourers.                                                                                         6.000000\n",
              " I support commonsense realism through an interpretation and application of Donald Davidson’s notion of triangulation, the triangle composed of two communicators coordinating and correcting their responses with a shared causal stimulus. This argument is important because it has a crucial advantage over the often used abductive argument for realism. My argument avoids unwarranted conclusions, whereas the abductive argument is “inflationary” because it reaches beyond the limits of evidence for its realist conclusion. To illustrate the problems of the abductive argument and motivate my Davidsonian approach, I take a brief look at the abductive argument for realism in Frederick Will’s work.                                                                                                                                       4.000000\n",
              " IoT|internet of things                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      11.000000\n",
              " IoT|internet of things.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      6.000000\n",
              " antiviral therapy|coronavirus disease 2019| severe acute respiratory syndrome coronavirus 2| vaccines| variant strains.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     10.000000\n",
              " bladder cancer| cell stress| cytokine| endoplasmic reticulum stress (ER stress)| exosome (vesicle)|extracellular vesicles|filed cancerization|inflammation|unfolded protein response (UPR)| urothelial carcinoma|cancer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    18.000000\n",
              " internet of things                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           9.000000\n",
              " second, in a software system there are usually much fewer defective modules than defect-free modules, so learning would have to be conducted over an imbalanced data set. In this paper, we address these two practical issues simultaneously by proposing a novel semi-supervised learning approach named Rocus. This method exploits the abundant unlabeled examples to improve the detection accuracy, as well as employs under-sampling to tackle the class-imbalance problem in the learning process. Experimental results of real-world software defect detection tasks show that Rocus is effective for software defect detection. Its performance is better than a semi-supervised learning method that ignores the class-imbalance nature of the task and a class-imbalance learning method that does not make effective use of unlabeled data.     5.000000\n",
              " yet these actions fail to satisfy the criteria for propositional knowledge. It is therefore my contention that there exists a form of intentional action that not only constitutes a genuine claim to knowledge but, in being irreducible to knowing that, resists the intellectualist argument for exhaustive epistemic reduction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         17.000000\n",
              "Antirheumatic drugs| Antiviral agents| COVID-19| Inflammation inhibitors| Low molecular weight heparins| SARS-CoV-2.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          5.000000\n",
              "COVID-19| Coronavirus| Diagnosis| SARS-CoV-2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  7.000000\n",
              "COVID-19| SARS-CoV-2| coronavirus| global health| pandemic|respiratory infection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             4.000000\n",
              "Cancer-associated fibroblasts|Field cancerization|Metastasis|Somatic Mutation Theory|Tissue Organization Field Theory|Tumor microenvironment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 10.000000\n",
              "Cancer| Gender| Kidney transplantation| Risk factor| Sex.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    10.000000\n",
              "Covid - 19 | sar-cov-2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        5.000000\n",
              "Covid - 19|coronavirus                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       18.000000\n",
              "DGAT1|glioblastoma|lipotoxicity|oxidative stress|triglycerides|cancer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        14.000000\n",
              "Heat shock proteins| apoptotic| cancer| cell proliferation| prognosis| therapeutics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         11.000000\n",
              "IgG4-related disease|autoimmune pancreatitis|cancer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         10.000000\n",
              "Internet of things.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           8.000000\n",
              "TMZ|checkpoint inhibitors|glioblastoma|long-term immune memory|magnetic resonance spectroscopic imaging|orthotopic immunocompetent tumours|therapy response biomarker.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       18.000000\n",
              "breast cancer|resistance|telomerase|therapy|cancer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          10.000000\n",
              "cancer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        3.000000\n",
              "cancer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       5.666667\n",
              "cancer| cancer treatment| metabolism| signaling pathways.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    10.000000\n",
              "cancer|breast cancer| cancer-adjacent tissues| field cancerization| histologically normal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    5.000000\n",
              "cancer|cure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  6.000000\n",
              "cancer|lung cancer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           4.000000\n",
              "cancer|tumor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 4.000000\n",
              "clinical outcome|glioblastoma (GBM)|mesenchymal transition|molecular subtypes|therapy responses|tumor microenvironment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      11.000000\n",
              "clonal evolution of cancer| gradualism| hopeful monsters| intratumour heterogeneity| neutral evolution| next-generation sequencing| punctuated equilibrium| saltation| selection| subclones.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  6.000000\n",
              "coronavirus|diagnostic methods|genome structure|pathogenesis.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 7.000000\n",
              "covid|covid-19.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               5.000000\n",
              "internet of things                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            7.000000\n",
              "internet of things.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          10.000000\n",
              "machine learning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              7.333333\n",
              "tumor|cancer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 8.000000\n",
              "Name: word_count, dtype: float64"
            ]
          },
          "execution_count": 9,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "jurnal['word_count'] = jurnal['title'].apply(lambda x: len(x.split()))\n",
        "jurnal.groupby('keywords')['word_count'].mean()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "yLr9Q67hbj80"
      },
      "source": [
        "**Vectorizer**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "id": "sfMyS-SnRRCG"
      },
      "outputs": [],
      "source": [
        "from numpy.lib.function_base import vectorize\n",
        "from sklearn.feature_extraction.text import TfidfVectorizer\n",
        "\n",
        "vectorizer = TfidfVectorizer(ngram_range=(2, 3))\n",
        "\n",
        "tfidf = vectorizer.fit_transform(jurnal[\"clean_title\"],[\"clean_abstract\"])"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QCnSJEelbecy"
      },
      "source": [
        "**1. similarity berdasarkan title**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "B3vsNKrZk9iY",
        "outputId": "81276201-5b23-4b82-f1c8-2c869ff2ad81"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Cancer comprises a bewildering assortment of diseases that kill 7.5 million people each year. Poor understanding of cancer's diversity currently thwarts our goal of a cure for every patient, but recent integration of genomic and stem cell technologies promises a route through this impasse.\n"
          ]
        },
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>journalId</th>\n",
              "      <th>title</th>\n",
              "      <th>abstract</th>\n",
              "      <th>keywords</th>\n",
              "      <th>clean_title</th>\n",
              "      <th>clean_abstract</th>\n",
              "      <th>word_count</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>12</td>\n",
              "      <td>Detection of Cancer DNA in Early Stage and Met...</td>\n",
              "      <td>Breast cancer is the leading cause of cancer i...</td>\n",
              "      <td>Biopsy|Blood|Breast cancer|Droplet digital|Li...</td>\n",
              "      <td>Detection of Cancer DNA in Early Stage and Met...</td>\n",
              "      <td>Breast cancer is the leading cause of cancer i...</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>30</th>\n",
              "      <td>31</td>\n",
              "      <td>An overview of internet of things</td>\n",
              "      <td>The internet of things is an emerging technolo...</td>\n",
              "      <td>IoT|internet of things.</td>\n",
              "      <td>An overview of internet of things</td>\n",
              "      <td>The internet of things is an emerging technolo...</td>\n",
              "      <td>6</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>27</th>\n",
              "      <td>28</td>\n",
              "      <td>Laboratory testing for the diagnosis of COVID-19</td>\n",
              "      <td>Rapid and accurate laboratory diagnosis of act...</td>\n",
              "      <td>COVID-19| Coronavirus| Diagnosis| SARS-CoV-2</td>\n",
              "      <td>Laboratory testing for the diagnosis of COVID-19</td>\n",
              "      <td>Rapid and accurate laboratory diagnosis of act...</td>\n",
              "      <td>7</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25</th>\n",
              "      <td>26</td>\n",
              "      <td>A Comprehensive Review of COVID-19 Virology, V...</td>\n",
              "      <td>Severe acute respiratory syndrome coronavirus ...</td>\n",
              "      <td>antiviral therapy|coronavirus disease 2019| s...</td>\n",
              "      <td>A Comprehensive Review of COVID-19 Virology, V...</td>\n",
              "      <td>Severe acute respiratory syndrome coronavirus ...</td>\n",
              "      <td>10</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "    journalId                                              title  \\\n",
              "11         12  Detection of Cancer DNA in Early Stage and Met...   \n",
              "30         31                  An overview of internet of things   \n",
              "27         28   Laboratory testing for the diagnosis of COVID-19   \n",
              "25         26  A Comprehensive Review of COVID-19 Virology, V...   \n",
              "\n",
              "                                             abstract  \\\n",
              "11  Breast cancer is the leading cause of cancer i...   \n",
              "30  The internet of things is an emerging technolo...   \n",
              "27  Rapid and accurate laboratory diagnosis of act...   \n",
              "25  Severe acute respiratory syndrome coronavirus ...   \n",
              "\n",
              "                                             keywords  \\\n",
              "11   Biopsy|Blood|Breast cancer|Droplet digital|Li...   \n",
              "30                            IoT|internet of things.   \n",
              "27       COVID-19| Coronavirus| Diagnosis| SARS-CoV-2   \n",
              "25   antiviral therapy|coronavirus disease 2019| s...   \n",
              "\n",
              "                                          clean_title  \\\n",
              "11  Detection of Cancer DNA in Early Stage and Met...   \n",
              "30                  An overview of internet of things   \n",
              "27   Laboratory testing for the diagnosis of COVID-19   \n",
              "25  A Comprehensive Review of COVID-19 Virology, V...   \n",
              "\n",
              "                                       clean_abstract  word_count  \n",
              "11  Breast cancer is the leading cause of cancer i...          12  \n",
              "30  The internet of things is an emerging technolo...           6  \n",
              "27  Rapid and accurate laboratory diagnosis of act...           7  \n",
              "25  Severe acute respiratory syndrome coronavirus ...          10  "
            ]
          },
          "execution_count": 11,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "from sklearn.metrics.pairwise import cosine_similarity # menggunakan pairwise untuk menghitung kedekatan antar kata\n",
        "import numpy as np\n",
        "\n",
        "#def search(title)\n",
        "def search(title): # Membuat fungsi search\n",
        "    print(title)\n",
        "    title = clean_title(title) # Memanggil fungsi clean_title\n",
        "    query_vec = vectorizer.transform([title]) # Mengubah isi dataframe title menjadi vektor\n",
        "    similarity = cosine_similarity(query_vec, tfidf).flatten() # Perhitungan cosinus antara pencarian kata dengan dataset\n",
        "    indices = np.argpartition(similarity, -10)[-10:] # Mendapatkan 5 data terdekat dari hasil pencarian\n",
        "    results = jurnal.iloc[indices].iloc[::-3] # Menunjukan lokasi data bedasarkan indices\n",
        "\n",
        "    return results\n",
        "\n",
        "search(\"Cancer comprises a bewildering assortment of diseases that kill 7.5 million people each year. Poor understanding of cancer's diversity currently thwarts our goal of a cure for every patient, but recent integration of genomic and stem cell technologies promises a route through this impasse.\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 49,
          "referenced_widgets": [
            "c4e05d41fde24ee29a7f0080566cfedc",
            "df7f3f1045494567b66bdb09df9d5af6",
            "0bc296fd1e1d420da036f6a7cd8ec60a",
            "59664960e51842d2971e32f7f1a0c347",
            "57cbb44b08ad48fb88495d4bf5a09bd2"
          ]
        },
        "id": "3qezbTzYlV3R",
        "outputId": "9d89bc92-0696-44ab-c412-1482f8675609"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.jupyter.widget-view+json": {
              "model_id": "3e1ea519859e4732921be6baff17d50c",
              "version_major": 2,
              "version_minor": 0
            },
            "text/plain": [
              "Text(value='Cancer and cure: A critical analysis', description='jurnal Title:')"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        },
        {
          "data": {
            "application/vnd.jupyter.widget-view+json": {
              "model_id": "a7cab141f2414c84bc1662765975d7bc",
              "version_major": 2,
              "version_minor": 0
            },
            "text/plain": [
              "Output()"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "# Membuat search bar interaktif\n",
        "import ipywidgets as widgets\n",
        "from IPython.display import display\n",
        "\n",
        "jurnal_input = widgets.Text( # Variabel input search bar\n",
        "    value='Cancer and cure: A critical analysis',\n",
        "    description='jurnal Title:',\n",
        "    disabled=False\n",
        ")\n",
        "jurnal_list = widgets.Output() # Menampilkan search bar\n",
        "\n",
        "def on_type(data): # Mencari data pada setiap ketikan input\n",
        "    with jurnal_list:\n",
        "        jurnal_list.clear_output()\n",
        "        title = data[\"new\"]\n",
        "        if len(title) > 5: # Membatasi minimal 5 karakter input untuk search\n",
        "            display(search(title)) # Menampilkan hasil search kepada output widget\n",
        "\n",
        "jurnal_input.observe(on_type, names='value') # Memanggil fungsi on_type ketika terjadi perubahan pada input bar\n",
        "\n",
        "display(jurnal_input, jurnal_list) # Menampilkan kedua widget yang dibuat"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "X-SYMO8f8WlO"
      },
      "source": [
        "**2. Similarity berdasarkan Abstract**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5Y1RAlw3X9yQ",
        "outputId": "ab15d1f4-1ed3-4f2d-9a61-3dd53bffb717"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Despite decades of research, glioblastoma (GBM) remains invariably fatal among all forms of cancers.\n"
          ]
        },
        {
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>journalId</th>\n",
              "      <th>title</th>\n",
              "      <th>abstract</th>\n",
              "      <th>keywords</th>\n",
              "      <th>clean_title</th>\n",
              "      <th>clean_abstract</th>\n",
              "      <th>word_count</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>89</th>\n",
              "      <td>90</td>\n",
              "      <td>Homogenization of Reynolds Equation by Two-Sca...</td>\n",
              "      <td>To increase the hydrodynamic performance in di...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Homogenization of Reynolds Equation by Two-Sca...</td>\n",
              "      <td>To increase the hydrodynamic performance in di...</td>\n",
              "      <td>7</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "    journalId                                              title  \\\n",
              "89         90  Homogenization of Reynolds Equation by Two-Sca...   \n",
              "\n",
              "                                             abstract keywords  \\\n",
              "89  To increase the hydrodynamic performance in di...      NaN   \n",
              "\n",
              "                                          clean_title  \\\n",
              "89  Homogenization of Reynolds Equation by Two-Sca...   \n",
              "\n",
              "                                       clean_abstract  word_count  \n",
              "89  To increase the hydrodynamic performance in di...           7  "
            ]
          },
          "execution_count": 13,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "from sklearn.metrics.pairwise import cosine_similarity # menggunakan pairwise untuk menghitung kedekatan antar kata\n",
        "import numpy as np\n",
        "\n",
        "#def search(abstract)\n",
        "def search(abstract): # Membuat fungsi search\n",
        "    print(abstract)\n",
        "    abstract = clean_abstract(abstract) # Memanggil fungsi clean_abstract\n",
        "    query_vec = vectorizer.transform([abstract]) # Mengubah isi dataframe abstract menjadi vektor\n",
        "    similarity = cosine_similarity(query_vec, tfidf).flatten() # Perhitungan cosinus antara pencarian kata dengan dataset\n",
        "    indices = np.argpartition(similarity, -10)[-10:] # Mendapatkan 5 data terdekat dari hasil pencarian\n",
        "    results = jurnal.iloc[indices].iloc[::-10] # Menunjukan lokasi data bedasarkan indices\n",
        "\n",
        "    return results\n",
        "\n",
        "search('Despite decades of research, glioblastoma (GBM) remains invariably fatal among all forms of cancers.')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "metadata": {},
      "outputs": [],
      "source": [
        "import streamlit as st\n",
        "import pickle\n",
        "import requests\n",
        "\n",
        "st.title('Sistem Rekomendasi Jurnal')\n",
        "selected_journal_name = st.selectbox(\n",
        "     'Enter a name of the movie to get the suggestions',\n",
        "     ([\"Cancer\"]))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {},
      "outputs": [],
      "source": [
        "def add_bg_from_url():\n",
        "    st.markdown(\n",
        "         f\"\"\"\n",
        "         <style>\n",
        "         .stApp {{\n",
        "             background-image: url(\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR60O2-muWvwgWvwmzklx-IydP5j0NZsLnHpg&usqp=CAU\");\n",
        "             background-attachment: fixed;\n",
        "             background-size: cover\n",
        "         }}\n",
        "         </style>\n",
        "         \"\"\",\n",
        "         unsafe_allow_html=True\n",
        "     )"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 19,
      "metadata": {},
      "outputs": [],
      "source": [
        "add_bg_from_url()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "id": "634X3zecJkrU"
      },
      "outputs": [],
      "source": [
        "#jurnal.loc[1]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "id": "BYbYGeW_1FI0"
      },
      "outputs": [],
      "source": [
        "#https://www.kaggle.com/code/saddamazyazy/klasifikasi-rekomendasi-jurnal"
      ]
    }
  ],
  "metadata": {
    "accelerator": "GPU",
    "colab": {
      "gpuType": "T4",
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.10.12"
    },
    "widgets": {
      "application/vnd.jupyter.widget-state+json": {
        "0bc296fd1e1d420da036f6a7cd8ec60a": {
          "model_module": "@jupyter-widgets/controls",
          "model_module_version": "1.5.0",
          "model_name": "DescriptionStyleModel",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "DescriptionStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "description_width": ""
          }
        },
        "57cbb44b08ad48fb88495d4bf5a09bd2": {
          "model_module": "@jupyter-widgets/base",
          "model_module_version": "1.2.0",
          "model_name": "LayoutModel",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "59664960e51842d2971e32f7f1a0c347": {
          "model_module": "@jupyter-widgets/output",
          "model_module_version": "1.0.0",
          "model_name": "OutputModel",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/output",
            "_model_module_version": "1.0.0",
            "_model_name": "OutputModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/output",
            "_view_module_version": "1.0.0",
            "_view_name": "OutputView",
            "layout": "IPY_MODEL_57cbb44b08ad48fb88495d4bf5a09bd2",
            "msg_id": "",
            "outputs": []
          }
        },
        "c4e05d41fde24ee29a7f0080566cfedc": {
          "model_module": "@jupyter-widgets/controls",
          "model_module_version": "1.5.0",
          "model_name": "TextModel",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "TextModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "TextView",
            "continuous_update": true,
            "description": "jurnal Title:",
            "description_tooltip": null,
            "disabled": false,
            "layout": "IPY_MODEL_df7f3f1045494567b66bdb09df9d5af6",
            "placeholder": "​",
            "style": "IPY_MODEL_0bc296fd1e1d420da036f6a7cd8ec60a",
            "value": "Cancer and cure: A critical analysis"
          }
        },
        "df7f3f1045494567b66bdb09df9d5af6": {
          "model_module": "@jupyter-widgets/base",
          "model_module_version": "1.2.0",
          "model_name": "LayoutModel",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        }
      }
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
