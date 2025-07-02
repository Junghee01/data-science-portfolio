def plot_mse_loss(var1, var2, df, order=None):
    if order:
      df[var1] = pd.Categorical(df[var1], categories=order, ordered=True)
    fig, ax = plt.subplots(1, 4)
    fig.set_size_inches(15, 4)
    sns.set_style("darkgrid", {"axes.facecolor": ".9"})

    sns.barplot(x=var1, y='train_mse', hue=var2, data=df, ax=ax[0], order=order)
    sns.barplot(x=var1, y='val_mse', hue=var2, data=df, ax=ax[1], order=order)
    sns.barplot(x=var1, y='test_mse', hue=var2, data=df, ax=ax[2], order=order)
    sns.barplot(x=var1, y='test_orig_loss', hue=name_var2, data=df, ax=ax[3], order=order)

    ax[0].set_title('Train MSE Loss')
    ax[1].set_title('Validation MSE Loss')
    ax[2].set_title('Test MSE Loss')
    ax[3].set_title('Test Orig MSE Loss')

    ax[0].get_legend().remove()
    ax[1].get_legend().remove()
    ax[2].get_legend().remove()
    ax[3].legend(loc='center left', bbox_to_anchor=(1.05, 0.5), title=var2)

    plt.tight_layout()

def plot_mae_loss(var1, var2, df, order=None):
    if order:
      df[var1] = pd.Categorical(df[var1], categories=order, ordered=True)
    fig, ax = plt.subplots(1, 4)
    fig.set_size_inches(15, 4)
    sns.set_style("darkgrid", {"axes.facecolor": ".9"})

    sns.barplot(x=var1, y='train_mae', hue=var2, data=df, ax=ax[0], order=order)
    sns.barplot(x=var1, y='val_mae', hue=var2, data=df, ax=ax[1], order=order)
    sns.barplot(x=var1, y='test_mae', hue=var2, data=df, ax=ax[2], order=order)
    sns.barplot(x=var1, y='test_mae_orig_loss', hue=name_var2, data=df, ax=ax[3], order=order)

    ax[0].set_title('Train MAE Loss')
    ax[1].set_title('Validation MAE Loss')
    ax[2].set_title('Test MAE Loss')
    ax[3].set_title('Test Orig MAE Loss')

    ax[0].get_legend().remove()
    ax[1].get_legend().remove()
    ax[2].get_legend().remove()
    ax[3].legend(loc='center left', bbox_to_anchor=(1.05, 0.5), title=var2)

    plt.tight_layout()



def plot_loss_variation(var1, var2, df, order_var1=None, order_var2=None,  **kwargs ) :


  list_v1 = df[var1].unique()
  list_v2 = df[var2].unique()
  list_data = []

  for value1 in list_v1:
      for value2 in list_v2:
          row = df.loc[df[var1]==value1]
          row = row.loc[row[var2]==value2]

          train_losses = list(row.train_losses)[0]
          val_losses = list(row.val_losses)[0]
          test_mse = list(row.test_mse)[0]

          for epoch, train_loss in enumerate(train_losses):
              list_data.append({'type':'train', 'loss':train_loss, 'testloss': test_mse, 'epoch':epoch, var1:value1, var2:value2})
          for epoch, val_loss in enumerate(val_losses):
              list_data.append({'type':'val', 'loss':val_loss, 'testloss': test_mse,'epoch':epoch, var1:value1, var2:value2})

  df = pd.DataFrame(list_data)
  if order_var1:
      df[var1] = pd.Categorical(df[var1], categories=order_var1, ordered=True)
  if order_var2:
      df[var2] = pd.Categorical(df[var2], categories=order_var2, ordered=True)

  g = sns.FacetGrid(df, row=var2, col=var1, hue='type', margin_titles=True, sharey=False)  
  g = g.map(plt.plot, 'epoch', 'loss', marker='.')

  def show_MaeLoss(x, y, metric, **kwargs):
      plt.scatter(x, y, alpha=0.3, s=1)   
      metric = "Test Loss: {:1.4f}".format(list(metric.values)[0])
      plt.text(0.05, 0.95, metric,  horizontalalignment='left', verticalalignment='center', transform=plt.gca().transAxes, bbox=dict(facecolor='yellow', alpha=0.5, boxstyle="round,pad=0.1"))
  g = g.map(show_MaeLoss, 'epoch', 'loss', 'testloss')  

  g.add_legend()
  g.fig.suptitle('Train MSELoss vs Val MSELoss')
  plt.subplots_adjust(top=0.89)


def plot_mae_loss_variation(var1, var2, df, order_var1=None, order_var2=None,  **kwargs ) :
    list_v1 = df[var1].unique()
    list_v2 = df[var2].unique()
    list_data = []

    for value1 in list_v1:
        for value2 in list_v2:
            row = df.loc[df[var1]==value1]
            row = row.loc[row[var2]==value2]

            train_mae_loss = list(row.train_mae_losses)[0]
            val_mae_loss = list(row.val_mae_losses)[0]   
            test_mae = list(row.test_mae)[0]        

            for epoch, train_loss in enumerate(train_mae_loss):
                list_data.append({'type':'train', 'MaeLoss':train_loss, 'test_MaeLoss':test_mae, 'epoch':epoch, var1:value1, var2:value2})   
            for epoch, val_loss in enumerate(val_mae_loss):
                list_data.append({'type':'val', 'MaeLoss':val_loss, 'test_MaeLoss':test_mae, 'epoch':epoch, var1:value1, var2:value2})

    df = pd.DataFrame(list_data)
    if order_var1:
        df[var1] = pd.Categorical(df[var1], categories=order_var1, ordered=True)
    if order_var2:
        df[var2] = pd.Categorical(df[var2], categories=order_var2, ordered=True)

    g = sns.FacetGrid(df, row=var2, col=var1, hue='type', margin_titles=True, sharey=False)
    g = g.map(plt.plot, 'epoch', 'MaeLoss', marker='.')

    def show_MaeLoss(x, y, metric, **kwargs):
          plt.scatter(x, y, alpha=0.3, s=1)    
          metric = "Test MaeLoss: {:1.4f}".format(list(metric.values)[0])
          plt.text(0.05, 0.95, metric,  horizontalalignment='left', verticalalignment='center', transform=plt.gca().transAxes, bbox=dict(facecolor='yellow', alpha=0.5, boxstyle="round,pad=0.1"))

    g = g.map(show_MaeLoss, 'epoch', 'MaeLoss', 'test_MaeLoss')   

    g.add_legend()
    g.fig.suptitle('Train MaeLoss vs Val MaeLoss')
    plt.subplots_adjust(top=0.89)



def plot_mae_loss_variation_add(var1, var2, df, order_var1=None, order_var2=None,  **kwargs ) :
    list_v1 = df[var1].unique()
    list_v2 = df[var2].unique()
    list_data = []

    for value1 in list_v1:
        for value2 in list_v2:
            row = df.loc[df[var1]==value1]
            row = row.loc[row[var2]==value2]

            train_mae_loss = list(row.train_mae_losses)[0]
            val_mae_loss = list(row.val_mae_losses)[0]
            val_mae_orig_loss = list(row.val_mae_orig_losses)[0]   
            test_orig_mae = list(row.test_mae_orig_loss)[0]         

            for epoch, train_loss in enumerate(train_mae_loss):
                list_data.append({'type':'train', 'MaeLoss':train_loss, 'test_orig_MaeLoss':test_orig_mae, 'epoch':epoch, var1:value1, var2:value2})   
            for epoch, val_loss in enumerate(val_mae_loss):
                list_data.append({'type':'val', 'MaeLoss':val_loss, 'test_orig_MaeLoss':test_orig_mae, 'epoch':epoch, var1:value1, var2:value2})
            for epoch, val_orig_loss in enumerate(val_mae_orig_loss):
                list_data.append({'type':'val_orig', 'MaeLoss':val_orig_loss, 'test_orig_MaeLoss':test_orig_mae, 'epoch':epoch, var1:value1, var2:value2})

    df = pd.DataFrame(list_data)
    if order_var1:
        df[var1] = pd.Categorical(df[var1], categories=order_var1, ordered=True)
    if order_var2:
        df[var2] = pd.Categorical(df[var2], categories=order_var2, ordered=True)

    g = sns.FacetGrid(df, row=var2, col=var1, hue='type', margin_titles=True, sharey=False)
    g = g.map(plt.plot, 'epoch', 'MaeLoss', marker='.')

    def show_MaeLoss(x, y, metric, **kwargs):
          plt.scatter(x, y, alpha=0.3, s=1)    
          metric = "Test Orig MaeLoss: {:1.3f}".format(list(metric.values)[0])
          plt.text(0.05, 0.95, metric,  horizontalalignment='left', verticalalignment='center', transform=plt.gca().transAxes, bbox=dict(facecolor='yellow', alpha=0.5, boxstyle="round,pad=0.1"))

    g = g.map(show_MaeLoss, 'epoch', 'MaeLoss', 'test_orig_MaeLoss')   

    g.add_legend()
    g.fig.suptitle('Train MaeLoss vs Val MaeLoss vs Val Orig MaeLoss')
    plt.subplots_adjust(top=0.89)

