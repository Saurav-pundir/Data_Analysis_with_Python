{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "da712a1b-b794-40b9-b60d-831a12aab2fe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0 1 2]\n",
      " [3 4 5]\n",
      " [6 7 8]]\n",
      "\n",
      "Mean : [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0]\n",
      "\n",
      "Variance : [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667]\n",
      "\n",
      "Standard deviation : [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611]\n",
      "\n",
      "Max : [[6, 7, 8], [2, 5, 8], 8]\n",
      "\n",
      "Min : [[0, 1, 2], [0, 3, 6], 0]\n",
      "\n",
      "Sum : [[9, 12, 15], [3, 12, 21], 36]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "def calculate(list):\n",
    "    if(len(list)!=9):\n",
    "        raise ValueError(\"Array can't contain less than 9 integers\")\n",
    "\n",
    "    else:\n",
    "        arr = np.array(list).reshape(3,3)\n",
    "        arr_sum = np.sum(arr).tolist()\n",
    "        print(arr)\n",
    "        mean_list = [np.mean(arr,axis=0).tolist() , np.mean(arr,axis=1).tolist(),np.mean(arr)]\n",
    "        print(\"\\nMean :\",mean_list)\n",
    "        var_list = [np.var(arr,axis=0).tolist() , np.var(arr,axis=1).tolist(),np.var(arr)]\n",
    "        print(\"\\nVariance :\",var_list)\n",
    "        std_list = [np.std(arr,axis=0).tolist() , np.std(arr,axis=1).tolist(),np.std(arr)]\n",
    "        print(\"\\nStandard deviation :\",std_list)\n",
    "        max_list = [np.max(arr,axis=0).tolist() , np.max(arr,axis=1).tolist(),np.max(arr)]\n",
    "        print(\"\\nMax :\",max_list)\n",
    "        min_list = [np.min(arr,axis=0).tolist() , np.min(arr,axis=1).tolist(),np.min(arr)]\n",
    "        print(\"\\nMin :\",min_list)\n",
    "        sum_list = [np.sum(arr, axis=0).tolist(),np.sum(arr, axis=1).tolist(), np.sum(arr)]\n",
    "        print(\"\\nSum :\",sum_list)\n",
    "\n",
    "calculate([0,1,2,3,4,5,6,7,8])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fd09d6ae-8f92-4c27-b10d-dc161cf0284f",
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
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
