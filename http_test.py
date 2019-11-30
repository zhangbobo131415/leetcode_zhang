# import requests
# a = requests.get('https://www.shadiao1024.tk')
# bb = a.headers
# for i in bb:
#     print(i,bb[i])
import matplotlib.pyplot as plt
import math

from sklearn.metrics import roc_curve, auc, mean_squared_error, accuracy_score
def check_fit(truth, prob):
    """
    truth: 真实的值 [1,0,1,1,1]
    prob: 预测的值 [0.9,0.7,0.8,0.2,0.3]
    """
    fpr, tpr, _ = roc_curve(truth, prob)     # drop_intermediate:(default=True) 
    roc_auc = auc(fpr, tpr)   # 计算auc值，roc曲线下面的面积 等价于 roc_auc_score(truth,prob)
 
    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([-0.1, 1.05])
    plt.ylim([-0.1, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")
    plt.show() 
 
    print('results are RMSE, accuracy, ROC')
    predics = [1 if i>=0.5 else 0 for i in prob]
    print(math.sqrt(mean_squared_error(truth, prob)), accuracy_score(truth, predics), roc_auc)
truth = [0,0,0,1,1,1]
prob = [0.2, 0.8, 0.65, 0.7, 0.9, 0.6]
check_fit(truth,prob)