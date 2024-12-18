# Aircrah analysis app
This app basically acts as an interface to display the analysis done using the airline crashes dataset which captures
aircrashes recorded from 1908-2023. This would provide insights to determine possible factors which could have contibuted to it as well as recommendations to enhance air travel safety

{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# PYTHON PROJECT WORK"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Making use of the Aircrahes dataset to make analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 312,
   "metadata": {},
   "outputs": [],
   "source": [
    "# import the necessary libraries\n",
    "\n",
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 313,
   "metadata": {},
   "outputs": [],
   "source": [
    "# load the dataset by defining a function\n",
    "\n",
    "def load_data():\n",
    "    file = 'C:/Users/HP/Data_Apps/Aircrashes_App/Air__Crash.xlsx'\n",
    "    df = pd.read_excel(file)\n",
    "    return df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 314,
   "metadata": {},
   "outputs": [],
   "source": [
    "# load the data\n",
    "df = load_data()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 315,
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
       "      <th>Crash Date</th>\n",
       "      <th>Country/Region</th>\n",
       "      <th>Aircraft Manufacturer</th>\n",
       "      <th>Aircraft</th>\n",
       "      <th>Location</th>\n",
       "      <th>Operator</th>\n",
       "      <th>Sum of Fatalities(ground)</th>\n",
       "      <th>Sum of Fatalities (air)</th>\n",
       "      <th>Sum of Aboard</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1908-09-17</td>\n",
       "      <td>Virgin Islandsia</td>\n",
       "      <td>Wright Flyer</td>\n",
       "      <td>Wright Flyer III?</td>\n",
       "      <td>Fort Myer Virgin Islandsia</td>\n",
       "      <td>U.S. Army - Military</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1909-09-07</td>\n",
       "      <td>France?</td>\n",
       "      <td>Wright</td>\n",
       "      <td>Wright ByplaneSC1</td>\n",
       "      <td>Juvisy-sur-Orge France</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1912-07-12</td>\n",
       "      <td>U.S.A.</td>\n",
       "      <td>Dirigible?</td>\n",
       "      <td>Dirigible?</td>\n",
       "      <td>Atlantic City New Jersey</td>\n",
       "      <td>US Navy - Military</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1913-08-06</td>\n",
       "      <td>British</td>\n",
       "      <td>Curtiss</td>\n",
       "      <td>Curtiss seaplane?</td>\n",
       "      <td>Victoria British</td>\n",
       "      <td>Canada          Columbia Private</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1913-09-09</td>\n",
       "      <td>North Sea</td>\n",
       "      <td>Zeppelin</td>\n",
       "      <td>Zeppelin L 1 (airship)?</td>\n",
       "      <td>Over the North Sea</td>\n",
       "      <td>German Navy - Military</td>\n",
       "      <td>0</td>\n",
       "      <td>14</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Crash Date    Country/Region Aircraft Manufacturer                 Aircraft  \\\n",
       "0 1908-09-17  Virgin Islandsia          Wright Flyer        Wright Flyer III?   \n",
       "1 1909-09-07           France?                Wright        Wright ByplaneSC1   \n",
       "2 1912-07-12            U.S.A.            Dirigible?               Dirigible?   \n",
       "3 1913-08-06           British               Curtiss        Curtiss seaplane?   \n",
       "4 1913-09-09         North Sea              Zeppelin  Zeppelin L 1 (airship)?   \n",
       "\n",
       "                     Location                          Operator  \\\n",
       "0  Fort Myer Virgin Islandsia              U.S. Army - Military   \n",
       "1      Juvisy-sur-Orge France                               NaN   \n",
       "2    Atlantic City New Jersey                US Navy - Military   \n",
       "3            Victoria British  Canada          Columbia Private   \n",
       "4          Over the North Sea            German Navy - Military   \n",
       "\n",
       "  Sum of Fatalities(ground)  Sum of Fatalities (air)  Sum of Aboard  \n",
       "0                         0                        1              2  \n",
       "1                         0                        1              1  \n",
       "2                         0                        5              5  \n",
       "3                         0                        1              1  \n",
       "4                         0                       14             20  "
      ]
     },
     "execution_count": 315,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# show the table\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 316,
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
       "      <th>Crash Date</th>\n",
       "      <th>Sum of Fatalities (air)</th>\n",
       "      <th>Sum of Aboard</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>4991</td>\n",
       "      <td>4991.000000</td>\n",
       "      <td>4991.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>1971-06-11 06:11:02.151873376</td>\n",
       "      <td>22.208976</td>\n",
       "      <td>30.924464</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1908-09-17 00:00:00</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>1951-05-02 00:00:00</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>6.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>1970-08-26 00:00:00</td>\n",
       "      <td>11.000000</td>\n",
       "      <td>16.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>1992-04-24 00:00:00</td>\n",
       "      <td>25.000000</td>\n",
       "      <td>34.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>2023-09-16 00:00:00</td>\n",
       "      <td>583.000000</td>\n",
       "      <td>644.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>NaN</td>\n",
       "      <td>34.944368</td>\n",
       "      <td>45.355400</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                          Crash Date  Sum of Fatalities (air)  Sum of Aboard\n",
       "count                           4991              4991.000000    4991.000000\n",
       "mean   1971-06-11 06:11:02.151873376                22.208976      30.924464\n",
       "min              1908-09-17 00:00:00                 0.000000       0.000000\n",
       "25%              1951-05-02 00:00:00                 4.000000       6.000000\n",
       "50%              1970-08-26 00:00:00                11.000000      16.000000\n",
       "75%              1992-04-24 00:00:00                25.000000      34.000000\n",
       "max              2023-09-16 00:00:00               583.000000     644.000000\n",
       "std                              NaN                34.944368      45.355400"
      ]
     },
     "execution_count": 316,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# do a quick summary statistics check\n",
    "\n",
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 317,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 4991 entries, 0 to 4990\n",
      "Data columns (total 9 columns):\n",
      " #   Column                     Non-Null Count  Dtype         \n",
      "---  ------                     --------------  -----         \n",
      " 0   Crash Date                 4991 non-null   datetime64[ns]\n",
      " 1   Country/Region             4983 non-null   object        \n",
      " 2   Aircraft Manufacturer      4991 non-null   object        \n",
      " 3   Aircraft                   4991 non-null   object        \n",
      " 4   Location                   4991 non-null   object        \n",
      " 5   Operator                   4973 non-null   object        \n",
      " 6   Sum of Fatalities(ground)  4991 non-null   object        \n",
      " 7   Sum of Fatalities (air)    4991 non-null   int64         \n",
      " 8   Sum of Aboard              4991 non-null   int64         \n",
      "dtypes: datetime64[ns](1), int64(2), object(6)\n",
      "memory usage: 351.1+ KB\n"
     ]
    }
   ],
   "source": [
    "# check for the presence of null or missing values \n",
    "\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 318,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Crash Date                    0\n",
       "Country/Region                8\n",
       "Aircraft Manufacturer         0\n",
       "Aircraft                      0\n",
       "Location                      0\n",
       "Operator                     18\n",
       "Sum of Fatalities(ground)     0\n",
       "Sum of Fatalities (air)       0\n",
       "Sum of Aboard                 0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 318,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "df.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 319,
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
       "      <th>Crash Date</th>\n",
       "      <th>Country/Region</th>\n",
       "      <th>Aircraft Manufacturer</th>\n",
       "      <th>Aircraft</th>\n",
       "      <th>Location</th>\n",
       "      <th>Operator</th>\n",
       "      <th>Sum of Fatalities(ground)</th>\n",
       "      <th>Sum of Fatalities (air)</th>\n",
       "      <th>Sum of Aboard</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1909-09-07</td>\n",
       "      <td>France?</td>\n",
       "      <td>Wright</td>\n",
       "      <td>Wright ByplaneSC1</td>\n",
       "      <td>Juvisy-sur-Orge France</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>1917-06-17</td>\n",
       "      <td>England?</td>\n",
       "      <td>Zepplin</td>\n",
       "      <td>Zepplin L 48 (air ship)L</td>\n",
       "      <td>Near Yarmouth England</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>14</td>\n",
       "      <td>16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>67</th>\n",
       "      <td>1922-04-08</td>\n",
       "      <td>China?</td>\n",
       "      <td>??</td>\n",
       "      <td>??</td>\n",
       "      <td>Pao Ting Fou China?</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>17</td>\n",
       "      <td>17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>69</th>\n",
       "      <td>1922-07-04</td>\n",
       "      <td>Germany?</td>\n",
       "      <td>LVG C</td>\n",
       "      <td>LVG C VI?</td>\n",
       "      <td>Fuhlsbuttel Germany?</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>114</th>\n",
       "      <td>1926-09-26</td>\n",
       "      <td>U.S.A.</td>\n",
       "      <td>Sikorsky</td>\n",
       "      <td>Sikorsky S 25?</td>\n",
       "      <td>New York</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>214</th>\n",
       "      <td>1930-01-02</td>\n",
       "      <td>California?</td>\n",
       "      <td>??</td>\n",
       "      <td>??</td>\n",
       "      <td>Off Venice California?</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>10</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>376</th>\n",
       "      <td>1935-05-29</td>\n",
       "      <td>Honduras?</td>\n",
       "      <td>??</td>\n",
       "      <td>??</td>\n",
       "      <td>San Barbra Honduras?</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>6</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>428</th>\n",
       "      <td>1936-08-03</td>\n",
       "      <td>Mexico</td>\n",
       "      <td>Lockheed 9</td>\n",
       "      <td>Lockheed 9 OrionXA BAY</td>\n",
       "      <td>Ciudad Serdan</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>463</th>\n",
       "      <td>1937-06-02</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Sirkorsky</td>\n",
       "      <td>Sirkorsky S 43 (flying boat)2</td>\n",
       "      <td>Desertores Island Región de Los LagosFuerzs Ae...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>9</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>514</th>\n",
       "      <td>1938-07-19</td>\n",
       "      <td>Andes</td>\n",
       "      <td>Douglas</td>\n",
       "      <td>Douglas DC 2NC14272</td>\n",
       "      <td>AndesPanagra</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>681</th>\n",
       "      <td>1943-07-04</td>\n",
       "      <td>Gibraltar</td>\n",
       "      <td>Consolidated Liberator B24</td>\n",
       "      <td>Consolidated Liberator B24 CA L</td>\n",
       "      <td>Gibraltar?</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>12</td>\n",
       "      <td>13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>857</th>\n",
       "      <td>1946-04-08</td>\n",
       "      <td>China?</td>\n",
       "      <td>??</td>\n",
       "      <td>??</td>\n",
       "      <td>Near Shensi China?</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>14</td>\n",
       "      <td>14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>971</th>\n",
       "      <td>1947-07-15</td>\n",
       "      <td>France</td>\n",
       "      <td>Junkers</td>\n",
       "      <td>Junkers Ju 52/3mF</td>\n",
       "      <td>Vichy</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015</th>\n",
       "      <td>1963-02-08</td>\n",
       "      <td>Syktyvkar</td>\n",
       "      <td>Antonov</td>\n",
       "      <td>Antonov AN 10ACCCP</td>\n",
       "      <td>Syktyvkar</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2053</th>\n",
       "      <td>1963-09-02</td>\n",
       "      <td>Laos</td>\n",
       "      <td>Curtiss</td>\n",
       "      <td>Curtiss C 46 Commando?</td>\n",
       "      <td>Northeast Laos?</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>15</td>\n",
       "      <td>16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3195</th>\n",
       "      <td>1983-01-09</td>\n",
       "      <td>Minnesota46826/109</td>\n",
       "      <td>Convair</td>\n",
       "      <td>Convair 580 11AN844H</td>\n",
       "      <td>Brainerd Minnesota46826/109</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>33</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3572</th>\n",
       "      <td>1989-09-28</td>\n",
       "      <td>Ukraine</td>\n",
       "      <td>Antonov</td>\n",
       "      <td>Antonov An 32CCCP</td>\n",
       "      <td>Semyonovka</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>9</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4803</th>\n",
       "      <td>2011-12-26</td>\n",
       "      <td>Florida?</td>\n",
       "      <td>Bell</td>\n",
       "      <td>Bell 206BN5016M</td>\n",
       "      <td>Green Grove Florida?</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Crash Date      Country/Region       Aircraft Manufacturer  \\\n",
       "1    1909-09-07             France?                      Wright   \n",
       "17   1917-06-17            England?                     Zepplin   \n",
       "67   1922-04-08              China?                          ??   \n",
       "69   1922-07-04            Germany?                       LVG C   \n",
       "114  1926-09-26              U.S.A.                    Sikorsky   \n",
       "214  1930-01-02         California?                          ??   \n",
       "376  1935-05-29           Honduras?                          ??   \n",
       "428  1936-08-03              Mexico                  Lockheed 9   \n",
       "463  1937-06-02                 NaN                   Sirkorsky   \n",
       "514  1938-07-19               Andes                     Douglas   \n",
       "681  1943-07-04           Gibraltar  Consolidated Liberator B24   \n",
       "857  1946-04-08              China?                          ??   \n",
       "971  1947-07-15              France                     Junkers   \n",
       "2015 1963-02-08           Syktyvkar                     Antonov   \n",
       "2053 1963-09-02                Laos                     Curtiss   \n",
       "3195 1983-01-09  Minnesota46826/109                     Convair   \n",
       "3572 1989-09-28             Ukraine                     Antonov   \n",
       "4803 2011-12-26            Florida?                        Bell   \n",
       "\n",
       "                             Aircraft  \\\n",
       "1                   Wright ByplaneSC1   \n",
       "17           Zepplin L 48 (air ship)L   \n",
       "67                                 ??   \n",
       "69                          LVG C VI?   \n",
       "114                    Sikorsky S 25?   \n",
       "214                                ??   \n",
       "376                                ??   \n",
       "428            Lockheed 9 OrionXA BAY   \n",
       "463     Sirkorsky S 43 (flying boat)2   \n",
       "514               Douglas DC 2NC14272   \n",
       "681   Consolidated Liberator B24 CA L   \n",
       "857                                ??   \n",
       "971                 Junkers Ju 52/3mF   \n",
       "2015               Antonov AN 10ACCCP   \n",
       "2053           Curtiss C 46 Commando?   \n",
       "3195             Convair 580 11AN844H   \n",
       "3572                Antonov An 32CCCP   \n",
       "4803                  Bell 206BN5016M   \n",
       "\n",
       "                                               Location Operator  \\\n",
       "1                                Juvisy-sur-Orge France      NaN   \n",
       "17                                Near Yarmouth England      NaN   \n",
       "67                                  Pao Ting Fou China?      NaN   \n",
       "69                                 Fuhlsbuttel Germany?      NaN   \n",
       "114                                            New York      NaN   \n",
       "214                              Off Venice California?      NaN   \n",
       "376                                San Barbra Honduras?      NaN   \n",
       "428                                       Ciudad Serdan      NaN   \n",
       "463   Desertores Island Región de Los LagosFuerzs Ae...      NaN   \n",
       "514                                        AndesPanagra      NaN   \n",
       "681                                          Gibraltar?      NaN   \n",
       "857                                  Near Shensi China?      NaN   \n",
       "971                                             Vichy        NaN   \n",
       "2015                                          Syktyvkar      NaN   \n",
       "2053                                    Northeast Laos?      NaN   \n",
       "3195                        Brainerd Minnesota46826/109      NaN   \n",
       "3572                                         Semyonovka      NaN   \n",
       "4803                               Green Grove Florida?      NaN   \n",
       "\n",
       "     Sum of Fatalities(ground)  Sum of Fatalities (air)  Sum of Aboard  \n",
       "1                            0                        1              1  \n",
       "17                           0                       14             16  \n",
       "67                           0                       17             17  \n",
       "69                           0                        2              3  \n",
       "114                          0                        2              5  \n",
       "214                          0                       10             10  \n",
       "376                          0                        6              9  \n",
       "428                          0                        1              1  \n",
       "463                          0                        9              9  \n",
       "514                          0                        4              4  \n",
       "681                          0                       12             13  \n",
       "857                          0                       14             14  \n",
       "971                          0                        1             19  \n",
       "2015                         0                        7              7  \n",
       "2053                         0                       15             16  \n",
       "3195                         0                        1             33  \n",
       "3572                         0                        9              9  \n",
       "4803                         0                        3              3  "
      ]
     },
     "execution_count": 319,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# here we view the specific rows in the Operator column with missing values\n",
    "\n",
    "df[df['Operator'].isna()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 320,
   "metadata": {},
   "outputs": [],
   "source": [
    "# we proceed to fill missing values\n",
    "\n",
    "df['Operator'] = df['Operator'].fillna('Unknown')\n",
    "df['Operator'] = df['Operator'].str.replace('Corporation Aviation National China','China National Aviation Corporation')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 321,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Crash Date                   0\n",
       "Country/Region               8\n",
       "Aircraft Manufacturer        0\n",
       "Aircraft                     0\n",
       "Location                     0\n",
       "Operator                     0\n",
       "Sum of Fatalities(ground)    0\n",
       "Sum of Fatalities (air)      0\n",
       "Sum of Aboard                0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 321,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# we check if the correction has been rectifed\n",
    "\n",
    "df.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 322,
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
       "      <th>Crash Date</th>\n",
       "      <th>Country/Region</th>\n",
       "      <th>Aircraft Manufacturer</th>\n",
       "      <th>Aircraft</th>\n",
       "      <th>Location</th>\n",
       "      <th>Operator</th>\n",
       "      <th>Sum of Fatalities(ground)</th>\n",
       "      <th>Sum of Fatalities (air)</th>\n",
       "      <th>Sum of Aboard</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>360</th>\n",
       "      <td>1934-12-31</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Tupolev</td>\n",
       "      <td>Tupolev ANT 9?</td>\n",
       "      <td>?Aeroflot</td>\n",
       "      <td>Aeroflot</td>\n",
       "      <td>0</td>\n",
       "      <td>10</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>463</th>\n",
       "      <td>1937-06-02</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Sirkorsky</td>\n",
       "      <td>Sirkorsky S 43 (flying boat)2</td>\n",
       "      <td>Desertores Island Región de Los LagosFuerzs Ae...</td>\n",
       "      <td>Unknown</td>\n",
       "      <td>0</td>\n",
       "      <td>9</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>464</th>\n",
       "      <td>1937-06-20</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Travel Air</td>\n",
       "      <td>Travel Air 6000TI 3</td>\n",
       "      <td>?ENTA</td>\n",
       "      <td>ENTA</td>\n",
       "      <td>0</td>\n",
       "      <td>6</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>586</th>\n",
       "      <td>1940-08-22</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Lockheed 10 Electra</td>\n",
       "      <td>Lockheed 10 Electra YU SBC</td>\n",
       "      <td>Gospic</td>\n",
       "      <td>Coatia Aeroput</td>\n",
       "      <td>0</td>\n",
       "      <td>11</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>645</th>\n",
       "      <td>1942-08-21</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Siebel</td>\n",
       "      <td>Siebel Si 204?</td>\n",
       "      <td>?Deutsche Lufthansa</td>\n",
       "      <td>Deutsche Lufthansa</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>998</th>\n",
       "      <td>1947-11-27</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Douglas</td>\n",
       "      <td>Douglas DC 3?</td>\n",
       "      <td>?China National Aviation Corporation</td>\n",
       "      <td>China National Aviation Corporation</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2882</th>\n",
       "      <td>1977-01-20</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Bristol 170 Freighter</td>\n",
       "      <td>Bristol 170 Freighter 31MC FWAD</td>\n",
       "      <td>?North Canada Air</td>\n",
       "      <td>Canada Air</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4445</th>\n",
       "      <td>2003-10-03</td>\n",
       "      <td>NaN</td>\n",
       "      <td>EMB 721C</td>\n",
       "      <td>EMB 721C SertanejoPT EBK</td>\n",
       "      <td>Sao Gabriel de CachoeriaAir taxi - Rumo Notre ...</td>\n",
       "      <td>Rumo Notre Air Taxi</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Crash Date Country/Region  Aircraft Manufacturer  \\\n",
       "360  1934-12-31            NaN                Tupolev   \n",
       "463  1937-06-02            NaN              Sirkorsky   \n",
       "464  1937-06-20            NaN             Travel Air   \n",
       "586  1940-08-22            NaN    Lockheed 10 Electra   \n",
       "645  1942-08-21            NaN                 Siebel   \n",
       "998  1947-11-27            NaN                Douglas   \n",
       "2882 1977-01-20            NaN  Bristol 170 Freighter   \n",
       "4445 2003-10-03            NaN               EMB 721C   \n",
       "\n",
       "                             Aircraft  \\\n",
       "360                    Tupolev ANT 9?   \n",
       "463     Sirkorsky S 43 (flying boat)2   \n",
       "464               Travel Air 6000TI 3   \n",
       "586        Lockheed 10 Electra YU SBC   \n",
       "645                    Siebel Si 204?   \n",
       "998                     Douglas DC 3?   \n",
       "2882  Bristol 170 Freighter 31MC FWAD   \n",
       "4445         EMB 721C SertanejoPT EBK   \n",
       "\n",
       "                                               Location  \\\n",
       "360                                           ?Aeroflot   \n",
       "463   Desertores Island Región de Los LagosFuerzs Ae...   \n",
       "464                                               ?ENTA   \n",
       "586                                              Gospic   \n",
       "645                                 ?Deutsche Lufthansa   \n",
       "998                ?China National Aviation Corporation   \n",
       "2882                                  ?North Canada Air   \n",
       "4445  Sao Gabriel de CachoeriaAir taxi - Rumo Notre ...   \n",
       "\n",
       "                                 Operator Sum of Fatalities(ground)  \\\n",
       "360                              Aeroflot                         0   \n",
       "463                               Unknown                         0   \n",
       "464                                  ENTA                         0   \n",
       "586                        Coatia Aeroput                         0   \n",
       "645                    Deutsche Lufthansa                         0   \n",
       "998   China National Aviation Corporation                         0   \n",
       "2882                           Canada Air                         0   \n",
       "4445                 Rumo Notre Air Taxi                          0   \n",
       "\n",
       "      Sum of Fatalities (air)  Sum of Aboard  \n",
       "360                        10             10  \n",
       "463                         9              9  \n",
       "464                         6              6  \n",
       "586                        11             11  \n",
       "645                         4              4  \n",
       "998                         2              3  \n",
       "2882                        1              2  \n",
       "4445                        4              4  "
      ]
     },
     "execution_count": 322,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# we repeat the same procedure for the Country/Region column\n",
    "df[df['Country/Region'].isna()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 323,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['Country/Region'] = df['Country/Region'].fillna('Unknown')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 324,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Crash Date                   0\n",
       "Country/Region               0\n",
       "Aircraft Manufacturer        0\n",
       "Aircraft                     0\n",
       "Location                     0\n",
       "Operator                     0\n",
       "Sum of Fatalities(ground)    0\n",
       "Sum of Fatalities (air)      0\n",
       "Sum of Aboard                0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 324,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# we check again if the correction has been rectified\n",
    "# the data is ready\n",
    "\n",
    "df.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 325,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 4991 entries, 0 to 4990\n",
      "Data columns (total 9 columns):\n",
      " #   Column                     Non-Null Count  Dtype         \n",
      "---  ------                     --------------  -----         \n",
      " 0   Crash Date                 4991 non-null   datetime64[ns]\n",
      " 1   Country/Region             4991 non-null   object        \n",
      " 2   Aircraft Manufacturer      4991 non-null   object        \n",
      " 3   Aircraft                   4991 non-null   object        \n",
      " 4   Location                   4991 non-null   object        \n",
      " 5   Operator                   4991 non-null   object        \n",
      " 6   Sum of Fatalities(ground)  4991 non-null   object        \n",
      " 7   Sum of Fatalities (air)    4991 non-null   int64         \n",
      " 8   Sum of Aboard              4991 non-null   int64         \n",
      "dtypes: datetime64[ns](1), int64(2), object(6)\n",
      "memory usage: 351.1+ KB\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "check the datatypes to see if its in the preferred format\n",
    "we can see that the Sum of Fatalities(Ground) column\n",
    "is in object format which will not help in our analysis\n",
    "so it needs to be converted to numeric format \n",
    "'''\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 326,
   "metadata": {},
   "outputs": [],
   "source": [
    "# convert the data type of the specific column from object to numeric\n",
    "\n",
    "# df['Sum of Fatalities(ground)'] = pd.to_numeric(df['Sum of Fatalities(ground)'])\n",
    "\n",
    "# An error is raised which says 'Unable to parse string \"vv \" at position 913'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 327,
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
       "      <th>Crash Date</th>\n",
       "      <th>Country/Region</th>\n",
       "      <th>Aircraft Manufacturer</th>\n",
       "      <th>Aircraft</th>\n",
       "      <th>Location</th>\n",
       "      <th>Operator</th>\n",
       "      <th>Sum of Fatalities(ground)</th>\n",
       "      <th>Sum of Fatalities (air)</th>\n",
       "      <th>Sum of Aboard</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1819</th>\n",
       "      <td>1960-04-22</td>\n",
       "      <td>Belgian</td>\n",
       "      <td>Douglas</td>\n",
       "      <td>Douglas C 54BOO</td>\n",
       "      <td>Bunia Belgian</td>\n",
       "      <td>Sobelair Congo SA (Belgium)</td>\n",
       "      <td>vv</td>\n",
       "      <td>35</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Crash Date Country/Region Aircraft Manufacturer         Aircraft  \\\n",
       "1819 1960-04-22        Belgian               Douglas  Douglas C 54BOO   \n",
       "\n",
       "           Location                     Operator Sum of Fatalities(ground)  \\\n",
       "1819  Bunia Belgian  Sobelair Congo SA (Belgium)                       vv    \n",
       "\n",
       "      Sum of Fatalities (air)  Sum of Aboard  \n",
       "1819                       35             35  "
      ]
     },
     "execution_count": 327,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# check the specific row where the error is located\n",
    "\n",
    "df[df['Sum of Fatalities(ground)'] == 'vv ']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 328,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Using the replace() function replace the error with an appropriate value\n",
    "\n",
    "df['Sum of Fatalities(ground)'] = df['Sum of Fatalities(ground)'].replace('vv ','0')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 329,
   "metadata": {},
   "outputs": [],
   "source": [
    "# we can now perform our data conversion\n",
    "\n",
    "df['Sum of Fatalities(ground)'] = pd.to_numeric(df['Sum of Fatalities(ground)'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 330,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 4991 entries, 0 to 4990\n",
      "Data columns (total 9 columns):\n",
      " #   Column                     Non-Null Count  Dtype         \n",
      "---  ------                     --------------  -----         \n",
      " 0   Crash Date                 4991 non-null   datetime64[ns]\n",
      " 1   Country/Region             4991 non-null   object        \n",
      " 2   Aircraft Manufacturer      4991 non-null   object        \n",
      " 3   Aircraft                   4991 non-null   object        \n",
      " 4   Location                   4991 non-null   object        \n",
      " 5   Operator                   4991 non-null   object        \n",
      " 6   Sum of Fatalities(ground)  4991 non-null   int64         \n",
      " 7   Sum of Fatalities (air)    4991 non-null   int64         \n",
      " 8   Sum of Aboard              4991 non-null   int64         \n",
      "dtypes: datetime64[ns](1), int64(3), object(5)\n",
      "memory usage: 351.1+ KB\n"
     ]
    }
   ],
   "source": [
    "# check to confirm\n",
    "\n",
    "df.info()\n",
    "\n",
    "# done!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 331,
   "metadata": {},
   "outputs": [],
   "source": [
    "# import the necessary data visualisation libraries\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 332,
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
       "      <th>Crash Date</th>\n",
       "      <th>Country/Region</th>\n",
       "      <th>Aircraft Manufacturer</th>\n",
       "      <th>Aircraft</th>\n",
       "      <th>Location</th>\n",
       "      <th>Operator</th>\n",
       "      <th>Sum of Fatalities(ground)</th>\n",
       "      <th>Sum of Fatalities (air)</th>\n",
       "      <th>Sum of Aboard</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1908-09-17</td>\n",
       "      <td>Virgin Islandsia</td>\n",
       "      <td>Wright Flyer</td>\n",
       "      <td>Wright Flyer III?</td>\n",
       "      <td>Fort Myer Virgin Islandsia</td>\n",
       "      <td>U.S. Army - Military</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1909-09-07</td>\n",
       "      <td>France?</td>\n",
       "      <td>Wright</td>\n",
       "      <td>Wright ByplaneSC1</td>\n",
       "      <td>Juvisy-sur-Orge France</td>\n",
       "      <td>Unknown</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1912-07-12</td>\n",
       "      <td>U.S.A.</td>\n",
       "      <td>Dirigible?</td>\n",
       "      <td>Dirigible?</td>\n",
       "      <td>Atlantic City New Jersey</td>\n",
       "      <td>US Navy - Military</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1913-08-06</td>\n",
       "      <td>British</td>\n",
       "      <td>Curtiss</td>\n",
       "      <td>Curtiss seaplane?</td>\n",
       "      <td>Victoria British</td>\n",
       "      <td>Canada          Columbia Private</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1913-09-09</td>\n",
       "      <td>North Sea</td>\n",
       "      <td>Zeppelin</td>\n",
       "      <td>Zeppelin L 1 (airship)?</td>\n",
       "      <td>Over the North Sea</td>\n",
       "      <td>German Navy - Military</td>\n",
       "      <td>0</td>\n",
       "      <td>14</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Crash Date    Country/Region Aircraft Manufacturer                 Aircraft  \\\n",
       "0 1908-09-17  Virgin Islandsia          Wright Flyer        Wright Flyer III?   \n",
       "1 1909-09-07           France?                Wright        Wright ByplaneSC1   \n",
       "2 1912-07-12            U.S.A.            Dirigible?               Dirigible?   \n",
       "3 1913-08-06           British               Curtiss        Curtiss seaplane?   \n",
       "4 1913-09-09         North Sea              Zeppelin  Zeppelin L 1 (airship)?   \n",
       "\n",
       "                     Location                          Operator  \\\n",
       "0  Fort Myer Virgin Islandsia              U.S. Army - Military   \n",
       "1      Juvisy-sur-Orge France                           Unknown   \n",
       "2    Atlantic City New Jersey                US Navy - Military   \n",
       "3            Victoria British  Canada          Columbia Private   \n",
       "4          Over the North Sea            German Navy - Military   \n",
       "\n",
       "   Sum of Fatalities(ground)  Sum of Fatalities (air)  Sum of Aboard  \n",
       "0                          0                        1              2  \n",
       "1                          0                        1              1  \n",
       "2                          0                        5              5  \n",
       "3                          0                        1              1  \n",
       "4                          0                       14             20  "
      ]
     },
     "execution_count": 332,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# view the data\n",
    "\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 333,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Crash Date', 'Country/Region', 'Aircraft Manufacturer', 'Aircraft',\n",
       "       'Location', 'Operator', 'Sum of Fatalities(ground)',\n",
       "       'Sum of Fatalities (air)', 'Sum of Aboard'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 333,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# view the column names\n",
    "\n",
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 334,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Extract the year to a new column\n",
    "\n",
    "df['Year'] = df['Crash Date'].dt.year"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 335,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    1908\n",
       "1    1909\n",
       "2    1912\n",
       "3    1913\n",
       "4    1913\n",
       "5    1913\n",
       "6    1915\n",
       "7    1915\n",
       "8    1916\n",
       "9    1916\n",
       "Name: Year, dtype: int32"
      ]
     },
     "execution_count": 335,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# View the column\n",
    "\n",
    "df['Year'].head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 336,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculate the total fatalities by adding the Sum of Fatalities(ground) and Sum of Fatalities (air) columns\n",
    "\n",
    "df['Total Fatalities'] = df['Sum of Fatalities(ground)'] + df['Sum of Fatalities (air)']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 337,
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
       "      <th>Crash Date</th>\n",
       "      <th>Country/Region</th>\n",
       "      <th>Aircraft Manufacturer</th>\n",
       "      <th>Aircraft</th>\n",
       "      <th>Location</th>\n",
       "      <th>Operator</th>\n",
       "      <th>Sum of Fatalities(ground)</th>\n",
       "      <th>Sum of Fatalities (air)</th>\n",
       "      <th>Sum of Aboard</th>\n",
       "      <th>Year</th>\n",
       "      <th>Total Fatalities</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1908-09-17</td>\n",
       "      <td>Virgin Islandsia</td>\n",
       "      <td>Wright Flyer</td>\n",
       "      <td>Wright Flyer III?</td>\n",
       "      <td>Fort Myer Virgin Islandsia</td>\n",
       "      <td>U.S. Army - Military</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1908</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1909-09-07</td>\n",
       "      <td>France?</td>\n",
       "      <td>Wright</td>\n",
       "      <td>Wright ByplaneSC1</td>\n",
       "      <td>Juvisy-sur-Orge France</td>\n",
       "      <td>Unknown</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1909</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1912-07-12</td>\n",
       "      <td>U.S.A.</td>\n",
       "      <td>Dirigible?</td>\n",
       "      <td>Dirigible?</td>\n",
       "      <td>Atlantic City New Jersey</td>\n",
       "      <td>US Navy - Military</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "      <td>1912</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1913-08-06</td>\n",
       "      <td>British</td>\n",
       "      <td>Curtiss</td>\n",
       "      <td>Curtiss seaplane?</td>\n",
       "      <td>Victoria British</td>\n",
       "      <td>Canada          Columbia Private</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1913</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1913-09-09</td>\n",
       "      <td>North Sea</td>\n",
       "      <td>Zeppelin</td>\n",
       "      <td>Zeppelin L 1 (airship)?</td>\n",
       "      <td>Over the North Sea</td>\n",
       "      <td>German Navy - Military</td>\n",
       "      <td>0</td>\n",
       "      <td>14</td>\n",
       "      <td>20</td>\n",
       "      <td>1913</td>\n",
       "      <td>14</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Crash Date    Country/Region Aircraft Manufacturer                 Aircraft  \\\n",
       "0 1908-09-17  Virgin Islandsia          Wright Flyer        Wright Flyer III?   \n",
       "1 1909-09-07           France?                Wright        Wright ByplaneSC1   \n",
       "2 1912-07-12            U.S.A.            Dirigible?               Dirigible?   \n",
       "3 1913-08-06           British               Curtiss        Curtiss seaplane?   \n",
       "4 1913-09-09         North Sea              Zeppelin  Zeppelin L 1 (airship)?   \n",
       "\n",
       "                     Location                          Operator  \\\n",
       "0  Fort Myer Virgin Islandsia              U.S. Army - Military   \n",
       "1      Juvisy-sur-Orge France                           Unknown   \n",
       "2    Atlantic City New Jersey                US Navy - Military   \n",
       "3            Victoria British  Canada          Columbia Private   \n",
       "4          Over the North Sea            German Navy - Military   \n",
       "\n",
       "   Sum of Fatalities(ground)  Sum of Fatalities (air)  Sum of Aboard  Year  \\\n",
       "0                          0                        1              2  1908   \n",
       "1                          0                        1              1  1909   \n",
       "2                          0                        5              5  1912   \n",
       "3                          0                        1              1  1913   \n",
       "4                          0                       14             20  1913   \n",
       "\n",
       "   Total Fatalities  \n",
       "0                 1  \n",
       "1                 1  \n",
       "2                 5  \n",
       "3                 1  \n",
       "4                14  "
      ]
     },
     "execution_count": 337,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# View the new column\n",
    "\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Research Questions using the Aircrash dataset\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* sum of Fatalities per year\n",
    "* Operators with the most number of crashes\n",
    "* Aircraft models with the most number of crashes\n",
    "* Sum of crashes per year\n",
    "* Total Fatalities recorded\n",
    "* Total Accidents occured\n",
    "* Total passengers aboard flights\n",
    "* Sum of ground casualties"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 372,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjEAAAHFCAYAAAADhKhmAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAABlVUlEQVR4nO3deVzU1f4/8BeKoBJMqMFIklp5zUK7LoXYopXrDa1rv/Rm8dVvXrMsjdRv5a2+Wd2vlt7UbliZmXpdwhYx20jNpExQNFFQxI1FhAFRGFZnPb8/iA+zLzAs85nX8/GYR/CZMzOf+UjMi3Pe5xw/IYQAERERkZfp0NYnQERERNQUDDFERETklRhiiIiIyCsxxBAREZFXYoghIiIir8QQQ0RERF6JIYaIiIi8EkMMEREReSWGGCIiIvJKDDFELoiNjcW1116LCxcuWN135coV9OzZE3fddReMRmOLn0teXh78/PywYcMGjzzfyZMnsXjxYuTl5Xnk+Txt8eLF8PPzc6mtEAJbt27F/fffj9DQUAQGBuLGG2/Es88+a/PfDgBeffVV3HDDDfD398e1117r9Dxs3RISElx+P5643hs2bICfn5/Zc8yYMQN9+vQxa7dkyRLs2LHD6vH79u2Dn58f9u3b1+RzIGoPGGKIXPDJJ5/A398ff//7363ue+6551BVVYWNGzeiQwfv+1/q5MmTeOONN9ptiHGV0WjEY489hscffxxKpRIbNmzAjz/+iPj4eOzcuRODBg3Cb7/9ZvaYr7/+Gv/3f/+H//qv/0JKSgr27Nnj9HWSk5ORmppqdnv00UddPs+Wut6vvfYakpKSzI7ZCzFDhgxBamoqhgwZ4tFzIGpt/m19AkTeQKlU4oMPPsDUqVOxZs0azJ49GwCQlJSEzz77DB988AFuvvnmFj0Hg8EAvV7foq/hitraWnTt2rWtT8PKO++8g23btuHtt9/GSy+9JB0fNWoUpk6diujoaDzyyCM4deqU1OOSlZUFAJg3bx7CwsJcep2hQ4eiR48eHj//5rrppptcbhsSEoLhw4e34NkQtRJBRC7729/+Jq655hqRm5srysrKRFhYmBgzZowQQoj09HQxceJEERoaKgIDA8Wf//xnsW3bNrPHl5aWimeeeUYMGDBABAUFieuuu07cd9994pdffjFrl5ubKwCId955R7z11luiT58+omPHjuKHH36Q7lu/fr0QQohffvlFABBbt261Ot+NGzcKAOLQoUM238/69esFAKtbw3OPHDlS3HbbbSIlJUXExMSILl26iKlTpwohhFCr1WLBggWiT58+olOnTiIiIkI8//zzorq62uw1AIhnn31W/Oc//xG33HKL6NKlixg0aJD45ptvrM7n22+/FbfffrsICAgQffr0EcuXLxevv/66cParSqPRiNDQUDFgwABhNBptttm6dasAIP71r38JIYTo3bu31ft+/fXX7b5Gw3lcunTJ5v3p6eli6tSponfv3qJz586id+/e4m9/+5vIy8uT2ji73rt27RKTJk0S119/vQgMDBQ33XSTeOqpp6xes+F5cnNzpWPTp08XvXv3lr639TojR44UQgjx888/CwDi559/tnoPzn6Ga2pqpH/3wMBAERoaKoYOHWrz54+opbEnhsgNq1evRkpKCp588klcd9110Gq1+PTTT/Hzzz9j/PjxiI6OxkcffQSFQoHExERMnToVtbW1mDFjBoD6+hkAeP3116FUKlFdXY2kpCSMGjUKP/30E0aNGmX2ev/+97/xpz/9Cf/6178QEhKCfv36WZ3TPffcg8GDB2P16tV47LHHzO5LSEjAHXfcgTvuuMPm+3nwwQexZMkS/OMf/8Dq1aul4QXTv+qLi4vxxBNP4MUXX8SSJUvQoUMH1NbWYuTIkSgsLMQ//vEPDBo0CCdOnMD//u//IjMzE3v27DGrY/nuu++Qnp6ON998E9dccw2WLVuGv/71r8jJycGNN94IAPjpp5/w0EMPISYmBomJiTAYDFi2bBlKSkqc/rscOXIE5eXleOqpp+zWz0ycOBEdOnTA7t27sWDBAiQlJWH16tVYt24dkpOToVAo0KtXL6evZdkj5ufnh44dOyIvLw/9+/fH3/72N3Tr1g3FxcX48MMPcccdd+DkyZPo0aOH0+t97tw5xMTE4O9//zsUCgXy8vKwYsUK3H333cjMzESnTp2cnl+D1NRU3H///bjvvvvw2muvAajvgbHH1Z/h+fPnY9OmTfjnP/+JwYMHo6amBllZWbh8+bLL50bkMW2dooi8zffffy/9Zbtp0yYhhBC33HKLGDx4sNDpdGZtY2NjRc+ePYXBYLD5XHq9Xuh0OvHAAw+Iv/71r9Lxht6Wm266SWi1WrPHWPbECNH4l/nRo0elY4cO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kdO188R187bPBz8hhPB07w4RERFRS2NNDBEREXklhhgiIiLySgwxRERE5JUYYoiIiMgrMcQQERGRV2KIISIiIq/EEENEREReiSGGiIiIvBJDDBG1GSEERo8ejXHjxlnd98EHH0ChUEibRBIRWWKIIaI24+fnh/Xr1+PgwYNYs2aNdDw3NxcvvfQS3nvvPdxwww0efU2dTufR5yOitsMQQ0RtKjIyEu+99x4WLlyI3NxcCCEwc+ZMPPDAA7jzzjvxl7/8Bddccw3Cw8MRFxeHsrIy6bHJycm4++67ce2116J79+6IjY3FuXPnpPvz8vLg5+eHzz//HKNGjULnzp2xefPmtnibRNQCuHcSEbULDz/8MCoqKvDII4/grbfeQnp6OoYNG4ZZs2bhv/7rv1BXV4eXXnoJer0ee/fuBQB89dVX8PPzw8CBA1FTU4P//d//RV5eHjIyMtChQwfk5eWhb9++6NOnD959910MHjwYgYGBiIiIaON3S0SewBBDRO1CaWkpoqKicPnyZXz55Zc4evQoDh48iB9//FFqU1hYiMjISOTk5OBPf/qT1XNcunQJYWFhyMzMRFRUlBRiVq1aheeff7413w4RtQIOJxFRuxAWFoannnoKAwYMwF//+lccOXIEP//8M6655hrpdssttwCANGR07tw5TJs2DTfeeCNCQkLQt29fALAqBh42bFjrvhkiahX+bX0CREQN/P394e9f/2vJaDRi4sSJeOedd6za9ezZEwAwceJEREZGYu3atYiIiIDRaERUVBS0Wq1Z+6CgoJY/eSJqdQwxRNQuDRkyBF999RX69OkjBRtTly9fRnZ2NtasWYN77rkHALB///7WPk0iakMcTiKidunZZ5/FlStX8Nhjj+HQoUM4f/48du3ahSeffBIGgwGhoaHo3r07Pv74Y5w9exZ79+7F/Pnz2/q0iagVMcQQUbsUERGB3377DQaDAePGjUNUVBSef/55KBQKdOjQAR06dEBiYiKOHDmCqKgovPDCC1i+fHlbnzYRtSLOTiIiIiKvxJ4YIiIi8koMMUREROSVGGKIiIjIKzHEEBERkVdiiCEiIiKvxBBDREREXokhhoiIiLwSQwwRERF5JYYYIiIi8koMMUREROSVGGKIiIjIKzHEEBERkVf6/1Yd5ICFSBl2AAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Use a line chart to show the relationship between Year and Total Fatalities\n",
    "Fatalities_per_year = df.groupby('Year')['Total Fatalities'].sum()\n",
    "ax = Fatalities_per_year.plot.area(x='Year',y='Total Fatalities',color='purple',\n",
    "                                   title='Yearly trend Of Fatalities')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 370,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Operator\n",
       "Private                                 27\n",
       "Philippine Air Lines                    31\n",
       "U.S. Army - Military                    31\n",
       "U.S. Army Air Forces - Military         32\n",
       "Indian Airlines                         32\n",
       "US Aerial Mail Service                  33\n",
       "American Airlines                       35\n",
       "U.S. Navy - Military                    35\n",
       "Pan American World Airways              40\n",
       "China National Aviation Corporation     41\n",
       "United Air Lines                        41\n",
       "Deutsche Lufthansa                      60\n",
       "Air France                              67\n",
       "U.S. Air Force - Military              154\n",
       "Aeroflot                               228\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 370,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# show the top 11 operators with the most number of crashes\n",
    "df2 = df['Operator'].value_counts().head(15).sort_values(ascending=True)\n",
    "df2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 371,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 1000x400 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# display this in a chart\n",
    "\n",
    "plt.figure(figsize=(10,4))\n",
    "plt.barh(df2.index,df2.values,color='purple')\n",
    "\n",
    "for i,value in enumerate(df2.values):\n",
    "    plt.annotate(str(value),xy=(value,i),\n",
    "    ha='left',va='center')\n",
    "plt.xlabel('Airline')\n",
    "plt.ylabel('Number of crashes')\n",
    "plt.title('Top 11 airlines with the most number of crashes')\n",
    "plt.yticks(rotation=0,ha='right')\n",
    "plt.show()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 368,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Aircraft\n",
       "Hawker Siddeley HS 748    18\n",
       "Convair CV 240            19\n",
       "Douglas DC 3VT            20\n",
       "Yakovlev YAK 40CCCP       20\n",
       "Douglas C 47              21\n",
       "Douglas DC 3PP            23\n",
       "Douglas DC 3 (C           23\n",
       "Boeing B 747              30\n",
       "McDonnell Douglas DC 8    35\n",
       "Britten  Norman BN        37\n",
       "Douglas C 47A             39\n",
       "McDonnell Douglas DC 9    40\n",
       "Boeing B 707              51\n",
       "Boeing B 727              55\n",
       "Boeing B 737              73\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 368,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# next we find the aircraft models with the most number of crashes \n",
    "# to see whether it's a manufacturer problem or as a result of a significant event\n",
    "df3 = df['Aircraft'].value_counts().head(15).sort_values(ascending=True)\n",
    "df3\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 369,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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SElJITk52XwEBwcTERFBcnKyRSIOMHfuXOrXr0/t2rULvTYRKT4zZ84kKyuLkJAQPDw8zMe1X5itXr2aunXr8thjjwHQrVs36taty6xZs6wVtoiIiMgNuaV7xn/77TfGjRvHggULCAsLIzk5WbvbFrMLFy6QmZlp8WizmJgYHn/8cXr16gVAaGgoQUFBREREMG3aNPMGbi1atCA4OBi4sunbO++8w8KFC2ncuDGLFi1i79691K1bFwAnJyd69+7NmDFjcHV1xc3NjXHjxhV524Kvry+5ubl88MEHdOjQge+//z7fH8YjR46kXbt2VK9endOnT5OQkGD+guDvTCYTsbGxhIaG0rx5c1566SX8/Pw4d+4cX331FWvXri3w0WZOTk75/l2WKVOG8uXL5yvPzs7miy++YMqUKTfw6YtIcbiR1VaRkZFERkbe+WBEREREbrMbnhmHK894feGFF6hatSqpqal89913fPXVV0rErSA+Ph4PDw+8vLxo27YtGzZsYPr06axatco842symVi5ciXlypWjefPmhIaG4uPjYzGrFBYWxquvvkp0dDQNGjTg7Nmz5mT+qqlTp9K4cWMef/xxQkNDadq0Kf7+/oXeV12nTh2mTp3KpEmTCAwMZPHixcTExFi0uXz5MlFRUfj7+9O2bVtq1KhR5HPqGzZsyI4dO/D19WXAgAH4+/vzxBNPkJqaWujj1W7G0qVLMQyD7t27/+O+RERERERErsdk3OCN3pMnT2bSpEm4u7vz1ltvER4efqdjk7tUTk4OlStXZsqUKfTr18/a4dwVsrOzcXFx4UVepBQ3tlmciBRunKHHaIqIiMi/09XcICsrC2dn50Lb3XAyXqJECRwcHAgNDc13r+214uLibj5auavt3r2b/fv307BhQ7Kyshg/fjwbN27k559/5oEHHrB2eHeFG/2BExERERGRe9uN5gY3fM94r169bvrRUnLvePfddzlw4AB2dnbUr1+fpKQkJeIiIiIiIiK36IZnxkWkcJoZFxERERERuPHc4KY2cBMRERERERGRf+6WHm0mIgWLcYnRBm4iRdDGbCIiIiJXaGZcREREREREpJgpGRcRkWIVExNDgwYNcHJyws3NjY4dO3LgwAGLNoZh8Prrr1OpUiUcHBwICQkhNTXVShGLiIiI3H5Kxq8RGRlJx44d71j/GzduxGQycebM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WJGScSvKzMxk2LBh+Pj4YG9vj6enJx06dOC7776zdmj5bN++nWefffaWzv3555/p06cPVapUwd7eHm9vb7p3786OHTs4efIktra2LFq0qMBzBw4cSFBQUIF1P/30E927d8fT0xMHBwf8/f15//33i4zDycmJsmXL5qtLTEykfv36lCpVCh8fH2bNmnVL1ypyv8vJyaF27dp8+OGH+eoMw6Bjx44cOXKEVatWsXv3bh566CFCQ0PJycmxQrQiIiIi1qN7xq3kl19+oWnTppQtW5bJkycTFBTEpUuXWLNmDVFRUezfv9/aIVqoUKFCkfWXLl3C1tY2X/mOHTto1aoVgYGBzJ49Gz8/P86ePcuqVasYPXo0iYmJPPbYY8TGxvLMM89YnPvXX3+xdOlSxo8fX+B77ty5kwoVKrBo0SI8PT3ZsmULzz77LCVLlmTo0KH54uvevTuPPPIIW7Zssag7evQo7du3Z8CAASxatIjvv/+eIUOGUKFCBTp37nwjH4+I/J927drRrl27AusOHTrE1q1b2bt3LzVr1gRgxowZuLm58dlnn9G/f//iDFVERETEqjQzbiVDhgzBZDKxbds2nnrqKapXr07NmjUZNWoUW7duNbdLT08nPDwcR0dHnJ2defrppzl58qS5/vXXX6dOnTp8+umneHl54eLiQrdu3Th79iwAs2fPpnLlyuTl5Vm8/xNPPEHv3r0BOHz4MOHh4VSsWBFHR0caNGjA+vXrLdr/fZm6yWRi1qxZhIeHU6ZMGSZMmJDvGg3DIDIykmrVqpGUlMRjjz2Gr68vderUYdy4caxatQqAfv36sWHDBn755ReL87/88kvOnz+fL0m/qm/fvkyfPp0WLVrg4+PDM888Q58+fYiLi8vX9pVXXsHPz4+nn346X92sWbN48MEHmTZtGv7+/vTv35++ffvy7rvvFvi+InJrLly4AECpUv9/k8OSJUtiZ2fH5s2brRWWiIiIiFUoGbeCP/74g/j4eKKioihTpky++qvLqK8u6fzjjz9ITExk3bp1HD58mK5du1q0P3z4MCtXruTrr7/m66+/JjExkbfffhuALl268L///Y8NGzaY258+fZo1a9YQEREBwLlz52jfvj3r169n9+7dhIWF0aFDB9LT04u8jnHjxhEeHk5KSgp9+/bNV5+cnExqaiqjR4+mRIn8/9SuXmf79u1x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DBgwgDJlypCWlsa6dessYu3fv7/5c//+++9v+LMoSnJyMuPGjaNnz54EBARgZ2dHYmIi8+bN44UXXijy3Ly8PGJjY+nduzc2Npb/pMuXL0/58uUtymxtbXF3d6dGjRoA+Pn5UbVqVQYOHMi7775L+fLlWblyJevWrePrr7++Ldcn8m+2Y8cOWrZsaX49atQoAHr37s38+fNZunQpY8eOJSIigj/++IOHHnqIiRMnMmjQIGuFLCIiInLX+9ck46+++ipHjx4lLCyM0qVL8+yzz9KxY8d8z6Bu2bIlu3btMife5cqVIyAggN9++80icb+WjY0Nn332GV27djUn5G+++SZubm7ExMRw5MgRypYtS7169XjppZduKu6GDRuyefNmBg0axG+//YajoyM1a9Zk5cqVhc5Yd+3alcOHD/PCCy9w/vx5OnfuzODBgy02aBs9ejQZGRlERkZSokQJ+vbty5NPPmnxedzsNQQFBZGYmMjLL7/MI488gmEY+Pr60rVrV4t21apVo0mTJpw6dYqHH374pj6PwlSpUgUvLy/eeOMNfvnlF0wmk/n1c889V+S569evJz09/YbuXS+Ira0t//nPf3jxxRfp0KED586do2rVqixYsID27dvfUp8i95KQkJB8j068lru7O7GxscUYkYiIiMi/n8ko6i8skQIYhoGfnx8DBw40z5Dd77Kzs3FxceFFXqQUpawdjshtM84YZ+0QRERERP5VruYGWVlZhT5BC/5FM+Nyd/j999/59NNPOXHihPmeaxEREREREbk5SsblplSsWJEHHniAjz/+mHLlylk7nLvO2KyxRX77JSIiIiIiAkrG5SbprgYREREREZF/rsT1m4iIiIiIiIjI7aRkXERERERERKSYKRkXERERERERKWZKxkVERERERESKmZJxERERERERkWKmZFxERERERESkmCkZFxERERERESlmSsZFREREREREipmScREREREREZFipmRcREREREREpJgpGRcREREREREpZjbWDkDkXmAYBgDZ2dlWjkRERERERKzpak5wNUcojJJxkdvg1KlTAHh6elo5EhERERERuRucPXsWFxeXQuuVjIvcBq6urgCkp6cX+QMnxSc7OxtPT0+OHz+Os7OztcMRNCZ3I43J3UdjcvfRmNydNC53H43J/2cYBmfPnqVSpUpFtlMyLnIblChxZfsFFxeX+/6Xz93G2dlZY3KX0ZjcfTQmdx+Nyd1HY3J30rjcfTQmV9zIBJ02cBMREREREREpZkrGRURERERERIqZknGR28De3p5x48Zhb29v7VDk/2hM7j4ak7uPxuTuozG5+2hM7k4al7uPxuTmmYzr7bcuIiIiIiIiIreVZsZFREREREREipmScREREREREZFipmRcREREREREpJgpGRcREREREREpZkrGRf6hGTNm4O3tTalSpahfvz5JSUnWDum+smnTJjp06EClSpUwmUysXLnSot4wDF5//XUqVaqEg4MDISEhpKamWifY+0BMTAwNGjTAyckJNzc3OnbsyIEDByzaaEyK18yZMwkKCsLZ2RlnZ2caN27Mt99+a67XeFhfTEwMJpOJkSNHmss0LsXv9ddfx2QyWRzu7u7meo2JdZw4cYJnnnmG8uXLU7p0aerUqcPOnTvN9RqX4uXl5ZXv58RkMhEVFQVoPG6WknGRf2DZsmWMHDmSl19+md27d/PII4/Qrl070tPTrR3afSMnJ4fatWvz4YcfFlg/efJkpk6dyocffsj27dtxd3endevWnD17tpgjvT8kJiYSFRXF1q1bWbduHbm5ubRp04acnBxzG41J8apSpQpvv/02O3bsYMeOHTz66KOEh4eb/zjSeFjX9u3b+fjjjwkKCrIo17hYR82aNcnIyDAfKSkp5jqNSfE7ffo0TZs2xdbWlm+//ZZ9+/YxZcoUypYta26jcSle27dvt/gZWbduHQBdunQBNB43zRCRW9awYUNj0KBBFmV+fn7Giy++aKWI7m+AsWLFCvPrvLw8w93d3Xj77bfNZefPnzdcXFyMWbNmWSHC+8/vv/9uAEZiYqJhGBqTu0W5cuWMTz75RONhZWfPnjWqVatmrFu3zmjRooUxYsQIwzD0c2It48aNM2rXrl1gncbEOl544QWjWbNmhdZrXKxvxIgRhq+vr5GXl6fxuAWaGRe5RRcvXmTnzp20adPGorxNmzZs2bLFSlHJtY4ePUpmZqbFGNnb29OiRQuNUTHJysoCwNXVFdCYWNvly5dZunQpOTk5NG7cWONhZVFRUTz22GOEhoZalGtcrOfQoUNUqlQJb29vunXrxpEjRwCNibWsXr2a4OBgunTpgpubG3Xr1mXOnDnmeo2LdV28eJFFixbRt29fTCaTxuMWKBkXuUX/+9//uHz5MhUrVrQor1ixIpmZmVaKSq51dRw0RtZhGAajRo2iWbNmBAYGAhoTa0lJScHR0RF7e3sGDRrEihUrCAgI0HhY0dKlS9m1axcxMTH56jQu1vHwww+zcOFC1qxZw5w5c8jMzKRJkyacOnVKY2IlR44cYebMmVSrVo01a9YwaNAghg8fzsKFCwH9rFjbypUrOXPmDJGRkYDG41bYWDsAkX87k8lk8dowjHxlYl0aI+sYOnQoe/bsYfPmzfnqNCbFq0aNGiQnJ3PmzBmWL19O7969SUxMNNdrPIrX8ePHGTFiBGvXrqVUqVKFttO4FK927dqZ/7tWrVo0btwYX19fFixYQKNGjQCNSXHLy8sjODiYt956C4C6deuSmprKzJkz6dWrl7mdxsU65s6dS7t27ahUqZJFucbjxmlmXOQWPfDAA5QsWTLfN32///57vm8ExTqu7oKrMSp+w4YNY/Xq1WzYsIEqVaqYyzUm1mFnZ0fVqlUJDg4mJiaG2rVr8/7772s8rGTnzp38/vvv1K9fHxsbG2xsbEhMTGT69OnY2NiYP3uNi3WVKVOGWrVqcejQIf2sWImHhwcBAQEWZf7+/uaNcjUu1nPs2DHWr19P//79zWUaj5unZFzkFtnZ2VG/fn3zLpJXrVu3jiZNmlgpKrmWt7c37u7uFmN08eJFEhMTNUZ3iGEYDB06lLi4OBISEvD29rao15jcHQzD4MKFCxoPK2nVqhUpKSkkJyebj+DgYCIiIkhOTsbHx0fjche4cOECaWlpeHh46GfFSpo2bZrv8ZgHDx7koYceAvT/FGuKjY3Fzc2Nxx57zFym8bgFVto4TuSesHTpUsPW1taYO3eusW/fPmPkyJFGmTJljF9++cXaod03zp49a+zevdvYvXu3ARhTp041du/ebRw7dswwDMN4++23DRcXFyMuLs5ISUkxunfvbnh4eBjZ2dlWjvzeNHjwYMPFxcXYuHGjkZGRYT7+/PNPcxuNSfEaO3assWnTJuPo0aPGnj17jJdeeskoUaKEsXbtWsMwNB53i2t3UzcMjYs1jB492ti4caNx5MgRY+vWrcbjjz9uODk5mf+frjEpftu2bTNsbGyMiRMnGocOHTIWL15slC5d2li0aJG5jcal+F2+fNl48MEHjRdeeCFfncbj5igZF/mHPvroI+Ohhx4y7OzsjHr16pkf4STFY8OGDQaQ7+jdu7dhGFceezJu3DjD3d3dsLe3N5o3b26kpKRYN+h7WEFjARixsbHmNhqT4tW3b1/z76gKFSoYrVq1MifihqHxuFv8PRnXuBS/rl27Gh4eHoatra1RqVIlo1OnTkZqaqq5XmNiHV999ZURGBho2NvbG35+fsbHH39sUa9xKX5r1qwxAOPAgQP56jQeN8dkGIZhlSl5ERERERERkfuU7hkXERERERERKWZKxkVERERERESKmZJxERERERERkWKmZFxERERERESkmCkZFxERERERESlmSsZFREREREREipmScREREREREZFipmRcREREREREpJgpGRcRERH5Pxs3bsRkMnHmzBmrvP+ff/5J586dcXZ2tmocIiJy5ykZFxERkfvOli1bKFmyJG3btrUob9KkCRkZGbi4uFglrgULFpCUlMSWLVvIyMjg9OnTmEwmkpOTrRKPiIjcOUrGRURE5L4zb948hg0bxubNm0lPTzeX29nZ4e7ujslkKvC8y5cvk5eXd1PvZRgGubm5N9T28OHD+Pv7ExgYWGQcIiLy76dkXERERO4rOTk5fP755wwePJjHH3+c+fPnm+v+vkx9/vz5lC1blq+//pqAgADs7e05duwYFy5cIDo6Gk9PT+zt7alWrRpz58616GPNmjUEBwdjb29PUlIShw8fJjw8nIoVK+Lo6EiDBg1Yv369+b1DQkKYMmUKmzZtwmQyERISgre3NwB169Y1l4mIyL1BybiIiIjcV5YtW0aNGjWoUaMGzzzzDLGxsRiGUWj7P//8k5iYGD755BNSU1Nxc3OjV69eLF26lOnTp5OWlsasWbNwdHS0OC86OpqYmBjS0tIICgri3LlztG/fnvXr17N7927CwsLo0KGDeWY+Li6OAQMG0LhxYzIyMoiLi2Pbtm0ArF+/3lwmIiL3BhtrByAiIiJSnObOncszzzwDQNu2bTl37hzfffcdoaGhBba/dOkSM2bMoHbt2gAcPHiQzz//nHXr1pnP8fHxyXfe+PHjad26tfl1+fLlzX0ATJgwgRUrVrB69WqGDh2Kq6srpUuXNi+VB8jOzjafe7VMRETuDZoZFxERkfvGgQMH2LZtG926dQPAxsaGrl27Mm/evELPsbOzIygoyPw6OTmZkiVL0qJFiyLfKzg42OJ1Tk4O0dHRBAQEULZsWRwdHdm/f7/FPesiInL/0My4iIiI3Dfmzp1Lbm4ulStXNpcZhoGtrS2nT58u8BwHBweLjdQcHBxu6L3KlClj8XrMmDGsWbOGd999l6pVq+Lg4MBTTz3FxYsXb+FKRETk307JuIiIiNwXcnNzWbhwIVOmTKFNmzYWdZ07d2bx4sUEBgZet59atWqRl5dHYmJioUvbC5KUlERkZCRPPvkkAOfOneOXX34p8hw7Ozvgyi7uIiJyb9EydREREbkvfP3115w+fZp+/foRGBhocTz11FPm3dCvx8vLi969e9O3b19WrlzJ0aNH2bhxI59//nmR51WtWpW4uDiSk5P56aef6NGjx3Ufk+bm5oaDgwPx8fGcPHmSrKysG75eERG5uykZFxERkfvC3LlzCQ0NxcXFJV9d586dSU5OZteuXTfU18yZM3nqqacYMmQIfn5+DBgwgJycnCLPee+99yhXrhxNmjShQ4cOhIWFUa9evSLPsbGxYfr06cyePZtKlSoRHh5+Q/GJiMjdz2QU9SwPEREREREREbntNDMuIiIiIiIiUsyUjIuIiIiIiIgUMyXjIiIiIiIiIsVMybiIiIiIiIhIMVMyLiIiIiIiIlLMlIyLiIiIiIiIFDMl4yIiIiIiIiLFTMm4iIiIiIiISDFTMi4iIiIiIiJSzJSMi4iIiIiIiBQzJeMiIiIiIiIixez/AcTq8e7dPt+ZAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1000x400 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# display a horizontal bar chart showing the information\n",
    "plt.figure(figsize=(10,4))\n",
    "plt.barh(df3.index,df3.values,color='purple')\n",
    "\n",
    "for i,value in enumerate(df3.values):\n",
    "    plt.annotate(str(value),xy=(value,i),\n",
    "    ha='left',va='center')\n",
    "plt.xlabel('Aircraft')\n",
    "plt.ylabel('Number of crashes')\n",
    "plt.title('Aircrafts with most accidents')\n",
    "plt.yticks(rotation=0,ha='right')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 361,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# find the Yearly trend of aircrashes\n",
    "Crashes_per_year = df.groupby('Year')['Aircraft'].count()\n",
    "ax = Crashes_per_year.plot.line(x='Year',y='Aircraft',color='purple',\n",
    "                                   title='Yearly trend Of Accidents',marker=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 364,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "119427"
      ]
     },
     "execution_count": 364,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Now we get the total fatalities recorded\n",
    "\n",
    "Total_Fatalities = df['Total Fatalities'].sum()\n",
    "Total_Fatalities"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 365,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4991"
      ]
     },
     "execution_count": 365,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Get the Total Accidents Occured\n",
    "\n",
    "Total_Accidents = df['Aircraft'].count()\n",
    "Total_Accidents"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 366,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "154344"
      ]
     },
     "execution_count": 366,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Get the Total passengers aboard flights\n",
    "Total_Passengers_aboard = df['Sum of Aboard'].sum()\n",
    "Total_Passengers_aboard"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 367,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8582"
      ]
     },
     "execution_count": 367,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Get the total ground casualties\n",
    "Casualties_ground = df['Sum of Fatalities(ground)'].sum()\n",
    "Casualties_ground"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Findings and Recommendations"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### After visualizing the data, the following findings were made:\n",
    "*\tAir crashes peaked most between 1939 - 1945 this can be attributed to the second world war which also occurred within that period.\n",
    "*\tStarting from the 2000s there has been a steady decline in the occurrence of air crashes which could be due to improved safety measures and much better engineering of aircrafts.\n",
    "*\tBoeing 737 B is the aircraft model with the greatest number of crashes mainly due to its wide usage amongst commercial airlines due to it being very economical\n",
    "*\tAeroflot which is a Russian airline has the greatest number of crashes in history as well as fatalities of about 8231 passengers which is five times more than any airline.\n",
    "*\tThe United States has the highest number of military aircraft crashes ever recorded in history.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Possible recommendations concerning the data:\n",
    "* Based on the analysis, reports can be generated priodically to summarize findings\n",
    ", highlight emerging trends, and provide actionable insights\n",
    "* We can engage with Aviation Authorities, Airlines, and safety boards to discuss findings\n",
    "and possible policy implications or safety recommendations"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
