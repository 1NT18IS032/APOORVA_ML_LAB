{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import random\n",
    "import numpy as np\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "col_names=['x','y','res']\n",
    "dataset = pd.read_csv(\"Student-University.csv\",header=None,names=col_names)\n",
    "test=dataset.values.tolist()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "train =[]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "80\n",
      "20\n"
     ]
    }
   ],
   "source": [
    "for i in range(80):\n",
    "    r =random.randrange(len(test))\n",
    "    train.append(test.pop(r))\n",
    "    \n",
    "print(len(train))\n",
    "print(len(test)) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "alpha=0.0001\n",
    "b0=0.1\n",
    "b1=0.2\n",
    "b2=0.3\n",
    "x=[i[0]for i in train]\n",
    "y=[i[1]for i in train]\n",
    "z=[i[2]for i in train]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "epoch =1000\n",
    "while(epoch>0):\n",
    "    for i in range(len(x)):\n",
    "        pred=round(1/(1+np.exp(-(b0+b1*x[i]+b2*y[i]))))\n",
    "        b0 =b0+alpha*(z[i]-pred)*pred*(1-pred)\n",
    "        b1 =b1+alpha*(z[i]-pred)*pred*(1-pred)*x[i]\n",
    "        b2 =b2+alpha*(z[i]-pred)*pred*(1-pred)*y[i]\n",
    "    epoch = epoch-1\n",
    "            \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.1 0.2 0.3\n",
      "20\n"
     ]
    }
   ],
   "source": [
    "print(b0,b1,b2)\n",
    "x_test=[i[0]for i in test]\n",
    "y_test=[i[1]for i in test]\n",
    "z_true=[i[2]for i in test]\n",
    "print(len(x_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "z_pred=[]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n"
     ]
    }
   ],
   "source": [
    "for i in range(len(x_test)):\n",
    "    pred_test = round((1/(1+np.exp(-(b0+b1*x_test[i]+b2*y_test[i])))))\n",
    "    z_pred.append(pred_test)\n",
    "    \n",
    "print(len(z_pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.75"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(z_true, z_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "x=dataset['x'].values\n",
    "y=dataset['y'].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[34.62365962 30.28671077 35.84740877 60.18259939 79.03273605 45.08327748\n",
      " 61.10666454 75.02474557 76.0987867  84.43281996 95.86155507 75.01365839\n",
      " 82.30705337 69.36458876 39.53833914 53.97105215 69.07014406 67.94685548\n",
      " 70.66150955 76.97878373 67.37202755 89.67677575 50.53478829 34.21206098\n",
      " 77.92409145 62.27101367 80.19018075 93.1143888  61.83020602 38.7858038\n",
      " 61.37928945 85.40451939 52.10797973 52.04540477 40.23689374 54.63510555\n",
      " 33.91550011 64.17698887 74.78925296 34.18364003 83.90239366 51.54772027\n",
      " 94.44336777 82.36875376 51.04775177 62.22267576 77.19303493 97.77159928\n",
      " 62.0730638  91.5649745  79.94481794 99.27252693 90.54671411 34.52451385\n",
      " 50.28649612 49.58667722 97.64563396 32.57720017 74.24869137 71.79646206\n",
      " 75.39561147 35.28611282 56.2538175  30.05882245 44.66826172 66.56089447\n",
      " 40.45755098 49.07256322 80.27957401 66.74671857 32.72283304 64.03932042\n",
      " 72.34649423 60.45788574 58.84095622 99.8278578  47.26426911 50.4581598\n",
      " 60.45555629 82.22666158 88.91389642 94.83450672 67.31925747 57.23870632\n",
      " 80.366756   68.46852179 42.07545454 75.47770201 78.63542435 52.34800399\n",
      " 94.09433113 90.44855097 55.48216114 74.49269242 89.84580671 83.48916274\n",
      " 42.26170081 99.31500881 55.34001756 74.775893  ]\n"
     ]
    }
   ],
   "source": [
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[78.02469282 43.89499752 72.90219803 86.3085521  75.34437644 56.31637178\n",
      " 96.51142588 46.55401354 87.42056972 43.53339331 38.22527806 30.60326323\n",
      " 76.4819633  97.71869196 76.03681085 89.20735014 52.74046973 46.67857411\n",
      " 92.92713789 47.57596365 42.83843832 65.79936593 48.85581153 44.2095286\n",
      " 68.97235999 69.95445795 44.82162893 38.80067034 50.25610789 64.99568096\n",
      " 72.80788731 57.05198398 63.12762377 69.43286012 71.16774802 52.21388588\n",
      " 98.86943574 80.90806059 41.57341523 75.23772034 56.30804622 46.85629026\n",
      " 65.56892161 40.61825516 45.82270146 52.06099195 70.4582     86.72782233\n",
      " 96.76882412 88.69629255 74.16311935 60.999031   43.39060181 60.39634246\n",
      " 49.80453881 59.80895099 68.86157272 95.59854761 69.82457123 78.45356225\n",
      " 85.75993667 47.02051395 39.26147251 49.59297387 66.45008615 41.09209808\n",
      " 97.53518549 51.88321182 92.11606081 60.99139403 43.30717306 78.03168802\n",
      " 96.22759297 73.0949981  75.85844831 72.36925193 88.475865   75.80985953\n",
      " 42.50840944 42.71987854 69.8037889  45.6943068  66.58935318 59.51428198\n",
      " 90.9601479  85.5943071  78.844786   90.424539   96.64742717 60.76950526\n",
      " 77.15910509 87.50879176 35.57070347 84.84513685 45.35828361 48.3802858\n",
      " 87.10385094 68.77540947 64.93193801 89.5298129 ]\n"
     ]
    }
   ],
   "source": [
    "print(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'z'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/pandas/core/indexes/base.py\u001b[0m in \u001b[0;36mget_loc\u001b[0;34m(self, key, method, tolerance)\u001b[0m\n\u001b[1;32m   2896\u001b[0m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2897\u001b[0;31m                 \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_engine\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_loc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2898\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/index.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/index.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/hashtable_class_helper.pxi\u001b[0m in \u001b[0;36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/hashtable_class_helper.pxi\u001b[0m in \u001b[0;36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;31mKeyError\u001b[0m: 'z'",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-14-1d62bb7a6753>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mz\u001b[0m\u001b[0;34m=\u001b[0m \u001b[0mdataset\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'z'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mvalues\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/pandas/core/frame.py\u001b[0m in \u001b[0;36m__getitem__\u001b[0;34m(self, key)\u001b[0m\n\u001b[1;32m   2978\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcolumns\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mnlevels\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2979\u001b[0m                 \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_getitem_multilevel\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2980\u001b[0;31m             \u001b[0mindexer\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcolumns\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_loc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2981\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mis_integer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mindexer\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2982\u001b[0m                 \u001b[0mindexer\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0mindexer\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/pandas/core/indexes/base.py\u001b[0m in \u001b[0;36mget_loc\u001b[0;34m(self, key, method, tolerance)\u001b[0m\n\u001b[1;32m   2897\u001b[0m                 \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_engine\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_loc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2898\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2899\u001b[0;31m                 \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_engine\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_loc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_maybe_cast_indexer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2900\u001b[0m         \u001b[0mindexer\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_indexer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmethod\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtolerance\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mtolerance\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2901\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mindexer\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mndim\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0;36m1\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mindexer\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msize\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/index.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/index.pyx\u001b[0m in \u001b[0;36mpandas._libs.index.IndexEngine.get_loc\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/hashtable_class_helper.pxi\u001b[0m in \u001b[0;36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/hashtable_class_helper.pxi\u001b[0m in \u001b[0;36mpandas._libs.hashtable.PyObjectHashTable.get_item\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;31mKeyError\u001b[0m: 'z'"
     ]
    }
   ],
   "source": [
    "z= dataset['z'].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
