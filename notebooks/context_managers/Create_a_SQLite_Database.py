{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlite3\n",
    "import pandas as pd\n",
    "from pandas import DataFrame\n",
    "\n",
    "conn = sqlite3.connect('../SQLDatabase.db')  \n",
    "c = conn.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<sqlite3.Cursor at 0x7fe178db9e30>"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create empty table with the column names corresponding to csv\n",
    "\n",
    "c.execute('''CREATE TABLE IF NOT EXISTS programming_trends (Month int, Python int, SQL int, R int, JavaScript int,\n",
    "       Visual_Basic_for_Applications int)''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# read data with pandas and push to SQL \n",
    "\n",
    "read_clients = pd.read_csv (r'../data/programming-trends.csv')\n",
    "read_clients.to_sql('programming_trends', conn, if_exists='append', index = False)"
   ]
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
