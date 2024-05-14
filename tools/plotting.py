
import matplotlib.pyplot as plt

plot_NDCG_a_5=[]
plot_NDCG_a_10=[]
plot_NDCG_a_15=[]
plot_NDCG_a_20=[]

plot_acc_a_5=[]
plot_acc_a_10=[]
plot_acc_a_15=[]
plot_acc_a_20=[]

plot_pred_a_5=[]
plot_pred_a_10=[]
plot_pred_a_15=[]
plot_pred_a_20=[]

plot_re_a_5=[]
plot_re_a_10=[]
plot_re_a_15=[]
plot_re_a_20=[]

plot_NDCG_c_5=[]
plot_NDCG_c_10=[]
plot_NDCG_c_15=[]
plot_NDCG_c_20=[]

plot_acc_c_5=[]
plot_acc_c_10=[]
plot_acc_c_15=[]
plot_acc_c_20=[]

plot_pred_c_5=[]
plot_pred_c_10=[]
plot_pred_c_15=[]
plot_pred_c_20=[]

plot_re_c_5=[]
plot_re_c_10=[]
plot_re_c_15=[]
plot_re_c_20=[]

def plotting():
    global plot_NDCG_a_5, plot_NDCG_a_10, plot_NDCG_a_15, plot_NDCG_a_20
    global plot_acc_a_5, plot_acc_a_10, plot_acc_a_15, plot_acc_a_20
    global plot_pred_a_5, plot_pred_a_10, plot_pred_a_15, plot_pred_a_20
    global plot_re_a_5,plot_re_a_10,plot_re_a_15,plot_re_a_20
    global plot_NDCG_c_5, plot_NDCG_c_10, plot_NDCG_c_15, plot_NDCG_c_20
    global plot_acc_c_5, plot_acc_c_10, plot_acc_c_15, plot_acc_c_20
    global plot_pred_c_5, plot_pred_c_10, plot_pred_c_15, plot_pred_c_20 
    global plot_re_c_5,plot_re_c_10,plot_re_c_15,plot_re_c_20
    
    # plt.plot(plot_NDCG_a_5)
    # plt.xlabel('X-axis Label')
    # plt.ylabel('Y-axis Label')
    # plt.title('NGDC for top 5 API prediction')
    # plt.legend()
    # plt.show()
    
    plt.plot(plot_NDCG_a_5, label='NDCG for top 5 API prediction')
    plt.plot(plot_NDCG_a_10, label='NDCG for top 10 API prediction')
    plt.plot(plot_NDCG_a_15, label='NDCG for top 15 API prediction')
    plt.plot(plot_NDCG_a_20, label='NDCG for top 20 API prediction')
    plt.xlabel('Epoch')
    plt.ylabel('Metric value')
    plt.title('NDCG of API recommendation')
    plt.legend()
    plt.show()
    
    # Plotting ACC for top 5 API prediction
    plt.plot(plot_acc_a_5, label='AvgP for top 5 API prediction')
    plt.plot(plot_acc_a_10, label='AvgP for top 10 API prediction')
    plt.plot(plot_acc_a_15, label='AvgP for top 15 API prediction')
    plt.plot(plot_acc_a_20, label='AvgP for top 20 API prediction')
    plt.xlabel('Epoch')
    plt.ylabel('Metric value')
    plt.title('Average precision of API recommendation')
    plt.legend()
    plt.show()

    # Plotting Prediction for top 5 API prediction
    plt.plot(plot_pred_a_5, label='Precision for top 5 API prediction')
    plt.plot(plot_pred_a_10, label='Precision for top 10 API prediction')
    plt.plot(plot_pred_a_15, label='Precision for top 15 API prediction')
    plt.plot(plot_pred_a_20, label='Precision for top 20 API prediction')
    plt.xlabel('Epoch')
    plt.ylabel('Metric value')
    plt.title('Precision for API prediction')
    plt.legend()
    plt.show()
    
    # Plotting Recall for top 5 API prediction
    plt.plot(plot_re_a_5, label='Recall for top 5 API prediction')
    plt.plot(plot_re_a_10, label='Recall for top 10 API prediction')
    plt.plot(plot_re_a_15, label='Recall for top 15 API prediction')
    plt.plot(plot_re_a_20, label='Recall for top 20 API prediction')
    plt.xlabel('Epoch')
    plt.ylabel('Metric value')
    plt.title('Recall for API prediction')
    plt.legend()
    plt.show()

    # Plotting NDCG for top 5 API prediction for class
    plt.plot(plot_NDCG_c_5, label='NDCG for top 5 API prediction for class')
    plt.plot(plot_NDCG_c_10, label='NDCG for top 10 API prediction for class')
    plt.plot(plot_NDCG_c_15, label='NDCG for top 15 API prediction for class')
    plt.plot(plot_NDCG_c_20, label='NDCG for top 20 API prediction for class')
    plt.xlabel('Epoch')
    plt.ylabel('Metric value')
    plt.title('NDCG for Category recommendation')
    plt.legend()
    plt.show()
    
    # Plotting ACC for top 5 API prediction for class
    plt.plot(plot_acc_c_5, label='AvgP for top 5 API prediction for class')
    plt.plot(plot_acc_c_10, label='AvgP for top 10 API prediction for class')
    plt.plot(plot_acc_c_15, label='AvgP for top 15 API prediction for class')
    plt.plot(plot_acc_c_20, label='AvgP for top 20 API prediction for class')
    plt.xlabel('Epoch')
    plt.ylabel('Metric value')
    plt.title('Average precision of Category Recommendation')
    plt.legend()
    plt.show()

    # Plotting Prediction for top 5 API prediction for class
    plt.plot(plot_pred_c_5, label='Precision for top 5 API prediction for class')
    plt.plot(plot_pred_c_10, label='Precision for top 10 API prediction for class')
    plt.plot(plot_pred_c_15, label='Precision for top 15 API prediction for class')
    plt.plot(plot_pred_c_20, label='Precision for top 20 API prediction for class')
    plt.xlabel('Epoch')
    plt.ylabel('Metric value')
    plt.title('Precision for Category prediction')
    plt.legend()
    plt.show()
    
    plt.plot(plot_re_c_5, label='Recall for top 5 API prediction for class')
    plt.plot(plot_re_c_10, label='Recall for top 10 API prediction for class')
    plt.plot(plot_re_c_15, label='Recall for top 15 API prediction for class')
    plt.plot(plot_re_c_20, label='Recall for top 20 API prediction for class')
    plt.xlabel('Epoch')
    plt.ylabel('Metric value')
    plt.title('Recall for Category prediction')
    plt.legend()
    plt.show()

def storing(ndcg_a,ndcg_c,pre_a,pre_c,ap_a,ap_c,api_loss,category_loss,recall_a,recall_c):
    global plot_NDCG_a_5, plot_NDCG_a_10, plot_NDCG_a_15, plot_NDCG_a_20
    global plot_acc_a_5, plot_acc_a_10, plot_acc_a_15, plot_acc_a_20
    global plot_pred_a_5, plot_pred_a_10, plot_pred_a_15, plot_pred_a_20
    global plot_re_a_5,plot_re_a_10,plot_re_a_15,plot_re_a_20
    global plot_NDCG_c_5, plot_NDCG_c_10, plot_NDCG_c_15, plot_NDCG_c_20
    global plot_acc_c_5, plot_acc_c_10, plot_acc_c_15, plot_acc_c_20
    global plot_pred_c_5, plot_pred_c_10, plot_pred_c_15, plot_pred_c_20    
    global plot_re_c_5,plot_re_c_10,plot_re_c_15,plot_re_c_20
    
    print(api_loss,category_loss)
    
    plot_NDCG_a_5.append(ndcg_a[1])
    plot_NDCG_a_10.append(ndcg_a[2])
    plot_NDCG_a_15.append(ndcg_a[3])
    plot_NDCG_a_20.append(ndcg_a[4])

    plot_acc_a_5.append(ap_a[1])
    plot_acc_a_10.append(ap_a[2])
    plot_acc_a_15.append(ap_a[3])
    plot_acc_a_20.append(ap_a[4])

    plot_pred_a_5.append(pre_a[1])
    plot_pred_a_10.append(pre_a[2])
    plot_pred_a_15.append(pre_a[3])
    plot_pred_a_20.append(pre_a[4])
    
    plot_re_a_5.append(recall_a[1])
    plot_re_a_10.append(recall_a[2])
    plot_re_a_15.append(recall_a[3])
    plot_re_a_20.append(recall_a[4])

    plot_NDCG_c_5.append(ndcg_c[1])
    plot_NDCG_c_10.append(ndcg_c[2])
    plot_NDCG_c_15.append(ndcg_c[3])
    plot_NDCG_c_20.append(ndcg_a[4])

    plot_acc_c_5.append(ap_c[1])
    plot_acc_c_10.append(ap_c[2])
    plot_acc_c_15.append(ap_c[3])
    plot_acc_c_20.append(ap_c[4])

    plot_pred_c_5.append(pre_c[1])
    plot_pred_c_10.append(pre_c[2])
    plot_pred_c_15.append(pre_c[3])
    plot_pred_c_20.append(pre_c[4])
    
    plot_re_c_5.append(recall_c[1])
    plot_re_c_10.append(recall_c[2])
    plot_re_c_15.append(recall_c[3])
    plot_re_c_20.append(recall_c[4])


# storing([0.36419,0.456213,0.485479,0.494441,0.499501,0.501952,0.502205],[0.36419,0.456213,0.485479,0.494441,0.499501,0.501952,0.502205],[0.36419,0.456213,0.485479,0.494441,0.499501,0.501952,0.502205],[0.36419,0.456213,0.485479,0.494441,0.499501,0.501952,0.502205],[0.36419,0.456213,0.485479,0.494441,0.499501,0.501952,0.502205],[0.36419,0.456213,0.485479,0.494441,0.499501,0.501952,0.502205])

# storing([0.36419,0.456213,0.485479,0.494441,0.499501,0.501952,0.502205],[0.36419,0.456213,0.485479,0.494441,0.499501,0.501952,0.502205],[0.36419,0.456213,0.485479,0.494441,0.499501,0.501952,0.502205],[0.36419,0.456213,0.485479,0.494441,0.499501,0.501952,0.502205],[0.36419,0.456213,0.485479,0.494441,0.499501,0.501952,0.502205],[0.36419,0.456213,0.485479,0.494441,0.499501,0.501952,0.502205])