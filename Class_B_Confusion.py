{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Class B - Confusion",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyP9eUqe38P3iy39dPphYphp",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Divyah-sys/google-form-to-analysis/blob/main/Class_B_Confusion.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 44,
      "metadata": {
        "id": "x-gxt6Au0AP8"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "Confusion = [2,2,1,1,0,1,3,2,3,2,1,2,1,1,1,1,1,0,0,0,3,0,2,0,0,0,0,2,3,3,0,3,1,1,3,0,0,0,0,0,1,1,1,2,1,1,0,1,2,0,0,2,2,2,2,2,2,0,2,2,2,2,2,3,2,1,1,2,2,2,2,2,2,3,3,2,3,1,3,3,1,2,3,2,2,3,3,3,3,3,3,3,1,1,2,2,1,2,3,2,1,3,2,0,0,3,3,1,1,0,1,1,1,1,2,2,0,1,0,2,0,0,0,0,1,0,1,3,3,1,1,2,1,2,2,3,1,2,1,1,0,0,0,1,2,1,0,2,1,1]"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "mean=np.mean(Confusion)\n",
        "mean"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7_ipxBwV1_4b",
        "outputId": "a13be7aa-9483-4096-ece0-9e3aec363d59"
      },
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1.4533333333333334"
            ]
          },
          "metadata": {},
          "execution_count": 45
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "median=np.median(Confusion)\n",
        "median"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "a0iSHqHi2IOJ",
        "outputId": "0d2a60d8-adac-4a26-ac9f-1354b0264b36"
      },
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1.0"
            ]
          },
          "metadata": {},
          "execution_count": 46
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import statistics as stats\n",
        "stats.mode(Confusion)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Z6dgQy_sSQBw",
        "outputId": "93ba0c7f-fe2b-41a2-e7c8-da3e54bc66f9"
      },
      "execution_count": 47,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2"
            ]
          },
          "metadata": {},
          "execution_count": 47
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "np.var(Confusion)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "E_DdDi917bez",
        "outputId": "17fd7adb-a784-4a6c-d30d-b79e5cbc3265"
      },
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1.0611555555555552"
            ]
          },
          "metadata": {},
          "execution_count": 48
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "std=np.std(Confusion)\n",
        "std"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e-ol_3h779EW",
        "outputId": "e6ef724d-497b-4828-e296-09beee6fea2d"
      },
      "execution_count": 49,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1.030124048624997"
            ]
          },
          "metadata": {},
          "execution_count": 49
        }
      ]
    }
  ]
}