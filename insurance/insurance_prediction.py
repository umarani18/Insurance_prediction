{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "88432414-b89d-4243-8b44-f4322f06f5a6",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: pandas in /home/umarani/.local/lib/python3.10/site-packages (2.2.3)\n",
      "Requirement already satisfied: tzdata>=2022.7 in /home/umarani/.local/lib/python3.10/site-packages (from pandas) (2025.1)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: numpy>=1.22.4 in /home/umarani/.local/lib/python3.10/site-packages (from pandas) (2.2.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in /usr/lib/python3/dist-packages (from pandas) (2022.1)\n",
      "Requirement already satisfied: six>=1.5 in /usr/lib/python3/dist-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n",
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: numpy in /home/umarani/.local/lib/python3.10/site-packages (2.2.2)\n",
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: matplotlib in /home/umarani/.local/lib/python3.10/site-packages (3.10.0)\n",
      "Requirement already satisfied: contourpy>=1.0.1 in /home/umarani/.local/lib/python3.10/site-packages (from matplotlib) (1.3.1)\n",
      "Requirement already satisfied: pillow>=8 in /usr/lib/python3/dist-packages (from matplotlib) (9.0.1)\n",
      "Requirement already satisfied: numpy>=1.23 in /home/umarani/.local/lib/python3.10/site-packages (from matplotlib) (2.2.2)\n",
      "Requirement already satisfied: fonttools>=4.22.0 in /home/umarani/.local/lib/python3.10/site-packages (from matplotlib) (4.56.0)\n",
      "Requirement already satisfied: python-dateutil>=2.7 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (2.9.0.post0)\n",
      "Requirement already satisfied: cycler>=0.10 in /home/umarani/.local/lib/python3.10/site-packages (from matplotlib) (0.12.1)\n",
      "Requirement already satisfied: kiwisolver>=1.3.1 in /home/umarani/.local/lib/python3.10/site-packages (from matplotlib) (1.4.8)\n",
      "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (24.2)\n",
      "Requirement already satisfied: pyparsing>=2.3.1 in /usr/lib/python3/dist-packages (from matplotlib) (2.4.7)\n",
      "Requirement already satisfied: six>=1.5 in /usr/lib/python3/dist-packages (from python-dateutil>=2.7->matplotlib) (1.16.0)\n",
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: seaborn in /home/umarani/.local/lib/python3.10/site-packages (0.13.2)\n",
      "Requirement already satisfied: numpy!=1.24.0,>=1.20 in /home/umarani/.local/lib/python3.10/site-packages (from seaborn) (2.2.2)\n",
      "Requirement already satisfied: pandas>=1.2 in /home/umarani/.local/lib/python3.10/site-packages (from seaborn) (2.2.3)\n",
      "Requirement already satisfied: matplotlib!=3.6.1,>=3.4 in /home/umarani/.local/lib/python3.10/site-packages (from seaborn) (3.10.0)\n",
      "Requirement already satisfied: kiwisolver>=1.3.1 in /home/umarani/.local/lib/python3.10/site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (1.4.8)\n",
      "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (24.2)\n",
      "Requirement already satisfied: fonttools>=4.22.0 in /home/umarani/.local/lib/python3.10/site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (4.56.0)\n",
      "Requirement already satisfied: pillow>=8 in /usr/lib/python3/dist-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (9.0.1)\n",
      "Requirement already satisfied: contourpy>=1.0.1 in /home/umarani/.local/lib/python3.10/site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (1.3.1)\n",
      "Requirement already satisfied: pyparsing>=2.3.1 in /usr/lib/python3/dist-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (2.4.7)\n",
      "Requirement already satisfied: cycler>=0.10 in /home/umarani/.local/lib/python3.10/site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (0.12.1)\n",
      "Requirement already satisfied: python-dateutil>=2.7 in /usr/local/lib/python3.10/dist-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in /usr/lib/python3/dist-packages (from pandas>=1.2->seaborn) (2022.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in /home/umarani/.local/lib/python3.10/site-packages (from pandas>=1.2->seaborn) (2025.1)\n",
      "Requirement already satisfied: six>=1.5 in /usr/lib/python3/dist-packages (from python-dateutil>=2.7->matplotlib!=3.6.1,>=3.4->seaborn) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install pandas\n",
    "!pip install numpy\n",
    "!pip install matplotlib\n",
    "!pip install seaborn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c7884f79-43e8-4754-a135-28506d2ac3fe",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "873043fe-b74c-4146-99d5-4ba5e604b589",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv('insurance.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1a6f54b8-61f1-4f49-9acc-d68036965569",
   "metadata": {},
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
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>bmi</th>\n",
       "      <th>children</th>\n",
       "      <th>smoker</th>\n",
       "      <th>region</th>\n",
       "      <th>expenses</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>19</td>\n",
       "      <td>female</td>\n",
       "      <td>27.9</td>\n",
       "      <td>0</td>\n",
       "      <td>yes</td>\n",
       "      <td>southwest</td>\n",
       "      <td>16884.92</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>18</td>\n",
       "      <td>male</td>\n",
       "      <td>33.8</td>\n",
       "      <td>1</td>\n",
       "      <td>no</td>\n",
       "      <td>southeast</td>\n",
       "      <td>1725.55</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>28</td>\n",
       "      <td>male</td>\n",
       "      <td>33.0</td>\n",
       "      <td>3</td>\n",
       "      <td>no</td>\n",
       "      <td>southeast</td>\n",
       "      <td>4449.46</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>33</td>\n",
       "      <td>male</td>\n",
       "      <td>22.7</td>\n",
       "      <td>0</td>\n",
       "      <td>no</td>\n",
       "      <td>northwest</td>\n",
       "      <td>21984.47</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>32</td>\n",
       "      <td>male</td>\n",
       "      <td>28.9</td>\n",
       "      <td>0</td>\n",
       "      <td>no</td>\n",
       "      <td>northwest</td>\n",
       "      <td>3866.86</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   age     sex   bmi  children smoker     region  expenses\n",
       "0   19  female  27.9         0    yes  southwest  16884.92\n",
       "1   18    male  33.8         1     no  southeast   1725.55\n",
       "2   28    male  33.0         3     no  southeast   4449.46\n",
       "3   33    male  22.7         0     no  northwest  21984.47\n",
       "4   32    male  28.9         0     no  northwest   3866.86"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4790a7d8-aa5d-46dc-b38f-189fc2ed1119",
   "metadata": {},
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
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>bmi</th>\n",
       "      <th>children</th>\n",
       "      <th>smoker</th>\n",
       "      <th>region</th>\n",
       "      <th>expenses</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1333</th>\n",
       "      <td>50</td>\n",
       "      <td>male</td>\n",
       "      <td>31.0</td>\n",
       "      <td>3</td>\n",
       "      <td>no</td>\n",
       "      <td>northwest</td>\n",
       "      <td>10600.55</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1334</th>\n",
       "      <td>18</td>\n",
       "      <td>female</td>\n",
       "      <td>31.9</td>\n",
       "      <td>0</td>\n",
       "      <td>no</td>\n",
       "      <td>northeast</td>\n",
       "      <td>2205.98</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1335</th>\n",
       "      <td>18</td>\n",
       "      <td>female</td>\n",
       "      <td>36.9</td>\n",
       "      <td>0</td>\n",
       "      <td>no</td>\n",
       "      <td>southeast</td>\n",
       "      <td>1629.83</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1336</th>\n",
       "      <td>21</td>\n",
       "      <td>female</td>\n",
       "      <td>25.8</td>\n",
       "      <td>0</td>\n",
       "      <td>no</td>\n",
       "      <td>southwest</td>\n",
       "      <td>2007.95</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1337</th>\n",
       "      <td>61</td>\n",
       "      <td>female</td>\n",
       "      <td>29.1</td>\n",
       "      <td>0</td>\n",
       "      <td>yes</td>\n",
       "      <td>northwest</td>\n",
       "      <td>29141.36</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      age     sex   bmi  children smoker     region  expenses\n",
       "1333   50    male  31.0         3     no  northwest  10600.55\n",
       "1334   18  female  31.9         0     no  northeast   2205.98\n",
       "1335   18  female  36.9         0     no  southeast   1629.83\n",
       "1336   21  female  25.8         0     no  southwest   2007.95\n",
       "1337   61  female  29.1         0    yes  northwest  29141.36"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "49694f81-2689-4728-ab60-5e529fa4f717",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1338, 7)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "d397dae9-6b1d-4da1-95d6-6234c7112bfc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1338 entries, 0 to 1337\n",
      "Data columns (total 7 columns):\n",
      " #   Column    Non-Null Count  Dtype  \n",
      "---  ------    --------------  -----  \n",
      " 0   age       1338 non-null   int64  \n",
      " 1   sex       1338 non-null   object \n",
      " 2   bmi       1338 non-null   float64\n",
      " 3   children  1338 non-null   int64  \n",
      " 4   smoker    1338 non-null   object \n",
      " 5   region    1338 non-null   object \n",
      " 6   expenses  1338 non-null   float64\n",
      "dtypes: float64(2), int64(2), object(3)\n",
      "memory usage: 73.3+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "cc1340bf-a761-473b-9842-cff6632d086c",
   "metadata": {},
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
       "      <th>age</th>\n",
       "      <th>bmi</th>\n",
       "      <th>children</th>\n",
       "      <th>expenses</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>1338.000000</td>\n",
       "      <td>1338.000000</td>\n",
       "      <td>1338.000000</td>\n",
       "      <td>1338.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>39.207025</td>\n",
       "      <td>30.665471</td>\n",
       "      <td>1.094918</td>\n",
       "      <td>13270.422414</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>14.049960</td>\n",
       "      <td>6.098382</td>\n",
       "      <td>1.205493</td>\n",
       "      <td>12110.011240</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>18.000000</td>\n",
       "      <td>16.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1121.870000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>27.000000</td>\n",
       "      <td>26.300000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>4740.287500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>39.000000</td>\n",
       "      <td>30.400000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>9382.030000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>51.000000</td>\n",
       "      <td>34.700000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>16639.915000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>64.000000</td>\n",
       "      <td>53.100000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>63770.430000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               age          bmi     children      expenses\n",
       "count  1338.000000  1338.000000  1338.000000   1338.000000\n",
       "mean     39.207025    30.665471     1.094918  13270.422414\n",
       "std      14.049960     6.098382     1.205493  12110.011240\n",
       "min      18.000000    16.000000     0.000000   1121.870000\n",
       "25%      27.000000    26.300000     0.000000   4740.287500\n",
       "50%      39.000000    30.400000     1.000000   9382.030000\n",
       "75%      51.000000    34.700000     2.000000  16639.915000\n",
       "max      64.000000    53.100000     5.000000  63770.430000"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "f9a5fadc-ce51-4205-b767-487d40b009a5",
   "metadata": {},
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
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>bmi</th>\n",
       "      <th>children</th>\n",
       "      <th>smoker</th>\n",
       "      <th>region</th>\n",
       "      <th>expenses</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>1338.000000</td>\n",
       "      <td>1338</td>\n",
       "      <td>1338.000000</td>\n",
       "      <td>1338.000000</td>\n",
       "      <td>1338</td>\n",
       "      <td>1338</td>\n",
       "      <td>1338.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unique</th>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>top</th>\n",
       "      <td>NaN</td>\n",
       "      <td>male</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>no</td>\n",
       "      <td>southeast</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>freq</th>\n",
       "      <td>NaN</td>\n",
       "      <td>676</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1064</td>\n",
       "      <td>364</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>39.207025</td>\n",
       "      <td>NaN</td>\n",
       "      <td>30.665471</td>\n",
       "      <td>1.094918</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>13270.422414</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>14.049960</td>\n",
       "      <td>NaN</td>\n",
       "      <td>6.098382</td>\n",
       "      <td>1.205493</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>12110.011240</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>18.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>16.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1121.870000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>27.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>26.300000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4740.287500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>39.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>30.400000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>9382.030000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>51.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>34.700000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>16639.915000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>64.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>53.100000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>63770.430000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                age   sex          bmi     children smoker     region  \\\n",
       "count   1338.000000  1338  1338.000000  1338.000000   1338       1338   \n",
       "unique          NaN     2          NaN          NaN      2          4   \n",
       "top             NaN  male          NaN          NaN     no  southeast   \n",
       "freq            NaN   676          NaN          NaN   1064        364   \n",
       "mean      39.207025   NaN    30.665471     1.094918    NaN        NaN   \n",
       "std       14.049960   NaN     6.098382     1.205493    NaN        NaN   \n",
       "min       18.000000   NaN    16.000000     0.000000    NaN        NaN   \n",
       "25%       27.000000   NaN    26.300000     0.000000    NaN        NaN   \n",
       "50%       39.000000   NaN    30.400000     1.000000    NaN        NaN   \n",
       "75%       51.000000   NaN    34.700000     2.000000    NaN        NaN   \n",
       "max       64.000000   NaN    53.100000     5.000000    NaN        NaN   \n",
       "\n",
       "            expenses  \n",
       "count    1338.000000  \n",
       "unique           NaN  \n",
       "top              NaN  \n",
       "freq             NaN  \n",
       "mean    13270.422414  \n",
       "std     12110.011240  \n",
       "min      1121.870000  \n",
       "25%      4740.287500  \n",
       "50%      9382.030000  \n",
       "75%     16639.915000  \n",
       "max     63770.430000  "
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe(include='all')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "042f9061-7da0-46b8-9a93-c386a7daa288",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "age         0\n",
       "sex         0\n",
       "bmi         0\n",
       "children    0\n",
       "smoker      0\n",
       "region      0\n",
       "expenses    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#misiing values\n",
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a5538f4b-9704-4e9d-8717-9fa958099a99",
   "metadata": {},
   "outputs": [],
   "source": [
    "#check duplicate\n",
    "df=df.drop_duplicates()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "6f0a8e31-26ef-4719-97bd-dd03b02f4715",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1337, 7)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4770fc3e-5c9f-4b8d-a474-423821ef7718",
   "metadata": {},
   "source": [
    "**_Data analysis_**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f9fe8cae-d09e-41c8-a130-e8f2d5fa7211",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/tmp/ipykernel_6117/3555010618.py:4: UserWarning: \n",
      "\n",
      "`distplot` is a deprecated function and will be removed in seaborn v0.14.0.\n",
      "\n",
      "Please adapt your code to use either `displot` (a figure-level function with\n",
      "similar flexibility) or `histplot` (an axes-level function for histograms).\n",
      "\n",
      "For a guide to updating your code to use the new functions, please see\n",
      "https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751\n",
      "\n",
      "  sns.distplot(df[x],ax=axes[0],kde=False)\n",
      "/tmp/ipykernel_6117/3555010618.py:4: UserWarning: \n",
      "\n",
      "`distplot` is a deprecated function and will be removed in seaborn v0.14.0.\n",
      "\n",
      "Please adapt your code to use either `displot` (a figure-level function with\n",
      "similar flexibility) or `histplot` (an axes-level function for histograms).\n",
      "\n",
      "For a guide to updating your code to use the new functions, please see\n",
      "https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751\n",
      "\n",
      "  sns.distplot(df[x],ax=axes[0],kde=False)\n",
      "/tmp/ipykernel_6117/3555010618.py:4: UserWarning: \n",
      "\n",
      "`distplot` is a deprecated function and will be removed in seaborn v0.14.0.\n",
      "\n",
      "Please adapt your code to use either `displot` (a figure-level function with\n",
      "similar flexibility) or `histplot` (an axes-level function for histograms).\n",
      "\n",
      "For a guide to updating your code to use the new functions, please see\n",
      "https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751\n",
      "\n",
      "  sns.distplot(df[x],ax=axes[0],kde=False)\n",
      "/tmp/ipykernel_6117/3555010618.py:4: UserWarning: \n",
      "\n",
      "`distplot` is a deprecated function and will be removed in seaborn v0.14.0.\n",
      "\n",
      "Please adapt your code to use either `displot` (a figure-level function with\n",
      "similar flexibility) or `histplot` (an axes-level function for histograms).\n",
      "\n",
      "For a guide to updating your code to use the new functions, please see\n",
      "https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751\n",
      "\n",
      "  sns.distplot(df[x],ax=axes[0],kde=False)\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAz8AAAFzCAYAAAAQULd9AAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAIlZJREFUeJzt3X90V/V9P/BXQiBEIYlBSUgFhFVFKiCFFnPUzQlHQMe0clq1rMdSj5y60FWzrZbN4o+2w1m3dvagTNupPZXauh3t8KxYBhVrCyg4/F0GlHPAQUKBkQDFEM39/tH5+fZD4o9IyAfyfjzOuefwue937ud13yfkxZN7PzdFWZZlAQAA0MsVF7oAAACAniD8AAAASRB+AACAJAg/AABAEoQfAAAgCcIPAACQBOEHAABIgvADAAAkoaTQBXwQ7e3tsX379hg4cGAUFRUVuhyAZGRZFvv27Yva2tooLvb/Z79PbwIojK70puMy/Gzfvj2GDh1a6DIAkrVt27Y49dRTC13GMUVvAiis99ObjsvwM3DgwIj43QmWl5cXuBqAdLS0tMTQoUNzP4f5//QmgMLoSm86LsPP27cTlJeXazAABeC2ro70JoDCej+9yQ3bAABAEoQfAAAgCcIPAACQBOEHAABIgvADAAAkQfgBAACSIPwAAABJEH4AAIAkCD8AAEAShB8AACAJwg8AAJCEkkIXUCiL12zt8ff89KRhPf6eAADA77jyAwAAJEH4AQAAkiD8AAAASRB+AACAJAg/AABAEoQfAAAgCcIPAACQBOEHAABIgvADAAAkQfgBAACSIPwAAABJEH4AAIAkCD8AAEAShB8AACAJwg8AAJCEkkIXAACkrbm5OQ4ePFjoMqBTZWVlUVFRUegy6CbCDwBQMM3NzXH/ffdF25tvFroU6FTfkpK4bs4cAaiXEH4AgII5ePBgtL35ZkwbPS6qThxQ6HKOe3sO7I+lr75gPbvJ2+t58OBB4aeXEH4AgIKrOnFAVA/0j8vuYj2hcx54AAAAJEH4AQAAkiD8AAAASRB+AACAJHQp/CxYsCA+9rGPxcCBA2Pw4MFx+eWXx4YNG/LmvPHGG1FfXx+DBg2KAQMGxMyZM6OpqSlvztatW+PSSy+NE044IQYPHhx//dd/HW96xCUAAHAUdSn8rFy5Murr62P16tWxbNmyaGtri4svvjgOHDiQm3PjjTfGkiVL4tFHH42VK1fG9u3b44orrsiNv/XWW3HppZfGoUOH4pe//GU89NBD8eCDD8b8+fO776wAAAAO06VHXS9dujTv9YMPPhiDBw+OdevWxR/+4R9Gc3NzfPe7343FixfHRRddFBERDzzwQJx11lmxevXqOPfcc+OnP/1pvPrqq/Gf//mfUV1dHeecc0589atfjZtuuiluvfXW6NevX/edHQAAwP85os/8NDc3R0REVVVVRESsW7cu2traYsqUKbk5o0aNimHDhsWqVasiImLVqlUxZsyYqK6uzs2ZOnVqtLS0xCuvvNLp+7S2tkZLS0veBgAA0BUfOPy0t7fHDTfcEOedd16cffbZERHR2NgY/fr1i8rKyry51dXV0djYmJvz+8Hn7fG3xzqzYMGCqKioyG1Dhw79oGUDAACJ+sDhp76+Pl5++eV45JFHurOeTs2bNy+am5tz27Zt2476ewIAAL1Llz7z87a5c+fGE088EU8//XSceuqpuf01NTVx6NCh2Lt3b97Vn6ampqipqcnNefbZZ/OO9/bT4N6ec7jS0tIoLS39IKUCAABERBev/GRZFnPnzo3HHnssVqxYESNGjMgbnzBhQvTt2zeWL1+e27dhw4bYunVr1NXVRUREXV1dvPTSS7Fz587cnGXLlkV5eXmMHj36SM4FAADgHXXpyk99fX0sXrw4fvzjH8fAgQNzn9GpqKiIsrKyqKioiGuvvTYaGhqiqqoqysvL4wtf+ELU1dXFueeeGxERF198cYwePTo+85nPxJ133hmNjY1x8803R319vas7AADAUdOl8HPvvfdGRMSFF16Yt/+BBx6Iz372sxER8c1vfjOKi4tj5syZ0draGlOnTo177rknN7dPnz7xxBNPxPXXXx91dXVx4oknxjXXXBO33377kZ0JAADAu+hS+Mmy7D3n9O/fPxYuXBgLFy58xznDhw+P//iP/+jKWwMAAByRI/o9PwAAAMcL4QcAAEiC8AMAACRB+AEAAJIg/AAAAEkQfgAAgCQIPwAAQBKEHwAAIAnCDwAAkAThBwAASILwAwAAJEH4AQAAkiD8AAAASRB+AACAJAg/AABAEoQfAAAgCcIPAACQBOEHAABIgvADAAAkQfgBAACSIPwAAABJEH4AAIAkCD8AAEAShB8AACAJwg8AAJAE4QcAAEiC8AMAACRB+AEA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p7gmh7vjjjuiqKgobrjhhty+FNfl1ltvjaKiorxt1KhRufEU1+Rt//M//xN/9md/FoMGDYqysrIYM2ZMrF27NjeeZVnMnz8/hgwZEmVlZTFlypTYuHFjASvmWKE3dU5vem960+/oTZ1LsS8JP4dZuXJl1NfXx+rVq2PZsmXR1tYWF198cRw4cCA358Ybb4wlS5bEo48+GitXrozt27fHFVdcUcCqj75TTz017rjjjli3bl2sXbs2LrroorjsssvilVdeiYg01+T3Pffcc/HP//zPMXbs2Lz9qa7LRz7ykdixY0due+aZZ3Jjqa7J//7v/8Z5550Xffv2jZ/85Cfx6quvxj/8wz/ESSedlJtz5513xt133x2LFi2KNWvWxIknnhhTp06NN954o4CVcyzQmzqnN707vSmf3pQv2b6U8a527tyZRUS2cuXKLMuybO/evVnfvn2zRx99NDfntddeyyIiW7VqVaHKLIiTTjop+853vpP8muzbty87/fTTs2XLlmV/9Ed/lH3xi1/Msizd75VbbrklGzduXKdjqa5JlmXZTTfdlJ1//vnvON7e3p7V1NRk3/jGN3L79u7dm5WWlmY/+MEPeqJEjiN60zvTm35Hb8qnN3WUal9y5ec9NDc3R0REVVVVRESsW7cu2traYsqUKbk5o0aNimHDhsWqVasKUmNPe+utt+KRRx6JAwcORF1dXfJrUl9fH5deemne+Uek/b2ycePGqK2tjZEjR8asWbNi69atEZH2mvz7v/97TJw4MT75yU/G4MGDY/z48XH//ffnxrds2RKNjY15a1NRURGTJk3q9WtD1+lNHelN+fSmjvSmfKn2JeHnXbS3t8cNN9wQ5513Xpx99tkREdHY2Bj9+vWLysrKvLnV1dXR2NhYgCp7zksvvRQDBgyI0tLS+PznPx+PPfZYjB49Ouk1eeSRR+L555+PBQsWdBhLdV0mTZoUDz74YCxdujTuvffe2LJlS1xwwQWxb9++ZNckIuLXv/513HvvvXH66afHk08+Gddff338xV/8RTz00EMREbnzr66uzvu6FNaGrtGb8ulNHelNHelNHaXal0oKXcCxrL6+Pl5++eW8e0JTduaZZ8b69eujubk5/vVf/zWuueaaWLlyZaHLKpht27bFF7/4xVi2bFn079+/0OUcM6ZPn57789ixY2PSpEkxfPjw+NGP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",
      "text/plain": [
       "<Figure size 1000x400 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 1000x400 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 1000x400 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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SzPR0dHmxIkTrWoexnx1e9eAgADzq1/9yhw6dMi89tprJiQkxPzpT3+y+rSm9z+8h7XJe3+bbWldMqZtr02tdV0yhrWppb7/m6LNhh9jjHnxxRdNly5dTFBQkBk2bJjZuXPnFT3+1q1bjaQ6j2nTphljvrql4C9+8QsTFxdnnE6nGTVqlMnNzXUb4/Tp02bKlCmmQ4cOJiwszPzwhz80Z8+edevz6aefmhtvvNE4nU7TqVMns2jRojq1vP7666Znz54mKCjI9O3b16xfv96judQ3D0lm+fLlVp/z58+b//zP/zQdO3Y0ISEh5o477jDHjx93G+fw4cNm7NixJjg42ERHR5tHH33UVFdX13ndrr32WhMUFGSuuuoqt2PUasrv9v777zddu3Y1QUFBJiYmxowaNcpaXFrTPBryzUWmtczn7rvvNgkJCSYoKMh06tTJ3H333W7fPdBa5lHr7bffNv369TNOp9P07t3bvPzyy27tren9D+9ibfq3pvxttqV1yZi2vTa11nXJGNamlvr+bwqHMcb4/vwSAAAAADSvNnnNDwAAAAB8E+EHAAAAgC0QfgAAAADYAuEHAAAAgC0QfgAAAADYAuEHAAAAgC0QfgAAAADYAuEHAAAAgC0QfgAAAADYAuEHAAAAgC0QfmBbLpdLmZmZ6tatm4KDgzVw4EC98cYbMsYoLS1No0ePljFGklRSUqLOnTvrqaeekiRt27ZNDodD69ev14ABA9SuXTtdf/312rdvn9sx3n//fd10000KDg5WUlKSHn74YVVUVFjtycnJeuaZZ3T//fcrNDRUXbp00csvv2y1V1VVac6cOUpISFC7du3UtWtXZWZmWu1nzpzRj370I8XExCgsLEwjR47Up59+arV/+umnGjFihEJDQxUWFqYhQ4Zo9+7dPnk9AQBNx9oE+JgBbOqXv/yl6d27t9m4caPJz883y5cvN06n02zbts0cPXrUdOzY0SxevNgYY8ydd95phg0bZqqrq40xxmzdutVIMn369DF///vfzd69e813v/tdk5ycbKqqqowxxuTl5Zn27dubF154wRw8eNB88MEHZtCgQWb69OlWDV27djWRkZFmyZIl5tChQyYzM9P4+fmZL774whhjzHPPPWeSkpLMjh07zOHDh817771nVq5cae2flpZmJkyYYHbt2mUOHjxoHn30URMVFWVOnz5tjDGmb9++5r777jMHDhwwBw8eNK+//rrJycm5Iq8vAMBzrE2AbxF+YEsXLlwwISEh5sMPP3TbPmPGDDNlyhRjjDGvv/66adeunXniiSdM+/btzcGDB61+tQvMqlWrrG2nT582wcHB5i9/+Ys11qxZs9zGf++994yfn585f/68MearBea+++6z2l0ul4mNjTVLly41xhgzd+5cM3LkSONyuerM4b333jNhYWHmwoULbtu7d+9ufve73xljjAkNDTUrVqzw7MUBADQL1ibA9wKa97wT0Dzy8vJ07tw53XLLLW7bq6qqNGjQIEnSnXfeqTfffFOLFi3S0qVLdfXVV9cZJzU11fo5MjJSvXr10oEDByR9dVp/7969eu2116w+xhi5XC4VFBSoT58+kqQBAwZY7Q6HQ/Hx8Tpx4oQkafr06brlllvUq1cvjRkzRt/97nd16623WuOXl5crKirKrabz588rPz9fkpSenq4f/ehHevXVV5WWlqY777xT3bt3b9yLBgDwKdYmwPcIP7Cl8vJySdL69evVqVMntzan0ylJOnfunPbs2SN/f38dOnSoUcd44IEH9PDDD9dp69Kli/VzYGCgW5vD4ZDL5ZIkDR48WAUFBdqwYYPeffdd3XXXXUpLS9Mbb7yh8vJyJSQkaNu2bXXGj4iIkCQ9/fTTuvfee7V+/Xpt2LBB8+fP16pVq3THHXd4PB8AgG+xNrE2wfcIP7Cla665Rk6nU4WFhfrOd75Tb59HH31Ufn5+2rBhg8aNG6fx48dr5MiRbn127txpLRZffvmlDh48aP1fs8GDB2v//v3q0aNHk2oNCwvT3XffrbvvvluTJ0/WmDFjVFJSosGDB6uoqEgBAQFKTk5ucP+ePXuqZ8+emjdvnqZMmaLly5ezwABAC8TaxNoE3yP8wJZCQ0P1k5/8RPPmzZPL5dKNN96o0tJSffDBBwoLC1N0dLReeeUVZWVlafDgwXrsscc0bdo07d27Vx07drTGWbhwoaKiohQXF6ef//znio6O1u233y5Jevzxx3X99ddrzpw5+tGPfqT27dtr//792rRpk377299eVp3PP/+8EhISNGjQIPn5+Wn16tWKj49XRESE0tLSlJqaqttvv13PPvusevbsqWPHjmn9+vW644471LdvXz322GOaPHmyunXrpqNHj2rXrl2aNGmSL15SAEATsTYBV0BzX3QENBeXy2UWL15sevXqZQIDA01MTIwZPXq02bZtm4mLizPPPPOM1beqqsoMGTLE3HXXXcaYf19U+vbbb5u+ffuaoKAgM2zYMPPpp5+6HeOjjz4yt9xyi+nQoYNp3769GTBggPnVr35ltXft2tW88MILbvsMHDjQzJ8/3xhjzMsvv2yuvfZa0759exMWFmZGjRplPv74Y6tvWVmZmTt3rklMTDSBgYEmKSnJTJ061RQWFprKykpzzz33mKSkJBMUFGQSExPNnDlzrAtaAQAtD2sT4FsOY/7/zeIBXLZt27ZpxIgR+vLLL63PMAMA0JxYm4Bvx5ecAgAAALAFwg8AAAAAW+BjbwAAAABsgTM/AAAAAGyB8AMAAADAFgg/AAAAAGyB8AMAAADAFgg/AAAAAGyB8AMAAADAFgg/AAAAAGyB8AMAAADAFgg/AAAAAGzh/wHlKriQvZ5bcAAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 1000x400 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "x_axis=['age','bmi','children','expenses']\n",
    "for x in x_axis:\n",
    "  fig, axes=plt.subplots(1,2, figsize=(10,4))\n",
    "  sns.distplot(df[x],ax=axes[0],kde=False)\n",
    "  sns.boxplot(df[x],ax=axes[1],orient=\"h\",showmeans=True,color=\"pink\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "160d464d-c359-472a-9c29-368b9a05c9dc",
   "metadata": {},
   "source": [
    "**Handle categorical problem**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "544dfd84-2d69-4655-94cc-c365ae007395",
   "metadata": {},
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
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>bmi</th>\n",
       "      <th>children</th>\n",
       "      <th>smoker</th>\n",
       "      <th>region</th>\n",
       "      <th>expenses</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>19</td>\n",
       "      <td>female</td>\n",
       "      <td>27.9</td>\n",
       "      <td>0</td>\n",
       "      <td>yes</td>\n",
       "      <td>southwest</td>\n",
       "      <td>16884.92</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>18</td>\n",
       "      <td>male</td>\n",
       "      <td>33.8</td>\n",
       "      <td>1</td>\n",
       "      <td>no</td>\n",
       "      <td>southeast</td>\n",
       "      <td>1725.55</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>28</td>\n",
       "      <td>male</td>\n",
       "      <td>33.0</td>\n",
       "      <td>3</td>\n",
       "      <td>no</td>\n",
       "      <td>southeast</td>\n",
       "      <td>4449.46</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>33</td>\n",
       "      <td>male</td>\n",
       "      <td>22.7</td>\n",
       "      <td>0</td>\n",
       "      <td>no</td>\n",
       "      <td>northwest</td>\n",
       "      <td>21984.47</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>32</td>\n",
       "      <td>male</td>\n",
       "      <td>28.9</td>\n",
       "      <td>0</td>\n",
       "      <td>no</td>\n",
       "      <td>northwest</td>\n",
       "      <td>3866.86</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   age     sex   bmi  children smoker     region  expenses\n",
       "0   19  female  27.9         0    yes  southwest  16884.92\n",
       "1   18    male  33.8         1     no  southeast   1725.55\n",
       "2   28    male  33.0         3     no  southeast   4449.46\n",
       "3   33    male  22.7         0     no  northwest  21984.47\n",
       "4   32    male  28.9         0     no  northwest   3866.86"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "06703b9e-d161-4d67-8810-7d27f2e2a1ae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['female', 'male'], dtype=object)"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.sex.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "968ede7e-c451-47d7-ab01-c17f9323f507",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['sex'] = df.sex.map({'male':1,'female':0})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "0284b8e8-4337-4918-a909-21eb2c578edb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['yes', 'no'], dtype=object)"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.smoker.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "87ce396a-e23d-4114-aa5b-26f73a825023",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['smoker']=df.smoker.map({'yes':1,'no':0})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "471bf326-4804-40cd-bd26-70679fd72005",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['southwest', 'southeast', 'northwest', 'northeast'], dtype=object)"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.region.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "baba7734-5196-40fd-9e4c-836fcd3a637c",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['region']=df.region.map({'southwest':1,'southeast':2,'northwest':3,'northeast':4})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "b3c988c7-66c2-4363-b682-f899b50227af",
   "metadata": {},
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
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>bmi</th>\n",
       "      <th>children</th>\n",
       "      <th>smoker</th>\n",
       "      <th>region</th>\n",
       "      <th>expenses</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>19</td>\n",
       "      <td>0</td>\n",
       "      <td>27.9</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>16884.92</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>18</td>\n",
       "      <td>1</td>\n",
       "      <td>33.8</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>1725.55</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>28</td>\n",
       "      <td>1</td>\n",
       "      <td>33.0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>4449.46</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>33</td>\n",
       "      <td>1</td>\n",
       "      <td>22.7</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>21984.47</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>32</td>\n",
       "      <td>1</td>\n",
       "      <td>28.9</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>3866.86</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   age  sex   bmi  children  smoker  region  expenses\n",
       "0   19    0  27.9         0       1       1  16884.92\n",
       "1   18    1  33.8         1       0       2   1725.55\n",
       "2   28    1  33.0         3       0       2   4449.46\n",
       "3   33    1  22.7         0       0       3  21984.47\n",
       "4   32    1  28.9         0       0       3   3866.86"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f2b90643-def6-4fa4-a3c2-ca200b7d5368",
   "metadata": {},
   "source": [
    "**Split the dataset**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "a42be287-4dce-477f-8ca6-de63482010fa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'expenses'], dtype='object')"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "f836b04f-86a1-4d6c-beb0-46d1a45ca50c",
   "metadata": {},
   "outputs": [],
   "source": [
    "x=df.drop(['expenses'],axis=1)\n",
    "y=df['expenses']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "cc592253-d6f4-4d61-84fa-7a205e838098",
   "metadata": {},
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
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>bmi</th>\n",
       "      <th>children</th>\n",
       "      <th>smoker</th>\n",
       "      <th>region</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>19</td>\n",
       "      <td>0</td>\n",
       "      <td>27.9</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>18</td>\n",
       "      <td>1</td>\n",
       "      <td>33.8</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>28</td>\n",
       "      <td>1</td>\n",
       "      <td>33.0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>33</td>\n",
       "      <td>1</td>\n",
       "      <td>22.7</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>32</td>\n",
       "      <td>1</td>\n",
       "      <td>28.9</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   age  sex   bmi  children  smoker  region\n",
       "0   19    0  27.9         0       1       1\n",
       "1   18    1  33.8         1       0       2\n",
       "2   28    1  33.0         3       0       2\n",
       "3   33    1  22.7         0       0       3\n",
       "4   32    1  28.9         0       0       3"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "0c85081f-35e8-4f96-a222-00d88fd41e73",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    16884.92\n",
       "1     1725.55\n",
       "2     4449.46\n",
       "3    21984.47\n",
       "4     3866.86\n",
       "Name: expenses, dtype: float64"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6e321671-f81b-451b-92d8-8fd9e82f18b2",
   "metadata": {},
   "source": [
    "**Train test split**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "c9623fe8-0c1f-4ccc-bc2a-23512f719093",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: scikit-learn in /home/umarani/.local/lib/python3.10/site-packages (1.6.1)\n",
      "Requirement already satisfied: threadpoolctl>=3.1.0 in /home/umarani/.local/lib/python3.10/site-packages (from scikit-learn) (3.5.0)\n",
      "Requirement already satisfied: joblib>=1.2.0 in /home/umarani/.local/lib/python3.10/site-packages (from scikit-learn) (1.4.2)\n",
      "Requirement already satisfied: numpy>=1.19.5 in /home/umarani/.local/lib/python3.10/site-packages (from scikit-learn) (2.2.2)\n",
      "Requirement already satisfied: scipy>=1.6.0 in /home/umarani/.local/lib/python3.10/site-packages (from scikit-learn) (1.15.1)\n"
     ]
    }
   ],
   "source": [
    "!pip install scikit-learn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "fd783daf-0b1f-4f9f-8246-5d829d49e008",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "eaddb7f4-d29c-4490-b91d-88520dc4a0a9",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "68a1c227-5da5-4ff2-8540-f0114659bb6a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1069, 6)"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_train.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "d159c3f7-36bc-4685-b382-98982e75a447",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(268, 6)"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_test.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "96f29329-b82c-45e7-8470-1e3bdd671c28",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8808240302683835"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Random forest regressor\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "rf=RandomForestRegressor()\n",
    "rf.fit(x_train,y_train)\n",
    "y_pred3=rf.predict(x_test)\n",
    "from sklearn.metrics import r2_score\n",
    "r2_score(y_test,y_pred3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "31efe3f5-8f6a-4730-959e-e3731147f36b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['insurance_model.pkl']"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import joblib\n",
    "joblib.dump(rf,'insurance_model.pkl')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c5e6f087-11aa-4b09-8189-e17492183314",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
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
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
